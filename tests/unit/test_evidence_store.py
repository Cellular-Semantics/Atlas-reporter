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
    EvidenceFileError,
    backfill,
    cell_labels,
    collect,
    is_evidence_file,
    load_records,
    record_files,
)


def _item(label: str = "Immune_oLAM", aspect: str = "location", summary: str = "s") -> dict:
    return {
        "cell_label": label,
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
        out / "papers" / "lorenzi2025" / "Mesen_Prepuce_Fetal.evidence.json",
        [_item("Mesen_Prepuce_Fetal", aspect="markers", summary="the prepuce cells")],
    )
    _write(
        out / "papers" / "lorenzi2025" / "Immune_oLAM.evidence.json",
        [_item("Immune_oLAM", aspect="function")],
    )
    # A cell-type scan: one cell type, several papers, filed under the cell type.
    _write(
        out / "Immune_oLAM" / "all_summaries.json",
        [_item("Immune_oLAM", aspect="naming"), _item("Immune_oLAM", aspect="location")],
    )
    # Not evidence, and sitting right where evidence sits: the assembled paper
    # the read quoted from, and a subject block, which is also a list of dicts.
    (out / "papers" / "lorenzi2025" / "paper.json").write_text(
        json.dumps({"narrative": {"text": "..."}, "legends": []}), encoding="utf-8"
    )
    (out / "subjects.json").write_text(
        json.dumps([{"cell_label": "Immune_oLAM", "cell_fullname": "ovary LAM"}]),
        encoding="utf-8",
    )
    return out


@pytest.mark.unit
def test_only_files_named_as_evidence_are_evidence(traversal: Path) -> None:
    """Job files, subject blocks and selections share the tree with evidence.

    A subject block is a list of dicts too, so shape does not separate them —
    and deciding by shape means opening every assembled paper to reject it.
    """
    found = {p.name for p in record_files(traversal)}
    assert "lorenzi2025.json" not in found
    assert found == {
        "Mesen_Prepuce_Fetal.evidence.json",
        "Immune_oLAM.evidence.json",
        "all_summaries.json",
    }


@pytest.mark.unit
def test_both_filing_orders_answer_the_same_question(traversal: Path) -> None:
    """The point of the whole arrangement: a consumer names a cell type and the
    layout is not its problem."""
    items = collect(traversal, "Immune_oLAM")
    assert sorted(i["aspect"] for i in items) == ["function", "location", "naming"]


@pytest.mark.unit
def test_an_item_is_about_exactly_one_cell_type(traversal: Path) -> None:
    """A paper read answers per atlas cell type, so what it says about one is
    not also filed against another. Where an upstream label was split across
    several atlas cell sets, each gets its own answer, because what the source
    says about one of them is rarely what it says about another."""
    (item,) = collect(traversal, "Mesen_Prepuce_Fetal")
    assert item["cell_label"] == "Mesen_Prepuce_Fetal"


@pytest.mark.unit
def test_nothing_else_comes_back(traversal: Path) -> None:
    """The property the per-cell-type directory used to give for free."""
    assert collect(traversal, "Endometrial_ciliated_epithelial") == []
    assert all(i["cell_label"] == "Immune_oLAM" for i in collect(traversal, "Immune_oLAM"))


@pytest.mark.unit
def test_collection_is_stable_between_runs(traversal: Path) -> None:
    assert collect(traversal, "Immune_oLAM") == collect(traversal, "Immune_oLAM")


@pytest.mark.unit
def test_labels_says_what_is_there(traversal: Path) -> None:
    assert cell_labels(traversal) == {"Immune_oLAM": 3, "Mesen_Prepuce_Fetal": 1}


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

    assert json.loads(path.read_text())[0]["cell_label"] == "Immune_uMac_Inf"


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
@pytest.mark.parametrize(
    "name",
    ["Immune_oLAM.evidence.json", "all_summaries.json", "location_evidence_summary.json"],
)
def test_the_evidence_names(name: str) -> None:
    """One new name and two legacy ones, so nothing already written stops being read."""
    assert is_evidence_file(Path("anywhere") / name)


@pytest.mark.unit
@pytest.mark.parametrize("name", ["paper.json", "subjects.json", "cell_type_selection.json"])
def test_what_is_not_evidence(name: str) -> None:
    assert not is_evidence_file(Path("anywhere") / name)


# --- a file that claims to be evidence and is not ----------------------------


@pytest.mark.unit
def test_a_broken_evidence_file_is_an_error_not_a_skip(traversal: Path) -> None:
    """The failure this arrangement exists to avoid.

    Skipping an unreadable file returns a short collection, and a consumer
    cannot tell a cell type with little evidence from one whose evidence would
    not load.
    """
    broken = traversal / "papers" / "lorenzi2025" / "Immune_oLAM.evidence.json"
    broken.write_text("{ not json", encoding="utf-8")

    with pytest.raises(EvidenceFileError) as caught:
        collect(traversal, "Immune_oLAM")

    assert str(broken) in str(caught.value)


@pytest.mark.unit
def test_an_evidence_file_holding_something_else_is_an_error(tmp_path: Path) -> None:
    path = tmp_path / "x.evidence.json"
    path.write_text(json.dumps(["a string, not an item"]), encoding="utf-8")

    with pytest.raises(EvidenceFileError):
        load_records(path)


@pytest.mark.unit
def test_a_lone_item_is_read_as_a_list_of_one(tmp_path: Path) -> None:
    """The legacy single-item form the hook has always accepted."""
    path = tmp_path / "location_evidence_summary.json"
    path.write_text(json.dumps(_item()), encoding="utf-8")

    assert load_records(path) == [_item()]


@pytest.mark.unit
def test_a_cell_label_of_the_wrong_shape_is_named_not_thrown(tmp_path: Path) -> None:
    """Said plainly, because it is what a producer written against an earlier
    shape would do, and a traceback does not tell anyone which file to fix."""
    path = tmp_path / "x.evidence.json"
    item = _item()
    item["cell_label"] = ["Immune_oLAM", "Immune_uftLAM"]
    path.write_text(json.dumps([item]), encoding="utf-8")

    with pytest.raises(EvidenceFileError, match="One cell type per item"):
        load_records(path)
