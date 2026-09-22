"""Unit tests for the differential-expression store."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest
from atlas_chat.services.degs import (
    DegsError,
    check_store,
    main,
    validate_document,
)

from atlas_chat.schemas import load_schema

pytestmark = pytest.mark.unit


def _gene(symbol: str, lfc: float) -> dict:
    return {
        "symbol": symbol,
        "direction": "up" if lfc > 0 else "down",
        "scores": {"log2FC": lfc, "padj": 1e-9},
    }


def _doc(**over) -> dict:
    comparison = {
        "comparison": "one-versus-rest against the other macrophage subsets",
        "comparison_is_quoted": True,
        "source": {"doi": "10.1/x", "file_id": "media-5.xlsx", "locator": "A. DEGs"},
        "effect_field": "log2FC",
        "n_genes": 3,
        "n_up": 2,
        "genes": [_gene("FCGBP", 3.2), _gene("PADI2", 4.6), _gene("DAB2", -1.4)],
    }
    comparison.update(over)
    return {"cell_label": "Immune_uftLAM", "comparisons": [comparison]}


def _store(tmp_path: Path, *, doc: dict | None = None, readme=True, script=True) -> Path:
    d = tmp_path / "degs"
    d.mkdir()
    if doc is not None:
        (d / "Immune_uftLAM.json").write_text(json.dumps(doc))
    if readme:
        (d / "README.md").write_text("converted from media-5.xlsx sheet A")
    if script:
        (d / "extract_media5.py").write_text("# the conversion")
    return d


def test_the_schema_is_well_formed():
    jsonschema.Draft202012Validator.check_schema(load_schema("degs.schema.json"))


def test_a_conforming_document_passes():
    assert validate_document(_doc()) == []


def test_scores_may_use_whatever_the_authors_called_them():
    """Papers score differently; enumerating the fields would fail on the next."""
    doc = _doc(
        effect_field="avg_log2FC",
        n_genes=1,
        n_up=1,
        genes=[
            {"symbol": "X", "direction": "up", "scores": {"avg_log2FC": 2.0, "p_val_adj": 0.01}}
        ],
    )
    assert validate_document(doc) == []


def test_a_comparison_must_say_what_was_compared():
    doc = _doc()
    del doc["comparisons"][0]["comparison"]
    assert validate_document(doc)


def test_a_source_without_a_doi_passes():
    """Results are not always published alongside a paper; a table can be
    supplied directly."""
    doc = _doc(source={"file_id": "uftLAM_degs.json", "locator": "Immune_uftLAM"})
    assert validate_document(doc) == []


def test_a_source_that_locates_nothing_is_rejected():
    doc = _doc(source={})
    assert validate_document(doc)


def test_the_effect_field_must_be_named():
    doc = _doc()
    del doc["comparisons"][0]["effect_field"]
    assert validate_document(doc)


def test_an_effect_field_absent_from_a_gene_is_caught():
    """A named score missing from some rows usually means a block boundary was
    crossed and the columns shifted."""
    doc = _doc(effect_field="logFC")
    errors = validate_document(doc)
    assert any("absent from 3 gene(s)" in e for e in errors)


def test_a_gene_count_that_disagrees_with_the_rows_is_caught():
    """A wrong count is worse than none: it is read as a statement about what
    the paper published, and used to interpret absence."""
    errors = validate_document(_doc(n_genes=99))
    assert any("n_genes is 99 but 3 are listed" in e for e in errors)


def test_an_up_count_that_disagrees_is_caught():
    errors = validate_document(_doc(n_up=3))
    assert any("n_up is 3 but 2 are marked up" in e for e in errors)


def test_direction_is_constrained():
    doc = _doc()
    doc["comparisons"][0]["genes"][0]["direction"] = "enriched"
    assert validate_document(doc)


def test_a_document_needs_at_least_one_comparison():
    assert validate_document({"cell_label": "X", "comparisons": []})


def test_unknown_fields_are_rejected():
    doc = _doc()
    doc["comparisons"][0]["pvalue_cutoff"] = 0.05
    assert validate_document(doc)


# --- the store, and whether it can be redone ---------------------------------


def test_a_complete_store_passes_and_counts_what_it_holds(tmp_path):
    report = check_store(_store(tmp_path, doc=_doc()))
    assert report.ok
    assert report.files == 1
    assert report.cell_sets == ["Immune_uftLAM"]
    assert report.comparisons == 1
    assert report.genes == 3


def test_a_store_without_the_conversion_code_fails(tmp_path):
    """Numbers nobody can trace back to a table are not evidence."""
    report = check_store(_store(tmp_path, doc=_doc(), script=False))
    assert not report.ok
    assert any("conversion" in e for e in report.errors)


def test_a_store_without_a_note_fails(tmp_path):
    report = check_store(_store(tmp_path, doc=_doc(), readme=False))
    assert not report.ok
    assert any("README" in e for e in report.errors)


def test_an_empty_store_fails_rather_than_passing_vacuously(tmp_path):
    report = check_store(_store(tmp_path))
    assert not report.ok
    assert any("no documents" in e for e in report.errors)


def test_an_invalid_document_is_reported_with_its_filename(tmp_path):
    report = check_store(_store(tmp_path, doc=_doc(n_genes=99)))
    assert any(e.startswith("Immune_uftLAM.json:") for e in report.errors)


def test_a_missing_store_is_an_error(tmp_path):
    with pytest.raises(DegsError):
        check_store(tmp_path / "nowhere")


def test_cli_reports_a_good_store(tmp_path, capsys):
    assert main(["--store", str(_store(tmp_path, doc=_doc()))]) == 0
    assert json.loads(capsys.readouterr().out)["ok"] is True


def test_cli_exits_nonzero_on_a_bad_document(tmp_path, capsys):
    store = _store(tmp_path, doc=_doc(n_up=3))
    assert main(["--file", str(store / "Immune_uftLAM.json")]) == 2
    assert "n_up" in capsys.readouterr().out


def test_cli_needs_exactly_one_of_store_or_file(capsys):
    assert main([]) == 2
    assert "exactly one" in capsys.readouterr().out
