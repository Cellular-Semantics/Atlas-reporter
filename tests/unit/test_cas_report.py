"""Unit tests for CAS+ as tables a person can read."""

from __future__ import annotations

import json

import pytest
from atlas_chat.services.cas_report import (
    BOM,
    CasReportError,
    annotations_table,
    columns,
    select,
    write,
)

pytestmark = pytest.mark.unit


def _cas() -> dict:
    """Two levels, with one label used at both — the case the accession exists for."""
    return {
        "annotations": [
            {
                "labelset": "L2",
                "cell_label": "Pericytes",
                "cell_fullname": "Pericytes",
                "cell_set_accession": "A:L2:01",
                "parent_cell_set_accession": None,
                "n_cells": 69711,
            },
            {
                "labelset": "L3",
                "cell_label": "Pericytes",
                "cell_fullname": "Pericytes",
                "cell_set_accession": "A:L3:02",
                "parent_cell_set_accession": "A:L2:01",
                "n_cells": 51593,
                "cell_ontology_term_id": "CL:0000669",
                "cell_ontology_term": "pericyte",
                "cell_ontology_match_type": "broad match",
                "cell_ontology_mapping_notes": "a note\twith a tab\nand a newline",
            },
            {
                "labelset": "L3",
                "cell_label": "Mesen_Cyc",
                "cell_fullname": "Cycling pericytes",
                "cell_set_accession": "A:L3:03",
                "parent_cell_set_accession": "A:L2:01",
                "n_cells": 12,
                "synonyms": ["cycling PC", "PC_cyc"],
            },
        ]
    }


def _rows(text: str) -> list[list[str]]:
    return [line.split("\t") for line in text.splitlines()[1:]]


def test_the_table_has_a_header_and_a_line_per_annotation():
    text = annotations_table(_cas())
    assert text.splitlines()[0].split("\t")[:3] == ["accession", "labelset", "label"]
    assert len(_rows(text)) == 3


def test_the_ontology_columns_are_there_by_default():
    assert columns()[-3:] == ("cl_id", "cl_term", "cl_match_type")
    row = _rows(annotations_table(_cas()))[1]
    assert row[-3:] == ["CL:0000669", "pericyte", "broad match"]


def test_an_unmapped_annotation_leaves_the_ontology_columns_empty():
    """Absent is not the same as unmapped-and-hidden: the columns stay aligned."""
    row = _rows(annotations_table(_cas()))[0]
    assert row[-3:] == ["", "", ""]


def test_the_ontology_columns_can_be_dropped():
    assert "cl_id" not in columns(ontology=False)
    assert len(_rows(annotations_table(_cas(), ontology=False))[0]) == 6


def test_one_label_naming_two_cell_sets_gives_two_rows_told_apart_by_accession():
    """The reason the accession is carried: a label does not identify a cell set."""
    rows = [r for r in _rows(annotations_table(_cas())) if r[2] == "Pericytes"]
    assert len(rows) == 2
    assert [r[0] for r in rows] == ["A:L2:01", "A:L3:02"]
    assert [r[5] for r in rows] == ["69711", "51593"]


def test_an_accession_selects_exactly_one_of_them():
    rows = _rows(annotations_table(_cas(), accessions=["A:L3:02"]))
    assert len(rows) == 1
    assert rows[0][0] == "A:L3:02"


def test_selecting_several_accessions_gives_one_table():
    rows = _rows(annotations_table(_cas(), accessions=["A:L2:01", "A:L3:03"]))
    assert [r[0] for r in rows] == ["A:L2:01", "A:L3:03"]


def test_an_unknown_accession_is_an_error_not_a_shorter_table():
    with pytest.raises(CasReportError, match="A:NOPE"):
        annotations_table(_cas(), accessions=["A:NOPE"])


def test_an_unknown_under_is_an_error_not_an_empty_table():
    with pytest.raises(CasReportError, match="Nonexistent"):
        annotations_table(_cas(), under="Nonexistent")


def test_under_an_ambiguous_label_takes_what_sits_beneath_either():
    rows = _rows(annotations_table(_cas(), under="Pericytes"))
    assert sorted(r[0] for r in rows) == ["A:L3:02", "A:L3:03"]


def test_filters_combine():
    rows = _rows(annotations_table(_cas(), under="Pericytes", labelset="L3", match="cycling"))
    assert [r[0] for r in rows] == ["A:L3:03"]


def test_a_full_name_identical_to_the_label_is_left_blank():
    assert _rows(annotations_table(_cas()))[0][3] == ""


def test_the_parent_is_named_so_a_subtree_is_visible():
    assert _rows(annotations_table(_cas()))[1][4] == "Pericytes"


def test_synonyms_and_mapping_notes_are_opt_in():
    assert "synonyms" not in columns()
    assert "cl_mapping_notes" not in columns()
    header = columns(synonyms=True, mapping_notes=True)
    assert header[-2:] == ("synonyms", "cl_mapping_notes")


def test_a_field_carrying_a_tab_or_newline_cannot_break_the_row():
    """Mapping notes are free text; a stray tab would silently shift every column."""
    text = annotations_table(_cas(), mapping_notes=True)
    widths = {len(r) for r in _rows(text)}
    assert widths == {len(columns(mapping_notes=True))}
    assert _rows(text)[1][-1] == "a note with a tab and a newline"


def test_select_returns_annotations_in_document_order():
    assert [a["cell_set_accession"] for a in select(_cas())] == ["A:L2:01", "A:L3:02", "A:L3:03"]


def test_a_document_with_no_annotations_gives_a_header_and_nothing_else():
    """The degradation case: a report on an empty document is empty, not an error."""
    text = annotations_table({"annotations": []})
    assert text == "\t".join(columns())
    assert _rows(text) == []


def test_a_file_gets_the_byte_order_mark_a_spreadsheet_needs(tmp_path):
    out = tmp_path / "t.tsv"
    write(annotations_table(_cas()), out)
    assert out.read_bytes().startswith(b"\xef\xbb\xbf")
    assert out.read_text(encoding="utf-8-sig").splitlines()[0].startswith("accession")


def test_the_byte_order_mark_can_be_refused(tmp_path):
    out = tmp_path / "t.tsv"
    write(annotations_table(_cas()), out, bom=False)
    assert not out.read_bytes().startswith(b"\xef\xbb\xbf")
    assert BOM not in out.read_text(encoding="utf-8")


def test_the_cli_writes_the_table(tmp_path, capsys):
    from atlas_chat.services.cas_report import main

    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps(_cas()), encoding="utf-8")
    out = tmp_path / "t.tsv"
    assert main(["annotations", "--cas", str(cas), "--out", str(out)]) == 0
    assert "3 annotations" in capsys.readouterr().out
    assert len(out.read_text(encoding="utf-8-sig").splitlines()) == 4


def test_the_cli_reports_a_bad_selection_without_a_traceback(tmp_path, capsys):
    from atlas_chat.services.cas_report import main

    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps(_cas()), encoding="utf-8")
    assert main(["annotations", "--cas", str(cas), "--accession", "A:NOPE"]) == 2
    assert "A:NOPE" in capsys.readouterr().out
