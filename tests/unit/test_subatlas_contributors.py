"""The cutoff-applied contributors view.

Thresholds are calibrated against the reference project (HCA_reproductive):
contribution >= 0.05 AND >= 50 cells gives a median of 2 qualifying papers per
cell set; a 0.02 within-source floor cuts labels listed per paper from a median
of 8 to 2 while keeping the informative minority calls.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from atlas_chat.services import subatlas_contributors as sc

pytestmark = pytest.mark.unit

SCHEMA = json.loads(
    (
        Path(__file__).resolve().parents[2]
        / "src/atlas_chat/atlas_chat/schemas/subatlas_contributors.schema.json"
    ).read_text()
)


def _ta(label, paper, count, *, total=None, labelset=None):
    item = {
        "transferred_cell_label": label,
        "subatlas_paper": paper,
        "cell_count": count,
        "source_labelset": labelset or paper,
    }
    if total:
        item["source_label_cell_count"] = total
    return item


def _doc(annotations, papers=None):
    return {
        "title": "t",
        "source": {
            "doi": "10.1/atlas",
            "subatlas_papers": papers if papers is not None else [{"label": "P", "doi": "10.1/p"}],
        },
        "labelsets": [],
        "annotations": annotations,
    }


def _annotation(transferred, n_cells=1000, label="set A"):
    return {
        "labelset": "L4",
        "cell_label": label,
        "n_cells": n_cells,
        "transferred_annotations": transferred,
    }


def _valid(result):
    return [e.message for e in Draft202012Validator(SCHEMA).iter_errors(result)]


# ---------------------------------------------------------------- denominators


def test_the_two_denominators_are_computed_separately():
    """The whole point of the object: contribution and purity are independent.

    A paper contributing 10% of the cell set having called all of it one thing,
    against one contributing 10% split three ways, are different findings.
    cell_ratio alone reads both as "10%".
    """
    ann = _annotation(
        [
            _ta("Capillary", "P", 59),
            _ta("tPCV", "P", 22),
            _ta("aPCV", "P", 19),
        ],
        n_cells=1000,
    )
    result = sc.summarise(ann, _doc([ann]))
    assert _valid(result) == []
    contributor = result["contributors"][0]
    assert contributor["from_source_cells"] == 100
    assert contributor["contribution"] == 0.1  # of the 1000-cell set
    assert contributor["purity"] == 0.59  # of the 100 cells this paper contributed
    assert contributor["dominant_label"] == "Capillary"
    # within_source_share, not share_of_set, is what shows the split.
    shares = {i["transferred_cell_label"]: i["within_source_share"] for i in contributor["labels"]}
    assert shares == {"Capillary": 0.59, "tPCV": 0.22, "aPCV": 0.19}
    assert contributor["labels"][0]["share_of_set"] == 0.059


def test_reverse_share_comes_from_the_atlas_wide_total():
    ann = _annotation([_ta("Capillary", "P", 200, total=1000)], n_cells=1000)
    label = sc.summarise(ann, _doc([ann]))["contributors"][0]["labels"][0]
    # This cell set holds a fifth of everything the upstream paper called Capillary.
    assert label["reverse_share"] == 0.2
    assert label["source_label_cell_count"] == 1000


def test_reverse_share_is_absent_when_the_total_is_not_recorded():
    ann = _annotation([_ta("Capillary", "P", 200)], n_cells=1000)
    label = sc.summarise(ann, _doc([ann]))["contributors"][0]["labels"][0]
    assert "reverse_share" not in label


# ---------------------------------------------------------------- the cutoff


@pytest.mark.parametrize(
    ("count", "n_cells", "expected"),
    [
        (200, 1000, "kept"),  # 20% and 200 cells
        (50, 1000, "kept"),  # exactly at both floors
        (49, 1000, "tail"),  # 4.9% — below the share floor
        (60, 2000, "tail"),  # 60 cells but only 3%
        (40, 100, "tail"),  # 40% but only 40 cells: a big share of a tiny set
    ],
)
def test_a_contributor_must_clear_both_floors(count, n_cells, expected):
    ann = _annotation([_ta("X", "P", count)], n_cells=n_cells)
    result = sc.summarise(ann, _doc([ann]))
    kept = [c["subatlas_paper"] for c in result["contributors"]]
    assert (kept == ["P"]) is (expected == "kept")
    assert (result["tail"]["papers"] == ["P"]) is (expected == "tail")


@pytest.mark.parametrize(
    ("count", "tier"), [(200, "primary"), (199, "secondary"), (50, "secondary")]
)
def test_tier_splits_at_the_primary_threshold(count, tier):
    """Tier is the cost control: only 'primary' warrants fetching the paper's text."""
    ann = _annotation([_ta("X", "P", count)], n_cells=1000)
    assert sc.summarise(ann, _doc([ann]))["contributors"][0]["tier"] == tier


def test_thresholds_are_recorded_on_the_output():
    ann = _annotation([_ta("X", "P", 200)], n_cells=1000)
    thresholds = sc.Thresholds(min_contribution=0.3, min_source_cells=1)
    result = sc.summarise(ann, _doc([ann]), thresholds=thresholds)
    assert result["thresholds"]["min_contribution"] == 0.3
    # A coverage claim in a report is only reproducible if the cutoff is on the file.
    assert result["contributors"] == []
    assert result["no_dominant_contributor"] is True


def test_the_tail_is_aggregated_never_dropped():
    ann = _annotation(
        [_ta("X", "Big", 500)] + [_ta("Y", f"Small{i}", 5) for i in range(12)],
        n_cells=1000,
    )
    papers = [{"label": "Big", "doi": "10.1/big"}] + [
        {"label": f"Small{i}", "doi": f"10.1/s{i}"} for i in range(12)
    ]
    result = sc.summarise(ann, _doc([ann], papers))
    assert [c["subatlas_paper"] for c in result["contributors"]] == ["Big"]
    assert result["tail"]["n_papers"] == 12
    assert result["tail"]["cell_count"] == 60
    assert result["tail"]["contribution"] == 0.06
    # Named, so a threshold change is diffable.
    assert len(result["tail"]["papers"]) == 12


def test_contributors_are_ordered_by_descending_contribution():
    ann = _annotation(
        [_ta("A", "Small", 100), _ta("B", "Big", 400), _ta("C", "Mid", 200)],
        n_cells=1000,
    )
    papers = [{"label": n, "doi": f"10.1/{n}"} for n in ("Small", "Big", "Mid")]
    result = sc.summarise(ann, _doc([ann], papers))
    assert [c["subatlas_paper"] for c in result["contributors"]] == ["Big", "Mid", "Small"]


# ---------------------------------------------------------------- within-source floor


def test_minor_labels_roll_up_within_a_contributor():
    ann = _annotation(
        [_ta("Dominant", "P", 500)] + [_ta(f"Noise{i}", "P", 1) for i in range(20)],
        n_cells=1000,
    )
    contributor = sc.summarise(ann, _doc([ann]))["contributors"][0]
    assert [i["transferred_cell_label"] for i in contributor["labels"]] == ["Dominant"]
    assert contributor["n_tail_labels"] == 20
    assert contributor["tail_cells"] == 20
    # Everything is still accounted for — the hook checks this invariant too.
    assert (
        sum(i["cell_count"] for i in contributor["labels"]) + contributor["tail_cells"]
        == contributor["from_source_cells"]
    )


def test_a_minority_label_above_the_floor_survives():
    """Ulrich's 11% `aPCV` is the label the atlas adopted; it must not be rolled up.

    Only the three largest of that contributor's labels here, so the purity
    denominator is 307 rather than the real 332 — the real numbers are pinned in
    ``test_the_reference_cell_set_reproduces_the_documented_numbers``.
    """
    ann = _annotation(
        [_ta("Capillary", "P", 197), _ta("tPCV", "P", 73), _ta("aPCV", "P", 37)],
        n_cells=4851,
    )
    contributor = sc.summarise(ann, _doc([ann]))["contributors"][0]
    labels = [i["transferred_cell_label"] for i in contributor["labels"]]
    assert labels == ["Capillary", "tPCV", "aPCV"]
    assert contributor["purity"] == pytest.approx(197 / 307, abs=1e-4)
    # 12% of this contributor's cells, well clear of the 2% floor.
    apcv = contributor["labels"][2]
    assert apcv["within_source_share"] == pytest.approx(37 / 307, abs=1e-4)


def test_the_dominant_label_survives_even_below_the_floor():
    """A contributor smeared over hundreds of labels still names its top call."""
    ann = _annotation([_ta(f"L{i}", "P", 1) for i in range(300)], n_cells=1000)
    contributor = sc.summarise(ann, _doc([ann]))["contributors"][0]
    assert len(contributor["labels"]) == 1
    assert contributor["n_tail_labels"] == 299
    assert contributor["dominant_label"] == contributor["labels"][0]["transferred_cell_label"]


# ---------------------------------------------------------------- edges


def test_no_contributor_over_the_cutoff_is_a_positive_finding():
    """62 of 303 reference cell sets land here — pooled or de-novo calls."""
    ann = _annotation([_ta("X", "P", 5)], n_cells=1000)
    result = sc.summarise(ann, _doc([ann]))
    assert result["no_dominant_contributor"] is True
    assert result["contributors"] == []
    assert _valid(result) == []


def test_a_contributor_with_no_publication_is_held_apart_from_the_tail():
    """It was not excluded for being small — there is simply nothing to retrieve."""
    ann = _annotation([_ta("Endo_Cap", "Sanger", 300), _ta("X", "P", 200)], n_cells=1000)
    papers = [{"label": "Sanger", "status": "unresolved"}, {"label": "P", "doi": "10.1/p"}]
    result = sc.summarise(ann, _doc([ann], papers))
    assert [c["subatlas_paper"] for c in result["contributors"]] == ["P"]
    assert result["unpublished_cells"] == 300
    assert result["tail"]["n_papers"] == 0


def test_non_paper_labels_are_counted_as_unpublished():
    ann = _annotation([_ta("X", "whole_embryo", 700), _ta("Y", "P", 200)], n_cells=1000)
    result = sc.summarise(ann, _doc([ann]), non_paper_labels=["whole_embryo"])
    assert [c["subatlas_paper"] for c in result["contributors"]] == ["P"]
    assert result["unpublished_cells"] == 700


def test_source_taxonomy_is_used_when_subatlas_paper_is_absent():
    ann = _annotation(
        [
            {
                "transferred_cell_label": "X",
                "source_taxonomy": "DOI:10.1/from-taxonomy",
                "cell_count": 200,
            }
        ],
        n_cells=1000,
    )
    contributor = sc.summarise(ann, _doc([ann], []))["contributors"][0]
    assert contributor["subatlas_paper"] == "DOI:10.1/from-taxonomy"
    assert contributor["doi"] == "10.1/from-taxonomy"


def test_registry_status_and_band_are_carried_through():
    """A 'no match' from an unreachable paper is a retrieval limit, not disagreement."""
    ann = _annotation([_ta("X", "P", 200)], n_cells=1000)
    papers = [
        {
            "label": "P",
            "doi": "10.1/p",
            "status": "needs_pdf",
            "asta_indexing": {"band": "abstract_only"},
        }
    ]
    contributor = sc.summarise(ann, _doc([ann], papers))["contributors"][0]
    assert contributor["status"] == "needs_pdf"
    assert contributor["asta_band"] == "abstract_only"


def test_missing_n_cells_raises_rather_than_reporting_nothing():
    ann = {"labelset": "L4", "cell_label": "x", "transferred_annotations": [_ta("X", "P", 5)]}
    with pytest.raises(ValueError, match="no n_cells"):
        sc.summarise(ann, _doc([ann]))


# ---------------------------------------------------------------- lookup + batch


def test_find_annotation_requires_a_labelset_when_the_label_is_ambiguous():
    doc = _doc(
        [
            {"labelset": "L4", "cell_label": "aPCV", "n_cells": 1},
            {"labelset": "L3", "cell_label": "aPCV", "n_cells": 2},
        ]
    )
    with pytest.raises(KeyError, match=r"labelsets \['L3', 'L4'\]"):
        sc.find_annotation(doc, "aPCV")
    assert sc.find_annotation(doc, "aPCV", "L3")["n_cells"] == 2


def test_find_annotation_names_the_missing_label():
    with pytest.raises(KeyError, match="no annotation with cell_label 'nope'"):
        sc.find_annotation(_doc([]), "nope")


def test_summarise_all_skips_sets_without_provenance_and_survives_a_bad_one(caplog):
    doc = _doc(
        [
            _annotation([_ta("X", "P", 200)], label="good"),
            {"labelset": "L4", "cell_label": "no provenance", "n_cells": 10},
            {
                "labelset": "L4",
                "cell_label": "no n_cells",
                "transferred_annotations": [_ta("X", "P", 5)],
            },
        ]
    )
    results = sc.summarise_all(doc)
    assert [r["cell_label"] for r in results] == ["good"]
    assert "no n_cells" in caplog.text


# ---------------------------------------------------------------- CLI


def test_cli_writes_one_cell_set(tmp_path, capsys):
    ann = _annotation([_ta("X", "P", 200)])
    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps(_doc([ann])))
    out = tmp_path / "subatlas_contributors.json"
    assert sc.main(["--cas", str(cas), "--cell-type", "set A", "--out", str(out)]) == 0
    result = json.loads(out.read_text())
    assert result["cell_label"] == "set A"
    assert "1 contributor(s) over the cutoff" in capsys.readouterr().out


def test_cli_whole_project_pass_emits_an_array(tmp_path):
    doc = _doc([_annotation([_ta("X", "P", 200)], label=f"set {i}") for i in range(3)])
    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps(doc))
    out = tmp_path / "subatlas_contributors.json"
    assert sc.main(["--cas", str(cas), "--out", str(out)]) == 0
    assert len(json.loads(out.read_text())) == 3


def test_cli_reports_an_unknown_cell_type_as_an_error(tmp_path, capsys):
    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps(_doc([])))
    assert sc.main(["--cas", str(cas), "--cell-type", "nope"]) == 2
    assert "no annotation with cell_label" in capsys.readouterr().err


def test_cli_threshold_overrides_reach_the_output(tmp_path):
    ann = _annotation([_ta("X", "P", 30)], n_cells=1000)
    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps(_doc([ann])))
    out = tmp_path / "subatlas_contributors.json"
    sc.main(
        [
            "--cas",
            str(cas),
            "--cell-type",
            "set A",
            "--out",
            str(out),
            "--min-contribution",
            "0.01",
            "--min-source-cells",
            "10",
        ]
    )
    result = json.loads(out.read_text())
    assert [c["subatlas_paper"] for c in result["contributors"]] == ["P"]
    assert result["thresholds"]["min_source_cells"] == 10


# ---------------------------------------------------------------- real data


def test_the_reference_cell_set_reproduces_the_documented_numbers():
    """The worked example in the project README, pinned.

    Guards the case the whole feature exists for: the atlas's own synonym for
    this cell set (`aPCV`) is a 6.8% contributor's 11% minority call, and only
    1.5% of that contributor's aPCV cells actually landed here.
    """
    cas_path = (
        Path(__file__).resolve().parents[2] / "projects/test_projects/hca_reproductive/cas.json"
    )
    if not cas_path.exists():  # pragma: no cover - project data is committed
        pytest.skip("reference project not present")
    doc = json.loads(cas_path.read_text())
    annotation = sc.find_annotation(doc, "Activated post-capillary venous endothelial", "L4")
    result = sc.summarise(annotation, doc)
    assert _valid(result) == []
    assert result["n_cells"] == 4851

    by_paper = {c["subatlas_paper"]: c for c in result["contributors"]}
    weigert = by_paper["celltype_Weigert2025"]
    assert weigert["tier"] == "primary"
    assert weigert["purity"] == 1.0
    assert weigert["dominant_label"] == "endothelial cell"

    ulrich = by_paper["celltype_Ulrich2024"]
    assert ulrich["tier"] == "secondary"
    assert ulrich["contribution"] == pytest.approx(0.068, abs=5e-4)
    assert ulrich["purity"] == pytest.approx(0.593, abs=5e-4)
    apcv = next(i for i in ulrich["labels"] if i["transferred_cell_label"] == "aPCV")
    assert apcv["within_source_share"] == pytest.approx(0.111, abs=5e-4)
    assert apcv["reverse_share"] == pytest.approx(0.015, abs=5e-4)
    assert "aPCV" in annotation["synonyms"]
