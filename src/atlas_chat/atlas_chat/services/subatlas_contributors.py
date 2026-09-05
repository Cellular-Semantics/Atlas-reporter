"""Which upstream papers contributed a cell set, and how cleanly.

A CAS+ annotation's ``transferred_annotations`` array is the joint table of what
each contributing study called the cells in this cell set. It cannot be read
directly to answer "which papers should this report compare itself against",
for two reasons.

**The denominator is wrong.** ``cell_ratio`` is a fraction of the whole cell set,
so it conflates a paper that barely contributed with a paper that contributed a
lot and split its labels across several calls. Separating the two — how much of
the cell set came from this paper (``contribution``) against how much of *that
paper's contribution* carried each label (``within_source_share``) — is what makes
the interesting case visible. On the reference project one cell set's top
contributor by cells (Weigert, 24%) called them all "endothelial cell", which
agrees with the atlas only in the sense that it agrees with everything; a smaller
contributor (Ulrich 2024, 7%) split the same cells `Capillary` 59% / `tPCV` 22% /
`aPCV` 11% — and `aPCV`, the 11% minority call, is the name the atlas adopted.
Ranking by contribution alone buries that; ranking by purity alone buries Weigert.

**The tail is long.** A median cell set has 16 upstream labels below any sensible
threshold and one has 195. They have to be aggregated — not listed, and not
silently dropped, because "provenance thinly spread over a dozen studies" is a
different finding from "one clean upstream parent" and only the aggregate shows it.

So this module derives a cutoff-applied view (``subatlas_contributors.schema.json``)
that the consistency step and the report read instead. Deterministic, stdlib only,
no LLM: every judgement about what the labels *mean* happens downstream.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from collections import defaultdict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

#: A contributor must account for at least this fraction of the cell set. At 0.05,
#: the reference project yields a median of 2 qualifying papers per cell set
#: (max 8) — a tractable retrieval budget. At 0.10 the median falls to 1 and 53 of
#: 303 cell sets lose every contributor.
DEFAULT_MIN_CONTRIBUTION = 0.05

#: ...and at least this many cells, so a large share of a tiny cell set cannot
#: qualify on a handful of cells.
DEFAULT_MIN_SOURCE_CELLS = 50

#: At or above this contribution, retrieving the paper's own text is worth it.
DEFAULT_PRIMARY_CONTRIBUTION = 0.2

#: Within a qualifying contributor, list a label individually above this share of
#: that contributor's cells. Deliberately low: the informative label is often a
#: minority one. At 0.02 a qualifying paper shows a median of 2 labels (p90 5)
#: instead of 8, while keeping Ulrich's 11% `aPCV`.
DEFAULT_MIN_WITHIN_SOURCE_SHARE = 0.02

_DOI_PREFIX = "DOI:"


@dataclass(frozen=True)
class Thresholds:
    """The cutoff. Recorded on the output so a coverage claim is reproducible."""

    min_contribution: float = DEFAULT_MIN_CONTRIBUTION
    min_source_cells: int = DEFAULT_MIN_SOURCE_CELLS
    primary_contribution: float = DEFAULT_PRIMARY_CONTRIBUTION
    min_within_source_share: float = DEFAULT_MIN_WITHIN_SOURCE_SHARE

    def to_dict(self) -> dict[str, Any]:
        return {
            "min_contribution": self.min_contribution,
            "min_source_cells": self.min_source_cells,
            "primary_contribution": self.primary_contribution,
            "min_within_source_share": self.min_within_source_share,
        }


def _registry(cas_doc: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    """``source.subatlas_papers`` keyed by label, for status/band/DOI lookup."""
    entries = (cas_doc.get("source") or {}).get("subatlas_papers") or []
    return {e["label"]: e for e in entries if e.get("label")}


def _contributor_key(item: Mapping[str, Any]) -> str:
    """The registry key for a transferred annotation.

    ``subatlas_paper`` when set, else ``source_taxonomy`` — both are permitted by
    the schema and real documents use each. Keying on the source labelset instead
    would split one paper across its labelsets.
    """
    return str(item.get("subatlas_paper") or item.get("source_taxonomy") or "")


def _doi_of(item: Mapping[str, Any], registry_entry: Mapping[str, Any]) -> str | None:
    doi = registry_entry.get("doi")
    if doi:
        return str(doi)
    taxonomy = str(item.get("source_taxonomy") or "")
    if taxonomy.startswith(_DOI_PREFIX):
        return taxonomy[len(_DOI_PREFIX) :]
    return None


def summarise(
    annotation: Mapping[str, Any],
    cas_doc: Mapping[str, Any],
    *,
    thresholds: Thresholds | None = None,
    non_paper_labels: Sequence[str] = (),
) -> dict[str, Any]:
    """Derive the contributors view for one CAS+ annotation.

    Args:
        annotation: One entry from ``cas_doc["annotations"]``.
        cas_doc: The whole document, read for ``source.subatlas_papers``.
        thresholds: The cutoff; defaults as documented on this module.
        non_paper_labels: Contributor keys that name no paper (an atlas-internal
            partition such as ``whole_embryo``). Their cells are counted under
            ``unpublished_cells`` rather than offered as something to compare
            against.

    Returns:
        An object conforming to ``subatlas_contributors.schema.json``.

    Raises:
        ValueError: If the annotation has no ``n_cells``. Every ratio here is a
            fraction of the cell set, so without it there is nothing to compute
            and a silent zero would read as "no contributors".
    """
    thresholds = thresholds or Thresholds()
    n_cells = annotation.get("n_cells")
    if not n_cells:
        raise ValueError(
            f"cell set {annotation.get('cell_label')!r} has no n_cells; "
            "contribution shares cannot be computed"
        )

    registry = _registry(cas_doc)
    skip = set(non_paper_labels)

    # Group by contributing paper, keeping each paper's labels together.
    grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    unpublished_cells = 0
    for item in annotation.get("transferred_annotations", []) or []:
        key = _contributor_key(item)
        if not key or key in skip:
            unpublished_cells += int(item.get("cell_count", 0))
            continue
        grouped[key].append(item)

    contributors: list[dict[str, Any]] = []
    tail_papers: list[str] = []
    tail_cells = 0

    for key, items in grouped.items():
        from_source_cells = sum(int(i.get("cell_count", 0)) for i in items)
        if not from_source_cells:
            continue
        entry = registry.get(key, {})
        doi = _doi_of(items[0], entry)
        contribution = from_source_cells / n_cells

        if doi is None:
            # Real provenance with nothing to retrieve. Held apart from the tail:
            # it was not excluded for being small.
            unpublished_cells += from_source_cells
            continue
        if contribution < thresholds.min_contribution or (
            from_source_cells < thresholds.min_source_cells
        ):
            tail_papers.append(key)
            tail_cells += from_source_cells
            continue

        ordered = sorted(
            items, key=lambda i: (-int(i.get("cell_count", 0)), i["transferred_cell_label"])
        )
        listed: list[dict[str, Any]] = []
        n_tail_labels = 0
        label_tail_cells = 0
        for item in ordered:
            count = int(item.get("cell_count", 0))
            within = count / from_source_cells
            if within < thresholds.min_within_source_share and listed:
                # `and listed` keeps the dominant label even when every label in a
                # broadly-smeared contributor falls under the floor.
                n_tail_labels += 1
                label_tail_cells += count
                continue
            label: dict[str, Any] = {
                "transferred_cell_label": item["transferred_cell_label"],
                "cell_count": count,
                "within_source_share": round(within, 4),
                "share_of_set": round(count / n_cells, 4),
            }
            total = item.get("source_label_cell_count")
            if total:
                label["source_label_cell_count"] = int(total)
                label["reverse_share"] = round(count / int(total), 4)
            listed.append(label)

        contributor: dict[str, Any] = {
            "subatlas_paper": key,
            "doi": doi,
            "tier": ("primary" if contribution >= thresholds.primary_contribution else "secondary"),
            "from_source_cells": from_source_cells,
            "contribution": round(contribution, 4),
            "purity": round(int(ordered[0].get("cell_count", 0)) / from_source_cells, 4),
            "dominant_label": ordered[0]["transferred_cell_label"],
            "labels": listed,
        }
        source_labelset = items[0].get("source_labelset")
        if source_labelset:
            contributor["source_labelset"] = str(source_labelset)
        if n_tail_labels:
            contributor["n_tail_labels"] = n_tail_labels
            contributor["tail_cells"] = label_tail_cells
        if entry.get("status"):
            contributor["status"] = str(entry["status"])
        band = (entry.get("asta_indexing") or {}).get("band")
        if band:
            contributor["asta_band"] = str(band)
        contributors.append(contributor)

    contributors.sort(key=lambda c: (-c["contribution"], c["subatlas_paper"]))

    out: dict[str, Any] = {
        "cell_label": annotation["cell_label"],
        "labelset": annotation.get("labelset", ""),
        "n_cells": int(n_cells),
        "thresholds": thresholds.to_dict(),
        "contributors": contributors,
        "tail": {
            "n_papers": len(tail_papers),
            "cell_count": tail_cells,
            "contribution": round(tail_cells / n_cells, 4),
            "papers": sorted(tail_papers),
        },
    }
    if annotation.get("cell_set_accession"):
        out["cell_set_accession"] = str(annotation["cell_set_accession"])
    if not contributors:
        out["no_dominant_contributor"] = True
    if unpublished_cells:
        out["unpublished_cells"] = unpublished_cells
    return out


def find_annotation(
    cas_doc: Mapping[str, Any], cell_label: str, labelset: str | None = None
) -> Mapping[str, Any]:
    """Locate one annotation by label, optionally within a labelset.

    Raises:
        KeyError: If no annotation matches, or if the label is ambiguous across
            labelsets and none was given — a hierarchical taxonomy can reuse a
            label at more than one level, and guessing which was meant would
            silently report the wrong cell set.
    """
    matches = [
        a
        for a in cas_doc.get("annotations", [])
        if a.get("cell_label") == cell_label and (labelset is None or a.get("labelset") == labelset)
    ]
    if not matches:
        where = f" in labelset {labelset!r}" if labelset else ""
        raise KeyError(f"no annotation with cell_label {cell_label!r}{where}")
    if len(matches) > 1:
        sets = sorted({str(a.get("labelset")) for a in matches})
        raise KeyError(f"cell_label {cell_label!r} occurs in labelsets {sets}; pass --labelset")
    return matches[0]


def summarise_all(
    cas_doc: Mapping[str, Any],
    *,
    thresholds: Thresholds | None = None,
    non_paper_labels: Sequence[str] = (),
) -> list[dict[str, Any]]:
    """Derive the contributors view for every annotation that has provenance.

    Annotations with no ``transferred_annotations`` are skipped; annotations that
    have provenance but no ``n_cells`` are logged and skipped rather than aborting
    a whole-project pass.
    """
    out = []
    for annotation in cas_doc.get("annotations", []):
        if not annotation.get("transferred_annotations"):
            continue
        try:
            out.append(
                summarise(
                    annotation,
                    cas_doc,
                    thresholds=thresholds,
                    non_paper_labels=non_paper_labels,
                )
            )
        except ValueError as exc:
            logger.warning("skipping cell set: %s", exc)
    return out


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m atlas_chat.cli_contributors",
        description=(
            "Derive the cutoff-applied subatlas-contributors view from a CAS+ "
            "document's transferred_annotations."
        ),
    )
    parser.add_argument("--cas", required=True, type=Path, help="CAS+ document")
    parser.add_argument(
        "--cell-type", help="one cell set's cell_label; omit to summarise all of them"
    )
    parser.add_argument("--labelset", help="disambiguate a cell_label reused across labelsets")
    parser.add_argument("--out", type=Path, help="write JSON here instead of stdout")
    parser.add_argument("--min-contribution", type=float, default=DEFAULT_MIN_CONTRIBUTION)
    parser.add_argument("--min-source-cells", type=int, default=DEFAULT_MIN_SOURCE_CELLS)
    parser.add_argument("--primary-contribution", type=float, default=DEFAULT_PRIMARY_CONTRIBUTION)
    parser.add_argument(
        "--min-within-source-share", type=float, default=DEFAULT_MIN_WITHIN_SOURCE_SHARE
    )
    parser.add_argument(
        "--non-paper-label",
        action="append",
        default=[],
        help="contributor key naming no paper (e.g. whole_embryo); repeatable",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cas_doc = json.loads(args.cas.read_text(encoding="utf-8"))
    thresholds = Thresholds(
        min_contribution=args.min_contribution,
        min_source_cells=args.min_source_cells,
        primary_contribution=args.primary_contribution,
        min_within_source_share=args.min_within_source_share,
    )

    if args.cell_type:
        try:
            annotation = find_annotation(cas_doc, args.cell_type, args.labelset)
        except KeyError as exc:
            print(exc.args[0], file=sys.stderr)
            return 2
        try:
            result: Any = summarise(
                annotation,
                cas_doc,
                thresholds=thresholds,
                non_paper_labels=args.non_paper_label,
            )
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        summary = (
            f"{result['cell_label']}: {len(result['contributors'])} contributor(s) "
            f"over the cutoff, {result['tail']['n_papers']} in the tail"
        )
    else:
        result = summarise_all(
            cas_doc, thresholds=thresholds, non_paper_labels=args.non_paper_label
        )
        n_none = sum(1 for r in result if r.get("no_dominant_contributor"))
        summary = (
            f"{len(result)} cell set(s) with provenance; "
            f"{n_none} with no contributor over the cutoff"
        )

    payload = json.dumps(result, indent=2, ensure_ascii=False)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(payload + "\n", encoding="utf-8")
        print(f"{summary} -> {args.out}")
    else:
        print(payload)
        print(summary, file=sys.stderr)
    return 0


__all__ = [
    "DEFAULT_MIN_CONTRIBUTION",
    "DEFAULT_MIN_SOURCE_CELLS",
    "DEFAULT_MIN_WITHIN_SOURCE_SHARE",
    "DEFAULT_PRIMARY_CONTRIBUTION",
    "Thresholds",
    "build_parser",
    "find_annotation",
    "main",
    "summarise",
    "summarise_all",
]
