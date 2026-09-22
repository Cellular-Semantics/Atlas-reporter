"""Where a set of atlas cell sets got their cells from, arranged by the read.

An atlas made by integrating other studies inherits many of its cell sets'
names and most of their cells from those studies, and CAS+ records that per
cell set: for each contributing study, which of *its* labels the cells carried.
Asked the obvious way round — for each cell set, which papers fed it — the
answer is unusable at any realistic size. Asking for reports on the fibroblasts
of one atlas reaches 69 cell sets and a couple of thousand rows of provenance.

Turned round, it is small. Key it by the contributing study and the label, and
list the cell sets that label fed: the same evidence comes to ninety-odd
entries, because one study's label commonly feeds a dozen of the atlas's cell
sets and reading that paper once answers for all of them.

Two numbers are recorded against every claim, and they answer different
questions:

* **share_of_contribution** — of the cells this study put into this atlas cell
  set, the share carrying this label. Its denominator is that study's
  contribution and not the whole cell set, because the rest of the cell set
  came from studies that never saw these cells.
* **share_of_subatlas_label** — of every cell this study gave this label
  anywhere in the atlas, the share that ended up here. Its denominator is
  atlas-wide, so it needs a set of cell sets covering every cell exactly once;
  where none can be validated it is simply absent, never guessed.

Neither number can see what a label means, which is why this produces a table
and stops. A label feeding twenty cell sets usually does so by being vague; a
label covering a few hundred cells is sometimes the one the population was
named after. Deciding between them is the routing agent's job.

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

logger = logging.getLogger(__name__)

#: Overlaps smaller than this are left out, unless the atlas names the
#: contributing study's label as a synonym of the cell set.
DEFAULT_MIN_OVERLAP_CELLS = 50

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

    ``subatlas_paper`` is the field for it; ``source_taxonomy`` carries the
    same study where a document predates that field, so it is the fallback.

    Args:
        transfer: one ``transferred_annotations`` entry.

    Returns:
        The study as named, or the empty string where neither field is set.
    """
    return str(transfer.get("subatlas_paper") or transfer.get("source_taxonomy") or "")


def _doi(key: str) -> str | None:
    """The DOI a study key carries, where it is one."""
    stripped = _DOI_PREFIX.sub("", key).strip()
    return stripped if stripped.startswith("10.") else None


# ------------------------------------------------------------------
# the atlas-wide denominator
# ------------------------------------------------------------------


def _labelset_totals(annotations: list[dict[str, Any]]) -> dict[str, int | None]:
    """Cells each labelset accounts for, or None where a set is missing a count."""
    totals: dict[str, int | None] = {}
    for annotation in annotations:
        labelset = annotation.get("labelset")
        if labelset is None:
            continue
        n_cells = annotation.get("n_cells")
        if labelset in totals and totals[labelset] is None:
            continue
        if n_cells is None:
            totals[labelset] = None
        else:
            totals[labelset] = (totals.get(labelset) or 0) + int(n_cells)
    return totals


def _covering_cell_sets(
    annotations: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Cell sets covering every cell exactly once, and how they were found.

    Three projects to hand answer this three different ways, so nothing about
    the shape of the document is assumed. Where the annotations form a
    hierarchy, the candidate is its leaves — the cell sets that are nobody's
    parent — which on a real atlas span several labelsets, so taking the finest
    labelset instead would miss whatever is annotated only coarsely. Otherwise
    each labelset is a candidate in its own right.

    A candidate has to be corroborated, and how many cells the atlas holds is
    not stated anywhere: it is inferred from two ways of counting agreeing. So
    the leaves are used when their total matches some labelset's, and a
    labelset is used when it is the only one or when the labelsets agree. Where
    a document offers two labelsets that disagree and nothing to arbitrate
    between them, there is no denominator, and taking the larger would be
    inventing one.

    Args:
        annotations: every annotation in the document.

    Returns:
        The covering cell sets and a record of the basis, or an empty list and
        the reason none could be validated.
    """
    labelset_totals = _labelset_totals(annotations)
    complete = {ls: total for ls, total in labelset_totals.items() if total is not None}
    if not complete:
        return [], {"basis": "none", "reason": "no cell set carries n_cells"}

    parents = {
        a.get("parent_cell_set_accession")
        for a in annotations
        if a.get("parent_cell_set_accession")
    }
    if parents:
        leaves = [a for a in annotations if a.get("cell_set_accession") not in parents]
        if all(a.get("n_cells") is not None for a in leaves):
            total = sum(int(a["n_cells"]) for a in leaves)
            if total in complete.values():
                return leaves, {
                    "basis": "hierarchy_leaves",
                    "n_cell_sets": len(leaves),
                    "total_cells": total,
                }

    agreed = len(labelset_totals) == 1 or len(set(complete.values())) == 1
    if agreed and len(complete) == len(labelset_totals):
        # Finest first: most cell sets for the same cells.
        chosen = max(
            complete,
            key=lambda ls: sum(1 for a in annotations if a.get("labelset") == ls),
        )
        sets = [a for a in annotations if a.get("labelset") == chosen]
        return sets, {
            "basis": "labelset",
            "labelset": chosen,
            "n_cell_sets": len(sets),
            "total_cells": complete[chosen],
        }

    return [], {
        "basis": "none",
        "reason": (
            "no set of cell sets covers the atlas once — "
            f"labelset totals {sorted(labelset_totals.items())}"
        ),
    }


def subatlas_label_totals(cas_doc: dict[str, Any]) -> tuple[dict[tuple[str, str], int], dict]:
    """Cells each contributing study gave each of its labels, atlas-wide.

    Read from ``source.subatlas_papers[].cell_sets[]`` where the document
    registers them, since those are counted from the cell table directly.
    Otherwise summed over cell sets that cover the atlas once.

    Args:
        cas_doc: the CAS+ document.

    Returns:
        The totals, keyed by study and label, and a record of how they were
        arrived at. Both are empty where no denominator could be validated.
    """
    source = cas_doc.get("source") or {}
    registry = source.get("subatlas_papers") or []
    registered: dict[tuple[str, str], int] = {}
    for paper in registry:
        for cell_set in paper.get("cell_sets") or []:
            if cell_set.get("n_cells") is None:
                continue
            registered[(str(paper.get("label", "")), str(cell_set["cell_label"]))] = int(
                cell_set["n_cells"]
            )
    if registered:
        return registered, {"basis": "registry", "n_cell_sets": len(registered)}

    annotations = cas_doc.get("annotations") or []
    covering, basis = _covering_cell_sets(annotations)
    if not covering:
        return {}, basis

    totals: dict[tuple[str, str], int] = defaultdict(int)
    for annotation in covering:
        for transfer in annotation.get("transferred_annotations") or []:
            key = (paper_key(transfer), str(transfer.get("transferred_cell_label", "")))
            totals[key] += int(transfer.get("cell_count") or 0)
    return dict(totals), basis


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


def _describe(annotation: dict[str, Any]) -> dict[str, Any]:
    """The identity of a requested cell set, with absent parts omitted."""
    out: dict[str, Any] = {
        "cell_label": annotation["cell_label"],
        "labelset": annotation.get("labelset", ""),
    }
    fullname = annotation.get("cell_fullname")
    if fullname and fullname != annotation["cell_label"]:
        out["cell_fullname"] = fullname
    for field in ("cell_set_accession", "n_cells"):
        if annotation.get(field) is not None:
            out[field] = annotation[field]
    if annotation.get("synonyms"):
        out["synonyms"] = list(annotation["synonyms"])
    return out


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
    totals, totals_basis = subatlas_label_totals(cas_doc)
    registry = _registry_index(cas_doc)
    accession_label = {
        a["cell_set_accession"]: a["cell_label"]
        for a in cas_doc.get("annotations") or []
        if a.get("cell_set_accession")
    }

    questions: dict[tuple[str, str], dict[str, Any]] = {}
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

        # Where the document does not state a study's whole contribution to
        # this cell set, the transfers naming that study are all there is.
        fallback: dict[str, int] = defaultdict(int)
        for transfer in transfers:
            fallback[paper_key(transfer)] += int(transfer.get("cell_count") or 0)

        for transfer in transfers:
            study = paper_key(transfer)
            upstream = str(transfer.get("transferred_cell_label", ""))
            overlap = int(transfer.get("cell_count") or 0)
            is_synonym = normalise_label(upstream) in synonyms
            doi = _doi(study)

            if doi is None:
                entry = unreadable.setdefault(
                    study, {"subatlas_paper": study, "overlap_cells": 0, "reached": set()}
                )
                entry["overlap_cells"] += overlap
                entry["reached"].add(label)
                continue

            if overlap < min_overlap_cells and not is_synonym:
                roll = dropped.setdefault(
                    study,
                    {"subatlas_paper": study, "n_subatlas_labels": 0, "overlap_cells": 0},
                )
                roll["n_subatlas_labels"] += 1
                roll["overlap_cells"] += overlap
                dropped_per_cell_set[label] += overlap
                continue

            contribution = transfer.get("subatlas_contribution_cells")
            if contribution is None:
                contribution = fallback[study]
            contribution = int(contribution) or overlap

            claimant: dict[str, Any] = {
                "cell_label": label,
                "overlap_cells": overlap,
                "share_of_contribution": round(overlap / contribution, 4) if contribution else 0.0,
            }
            if annotation.get("labelset"):
                claimant["labelset"] = annotation["labelset"]
            if annotation.get("cell_set_accession"):
                claimant["cell_set_accession"] = annotation["cell_set_accession"]
            total = totals.get((study, upstream))
            if total:
                claimant["share_of_subatlas_label"] = round(overlap / total, 4)
            if is_synonym:
                claimant["named_as_synonym"] = True

            question = questions.setdefault(
                (study, upstream),
                _new_question(
                    study, upstream, transfer, registry, doi, totals.get((study, upstream))
                ),
            )
            question["atlas_cell_sets"].append(claimant)
            served[label] += 1

    atlas_only = _atlas_only(requested, served, rows_per_cell_set, dropped_per_cell_set, unreadable)

    table: dict[str, Any] = {
        "min_overlap_cells": min_overlap_cells,
        "subatlas_label_totals": totals_basis,
        "requested": [_describe(a) for a in requested],
        "questions": _ordered(questions),
        "atlas_only": atlas_only,
    }
    if cas_source:
        table["cas_source"] = cas_source
    atlas_doi = (cas_doc.get("source") or {}).get("doi")
    if atlas_doi:
        table["atlas_doi"] = str(atlas_doi)
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
    # Parent labels are worth carrying only where the parent was itself asked for.
    wanted = {a.get("cell_set_accession") for a in requested}
    for described, annotation in zip(table["requested"], requested, strict=True):
        parent = annotation.get("parent_cell_set_accession")
        if parent and parent in wanted:
            described["parent"] = accession_label[parent]
    return table


def _new_question(
    study: str,
    upstream: str,
    transfer: dict[str, Any],
    registry: dict[str, dict[str, Any]],
    doi: str,
    total: int | None,
) -> dict[str, Any]:
    """A question about one of a contributing study's labels, before claimants."""
    question: dict[str, Any] = {
        "subatlas_paper": study,
        "doi": doi,
        "subatlas_cell_label": upstream,
        "atlas_cell_sets": [],
    }
    if transfer.get("source_labelset"):
        question["source_labelset"] = str(transfer["source_labelset"])
    if total:
        question["subatlas_label_total_cells"] = total
    paper = registry.get(study) or registry.get(doi) or {}
    for field in ("first_author", "year", "title"):
        if paper.get(field) is not None:
            question[field] = paper[field]
    band = (paper.get("asta_indexing") or {}).get("band")
    if band:
        question["asta_band"] = band
    return question


def _ordered(questions: dict[tuple[str, str], dict[str, Any]]) -> list[dict[str, Any]]:
    """Questions grouped by study, largest contributor first, since a paper is read once."""
    per_study: dict[str, int] = defaultdict(int)
    for (study, _), question in questions.items():
        per_study[study] += sum(c["overlap_cells"] for c in question["atlas_cell_sets"])
    out = sorted(
        questions.values(),
        key=lambda q: (
            -per_study[q["subatlas_paper"]],
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
    lines = [
        f"{len(table['requested'])} cell sets requested",
        f"{len(table['questions'])} questions across "
        f"{len({q['subatlas_paper'] for q in table['questions']})} papers",
    ]
    basis = table["subatlas_label_totals"]
    if basis["basis"] == "none":
        lines.append(f"no atlas-wide denominator: {basis.get('reason', '')}")
    else:
        lines.append(f"denominator: {basis['basis']}")
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
