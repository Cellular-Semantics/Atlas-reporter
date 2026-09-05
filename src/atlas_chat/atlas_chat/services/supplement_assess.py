"""Prepare a paper's supplementary material to be judged, and record the verdicts.

``triage --sheets`` fills every mechanical field of a pointer and leaves one
blank: ``description``. On a forty-table bundle that is forty judgements, and
they are shallow ones — read the columns, say what the table is for. This module
does everything around those judgements and none of them: it opens the files,
bounds what is read, renders each unit into a block a reader can judge from, and
merges the verdicts back into the manifest.

The judging is not here. It is a cheap-model subagent, driven by the
``index-supplements`` skill: ``units`` hands out the evidence, ``record`` takes
the verdicts back. Nothing in this module calls a model or needs an API key.

Two answers are wanted per unit — what it contains, and whether it names cell
types — because the second decides how the unit is used, and that follows the
format:

* **Prose** that names cell types is read *whole*, alongside the paper text.
  There is nothing to slice and the documents are small: Gopee's table-legends
  and discussion come to about 15 KB together.
* **Tables** are never folded into a context. They get a description and their
  columns, and a reader slices what it needs when it needs it.

So there is no fold-in scale to estimate, only a boolean, and only prose acts on
it. What a unit *contains* still needs saying either way.

Bounded reads are the hazard throughout. A sheet is judged from its columns and
a few rows, a very long document from a sample, so "no cell types here" is a
statement about what was seen and never about the file. Each unit says which it
was, so a bounded negative cannot harden into a claim that the file is empty.

Spreadsheets need the ``supplements`` extra; PDFs need ``text-access``.
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

#: Prose is sampled rather than read whole above this many characters. Set well
#: above a typical legends or discussion document, so the common case is judged
#: on the complete text and `evidence` says so.
PROSE_SAMPLE_THRESHOLD = 24_000

#: Characters kept when a document is over the threshold, split across its head,
#: middle and tail. A legends document lists tables in order, so reading only
#: the head would characterise the first few and miss the rest.
PROSE_SAMPLE_BUDGET = 12_000

#: Cell-type labels passed to the judge as context. Above this many, the roster
#: stops being context and becomes the bulk of the prompt, so the question is
#: asked in general terms instead.
ROSTER_PROMPT_CAP = 150

#: Sample rows shown per sheet. Enough to see what the columns actually hold.
SHEET_SAMPLE_ROWS = 5

#: Media types read as prose. `txt` appears here and in triage's INSPECTABLE:
#: a text file may be either, and is recorded as whichever it yields.
PROSE_MEDIA = {"docx", "pdf", "txt"}

#: Maps a media type to the `extractor` recorded on the pointer.
_EXTRACTOR = {"docx": "docx", "pdf": "pdf", "txt": "plaintext"}


class SupplementAssessError(RuntimeError):
    """Units could not be prepared, or verdicts could not be recorded."""


@dataclass
class Unit:
    """One thing to judge: a stable id, the draft pointer, and the evidence."""

    unit_id: str
    kind: str  # "table" | "prose"
    pointer: dict[str, Any]
    evidence_block: str

    def as_task(self) -> dict[str, Any]:
        """The shape handed to a judge — an id and what to read, nothing else."""
        return {"unit_id": self.unit_id, "kind": self.kind, "evidence": self.evidence_block}


@dataclass
class AssessResult:
    """Pointers ready to write into a manifest, and what could not be done."""

    tables: list[dict[str, Any]] = field(default_factory=list)
    prose: list[dict[str, Any]] = field(default_factory=list)
    gaps: list[dict[str, Any]] = field(default_factory=list)


# ------------------------------------------------------------------
# Sampling and rendering — pure
# ------------------------------------------------------------------


def sample_prose(
    text: str,
    threshold: int = PROSE_SAMPLE_THRESHOLD,
    budget: int = PROSE_SAMPLE_BUDGET,
) -> tuple[str, bool]:
    """Reduce a document to something cheap to read, or leave it whole.

    Takes equal parts from the head, the middle and the tail rather than a
    prefix. A legends document describes its tables in order, so a prefix
    characterises the first few and says nothing about the rest — and the
    verdict wanted here is about the whole document.

    Args:
        text: The full extracted text.
        threshold: Documents at or below this length are returned unchanged.
        budget: Characters to keep when sampling.

    Returns:
        The text to show a judge, and whether it is the complete document.
    """
    if len(text) <= threshold:
        return text, True

    part = budget // 3
    middle = (len(text) - part) // 2
    marker = "\n\n[...]\n\n"
    sampled = marker.join((text[:part], text[middle : middle + part], text[-part:]))
    return sampled, False


def render_sheet(candidate: dict[str, Any], rows: list[list[str]]) -> str:
    """The bounded view of a sheet a judge is shown.

    Cost is flat in the size of the file: the columns and a handful of rows,
    with the true dimensions stated so the judge can see it is looking at the
    corner of a large table rather than at a small one.
    """
    columns = ", ".join(c["name"] for c in candidate.get("columns") or []) or "(none read)"
    lines = [
        f"Kind: spreadsheet sheet (a bounded view — {candidate.get('n_rows', 0)} data "
        f"rows and {candidate.get('n_columns', 0)} columns in total)",
        f"Sheet: {candidate.get('locator') or '(single table)'}",
        f"Columns: {columns}",
    ]
    if candidate.get("relevance_note"):
        lines.append(f"Column-pattern guess: {candidate['relevance_note']}")
    if rows:
        lines.append(f"First {len(rows)} data rows:")
        lines += ["  " + " | ".join(str(cell) for cell in row) for row in rows]
    return "\n".join(lines)


def render_prose(name: str, text: str, complete: bool) -> str:
    """The view of a document a judge is shown, saying plainly if it is partial."""
    what = (
        "complete text"
        if complete
        else "A SAMPLE — head, middle and tail only; the parts between were not shown"
    )
    return f"Kind: document prose ({what})\nFile: {name}\n\nText:\n{text}"


def roster_block(labels: list[str], cap: int = ROSTER_PROMPT_CAP) -> str:
    """Ground the cell-type question in the project's own labels, where it fits.

    Real labels are what let a judge recognise ``LC_1`` or ``mCL2`` as a cell
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


# ------------------------------------------------------------------
# Building units from a store
# ------------------------------------------------------------------


def prose_units(store_root: Path, doi: str, manifest: dict[str, Any]) -> list[Unit]:
    """Extract every prose-bearing supplement and prepare it to be judged.

    Text is written to disk under the paper's directory, because prose that
    names cell types is meant to be read whole later and re-extracting it then
    would be wasted work. The pointer records where it went.
    """
    from atlas_chat.services.supplement_store import extract_text, paper_dir
    from atlas_chat.services.supplement_triage import indexable

    out_dir = paper_dir(store_root, doi) / "text"
    units: list[Unit] = []

    for item in indexable(manifest):
        path = store_root / item["path"]
        kind = _media_type(path.name)
        if kind not in PROSE_MEDIA:
            continue
        try:
            result = extract_text(path, max_chars=2_000_000)
        except Exception as exc:  # noqa: BLE001 - one bad file must not stop the run
            logger.warning("%s: %s", item["path"], exc)
            continue
        text = result.get("text") or ""
        if not text.strip():
            logger.info("%s: no prose (%s)", item["path"], result.get("note") or "empty")
            continue

        out_dir.mkdir(parents=True, exist_ok=True)
        text_path = out_dir / f"{Path(item['path']).stem}.txt"
        text_path.write_text(text, encoding="utf-8")

        shown, complete = sample_prose(text)
        pointer: dict[str, Any] = {
            "file_id": item["file_id"],
            "text_file": _rel(store_root, text_path),
            "n_chars": len(text),
            "extractor": _EXTRACTOR[kind],
            "evidence": "full_text" if complete else "sampled_text",
        }
        if item.get("member_path"):
            pointer["member_path"] = item["member_path"]
        units.append(
            Unit(
                unit_id=_prose_key(pointer),
                kind="prose",
                pointer=pointer,
                evidence_block=render_prose(path.name, shown, complete),
            )
        )
    return units


def table_units(store_root: Path, doi: str, manifest: dict[str, Any]) -> list[Unit]:
    """Draft pointers from triage, each with a few sample rows for the judge."""
    from atlas_chat.services.supplement_store import SupplementStoreError, outline_file
    from atlas_chat.services.supplement_triage import sheet_candidates

    rows_by_key = _sample_rows(store_root, manifest, outline_file, SupplementStoreError)
    units: list[Unit] = []
    for candidate in sheet_candidates(store_root, doi, manifest):
        key = (candidate["file_id"], candidate.get("member_path"), candidate.get("locator"))
        rows = rows_by_key.get(key, [])
        pointer = {**candidate, "evidence": "rows_read" if rows else "headers"}
        units.append(
            Unit(
                unit_id=_table_key(pointer),
                kind="table",
                pointer=pointer,
                evidence_block=render_sheet(candidate, rows),
            )
        )
    return units


def prepare_units(
    store_root: str | Path, doi: str, manifest: dict[str, Any] | None = None
) -> list[Unit]:
    """Every table and prose unit of one paper, ready to be judged.

    The store root is an argument, never derived: nothing here knows about
    project layouts.

    Raises:
        SupplementAssessError: The paper has no manifest.
    """
    from atlas_chat.services.supplement_store import load_manifest

    root = Path(store_root)
    manifest = manifest or load_manifest(root, doi)
    if manifest is None:
        raise SupplementAssessError(f"no manifest for {doi} in {root}")

    units = table_units(root, doi, manifest) + prose_units(root, doi, manifest)
    logger.info("%s: %d unit(s) to judge", doi, len(units))
    return units


def _sample_rows(
    store_root: Path,
    manifest: dict[str, Any],
    outline_file: Any,
    store_error: type[Exception],
) -> dict[tuple[str, str | None, str | None], list[list[str]]]:
    """A few data rows per sheet, keyed the way a candidate identifies itself."""
    from atlas_chat.services.supplement_triage import INSPECTABLE

    out: dict[tuple[str, str | None, str | None], list[list[str]]] = {}
    for entry in manifest.get("files", []):
        for item in entry.get("members") or [entry]:
            path, kind = item.get("path"), item.get("media_type") or ""
            if not path or kind not in INSPECTABLE:
                continue
            try:
                outline = outline_file(store_root / path, sample_rows=8, max_cols=60)
            except store_error:
                continue
            member = item.get("member_path") if item is not entry else None
            for table in outline.get("tables") or []:
                header = table.get("header_row_guess", 0)
                rows = (table.get("rows") or [])[header + 1 :]
                out[(entry["file_id"], member, table.get("locator"))] = rows[:SHEET_SAMPLE_ROWS]
    return out


def _media_type(name: str) -> str:
    from atlas_chat.services.supplement_store import media_type

    return media_type(name)


def _rel(store_root: Path, path: Path) -> str:
    try:
        return str(path.relative_to(store_root))
    except ValueError:
        return str(path)


def _table_key(p: dict[str, Any]) -> str:
    return "|".join(("table", p["file_id"], p.get("member_path") or "", p.get("locator") or ""))


def _prose_key(p: dict[str, Any]) -> str:
    return "|".join(("prose", p["file_id"], p.get("member_path") or ""))


# ------------------------------------------------------------------
# Taking the verdicts back
# ------------------------------------------------------------------


def apply_verdicts(units: list[Unit], verdicts: dict[str, Any]) -> AssessResult:
    """Attach one verdict per unit, and record a gap for every unit without one.

    A unit nobody judged must not simply be absent from the manifest, where its
    absence reads as "there is nothing here".

    Args:
        units: What was handed out, from :func:`prepare_units`.
        verdicts: ``unit_id`` to an object carrying ``description``,
            ``mentions_cell_types`` and optionally ``mentions_cell_types_note``.

    Returns:
        AssessResult: Pointers by kind, plus a gap per unjudged unit.
    """
    result = AssessResult()
    for unit in units:
        verdict = verdicts.get(unit.unit_id)
        try:
            if verdict is None:
                raise SupplementAssessError("no verdict was returned for it")
            description, mentions, note = _read_verdict(verdict)
        except SupplementAssessError as exc:
            result.gaps.append(_gap(unit, str(exc)))
            continue

        pointer = dict(unit.pointer)
        pointer["description"] = description
        pointer["mentions_cell_types"] = mentions
        if note:
            pointer["mentions_cell_types_note"] = note
        (result.prose if unit.kind == "prose" else result.tables).append(pointer)

    logger.info(
        "recorded %d table(s), %d prose unit(s), %d gap(s)",
        len(result.tables),
        len(result.prose),
        len(result.gaps),
    )
    return result


def _read_verdict(verdict: Any) -> tuple[str, bool, str]:
    if not isinstance(verdict, dict):
        raise SupplementAssessError(f"verdict was {type(verdict).__name__}, not an object")
    description = str(verdict.get("description") or "").strip()
    if not description:
        raise SupplementAssessError("verdict had no `description`")
    if "mentions_cell_types" not in verdict:
        raise SupplementAssessError("verdict had no `mentions_cell_types`")
    return (
        description,
        bool(verdict["mentions_cell_types"]),
        str(verdict.get("mentions_cell_types_note") or "").strip(),
    )


def _gap(unit: Unit, why: str) -> dict[str, Any]:
    gap: dict[str, Any] = {
        "file_id": unit.pointer["file_id"],
        "reason": (
            f"{unit.unit_id} was not assessed: {why}. It is unjudged, not empty — "
            "index or fold it in rather than dropping it."
        ),
        "action": "re-run the assessment for this paper",
    }
    if unit.pointer.get("member_path"):
        gap["member_path"] = unit.pointer["member_path"]
    return gap


def write_into_manifest(store_root: Path, doi: str, result: AssessResult) -> Path:
    """Merge assessed pointers into the paper's manifest, preserving any uptake.

    A ``cas_uptake`` note already on a pointer survives a re-assessment: it
    records something a later step did, which this pass knows nothing about and
    must not erase.
    """
    from atlas_chat.services.supplement_store import (
        load_manifest,
        validate_manifest,
        write_manifest,
    )

    manifest = load_manifest(store_root, doi)
    if manifest is None:
        raise SupplementAssessError(f"no manifest for {doi} in {store_root}")

    manifest["tables"] = _merge(manifest.get("tables") or [], result.tables, _table_key)
    manifest["prose"] = _merge(manifest.get("prose") or [], result.prose, _prose_key)
    if result.gaps:
        manifest["gaps"] = _dedupe(list(manifest.get("gaps") or []) + result.gaps)
    validate_manifest(manifest)
    return write_manifest(store_root, doi, manifest)


def record_cas_uptake(store_root: str | Path, doi: str, unit_id: str, note: str, at: str) -> Path:
    """Note on a pointer that its content was taken into CAS+ at setup.

    Called by whatever performed the uptake, because only it knows what it took.
    The note lets a later run tell a CAS-supplied fact from a paper-found one,
    and stops a re-run re-deriving what is already curated.

    Args:
        store_root: The supplement store.
        doi: The paper.
        unit_id: The pointer's id, as :func:`prepare_units` issued it.
        note: What was taken and into which part of CAS+, in a sentence.
        at: ISO-8601 UTC timestamp of the uptake.

    Raises:
        SupplementAssessError: No manifest, or no pointer with that id.
    """
    from atlas_chat.services.supplement_store import (
        load_manifest,
        validate_manifest,
        write_manifest,
    )

    root = Path(store_root)
    manifest = load_manifest(root, doi)
    if manifest is None:
        raise SupplementAssessError(f"no manifest for {doi} in {root}")

    for pointers, key in (
        (manifest.get("tables") or [], _table_key),
        (manifest.get("prose") or [], _prose_key),
    ):
        for pointer in pointers:
            if key(pointer) == unit_id:
                pointer["cas_uptake"] = {"at": at, "note": note}
                validate_manifest(manifest)
                return write_manifest(root, doi, manifest)

    raise SupplementAssessError(f"no pointer with id {unit_id!r} in the {doi} manifest")


def _merge(
    existing: list[dict[str, Any]], fresh: list[dict[str, Any]], key: Any
) -> list[dict[str, Any]]:
    uptake = {key(p): p["cas_uptake"] for p in existing if p.get("cas_uptake")}
    out = []
    for pointer in fresh:
        pointer = dict(pointer)
        if key(pointer) in uptake:
            pointer["cas_uptake"] = uptake[key(pointer)]
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
        prog="atlas_chat.cli_supplement_assess",
        description=(
            "Hand out a paper's supplementary material to be judged, and take the "
            "verdicts back. The judging happens elsewhere; nothing here calls a model."
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    units = sub.add_parser("units", help="the units to judge, one evidence block each")
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
    """Run the CLI. Returns 0 on success, 2 when some units went unjudged."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = build_parser().parse_args(argv)
    handlers = {"units": _cmd_units, "record": _cmd_record, "cas-uptake": _cmd_cas_uptake}
    try:
        return handlers[args.command](args)
    except SupplementAssessError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())


__all__ = [
    "AssessResult",
    "SupplementAssessError",
    "Unit",
    "apply_verdicts",
    "build_parser",
    "labels_from_cas",
    "main",
    "prepare_units",
    "prose_units",
    "record_cas_uptake",
    "render_prose",
    "render_sheet",
    "roster_block",
    "sample_prose",
    "table_units",
    "write_into_manifest",
]
