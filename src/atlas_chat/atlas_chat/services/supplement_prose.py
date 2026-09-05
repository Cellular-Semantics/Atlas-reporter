"""Make a paper's supplementary *prose* readable, and record what it contains.

`tables` covers everything with a header row, and `index-supplements` already
characterises those well — `outline` shows a sheet's title rows and block
headers, `slice` reads any region of it. Prose has none of that. A Supplementary
Discussion or a table-legends document has no columns to read, so `outline_file`
sees nothing in it and the manifest has nowhere to record it. Gopee's bundle
ships 15 KB of exactly that, and the legends are where Supplementary Table 22
announces itself as the DEG table for the four macrophage subsets.

So this module does for prose what the store already does for tables: extract
it, say how big it is, and give a reader enough to decide whether to open it.

How much it gives depends on size, because the decision differs:

* **Short enough to read** — the whole text. There is nothing to decide; the
  indexing agent reads it directly, and a cheap intermediary would only lose
  fidelity on the highest-leverage read in the bundle.
* **Too long to read on spec** — a characterisation instead. For a PDF that is
  its outline: pymupdf4llm tags every paragraph with the heading above it, so
  the section list says what the document is almost for free, and a Supplementary
  Methods announces itself without being read. Failing that, a sample of the
  head, middle and tail. Either goes to a cheap judge, which answers only
  whether it is worth folding in.

That question — does it name cell types — is what routes prose, because prose
that does is read *whole* alongside the paper text. Tables never are, however
relevant: Supplementary Table 5 in this bundle is 95 MB and 396,877 rows. The
format decides, not a score.

No model is called here. The judging is a subagent driven by the
``index-supplements`` skill: ``units`` hands out the evidence, ``record`` takes
the verdicts back.

PDFs need the ``text-access`` extra.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

#: Prose at or below this many characters is handed over whole — roughly the
#: size of a long legends document, which is worth reading in full. Above it,
#: a reader gets a characterisation and decides from that.
READ_WHOLE_THRESHOLD = 24_000

#: Characters kept when a document is too long and has no usable outline, split
#: across its head, middle and tail. A legends document lists its tables in
#: order, so a prefix would characterise the first few and miss the rest.
SAMPLE_BUDGET = 12_000

#: Cell-type labels passed to a judge as context. Above this many, the roster
#: stops being context and becomes the bulk of the prompt, so the question is
#: asked in general terms instead.
ROSTER_PROMPT_CAP = 150

#: Sections shown in an outline. A real document has far more headings than are
#: worth listing — every run-in bold line becomes one — and a hundred-line
#: outline is no longer a cheap characterisation.
OUTLINE_CAP = 25

#: Media types read as prose.
PROSE_MEDIA = {"docx", "pdf", "txt"}

#: Maps a media type to the `extractor` recorded on the pointer.
_EXTRACTOR = {"docx": "docx", "pdf": "pdf", "txt": "plaintext"}

#: The parser's label for text with no heading above it, and for text found
#: inside a figure. Neither names a section, so neither belongs in an outline.
_UNSECTIONED = {"BODY", "IN_FIGURE"}


class SupplementProseError(RuntimeError):
    """Prose could not be prepared, or verdicts could not be recorded."""


@dataclass
class Unit:
    """One prose document: a stable id, its draft pointer, and what to read."""

    unit_id: str
    pointer: dict[str, Any]
    evidence_block: str

    @property
    def readable_whole(self) -> bool:
        """Whether the evidence is the document itself rather than a stand-in."""
        return self.pointer["evidence"] == "full_text"

    def as_task(self) -> dict[str, Any]:
        """The shape handed to a reader — an id, what to read, and how complete."""
        return {
            "unit_id": self.unit_id,
            "evidence_kind": self.pointer["evidence"],
            "n_chars": self.pointer["n_chars"],
            "evidence": self.evidence_block,
        }


@dataclass
class AssessResult:
    """Prose pointers ready to write into a manifest, and what could not be done."""

    prose: list[dict[str, Any]] = field(default_factory=list)
    gaps: list[dict[str, Any]] = field(default_factory=list)


# ------------------------------------------------------------------
# Characterising a document — pure
# ------------------------------------------------------------------


def outline_sections(sections: list[tuple[str, int]], cap: int = OUTLINE_CAP) -> str:
    """The document's substantial headings in order, with how much sits under each.

    Far better than sampling characters when it is available: a section list
    says what a document *is*, and the sizes say where its substance is. A
    Supplementary Methods running to forty pages identifies itself here without
    a word of it being read.

    A real document has more headings than are worth listing — every run-in
    bold line becomes one, and a hundred-line outline is not a cheap
    characterisation. So the largest ``cap`` sections are kept, shown back in
    document order, and what was dropped is stated. That last part matters: a
    silently truncated outline reads as a complete one, and a reader would
    conclude a section is absent when it was only omitted.

    Args:
        sections: ``(heading, characters)`` in document order, already merged
            so a heading appears once.
        cap: How many sections to show.
    """
    if not sections:
        return "Sections: none — the extractor found no headings in this document."

    keep = sorted(sections, key=lambda s: s[1], reverse=True)[:cap]
    kept = {name for name, _ in keep}
    lines = [f"  {name} — {chars} chars" for name, chars in sections if name in kept]

    dropped = len(sections) - len(lines)
    header = f"Sections, in order ({len(sections)} in total"
    if dropped:
        omitted = sum(chars for name, chars in sections if name not in kept)
        header += f"; the {dropped} smallest are omitted, holding {omitted} chars between them"
    return f"{header}):\n" + "\n".join(lines)


def sample_text(text: str, budget: int = SAMPLE_BUDGET) -> str:
    """Head, middle and tail of a document, for when it has no usable outline.

    A prefix would characterise a document's opening and say nothing about the
    rest, and the question asked of a sample is about the whole thing.
    """
    part = budget // 3
    if len(text) <= budget:
        return text
    middle = (len(text) - part) // 2
    return "\n\n[...]\n\n".join((text[:part], text[middle : middle + part], text[-part:]))


def render_evidence(name: str, body: str, evidence: str, n_chars: int) -> str:
    """What a reader is shown, saying plainly what kind of view it is."""
    what = {
        "full_text": "the complete text",
        "outline": (
            f"AN OUTLINE ONLY — the section headings of a {n_chars}-character document, "
            "not its text"
        ),
        "sampled_text": (
            f"A SAMPLE — head, middle and tail of a {n_chars}-character document; "
            "the parts between were not shown"
        ),
    }[evidence]
    return f"File: {name}\nYou are shown: {what}\n\n{body}"


def roster_block(labels: list[str], cap: int = ROSTER_PROMPT_CAP) -> str:
    """Ground the cell-type question in the project's own labels, where it fits.

    Real labels are what let a reader recognise ``LC_1`` or ``mCL2`` as a cell
    type at all. Past the cap the roster would dominate the prompt, so the
    question is asked in general terms — a worse question, and the block says
    which one was asked.
    """
    general = (
        "Judge cell-type mentions on general biological grounds: named cell types "
        "or states, or cluster identifiers used as stand-ins for them."
    )
    if not labels:
        return f"== Cell types ==\nNo roster available. {general}"
    if len(labels) > cap:
        return (
            f"== Cell types ==\nThis project annotates {len(labels)} cell types — too "
            f"many to list. {general}"
        )
    return "== Cell types ==\nThis project annotates:\n" + "\n".join(f"- {x}" for x in labels)


def merge_sections(segments: list[tuple[str, str]]) -> list[tuple[str, int]]:
    """Collapse tagged paragraphs into one entry per heading, in order.

    The parser tags every paragraph with the heading above it, so a section
    with nine paragraphs appears nine times. Unheaded and figure-internal text
    carry no heading and are left out.

    Args:
        segments: ``(section, text)`` in document order.

    Returns:
        ``(heading, characters)`` in first-appearance order.
    """
    order: list[str] = []
    chars: dict[str, int] = {}
    for section, text in segments:
        if section in _UNSECTIONED:
            continue
        if section not in chars:
            order.append(section)
            chars[section] = 0
        chars[section] += len(text)
    return [(name, chars[name]) for name in order]


# ------------------------------------------------------------------
# Reading the files
# ------------------------------------------------------------------


def _extract(path: Path, kind: str) -> tuple[str, list[tuple[str, int]]]:
    """A document's text, and its section outline where the format carries one.

    Only the PDF path yields an outline: pymupdf4llm reports markdown headings
    and the parser tags each paragraph with the one above it. docx and plain
    text come back as text alone.
    """
    from atlas_chat.services.supplement_store import extract_text

    if kind != "pdf":
        result = extract_text(path, max_chars=2_000_000)
        return result.get("text") or "", []

    from atlas_chat.services._pdf_parser import extract_pdf_segments

    segments = extract_pdf_segments(path)
    body = [(s.section, s.text) for s in segments if s.section != "IN_FIGURE"]
    return "\n\n".join(text for _, text in body), merge_sections(body)


def prose_units(store_root: Path, doi: str, manifest: dict[str, Any]) -> list[Unit]:
    """Every prose-bearing supplement, extracted to disk and ready to read.

    Text is written out because prose that names cell types is read whole later,
    and re-extracting it then would be wasted work. The pointer records where it
    went, and how much of it the evidence block represents.
    """
    from atlas_chat.services.supplement_store import media_type, paper_dir
    from atlas_chat.services.supplement_triage import indexable

    out_dir = paper_dir(store_root, doi) / "text"
    units: list[Unit] = []

    for item in indexable(manifest):
        path = store_root / item["path"]
        kind = media_type(path.name)
        if kind not in PROSE_MEDIA:
            continue
        try:
            text, sections = _extract(path, kind)
        except Exception as exc:  # noqa: BLE001 - one bad file must not stop the run
            logger.warning("%s: %s", item["path"], exc)
            continue
        if not text.strip():
            logger.info("%s: no prose extracted", item["path"])
            continue

        out_dir.mkdir(parents=True, exist_ok=True)
        text_path = out_dir / f"{Path(item['path']).stem}.txt"
        text_path.write_text(text, encoding="utf-8")

        if len(text) <= READ_WHOLE_THRESHOLD:
            evidence, body = "full_text", text
        elif sections:
            evidence, body = "outline", outline_sections(sections)
        else:
            evidence, body = "sampled_text", sample_text(text)

        pointer: dict[str, Any] = {
            "file_id": item["file_id"],
            "text_file": _rel(store_root, text_path),
            "n_chars": len(text),
            "extractor": _EXTRACTOR[kind],
            "evidence": evidence,
        }
        if item.get("member_path"):
            pointer["member_path"] = item["member_path"]
        units.append(
            Unit(
                unit_id=_prose_key(pointer),
                pointer=pointer,
                evidence_block=render_evidence(path.name, body, evidence, len(text)),
            )
        )
    return units


def prepare_units(
    store_root: str | Path, doi: str, manifest: dict[str, Any] | None = None
) -> list[Unit]:
    """Every prose unit of one paper, ready to read.

    The store root is an argument, never derived: nothing here knows about
    project layouts.

    Raises:
        SupplementProseError: The paper has no manifest.
    """
    from atlas_chat.services.supplement_store import load_manifest

    root = Path(store_root)
    manifest = manifest or load_manifest(root, doi)
    if manifest is None:
        raise SupplementProseError(f"no manifest for {doi} in {root}")

    units = prose_units(root, doi, manifest)
    whole = sum(1 for u in units if u.readable_whole)
    logger.info("%s: %d prose unit(s), %d readable whole", doi, len(units), whole)
    return units


def _rel(store_root: Path, path: Path) -> str:
    try:
        return str(path.relative_to(store_root))
    except ValueError:
        return str(path)


def _prose_key(p: dict[str, Any]) -> str:
    return "|".join(("prose", p["file_id"], p.get("member_path") or ""))


# ------------------------------------------------------------------
# Taking the verdicts back
# ------------------------------------------------------------------


def apply_verdicts(units: list[Unit], verdicts: dict[str, Any]) -> AssessResult:
    """Attach one verdict per unit, and record a gap for every unit without one.

    A unit nobody read must not simply be absent from the manifest, where its
    absence reads as "there is nothing here".

    Args:
        units: What was handed out, from :func:`prepare_units`.
        verdicts: ``unit_id`` to an object carrying ``description``,
            ``mentions_cell_types`` and optionally ``mentions_cell_types_note``.

    Returns:
        AssessResult: Prose pointers, plus a gap per unread unit.
    """
    result = AssessResult()
    for unit in units:
        verdict = verdicts.get(unit.unit_id)
        try:
            if verdict is None:
                raise SupplementProseError("no verdict was returned for it")
            description, mentions, note = _read_verdict(verdict)
        except SupplementProseError as exc:
            result.gaps.append(_gap(unit, str(exc)))
            continue

        pointer = dict(unit.pointer)
        pointer["description"] = description
        pointer["mentions_cell_types"] = mentions
        if note:
            pointer["mentions_cell_types_note"] = note
        result.prose.append(pointer)

    logger.info("recorded %d prose unit(s), %d gap(s)", len(result.prose), len(result.gaps))
    return result


def _read_verdict(verdict: Any) -> tuple[str, bool, str]:
    if not isinstance(verdict, dict):
        raise SupplementProseError(f"verdict was {type(verdict).__name__}, not an object")
    description = str(verdict.get("description") or "").strip()
    if not description:
        raise SupplementProseError("verdict had no `description`")
    if "mentions_cell_types" not in verdict:
        raise SupplementProseError("verdict had no `mentions_cell_types`")
    return (
        description,
        bool(verdict["mentions_cell_types"]),
        str(verdict.get("mentions_cell_types_note") or "").strip(),
    )


def _gap(unit: Unit, why: str) -> dict[str, Any]:
    gap: dict[str, Any] = {
        "file_id": unit.pointer["file_id"],
        "reason": (
            f"{unit.unit_id} was not characterised: {why}. It is unread, not empty — "
            "read it or fold it in rather than dropping it."
        ),
        "action": f"read {unit.pointer['text_file']} and record what it contains",
    }
    if unit.pointer.get("member_path"):
        gap["member_path"] = unit.pointer["member_path"]
    return gap


def write_into_manifest(store_root: Path, doi: str, result: AssessResult) -> Path:
    """Merge prose pointers into the paper's manifest, preserving any uptake.

    ``tables`` is left alone: it is the indexing agent's to write, from the
    store's own outline and slice, and nothing here has looked at a spreadsheet.
    """
    from atlas_chat.services.supplement_store import (
        load_manifest,
        validate_manifest,
        write_manifest,
    )

    manifest = load_manifest(store_root, doi)
    if manifest is None:
        raise SupplementProseError(f"no manifest for {doi} in {store_root}")

    manifest["prose"] = _merge(manifest.get("prose") or [], result.prose)
    if result.gaps:
        manifest["gaps"] = _dedupe(list(manifest.get("gaps") or []) + result.gaps)
    validate_manifest(manifest)
    return write_manifest(store_root, doi, manifest)


def record_cas_uptake(store_root: str | Path, doi: str, unit_id: str, note: str, at: str) -> Path:
    """Note on a pointer that its content was taken into CAS+ at setup.

    Called by whatever performed the uptake, because only it knows what it took.
    The note lets a later run tell a CAS-supplied fact from a paper-found one,
    and stops a re-run re-deriving what is already curated. Works for a table
    pointer as much as a prose one — a cluster-to-name sheet is the commonest
    thing to take.

    Args:
        store_root: The supplement store.
        doi: The paper.
        unit_id: The pointer's id. Prose ids come from :func:`prepare_units`;
            a table's is ``table|<file_id>|<member_path>|<locator>``.
        note: What was taken and into which part of CAS+, in a sentence.
        at: ISO-8601 UTC timestamp of the uptake.

    Raises:
        SupplementProseError: No manifest, or no pointer with that id.
    """
    from atlas_chat.services.supplement_store import (
        load_manifest,
        validate_manifest,
        write_manifest,
    )

    root = Path(store_root)
    manifest = load_manifest(root, doi)
    if manifest is None:
        raise SupplementProseError(f"no manifest for {doi} in {root}")

    for pointer in (manifest.get("prose") or []) + (manifest.get("tables") or []):
        if _pointer_id(pointer) == unit_id:
            pointer["cas_uptake"] = {"at": at, "note": note}
            validate_manifest(manifest)
            return write_manifest(root, doi, manifest)

    raise SupplementProseError(f"no pointer with id {unit_id!r} in the {doi} manifest")


def _pointer_id(p: dict[str, Any]) -> str:
    if "text_file" in p:
        return _prose_key(p)
    return "|".join(("table", p["file_id"], p.get("member_path") or "", p.get("locator") or ""))


def _merge(existing: list[dict[str, Any]], fresh: list[dict[str, Any]]) -> list[dict[str, Any]]:
    uptake = {_prose_key(p): p["cas_uptake"] for p in existing if p.get("cas_uptake")}
    out = []
    for pointer in fresh:
        pointer = dict(pointer)
        if _prose_key(pointer) in uptake:
            pointer["cas_uptake"] = uptake[_prose_key(pointer)]
        out.append(pointer)
    return out


def _dedupe(gaps: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    out = []
    for gap in gaps:
        marker = gap.get("reason", "")
        if marker not in seen:
            seen.add(marker)
            out.append(gap)
    return out


def labels_from_cas(cas: dict[str, Any]) -> list[str]:
    """Every annotation label in a CAS+ document, de-duplicated, order preserved."""
    seen: list[str] = []
    for annotation in cas.get("annotations") or []:
        label = annotation.get("cell_label") or annotation.get("label")
        if label and label not in seen:
            seen.append(str(label))
    return seen


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="atlas_chat.cli_supplement_prose",
        description=(
            "Extract a paper's supplementary prose and hand it out to be read. "
            "Tables are not touched — they are the store's outline and slice."
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    units = sub.add_parser("units", help="the prose to read, one evidence block each")
    units.add_argument("--store", required=True, help="supplement store root")
    units.add_argument("--doi", required=True, help="paper DOI")
    units.add_argument("--cas", help="CAS+ document, to ground the cell-type question")
    units.add_argument("--out", help="write the units here instead of to stdout")

    record = sub.add_parser("record", help="merge verdicts into the paper's manifest")
    record.add_argument("--store", required=True, help="supplement store root")
    record.add_argument("--doi", required=True, help="paper DOI")
    record.add_argument("--verdicts", required=True, help="JSON file of unit_id -> verdict")

    uptake = sub.add_parser("cas-uptake", help="note that a unit fed CAS+ at setup")
    uptake.add_argument("--store", required=True, help="supplement store root")
    uptake.add_argument("--doi", required=True, help="paper DOI")
    uptake.add_argument("--unit-id", required=True, help="the pointer's unit id")
    uptake.add_argument("--note", required=True, help="what was taken, in a sentence")
    uptake.add_argument("--at", required=True, help="ISO-8601 UTC timestamp")
    return parser


def _cmd_units(args: argparse.Namespace) -> int:
    labels: list[str] = []
    if args.cas:
        labels = labels_from_cas(json.loads(Path(args.cas).read_text(encoding="utf-8")))

    units = prepare_units(args.store, args.doi)
    payload = {
        "doi": args.doi,
        "roster": roster_block(labels),
        "units": [unit.as_task() for unit in units],
    }
    text = json.dumps(payload, indent=2)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(args.out)
    else:
        print(text)
    return 0


def _cmd_record(args: argparse.Namespace) -> int:
    verdicts = json.loads(Path(args.verdicts).read_text(encoding="utf-8"))
    units = prepare_units(args.store, args.doi)
    result = apply_verdicts(units, verdicts)
    path = write_into_manifest(Path(args.store), args.doi, result)
    print(path)
    for gap in result.gaps:
        print(f"GAP: {gap['reason']}", file=sys.stderr)
    return 2 if result.gaps else 0


def _cmd_cas_uptake(args: argparse.Namespace) -> int:
    print(record_cas_uptake(args.store, args.doi, args.unit_id, args.note, args.at))
    return 0


def main(argv: list[str] | None = None) -> int:
    """Run the CLI. Returns 0 on success, 2 when some prose went unread."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = build_parser().parse_args(argv)
    handlers = {"units": _cmd_units, "record": _cmd_record, "cas-uptake": _cmd_cas_uptake}
    try:
        return handlers[args.command](args)
    except SupplementProseError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())


__all__ = [
    "AssessResult",
    "SupplementProseError",
    "Unit",
    "apply_verdicts",
    "build_parser",
    "labels_from_cas",
    "main",
    "merge_sections",
    "outline_sections",
    "prepare_units",
    "prose_units",
    "record_cas_uptake",
    "render_evidence",
    "roster_block",
    "sample_text",
    "write_into_manifest",
]
