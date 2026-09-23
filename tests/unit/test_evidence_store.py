"""The evidence store: finding items, and reading back the ones about a cell type.

The contract this pins is that a consumer asks for a cell type and gets every
item about it, wherever it was written and whatever produced it — and gets
nothing else. A producer filing somewhere new must not need a consumer change,
and that is what most of these assert.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from atlas_chat.services.evidence_store import (
    backfill,
    cell_labels,
    collect,
    looks_like_record,
    record_files,
)


def _item(*labels: str, aspect: str = "location", summary: str = "s") -> dict:
    return {
        "cell_label": list(labels),
        "source_paper": {"doi": "10.1/x", "role": "atlas"},
        "retrieval_method": "corpus_snippet",
        "aspect": aspect,
        "found": True,
        "summary": summary,
        "quotes": ["q"],
    }


def _write(path: Path, items: list[dict]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(items, indent=2), encoding="utf-8")
    return path


@pytest.fixture
def traversal(tmp_path: Path) -> Path:
    """Both filing orders at once, which is the situation the store exists for."""
    out = tmp_path / "traversal_output"
    # A paper read: one paper, several cell types, filed under the paper.
    _write(
        out / "papers" / "lorenzi2025" / "Mesen_Prepuce_Fetal.json",
        [
            _item(
                "Mesen_Prepuce_Fetal",
                "Mesen_LabioScrotalSwelling_Fetal",
                aspect="markers",
                summary="split three ways",
            )
        ],
    )
    _write(
        out / "papers" / "lorenzi2025" / "Immune_oLAM.json",
        [_item("Immune_oLAM", aspect="function")],
    )
    # A cell-type scan: one cell type, several papers, filed under the cell type.
    _write(
        out / "Immune_oLAM" / "all_summaries.json",
        [_item("Immune_oLAM", aspect="naming"), _item("Immune_oLAM", aspect="location")],
    )
    # Not evidence: an assembled paper, sitting where evidence also sits.
    (out / "papers" / "lorenzi2025.json").write_text(
        json.dumps({"narrative": {"text": "..."}, "legends": []}), encoding="utf-8"
    )
    return out


@pytest.mark.unit
def test_an_assembled_paper_is_not_evidence(traversal: Path) -> None:
    """Job files, subject blocks and selections share the directory with evidence.

    Telling them apart by shape rather than by filename is what lets a producer
    name its output whatever suits it.
    """
    found = {p.name for p in record_files(traversal)}
    assert "lorenzi2025.json" not in found
    assert found == {"Mesen_Prepuce_Fetal.json", "Immune_oLAM.json", "all_summaries.json"}


@pytest.mark.unit
def test_both_filing_orders_answer_the_same_question(traversal: Path) -> None:
    """The point of the whole arrangement: a consumer names a cell type and the
    layout is not its problem."""
    items = collect(traversal, "Immune_oLAM")
    assert sorted(i["aspect"] for i in items) == ["function", "location", "naming"]


@pytest.mark.unit
def test_an_item_about_several_cell_types_is_returned_for_each(traversal: Path) -> None:
    for label in ("Mesen_Prepuce_Fetal", "Mesen_LabioScrotalSwelling_Fetal"):
        assert [i["summary"] for i in collect(traversal, label)] == ["split three ways"]


@pytest.mark.unit
def test_a_collected_item_still_names_its_other_cell_types(traversal: Path) -> None:
    """A finding about a boundary between three cell sets has to be reportable as
    one, so the item keeps saying what else it is about."""
    (item,) = collect(traversal, "Mesen_Prepuce_Fetal")
    assert item["cell_label"] == ["Mesen_Prepuce_Fetal", "Mesen_LabioScrotalSwelling_Fetal"]


@pytest.mark.unit
def test_nothing_else_comes_back(traversal: Path) -> None:
    """The property the per-cell-type directory used to give for free."""
    assert collect(traversal, "Endometrial_ciliated_epithelial") == []
    assert all("Immune_oLAM" in i["cell_label"] for i in collect(traversal, "Immune_oLAM"))


@pytest.mark.unit
def test_collection_is_stable_between_runs(traversal: Path) -> None:
    assert collect(traversal, "Immune_oLAM") == collect(traversal, "Immune_oLAM")


@pytest.mark.unit
def test_labels_says_what_is_there(traversal: Path) -> None:
    assert cell_labels(traversal) == {
        "Immune_oLAM": 3,
        "Mesen_LabioScrotalSwelling_Fetal": 1,
        "Mesen_Prepuce_Fetal": 1,
    }


# --- backfill ----------------------------------------------------------------


@pytest.mark.unit
def test_backfill_takes_the_label_from_the_directory(tmp_path: Path) -> None:
    """Evidence written before items carried a label was identified by where it
    sat, so recovering it is a rename, not a judgement."""
    out = tmp_path / "traversal_output"
    legacy = _item()
    del legacy["cell_label"]
    path = _write(out / "Immune_uMac_Inf" / "all_summaries.json", [legacy])

    backfill(out)

    assert json.loads(path.read_text())[0]["cell_label"] == ["Immune_uMac_Inf"]


@pytest.mark.unit
def test_backfill_leaves_a_label_that_is_already_there(traversal: Path) -> None:
    before = {p: p.read_text() for p in record_files(traversal)}
    assert backfill(traversal) == []
    assert {p: p.read_text() for p in record_files(traversal)} == before


@pytest.mark.unit
def test_a_dry_run_writes_nothing(tmp_path: Path) -> None:
    out = tmp_path / "traversal_output"
    legacy = _item()
    del legacy["cell_label"]
    path = _write(out / "Immune_uMac_Inf" / "all_summaries.json", [legacy])

    report = backfill(out, dry_run=True)

    assert report and "would fill" in report[0]
    assert "cell_label" not in json.loads(path.read_text())[0]


@pytest.mark.unit
def test_an_unattributable_item_is_reported_not_guessed(tmp_path: Path) -> None:
    """A file at the top of the traversal directory has no cell type name to take.

    Reporting it leaves someone to deal with; filling it with the nearest
    available string files evidence under a cell type that was never read.
    """
    out = tmp_path / "traversal_output"
    legacy = _item()
    del legacy["cell_label"]
    path = _write(out / "all_summaries.json", [legacy])

    (line,) = backfill(out)

    assert "skipped" in line
    assert "cell_label" not in json.loads(path.read_text())[0]


@pytest.mark.unit
def test_looks_like_record_wants_all_three_fields() -> None:
    assert looks_like_record(_item("X"))
    assert not looks_like_record({"summary": "s", "quotes": []})
    assert not looks_like_record("a string")
