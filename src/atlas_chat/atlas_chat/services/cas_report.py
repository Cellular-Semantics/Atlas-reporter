"""CAS+ as tables a person can read.

A CAS+ document is mostly the breakdown of every descriptor over every cell and
the provenance of every label it inherited. Both run to thousands of entries and
neither says what a cell type is called, where it sits, or what it was mapped to.
Strip them out and what is left is a few hundred short lines — small enough to
read end to end, and to open in a spreadsheet.

The ontology columns are here because a mapping is reviewed by reading it beside
the label it was made for. ``cell_ontology_match_type`` is carried next to the
term rather than left out: a broad match and an exact one are different claims,
and a reviewer scanning for the mappings worth challenging is scanning for that
column.

Cell sets are identified by accession. A label is not unique — an atlas may use
one at two levels of its hierarchy, for cell sets with different members and
different terms — so a selection may legitimately return several, and the table
carries the accession to tell them apart.

Nothing here is computed that the document does not already state, and nothing
here calls a model.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

#: The accession, carried first where it is carried at all. Optional only
#: because :func:`project_paths.outline` predates it and callers read its
#: columns by position.
ACCESSION_COLUMN = "accession"

#: Columns always present, in order.
BASE_COLUMNS = ("labelset", "label", "full name", "parent", "cells")

#: Columns carrying the ontology mapping, in order. Present by default: a
#: document with no mappings yields them empty, which is itself worth seeing.
ONTOLOGY_COLUMNS = ("cl_id", "cl_term", "cl_match_type")

#: Opt-in columns, each wide enough to spoil the table for readers who did not
#: ask for it.
SYNONYM_COLUMN = "synonyms"
MAPPING_NOTES_COLUMN = "cl_mapping_notes"

#: Written at the head of a TSV file so a spreadsheet reads it as UTF-8 rather
#: than as the machine's legacy codepage.
BOM = "﻿"


class CasReportError(RuntimeError):
    """Raised when a selection cannot be resolved."""


def _searchable(annotation: dict[str, Any]) -> str:
    parts = [annotation.get("cell_label", ""), annotation.get("cell_fullname") or ""]
    parts.extend(annotation.get("synonyms") or [])
    return " ".join(parts).lower()


def _descendants(root: str, by_parent: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    stack = list(by_parent.get(root, []))
    while stack:
        node = stack.pop()
        out.append(node)
        stack.extend(by_parent.get(node.get("cell_set_accession") or "", []))
    return out


def select(
    cas: dict[str, Any],
    *,
    labelset: str | None = None,
    match: str | None = None,
    under: str | None = None,
    accessions: list[str] | None = None,
) -> list[dict[str, Any]]:
    """The annotations a request names, in document order.

    Filters combine: each narrows what the ones before it left. ``under`` naming
    a label used at two levels takes what sits under both, because the result is
    one table keyed by accession and the two subtrees are distinguishable in it.

    Args:
        cas: the CAS+ document.
        labelset: keep only this level.
        match: keep annotations whose label, full name or synonyms contain this.
        under: keep everything beneath the annotation(s) with this label.
        accessions: keep exactly these cell sets.

    Returns:
        The annotations selected, in document order.

    Raises:
        CasReportError: an accession or an ``under`` label is not in the
            document. Silently returning a smaller table would read as a finding.
    """
    annotations = cas.get("annotations") or []
    by_parent: dict[str, list[dict[str, Any]]] = {}
    for a in annotations:
        by_parent.setdefault(a.get("parent_cell_set_accession") or "", []).append(a)

    kept = list(annotations)
    if accessions:
        known = {a.get("cell_set_accession") for a in annotations}
        missing = [x for x in accessions if x not in known]
        if missing:
            raise CasReportError(f"not in the document: {', '.join(sorted(missing))}")
        wanted = set(accessions)
        kept = [a for a in kept if a.get("cell_set_accession") in wanted]
    if under:
        roots = [a for a in annotations if a.get("cell_label") == under]
        if not roots:
            raise CasReportError(f"not in the document: {under}")
        beneath = {
            id(a)
            for root in roots
            for a in _descendants(root.get("cell_set_accession") or "", by_parent)
        }
        kept = [a for a in kept if id(a) in beneath]
    if labelset:
        kept = [a for a in kept if a.get("labelset") == labelset]
    if match:
        needle = match.lower()
        kept = [a for a in kept if needle in _searchable(a)]
    return kept


def columns(
    *,
    accession: bool = True,
    ontology: bool = True,
    synonyms: bool = False,
    mapping_notes: bool = False,
) -> tuple[str, ...]:
    """The header, in the order the rows are written."""
    out = ([ACCESSION_COLUMN] if accession else []) + list(BASE_COLUMNS)
    if ontology:
        out.extend(ONTOLOGY_COLUMNS)
    if synonyms:
        out.append(SYNONYM_COLUMN)
    if mapping_notes:
        out.append(MAPPING_NOTES_COLUMN)
    return tuple(out)


def _cell(value: Any) -> str:
    """One field, with the tabs and newlines a TSV row cannot carry removed."""
    if value is None:
        return ""
    text = str(value)
    return " ".join(text.split()) if ("\t" in text or "\n" in text) else text


def row(
    annotation: dict[str, Any],
    *,
    label_of: dict[str, str],
    accession: bool = True,
    ontology: bool = True,
    synonyms: bool = False,
    mapping_notes: bool = False,
) -> list[str]:
    """One annotation as fields, matching :func:`columns`."""
    fullname = annotation.get("cell_fullname") or ""
    out = [_cell(annotation.get("cell_set_accession"))] if accession else []
    out += [
        _cell(annotation.get("labelset")),
        _cell(annotation.get("cell_label")),
        "" if fullname == annotation.get("cell_label") else _cell(fullname),
        _cell(label_of.get(annotation.get("parent_cell_set_accession") or "")),
        _cell(annotation.get("n_cells")),
    ]
    if ontology:
        term_id = annotation.get("cell_ontology_term_id")
        # An ambiguous mapping is stored as a list rather than dropped; show it
        # as one rather than showing the first and implying a decision.
        out.extend(
            [
                ";".join(term_id) if isinstance(term_id, list) else _cell(term_id),
                _cell(annotation.get("cell_ontology_term")),
                _cell(annotation.get("cell_ontology_match_type")),
            ]
        )
    if synonyms:
        out.append(";".join(annotation.get("synonyms") or []))
    if mapping_notes:
        out.append(_cell(annotation.get("cell_ontology_mapping_notes")))
    return out


def annotations_table(
    cas: dict[str, Any],
    *,
    labelset: str | None = None,
    match: str | None = None,
    under: str | None = None,
    accessions: list[str] | None = None,
    accession_column: bool = True,
    ontology: bool = True,
    synonyms: bool = False,
    mapping_notes: bool = False,
) -> str:
    """The annotation hierarchy and its mappings, as a TSV table.

    Args:
        cas: the CAS+ document.
        labelset: keep only this level.
        match: keep annotations whose label, full name or synonyms contain this.
        under: keep everything beneath the annotation(s) with this label.
        accessions: keep exactly these cell sets.
        accession_column: carry the accession, which alone identifies a cell set.
        ontology: carry the ontology mapping columns.
        synonyms: carry the synonyms column.
        mapping_notes: carry the mapping-notes column.

    Returns:
        A header line and one line per annotation, tab-separated, in document
        order. Empty where a field is absent, so the columns stay aligned.

    Raises:
        CasReportError: the selection names something not in the document.
    """
    kept = select(cas, labelset=labelset, match=match, under=under, accessions=accessions)
    label_of = {
        a["cell_set_accession"]: a["cell_label"]
        for a in (cas.get("annotations") or [])
        if a.get("cell_set_accession")
    }
    header = columns(
        accession=accession_column,
        ontology=ontology,
        synonyms=synonyms,
        mapping_notes=mapping_notes,
    )
    lines = ["\t".join(header)]
    lines += [
        "\t".join(
            row(
                a,
                label_of=label_of,
                accession=accession_column,
                ontology=ontology,
                synonyms=synonyms,
                mapping_notes=mapping_notes,
            )
        )
        for a in kept
    ]
    return "\n".join(lines)


def write(table: str, out: Path, *, bom: bool = True) -> None:
    """Write a table to a file, with the byte-order mark a spreadsheet needs."""
    out.write_text((BOM if bom else "") + table + "\n", encoding="utf-8")


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m atlas_chat.cli_report",
        description="CAS+ as tables a person can read.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    table = sub.add_parser("annotations", help="the annotation hierarchy and its mappings")
    table.add_argument("--cas", required=True, help="the CAS+ document")
    table.add_argument("--labelset", help="keep only this level")
    table.add_argument("--match", help="keep annotations whose label, full name or synonyms match")
    table.add_argument("--under", help="keep everything beneath this annotation")
    table.add_argument(
        "--accession",
        action="append",
        help="repeatable; names a cell set exactly, for a label used at more than one level",
    )
    table.add_argument(
        "--no-ontology", action="store_true", help="drop the ontology mapping columns"
    )
    table.add_argument("--synonyms", action="store_true", help="include synonyms")
    table.add_argument(
        "--mapping-notes", action="store_true", help="include the mapping-notes column"
    )
    table.add_argument("--out", help="write here instead of stdout")
    table.add_argument(
        "--no-bom",
        action="store_true",
        help="omit the byte-order mark; it is written to a file so a spreadsheet reads UTF-8",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cas = json.loads(Path(args.cas).read_text(encoding="utf-8"))
    try:
        table = annotations_table(
            cas,
            labelset=args.labelset,
            match=args.match,
            under=args.under,
            accessions=args.accession,
            ontology=not args.no_ontology,
            synonyms=args.synonyms,
            mapping_notes=args.mapping_notes,
        )
    except CasReportError as exc:
        print(str(exc))
        return 2
    if args.out:
        write(table, Path(args.out), bom=not args.no_bom)
        print(f"{len(table.splitlines()) - 1} annotations -> {args.out}")
    else:
        print(table)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
