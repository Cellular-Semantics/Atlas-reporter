"""Unit tests for CAS+ as tables a person can read."""

from __future__ import annotations

import json

import pytest
from atlas_chat.services.cas_report import (
    BOM,
    COLUMNS,
    CasReportError,
    annotations_table,
    chosen,
    rows,
    select,
    write_text,
    write_xlsx,
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


def _names(cols) -> list[str]:
    return [c.name for c in cols]


def test_every_tabular_annotation_field_has_a_column():
    """The three left out are tables in their own right, or an open-ended object."""
    fields = {c.field for c in COLUMNS}
    assert {"marker_gene_evidence", "comment", "rationale", "rationale_dois"} <= fields
    assert not fields & {"composition", "transferred_annotations", "author_annotation_fields"}


def test_the_ontology_columns_are_there_by_default():
    assert _names(chosen())[6:9] == ["cl_id", "cl_term", "cl_match_type"]
    row = _rows(annotations_table(_cas()))[1]
    assert row[6:9] == ["CL:0000669", "pericyte", "broad match"]


def test_an_unmapped_annotation_leaves_the_ontology_columns_empty():
    """Absent is not the same as unmapped-and-hidden: the columns stay aligned."""
    row = _rows(annotations_table(_cas()))[0]
    assert row[-3:] == ["", "", ""]


def test_minimal_drops_the_free_text_columns_and_nothing_else():
    full, lean = _names(chosen()), _names(chosen(minimal=True))
    assert set(full) - set(lean) == {"cl_mapping_notes", "comment", "rationale"}
    assert "markers" in lean and "synonyms" in lean


def test_named_columns_come_back_in_the_order_asked_for():
    assert _names(chosen(only=["cells", "label"])) == ["cells", "label"]
    rows_ = _rows(annotations_table(_cas(), only=["cells", "label"]))
    assert rows_[0] == ["69711", "Pericytes"]


def test_an_unknown_column_name_says_what_is_available():
    with pytest.raises(CasReportError, match="no such column: nope"):
        chosen(only=["nope"])


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


def test_markers_and_the_other_evidence_fields_are_carried():
    header = _names(chosen())
    assert {"markers", "negative_markers", "synonyms", "rationale_dois"} <= set(header)
    row = _rows(annotations_table(_cas()))[2]
    assert row[header.index("synonyms")] == "cycling PC;PC_cyc"


def test_a_field_carrying_a_tab_or_newline_cannot_break_the_row():
    """Free text would otherwise split one annotation across several rows."""
    text = annotations_table(_cas())
    assert {len(r) for r in _rows(text)} == {len(chosen())}
    notes = _rows(text)[1][_names(chosen()).index("cl_mapping_notes")]
    assert notes == "a note with a tab and a newline"


def test_select_returns_annotations_in_document_order():
    assert [a["cell_set_accession"] for a in select(_cas())] == ["A:L2:01", "A:L3:02", "A:L3:03"]


def test_a_document_with_no_annotations_gives_a_header_and_nothing_else():
    """The degradation case: a report on an empty document is empty, not an error."""
    text = annotations_table({"annotations": []})
    assert text == "\t".join(c.name for c in chosen())
    assert _rows(text) == []


def _written(cas: dict) -> tuple:
    cols = chosen()
    return cols, rows(cas, cols)


def test_a_file_gets_the_byte_order_mark_a_spreadsheet_needs(tmp_path):
    out = tmp_path / "t.tsv"
    write_text(*_written(_cas()), out)
    assert out.read_bytes().startswith(b"\xef\xbb\xbf")
    assert out.read_text(encoding="utf-8-sig").splitlines()[0].startswith("accession")


def test_the_byte_order_mark_can_be_refused(tmp_path):
    out = tmp_path / "t.tsv"
    write_text(*_written(_cas()), out, bom=False)
    assert not out.read_bytes().startswith(b"\xef\xbb\xbf")
    assert BOM not in out.read_text(encoding="utf-8")


def test_the_cli_writes_the_table(tmp_path, capsys):
    from atlas_chat.services.cas_report import main

    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps(_cas()), encoding="utf-8")
    out = tmp_path / "t.tsv"
    assert main(["annotations", "--cas", str(cas), "--format", "tsv", "--out", str(out)]) == 0
    assert "3 annotations" in capsys.readouterr().out
    assert len(out.read_text(encoding="utf-8-sig").splitlines()) == 4


def test_the_cli_reports_a_bad_selection_without_a_traceback(tmp_path, capsys):
    from atlas_chat.services.cas_report import main

    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps(_cas()), encoding="utf-8")
    assert main(["annotations", "--cas", str(cas), "--accession", "A:NOPE"]) == 2
    assert "A:NOPE" in capsys.readouterr().out


# ------------------------------------------------------------------
# The spreadsheet, which is what most readers will actually open
# ------------------------------------------------------------------


def test_the_spreadsheet_carries_the_header_and_every_row(tmp_path):
    from openpyxl import load_workbook

    out = tmp_path / "t.xlsx"
    write_xlsx(*_written(_cas()), out)
    sheet = load_workbook(out).active
    assert sheet.title == "annotations"
    assert [c.value for c in sheet[1]] == _names(chosen())
    assert sheet.max_row == 4
    assert sheet.cell(row=2, column=3).value == "Pericytes"


def test_the_spreadsheet_keeps_the_header_in_view_and_filterable(tmp_path):
    from openpyxl import load_workbook

    out = tmp_path / "t.xlsx"
    write_xlsx(*_written(_cas()), out)
    sheet = load_workbook(out).active
    assert sheet.freeze_panes == "A2"
    assert sheet.auto_filter.ref is not None


def test_the_wide_columns_wrap_and_the_narrow_ones_do_not(tmp_path):
    """A free-text column that does not wrap runs out under its neighbours."""
    from openpyxl import load_workbook
    from openpyxl.utils import get_column_letter

    cols, table = _written(_cas())
    out = tmp_path / "t.xlsx"
    write_xlsx(cols, table, out)
    sheet = load_workbook(out).active
    widths = {
        c.name: sheet.column_dimensions[get_column_letter(i)].width
        for i, c in enumerate(cols, start=1)
    }
    assert widths["comment"] > widths["labelset"]
    index = {c.name: i for i, c in enumerate(cols, start=1)}
    assert sheet.cell(row=2, column=index["comment"]).alignment.wrap_text
    assert not sheet.cell(row=2, column=index["labelset"]).alignment.wrap_text


def test_an_empty_selection_still_writes_a_readable_sheet(tmp_path):
    from openpyxl import load_workbook

    cols = chosen()
    out = tmp_path / "t.xlsx"
    write_xlsx(cols, [], out)
    sheet = load_workbook(out).active
    assert sheet.max_row == 1
    assert sheet.auto_filter.ref is None


def test_xlsx_is_the_default_and_needs_somewhere_to_go(tmp_path, capsys):
    from atlas_chat.services.cas_report import main

    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps(_cas()), encoding="utf-8")
    assert main(["annotations", "--cas", str(cas)]) == 2
    assert "--out" in capsys.readouterr().out

    out = tmp_path / "t.xlsx"
    assert main(["annotations", "--cas", str(cas), "--out", str(out)]) == 0
    assert out.exists()


def test_csv_quotes_what_a_comma_would_otherwise_split(tmp_path):
    cas = _cas()
    cas["annotations"][0]["comment"] = "one, two"
    text = annotations_table(cas, delimiter=",")
    assert '"one, two"' in text
    assert len(text.splitlines()) == 4
