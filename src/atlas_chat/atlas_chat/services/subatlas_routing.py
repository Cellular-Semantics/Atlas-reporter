"""Where a set of atlas cell sets got their cells from, arranged by the read.

An atlas made by integrating other studies inherits many of its cell sets'
names and most of their cells from those studies, and CAS+ records that per
cell set: for each contributing study, which of *its* labels the cells carried,
how many, and the three overlap measures described in ``docs/subatlas_measures.md``.
Asked the obvious way round — for each cell set, which papers fed it — the
answer is unusable at any realistic size. Asking for reports on the fibroblasts
of one atlas reaches 69 cell sets and a couple of thousand rows of provenance.

Turned round, it is small. Key it by the contributing study and the label, and
list the cell sets that label fed: the same evidence comes to seventy-odd
entries, because one study's label commonly feeds a dozen of the atlas's cell
sets and reading that paper once answers for all of them.

**Nothing here is measured.** The measures are counted at ingest, stored in
CAS+ beside the counts they divide, and checked on write; this carries them
through. The temptation to recompute one in passing will recur, and giving in
to it puts a second answer to the same question in a second place.

What is done here is selection and arrangement: resolve the request, apply the
floor and the synonym exemption, invert to (paper, label), and account for
everything left over. None of that can see what a label *means* — a label
feeding twenty cell sets usually does so by being vague, a label covering a few
hundred cells is sometimes the one the population was named after — which is
why this produces a table and stops. Deciding between them is the routing
agent's job.

One thing is carried that no count could produce: where the atlas records a
contributing study's label among a cell set's synonyms, the authors are
asserting the two name the same cells. Those rows are kept whatever their size.

Nothing here calls a model.
"""

from __future__ import annotations

import argparse
import json
import logging
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

from atlas_chat.services.subject_block import build as build_subject_block
from atlas_chat.services.subject_block import relations

logger = logging.getLogger(__name__)

#: Overlaps smaller than this are left out, unless the atlas names the
#: contributing study's label as a synonym of the cell set.
DEFAULT_MIN_OVERLAP_CELLS = 50

#: Measure on a CAS+ transferred annotation -> name it is carried under here.
#: cell_ratio is the third measure; the table says which denominator it uses,
#: while CAS+ keeps the name for parallelism with CompositionValue.cell_ratio.
MEASURES = {
    "share_of_subatlas_contribution": "share_of_subatlas_contribution",
    "share_of_subatlas_label": "share_of_subatlas_label",
    "cell_ratio": "share_of_atlas_cell_set",
}

_DOI_PREFIX = re.compile(r"^doi:\s*", re.IGNORECASE)


class RoutingError(RuntimeError):
    """Raised when the requested cell sets cannot be resolved."""


# ------------------------------------------------------------------
# naming
# ------------------------------------------------------------------


def normalise_label(label: str) -> str:
    """Fold a cell-set label for comparison without losing a marker's sign.

    Separators and case vary freely between an atlas and the studies it
    integrates — ``ePV2`` and ``ePV_2`` are one cell set — so both are folded
    away. A trailing ``+`` or ``-`` is not: ``PV-MYH11_CDKN1A+`` and
    ``PV-MYH11_CDKN1A-`` are opposite marker states, and folding them together
    would match a synonym to the population it was defined against.

    Args:
        label: the label as written.

    Returns:
        The folded form, for equality comparison only.
    """
    text = label.strip().casefold()
    sign = text[-1] if text[-1:] in "+-" else ""
    if sign:
        text = text[: -len(sign)]
    text = re.sub(r"[_\-/\s]+", "", text)
    return text + sign


def paper_key(transfer: dict[str, Any]) -> str:
    """The contributing study a transferred annotation names, verbatim.

    ``subatlas_paper`` is the field for it; ``source_labelset`` is the obs
    column the study's labels came from and is what a populated registry keys
    on; ``source_taxonomy`` carries the study where neither is set.

    Args:
        transfer: one ``transferred_annotations`` entry.

    Returns:
        The study as named, or the empty string where no field identifies one.
    """
    return str(
        transfer.get("subatlas_paper")
        or transfer.get("source_labelset")
        or transfer.get("source_taxonomy")
        or ""
    )


def _doi(key: str, registered: dict[str, Any], transfer: dict[str, Any]) -> str | None:
    """The DOI for a study, from whichever of three places names one.

    The registry is the authority where a document has one. Without it the key
    is the obs column the study's labels came from — which identifies the study
    but is not resolvable — so the DOI has to come off the transfer itself.
    Missing it there would make every contributor of an un-enriched document
    unreadable, which is a much larger claim than the document supports.
    """
    if registered.get("doi"):
        return str(registered["doi"])
    for candidate in (
        key,
        transfer.get("source_taxonomy") or "",
        transfer.get("subatlas_paper") or "",
    ):
        stripped = _DOI_PREFIX.sub("", str(candidate)).strip()
        if stripped.startswith("10."):
            return stripped
    return None


# ------------------------------------------------------------------
# resolving the request
# ------------------------------------------------------------------


def resolve_requested(
    cas_doc: dict[str, Any],
    cell_labels: list[str] | None = None,
    accessions: list[str] | None = None,
) -> list[dict[str, Any]]:
    """The annotations reports were asked for, in the order asked for.

    Args:
        cas_doc: the CAS+ document.
        cell_labels: labels to resolve. An atlas may use the same label at two
            levels, and picking either would be wrong, so an ambiguous label is
            refused rather than resolved.
        accessions: accessions to resolve, which are never ambiguous.

    Returns:
        The annotations. All of them where neither argument is given.

    Raises:
        RoutingError: a label or accession is not in the document, or a label
            names more than one cell set.
    """
    annotations = cas_doc.get("annotations") or []
    if not cell_labels and not accessions:
        return list(annotations)

    by_accession = {a["cell_set_accession"]: a for a in annotations if a.get("cell_set_accession")}
    by_label: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for annotation in annotations:
        by_label[annotation["cell_label"]].append(annotation)

    out: list[dict[str, Any]] = []
    problems: list[str] = []
    for accession in accessions or []:
        if accession in by_accession:
            out.append(by_accession[accession])
        else:
            problems.append(f"no cell set with accession {accession}")
    for label in cell_labels or []:
        matches = by_label.get(label) or []
        if not matches:
            problems.append(f"no cell set labelled {label!r}")
        elif len(matches) > 1:
            where = ", ".join(f"{m.get('labelset')} {m.get('cell_set_accession')}" for m in matches)
            problems.append(
                f"{label!r} names {len(matches)} cell sets ({where}) — ask by accession"
            )
        else:
            out.append(matches[0])
    if problems:
        raise RoutingError("; ".join(problems))
    return out


# ------------------------------------------------------------------
# the table
# ------------------------------------------------------------------


def _registry_index(cas_doc: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Registered contributing studies, reachable by label and by DOI."""
    index: dict[str, dict[str, Any]] = {}
    for paper in (cas_doc.get("source") or {}).get("subatlas_papers") or []:
        if paper.get("label"):
            index[str(paper["label"])] = paper
        if paper.get("doi"):
            index[str(paper["doi"])] = paper
    return index


def _measures(transfer: dict[str, Any]) -> dict[str, float]:
    """The stored overlap measures, under the names this table uses.

    Absent measures are absent, not estimated: a project whose registry has not
    been populated has no atlas-wide denominator, and the recall side of the
    overlap genuinely cannot be stated.
    """
    return {
        name: float(transfer[field])
        for field, name in MEASURES.items()
        if transfer.get(field) is not None
    }


def build_table(
    cas_doc: dict[str, Any],
    cell_labels: list[str] | None = None,
    accessions: list[str] | None = None,
    *,
    min_overlap_cells: int = DEFAULT_MIN_OVERLAP_CELLS,
    cas_source: str | None = None,
) -> dict[str, Any]:
    """Arrange the provenance of the requested cell sets by the read.

    Args:
        cas_doc: the CAS+ document.
        cell_labels: labels of the cell sets reports were asked for.
        accessions: accessions of the same, for labels used at two levels.
        min_overlap_cells: floor on an overlap, below which a contribution is
            rolled up rather than asked about. Rows the atlas names as a
            synonym are kept whatever their size.
        cas_source: path to record on the table.

    Returns:
        The routing table, conforming to ``subatlas_routing_table.schema.json``.

    Raises:
        RoutingError: the request could not be resolved against the document.
    """
    requested = resolve_requested(cas_doc, cell_labels, accessions)
    registry = _registry_index(cas_doc)
    label_of, children = relations(cas_doc.get("annotations") or [])

    questions: dict[tuple[str, str], dict[str, Any]] = {}
    papers: dict[str, dict[str, Any]] = {}
    dropped: dict[str, dict[str, Any]] = {}
    unreadable: dict[str, dict[str, Any]] = {}
    served: dict[str, int] = defaultdict(int)
    dropped_per_cell_set: dict[str, int] = defaultdict(int)
    rows_per_cell_set: dict[str, int] = defaultdict(int)

    for annotation in requested:
        label = annotation["cell_label"]
        transfers = annotation.get("transferred_annotations") or []
        rows_per_cell_set[label] = len(transfers)
        synonyms = {normalise_label(s) for s in annotation.get("synonyms") or []}

        for transfer in transfers:
            study = paper_key(transfer)
            upstream = str(transfer.get("transferred_cell_label", ""))
            overlap = int(transfer.get("cell_count") or 0)
            is_synonym = normalise_label(upstream) in synonyms
            registered = registry.get(study) or {}
            doi = _doi(study, registered, transfer)

            if doi is None:
                entry = unreadable.setdefault(
                    study, {"subatlas_paper": study, "overlap_cells": 0, "reached": set()}
                )
                entry["overlap_cells"] += overlap
                entry["reached"].add(label)
                continue

            if overlap < min_overlap_cells and not is_synonym:
                roll = dropped.setdefault(
                    study, {"subatlas_paper": study, "n_subatlas_labels": 0, "overlap_cells": 0}
                )
                roll["n_subatlas_labels"] += 1
                roll["overlap_cells"] += overlap
                dropped_per_cell_set[label] += overlap
                continue

            # Labelset is not repeated here: it is on the requested cell set,
            # and the accession is what disambiguates a label used at two levels.
            claimant: dict[str, Any] = {"cell_label": label, "overlap_cells": overlap}
            if annotation.get("cell_set_accession"):
                claimant["cell_set_accession"] = annotation["cell_set_accession"]
            claimant.update(_measures(transfer))
            if is_synonym:
                claimant["named_as_synonym"] = True

            question = questions.setdefault(
                (study, upstream), _new_question(study, upstream, transfer)
            )
            question["atlas_cell_sets"].append(claimant)
            served[label] += 1

            paper = papers.setdefault(study, _new_paper(study, doi, registered))
            paper["cells_contributed"] += overlap
            paper["_reached"].add(label)

    for study, _ in questions:
        papers[study]["_n_questions"] += 1

    table: dict[str, Any] = {
        "min_overlap_cells": min_overlap_cells,
        "requested": [
            _describe(a, label_of=label_of, children=children, min_ratio=0.01) for a in requested
        ],
        "papers": _finish_papers(papers),
        "questions": _ordered(questions, papers),
        "atlas_only": _atlas_only(
            requested, served, rows_per_cell_set, dropped_per_cell_set, unreadable
        ),
    }
    if cas_source:
        table["cas_source"] = cas_source
    source = cas_doc.get("source") or {}
    if source.get("doi"):
        atlas: dict[str, Any] = {"doi": str(source["doi"])}
        if source.get("title"):
            atlas["title"] = str(source["title"])
        table["atlas_paper"] = atlas
    if dropped:
        table["dropped"] = sorted(dropped.values(), key=lambda d: -d["overlap_cells"])
    if unreadable:
        table["unreadable"] = [
            {
                "subatlas_paper": entry["subatlas_paper"],
                "overlap_cells": entry["overlap_cells"],
                "n_atlas_cell_sets": len(entry["reached"]),
            }
            for entry in sorted(unreadable.values(), key=lambda u: -u["overlap_cells"])
        ]
    return table


def _describe(
    annotation: dict[str, Any],
    *,
    label_of: dict[str, str],
    children: dict[str, list[str]],
    min_ratio: float,
) -> dict[str, Any]:
    """The identity of a requested cell set, as a reader would be given it.

    Assembled by the same code that prepares a reading agent's subject block,
    minus the sampling context. Children are kept because they are what tell
    "the atlas subdivides this" apart from "the contributing study subdivides
    this", which is what most of the interesting overlaps turn on. Context is
    dropped: which organ a cell set was sampled from says little about which
    paper to read, and across a selection of any size it is both repetitive and
    the largest single thing in the table.
    """
    block = build_subject_block(
        annotation, label_of=label_of, children=children, min_ratio=min_ratio
    )
    block.pop("context", None)
    if annotation.get("cell_set_accession"):
        block["cell_set_accession"] = annotation["cell_set_accession"]
    return block


def _new_question(study: str, upstream: str, transfer: dict[str, Any]) -> dict[str, Any]:
    """A question about one of a contributing study's labels, before claimants.

    Carries no identity of its own — that is on the paper, which is read once
    however many of its labels are asked about.
    """
    question: dict[str, Any] = {
        "subatlas_paper": study,
        "subatlas_cell_label": upstream,
        "atlas_cell_sets": [],
    }
    if transfer.get("source_labelset"):
        question["source_labelset"] = str(transfer["source_labelset"])
    if transfer.get("subatlas_label_total_cells") is not None:
        question["subatlas_label_total_cells"] = int(transfer["subatlas_label_total_cells"])
    return question


def _new_paper(study: str, doi: str, registered: dict[str, Any]) -> dict[str, Any]:
    """A contributing paper, with whatever the registry knows about it."""
    paper: dict[str, Any] = {
        "subatlas_paper": study,
        "doi": doi,
        "cells_contributed": 0,
        "_reached": set(),
        "_n_questions": 0,
    }
    for field in ("first_author", "year", "title", "venue", "status"):
        if registered.get(field) is not None:
            paper[field] = registered[field]
    band = (registered.get("asta_indexing") or {}).get("band")
    if band:
        paper["asta_band"] = band
    if registered.get("total_cells") is not None:
        paper["total_cells_in_atlas"] = registered["total_cells"]
    return paper


def _finish_papers(papers: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """Papers in contribution order, with the working fields turned into counts."""
    out = []
    for paper in sorted(papers.values(), key=lambda p: -p["cells_contributed"]):
        finished = {k: v for k, v in paper.items() if not k.startswith("_")}
        finished["n_atlas_cell_sets_reached"] = len(paper["_reached"])
        finished["n_questions"] = paper["_n_questions"]
        out.append(finished)
    return out


def _ordered(
    questions: dict[tuple[str, str], dict[str, Any]], papers: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    """Questions grouped by study, largest contributor first, since a paper is read once."""
    out = sorted(
        questions.values(),
        key=lambda q: (
            -papers[q["subatlas_paper"]]["cells_contributed"],
            q["subatlas_paper"],
            -sum(c["overlap_cells"] for c in q["atlas_cell_sets"]),
        ),
    )
    for question in out:
        question["atlas_cell_sets"].sort(key=lambda c: -c["overlap_cells"])
    return out


def _atlas_only(
    requested: list[dict[str, Any]],
    served: dict[str, int],
    rows_per_cell_set: dict[str, int],
    dropped_per_cell_set: dict[str, int],
    unreadable: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Requested cell sets with no contributing paper to read, and why.

    The three reasons are different findings. No provenance at all means the
    atlas built the cell set from its own data. Contributions that all fell
    below the floor mean several studies put cells here without any of their
    labels corresponding to it. A contribution with no DOI means there is a
    source and it cannot be read.
    """
    out: list[dict[str, Any]] = []
    for annotation in requested:
        label = annotation["cell_label"]
        if served.get(label):
            continue
        if not rows_per_cell_set.get(label):
            reason = "no_provenance"
        elif dropped_per_cell_set.get(label):
            reason = "all_below_floor"
        elif unreadable:
            reason = "no_readable_source"
        else:
            reason = "all_below_floor"
        entry: dict[str, Any] = {"cell_label": label, "reason": reason}
        if annotation.get("labelset"):
            entry["labelset"] = annotation["labelset"]
        if annotation.get("cell_set_accession"):
            entry["cell_set_accession"] = annotation["cell_set_accession"]
        if dropped_per_cell_set.get(label):
            entry["overlap_cells_dropped"] = dropped_per_cell_set[label]
        out.append(entry)
    return out


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------


def summarise(table: dict[str, Any]) -> str:
    """A few lines saying what the table came to, for a reader at a terminal."""
    claimants = [c for q in table["questions"] for c in q["atlas_cell_sets"]]
    lines = [
        f"{len(table['requested'])} cell sets requested",
        f"{len(table['questions'])} questions across {len(table['papers'])} papers",
    ]
    without = sum(1 for c in claimants if "share_of_subatlas_label" not in c)
    if claimants and without:
        lines.append(
            f"{without} of {len(claimants)} overlaps carry no share_of_subatlas_label — "
            "the document's subatlas registry is not populated"
        )
    if table["atlas_only"]:
        reasons: dict[str, int] = defaultdict(int)
        for entry in table["atlas_only"]:
            reasons[entry["reason"]] += 1
        detail = ", ".join(f"{count} {reason}" for reason, count in sorted(reasons.items()))
        lines.append(f"{len(table['atlas_only'])} atlas-paper-only ({detail})")
    for entry in table.get("unreadable") or []:
        lines.append(
            f"no DOI to read: {entry['subatlas_paper']} — "
            f"{entry['overlap_cells']:,} cells across "
            f"{entry['n_atlas_cell_sets']} of the requested cell sets"
        )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m atlas_chat.cli_route",
        description="Arrange the provenance of requested cell sets by the read.",
    )
    parser.add_argument("--cas", required=True, help="the CAS+ document")
    parser.add_argument(
        "--label", action="append", help="repeatable; all cell sets when nothing is named"
    )
    parser.add_argument(
        "--accession", action="append", help="repeatable; for a label used at two levels"
    )
    parser.add_argument("--out", help="write JSON here instead of stdout")
    parser.add_argument(
        "--min-overlap-cells",
        type=int,
        default=DEFAULT_MIN_OVERLAP_CELLS,
        help=(
            "floor on an overlap; rows the atlas names as a synonym are kept regardless "
            f"(default {DEFAULT_MIN_OVERLAP_CELLS})"
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cas_doc = json.loads(Path(args.cas).read_text(encoding="utf-8"))
    try:
        table = build_table(
            cas_doc,
            args.label,
            args.accession,
            min_overlap_cells=args.min_overlap_cells,
            cas_source=args.cas,
        )
    except RoutingError as exc:
        print(str(exc))
        return 2
    payload = json.dumps(table, indent=2)
    if args.out:
        Path(args.out).write_text(payload + "\n", encoding="utf-8")
        print(summarise(table))
        print(f"-> {args.out}")
    else:
        print(payload)
    return 0
