"""Turn integration provenance in ``obs`` into CAS+ ``transferred_annotations``.

An integrated atlas usually keeps each contributing study's own cell-type calls as
extra ``obs`` columns — ``celltype_Ulrich2024``, ``Sridhar_et_al_2020_CellPress``,
and so on. Cross-tabulating one of those against the atlas's own cell-type column
says, for every atlas cell set, what the upstream study called those same cells.
That is the raw material for judging whether an atlas label agrees with the labels
it was built from, and CAS+ already has the slot for it:
``annotations[].transferred_annotations[]``.

The work splits three ways, deliberately:

* :func:`crosstab` — count cells per (atlas label, source column, source value).
  Trivial, stdlib-only, and the part a caller with pandas or zarr already has.
* :func:`build_transferred_annotations` — shape those counts into CAS+
  ``TransferredAnnotation`` objects. This is the part worth testing.
* :func:`backfill_source_label_totals` — a whole-document pass filling in
  ``source_label_cell_count``, each upstream label's atlas-wide total.

The totals need the whole document because they must be summed over **leaf** cell
sets only. Leaves partition the cells; summing over every annotation in a
hierarchical taxonomy would count each cell once per level.

Nothing here calls an LLM or the network.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from collections import defaultdict
from collections.abc import Collection, Iterable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

#: Values that mean "this study said nothing about this cell". A cell only carries
#: an upstream label if that study actually saw and annotated it, so absence is the
#: common case, not an anomaly.
NULL_VALUES = frozenset(
    {
        "",
        "nan",
        "NaN",
        "NA",
        "N/A",
        "None",
        "none",
        "null",
        "NULL",
        "unknown",
        "Unknown",
        "not applicable",
        "Not applicable",
        "-",
    }
)

#: A ``Counts`` maps atlas cell label -> source column -> source value -> cell count.
Counts = dict[str, dict[str, dict[str, int]]]


@dataclass(frozen=True)
class TransferSource:
    """One ``obs`` column holding another study's cell-type labels.

    Args:
        column: The ``obs`` column name, used as ``source_labelset``.
        label: Registry key for the contributing paper — matches a
            ``source.subatlas_papers[].label``. Defaults to ``column``.
        doi: The contributing paper's DOI, or ``None`` for data with no
            publication (newly generated cells, an atlas-internal partition).
        first_author: First author, for the registry entry.
        year: Publication year, for the registry entry.
    """

    column: str
    label: str | None = None
    doi: str | None = None
    first_author: str | None = None
    year: int | None = None

    @property
    def registry_label(self) -> str:
        return self.label or self.column


def crosstab(
    cell_labels: Sequence[str | None],
    transfer_columns: Mapping[str, Sequence[str | None]],
    *,
    drop_values: Collection[str] = NULL_VALUES,
) -> tuple[Counts, dict[str, int]]:
    """Count cells per (atlas label, source column, source value).

    Args:
        cell_labels: The atlas's own cell-type label, one entry per cell.
        transfer_columns: Source column name -> that column's per-cell values.
            Every sequence must be the same length as ``cell_labels``.
        drop_values: Values treated as "not annotated by this study".

    Returns:
        ``(counts, set_sizes)`` where ``set_sizes`` maps each atlas label to its
        total cell count — the denominator for ``cell_ratio``.

    Raises:
        ValueError: If a transfer column's length differs from ``cell_labels``.
    """
    n = len(cell_labels)
    for column, values in transfer_columns.items():
        if len(values) != n:
            raise ValueError(f"column {column!r} has {len(values)} values, expected {n}")

    drop = set(drop_values)
    counts: Counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    set_sizes: dict[str, int] = defaultdict(int)
    for i, label in enumerate(cell_labels):
        if label is None or label in drop:
            continue
        set_sizes[label] += 1
        for column, values in transfer_columns.items():
            value = values[i]
            if value is None or value in drop:
                continue
            counts[label][column][value] += 1
    return (
        {k: {c: dict(v) for c, v in cols.items()} for k, cols in counts.items()},
        dict(set_sizes),
    )


def counts_from_joint(doc: Mapping[str, Any]) -> tuple[Counts, dict[str, int]]:
    """Read a ``label_transfers__<col>.json`` produced by ``anndata-zarr-summary``.

    That file is the same joint table :func:`crosstab` computes, already
    aggregated — so a project whose ``obs`` lives in a remote zarr never has to
    materialise a per-cell export just to get its integration provenance.

    Args:
        doc: The parsed file: ``{"source": ..., "cell_sets": {label: {"n_cells":
            int, "transfers": {column: [{"value": str, "n": int}, ...]}}}}``.

    Returns:
        ``(counts, set_sizes)``, the same pair :func:`crosstab` returns.

    Raises:
        ValueError: If the document has no ``cell_sets`` key.
    """
    cell_sets = doc.get("cell_sets")
    if cell_sets is None:
        raise ValueError("not a label_transfers document: no 'cell_sets' key")
    counts: Counts = {}
    set_sizes: dict[str, int] = {}
    for cell_label, record in cell_sets.items():
        set_sizes[cell_label] = int(record.get("n_cells", 0))
        columns: dict[str, dict[str, int]] = {}
        for column, items in (record.get("transfers") or {}).items():
            columns[column] = {item["value"]: int(item["n"]) for item in items}
        if columns:
            counts[cell_label] = columns
    return counts, set_sizes


def build_transferred_annotations(
    counts: Counts,
    set_sizes: Mapping[str, int],
    sources: Iterable[TransferSource],
    *,
    ratio_precision: int = 4,
) -> dict[str, list[dict[str, Any]]]:
    """Shape cross-tab counts into CAS+ ``TransferredAnnotation`` objects.

    One object per (cell set, source column, upstream label), sorted by descending
    cell count within each source so the dominant upstream label reads first.
    ``source_label_cell_count`` is left for :func:`backfill_source_label_totals`,
    which needs the whole document.

    Args:
        counts: As returned by :func:`crosstab`.
        set_sizes: Atlas label -> total cells, the ``cell_ratio`` denominator.
        sources: The columns to emit, with their paper provenance. Columns present
            in ``counts`` but absent here are skipped — the caller decides what
            counts as integration provenance.
        ratio_precision: Decimal places for ``cell_ratio``.

    Returns:
        Atlas cell label -> its list of transferred-annotation objects. Labels with
        no upstream annotation at all are absent from the mapping.
    """
    by_column = {s.column: s for s in sources}
    out: dict[str, list[dict[str, Any]]] = {}
    for cell_label, columns in counts.items():
        total = set_sizes.get(cell_label, 0)
        if not total:
            logger.warning("cell set %r has no cells; skipping its transfers", cell_label)
            continue
        items: list[dict[str, Any]] = []
        for column, values in columns.items():
            source = by_column.get(column)
            if source is None:
                continue
            for value, count in sorted(values.items(), key=lambda kv: (-kv[1], kv[0])):
                item: dict[str, Any] = {
                    "transferred_cell_label": value,
                    "source_labelset": column,
                    "subatlas_paper": source.registry_label,
                    "cell_count": count,
                    "cell_ratio": round(count / total, ratio_precision),
                }
                if source.doi:
                    item["source_taxonomy"] = f"DOI:{source.doi}"
                else:
                    item["comment"] = (
                        "Contributing data has no publication; there is no subatlas "
                        "paper to compare this label against."
                    )
                items.append(item)
        if items:
            out[cell_label] = items
    return out


def leaf_accessions(annotations: Sequence[Mapping[str, Any]]) -> set[str]:
    """Accessions of cell sets that are nobody's parent.

    Leaves partition the cells, so they are the only level that can be summed
    without multiply-counting through the hierarchy. A flat (single-labelset)
    document is all leaves.
    """
    parents = {a.get("parent_cell_set_accession") for a in annotations}
    return {
        str(a["cell_set_accession"])
        for a in annotations
        if "cell_set_accession" in a and a["cell_set_accession"] not in parents
    }


def backfill_source_label_totals(cas_doc: dict[str, Any]) -> int:
    """Fill in ``source_label_cell_count`` across a CAS+ document, in place.

    For each (``source_labelset``, ``transferred_cell_label``) pair, sums
    ``cell_count`` over leaf cell sets — the upstream label's atlas-wide total.
    A consumer divides by it to get the reverse share: "this cell set captured 12%
    of the cells the source called Capillary". That distinguishes an upstream cell
    type the atlas *split* from one it merely *renamed*, which per-set counts alone
    cannot show.

    Annotations without ``cell_set_accession`` are skipped for the totals but still
    receive them, since a flat document may not use accessions at all.

    Args:
        cas_doc: A CAS+ document. Mutated in place.

    Returns:
        The number of transferred annotations given a total.
    """
    annotations = cas_doc.get("annotations", []) or []
    accessions = [a for a in annotations if "cell_set_accession" in a]
    leaves = leaf_accessions(accessions) if accessions else None

    totals: dict[tuple[str, str], int] = defaultdict(int)
    for ann in annotations:
        if leaves is not None and str(ann.get("cell_set_accession", "")) not in leaves:
            continue
        for item in ann.get("transferred_annotations", []) or []:
            key = (item.get("source_labelset", ""), item["transferred_cell_label"])
            totals[key] += int(item.get("cell_count", 0))

    n_filled = 0
    for ann in annotations:
        for item in ann.get("transferred_annotations", []) or []:
            key = (item.get("source_labelset", ""), item["transferred_cell_label"])
            total = totals.get(key, 0)
            if total:
                item["source_label_cell_count"] = total
                n_filled += 1
    return n_filled


def subatlas_registry(
    sources: Iterable[TransferSource],
    cas_doc: Mapping[str, Any],
) -> list[dict[str, Any]]:
    """Build ``source.subatlas_papers`` entries for the transfer sources.

    Registering the contributors is what lets a ``transferred_annotations`` entry
    resolve to a paper with an ingest status and a measured ASTA band, so the
    consistency step knows whether that paper's text is reachable at all. Status
    starts at ``candidate`` (a DOI to confirm) or ``unresolved`` (no publication);
    ``subatlas_resolver.ingest`` moves it on from there.

    ``total_cells`` is summed over leaf cell sets, same reasoning as
    :func:`backfill_source_label_totals`.
    """
    annotations = cas_doc.get("annotations", []) or []
    accessions = [a for a in annotations if "cell_set_accession" in a]
    leaves = leaf_accessions(accessions) if accessions else None

    per_column: dict[str, int] = defaultdict(int)
    for ann in annotations:
        if leaves is not None and str(ann.get("cell_set_accession", "")) not in leaves:
            continue
        for item in ann.get("transferred_annotations", []) or []:
            per_column[item.get("source_labelset", "")] += int(item.get("cell_count", 0))

    entries: list[dict[str, Any]] = []
    for source in sources:
        entry: dict[str, Any] = {
            "label": source.registry_label,
            "status": "candidate" if source.doi else "unresolved",
        }
        if source.first_author:
            entry["first_author"] = source.first_author
        if source.year:
            entry["year"] = source.year
        if source.doi:
            entry["doi"] = source.doi
        total = per_column.get(source.column, 0)
        if total:
            entry["total_cells"] = total
        entries.append(entry)
    return entries


def apply_to_cas(
    cas_doc: dict[str, Any],
    transferred: Mapping[str, list[dict[str, Any]]],
    *,
    labelset: str,
    replace: bool = True,
) -> tuple[int, list[str]]:
    """Attach transferred annotations to a CAS+ document's annotations, in place.

    Matches on (``labelset``, ``cell_label``). Cell labels present in
    ``transferred`` but absent from the document are returned rather than raised
    on: a cross-tab from a newer ``obs`` legitimately sees labels a hand-curated
    CAS+ document has not caught up with, and the caller should see the list.

    Args:
        cas_doc: A CAS+ document. Mutated in place.
        transferred: As returned by :func:`build_transferred_annotations`.
        labelset: Which labelset these cell labels belong to.
        replace: Overwrite any existing ``transferred_annotations``. When False,
            appends — use it to add a second source column to a document that
            already carries others.

    Returns:
        ``(n_annotations_updated, unmatched_cell_labels)``.
    """
    by_label = {
        a["cell_label"]: a for a in cas_doc.get("annotations", []) if a.get("labelset") == labelset
    }
    n = 0
    for cell_label, items in transferred.items():
        ann = by_label.get(cell_label)
        if ann is None:
            continue
        if replace or "transferred_annotations" not in ann:
            ann["transferred_annotations"] = list(items)
        else:
            ann["transferred_annotations"].extend(items)
        n += 1
    unmatched = sorted(set(transferred) - set(by_label))
    return n, unmatched


def parse_sources(specs: Iterable[str]) -> list[TransferSource]:
    """Parse ``column[=doi][;first_author][;year]`` CLI specs.

    ``celltype_Ulrich2024=10.1073/pnas.2404775121;Ulrich;2024`` and the bare
    ``celltype_OvarySanger2026`` (no publication) are both valid.
    """
    out: list[TransferSource] = []
    for spec in specs:
        head, _, rest = spec.partition(";")
        column, _, doi = head.partition("=")
        parts = [p.strip() for p in rest.split(";")] if rest else []
        first_author = parts[0] if parts and parts[0] else None
        year: int | None = None
        if len(parts) > 1 and parts[1]:
            try:
                year = int(parts[1])
            except ValueError as exc:
                raise ValueError(f"bad year in source spec {spec!r}") from exc
        out.append(
            TransferSource(
                column=column.strip(),
                doi=doi.strip() or None,
                first_author=first_author,
                year=year,
            )
        )
    return out


def read_delimited(path: Path, columns: Sequence[str]) -> tuple[dict[str, list[str | None]], int]:
    """Read named columns from a CSV/TSV obs export.

    Delimiter is inferred from the suffix (``.tsv``/``.txt`` are tab-separated).

    Raises:
        ValueError: If a requested column is missing from the header.
    """
    import csv

    delimiter = "\t" if path.suffix.lower() in {".tsv", ".txt"} else ","
    data: dict[str, list[str | None]] = {c: [] for c in columns}
    n_rows = 0
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        missing = [c for c in columns if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"{path.name} has no column(s): {', '.join(missing)}")
        for row in reader:
            n_rows += 1
            for column in columns:
                data[column].append(row.get(column))
    return data, n_rows


def load_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m atlas_chat.cli_cas",
        description="Populate CAS+ integration provenance from obs transfer columns.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    transfer = sub.add_parser(
        "transfer",
        help="cross-tabulate obs transfer columns and write transferred_annotations",
    )
    transfer.add_argument("--cas", required=True, type=Path, help="CAS+ document to update")
    counted = transfer.add_mutually_exclusive_group(required=True)
    counted.add_argument(
        "--obs",
        type=Path,
        help="obs export as CSV/TSV, one row per cell (tab-separated for .tsv/.txt)",
    )
    counted.add_argument(
        "--transfers",
        type=Path,
        help="label_transfers__<col>.json from anndata-zarr-summary --transfer-cols "
        "(already aggregated; no per-cell export needed)",
    )
    transfer.add_argument(
        "--cell-type-col",
        help="obs column holding the atlas's own cell-type label (required with --obs)",
    )
    transfer.add_argument(
        "--labelset",
        required=True,
        help="the CAS+ labelset --cell-type-col corresponds to",
    )
    transfer.add_argument(
        "--source",
        action="append",
        default=[],
        required=True,
        metavar="COL[=DOI][;AUTHOR][;YEAR]",
        help="a transfer column and its paper; repeatable",
    )
    transfer.add_argument(
        "--append",
        action="store_true",
        help="add to existing transferred_annotations instead of replacing them",
    )
    transfer.add_argument(
        "--no-registry",
        action="store_true",
        help="don't touch source.subatlas_papers",
    )
    transfer.add_argument("--out", type=Path, help="write here instead of over --cas")
    transfer.add_argument(
        "--dry-run", action="store_true", help="report what would change, write nothing"
    )

    backfill = sub.add_parser(
        "backfill-totals",
        help="fill in source_label_cell_count across an existing CAS+ document",
    )
    backfill.add_argument("--cas", required=True, type=Path)
    backfill.add_argument("--out", type=Path, help="write here instead of over --cas")
    return parser


def _cmd_transfer(args: argparse.Namespace) -> int:
    sources = parse_sources(args.source)
    cas_doc = load_json(args.cas)

    if args.obs:
        if not args.cell_type_col:
            print("--cell-type-col is required with --obs", file=sys.stderr)
            return 2
        columns = [args.cell_type_col, *(s.column for s in sources)]
        data, n_rows = read_delimited(args.obs, columns)
        counts, set_sizes = crosstab(
            data[args.cell_type_col],
            {s.column: data[s.column] for s in sources},
        )
        scale = f"{n_rows} cells"
    else:
        counts, set_sizes = counts_from_joint(load_json(args.transfers))
        missing = [s.column for s in sources if not any(s.column in c for c in counts.values())]
        if missing:
            print(
                f"transfer columns absent from {args.transfers.name}: {', '.join(missing)}",
                file=sys.stderr,
            )
        scale = f"{len(set_sizes)} cell sets"
    transferred = build_transferred_annotations(counts, set_sizes, sources)
    n_updated, unmatched = apply_to_cas(
        cas_doc, transferred, labelset=args.labelset, replace=not args.append
    )
    n_filled = backfill_source_label_totals(cas_doc)
    if not args.no_registry:
        source = cas_doc.setdefault("source", {})
        existing = {e.get("label"): e for e in source.get("subatlas_papers", []) or []}
        for entry in subatlas_registry(sources, cas_doc):
            # Never clobber a confirmed DOI or an ingest status the resolver set.
            prior = existing.get(entry["label"])
            if prior and prior.get("doi"):
                prior["total_cells"] = entry.get("total_cells", prior.get("total_cells"))
            else:
                existing[entry["label"]] = {**(prior or {}), **entry}
        source["subatlas_papers"] = list(existing.values())

    n_items = sum(len(v) for v in transferred.values())
    print(
        f"transfer: {scale}, {len(sources)} source column(s) -> "
        f"{n_items} transferred annotations on {n_updated} cell set(s) "
        f"in labelset {args.labelset!r}; {n_filled} atlas-wide totals filled"
    )
    if unmatched:
        print(
            f"  {len(unmatched)} cell label(s) in obs but not in labelset "
            f"{args.labelset!r}: {', '.join(unmatched[:8])}"
            + (" ..." if len(unmatched) > 8 else ""),
            file=sys.stderr,
        )
    if args.dry_run:
        print("  --dry-run: nothing written")
        return 0
    write_json(args.out or args.cas, cas_doc)
    print(f"  wrote {args.out or args.cas}")
    return 0


def _cmd_backfill(args: argparse.Namespace) -> int:
    cas_doc = load_json(args.cas)
    n_filled = backfill_source_label_totals(cas_doc)
    write_json(args.out or args.cas, cas_doc)
    print(f"backfill-totals: {n_filled} transferred annotations given atlas-wide totals")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "transfer":
        return _cmd_transfer(args)
    if args.command == "backfill-totals":
        return _cmd_backfill(args)
    return 2


__all__ = [
    "NULL_VALUES",
    "Counts",
    "TransferSource",
    "apply_to_cas",
    "backfill_source_label_totals",
    "build_parser",
    "build_transferred_annotations",
    "counts_from_joint",
    "crosstab",
    "leaf_accessions",
    "main",
    "parse_sources",
    "read_delimited",
    "subatlas_registry",
]
