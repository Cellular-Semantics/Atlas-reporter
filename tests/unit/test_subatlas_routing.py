"""Unit tests for arranging cell-set provenance by the read.

The fixture is a miniature of the shape the real documents have: a two-level
hierarchy, several contributing studies, one of them unpublished, a label the
atlas records as a synonym, and a marker-sign pair that a careless fold would
merge.
"""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest
from atlas_chat.services.subatlas_routing import (
    RoutingError,
    build_table,
    main,
    normalise_label,
    resolve_requested,
    subatlas_label_totals,
)

from atlas_chat.schemas import load_schema

pytestmark = pytest.mark.unit


def _transfer(paper: str, label: str, cells: int, contribution: int | None = None) -> dict:
    out: dict = {
        "transferred_cell_label": label,
        "subatlas_paper": paper,
        "cell_count": cells,
    }
    if contribution is not None:
        out["subatlas_contribution_cells"] = contribution
    return out


def _cas() -> dict:
    """Two parents, four leaves, four contributing studies."""
    return {
        "source": {"doi": "10.1000/atlas"},
        "labelsets": [{"name": "broad"}, {"name": "fine"}],
        "annotations": [
            {
                "labelset": "broad",
                "cell_label": "Fibroblasts",
                "cell_set_accession": "B1",
                "n_cells": 900,
                "transferred_annotations": [
                    _transfer("DOI:10.1000/coarse", "mesenchyme", 600, 620),
                    _transfer("DOI:10.1000/fine", "FibA", 200, 280),
                    _transfer("Institute (no DOI)", "local_fib", 80, 80),
                ],
            },
            {
                "labelset": "fine",
                "cell_label": "Fib_A",
                "cell_set_accession": "F1",
                "parent_cell_set_accession": "B1",
                "n_cells": 500,
                "synonyms": ["FibA", "PV_CDKN1A+"],
                "transferred_annotations": [
                    _transfer("DOI:10.1000/coarse", "mesenchyme", 400, 400),
                    _transfer("DOI:10.1000/fine", "FibA", 60, 90),
                    _transfer("DOI:10.1000/signs", "PV_CDKN1A-", 30, 30),
                ],
            },
            {
                "labelset": "fine",
                "cell_label": "Fib_B",
                "cell_set_accession": "F2",
                "parent_cell_set_accession": "B1",
                "n_cells": 300,
                "transferred_annotations": [
                    _transfer("DOI:10.1000/coarse", "mesenchyme", 200, 220),
                    _transfer("DOI:10.1000/fine", "FibA", 140, 190),
                ],
            },
            {
                "labelset": "fine",
                "cell_label": "Fib_C",
                "cell_set_accession": "F3",
                "parent_cell_set_accession": "B1",
                "n_cells": 40,
                "transferred_annotations": [
                    _transfer("DOI:10.1000/fine", "FibA", 5, 12),
                    _transfer("DOI:10.1000/coarse", "mesenchyme", 7, 7),
                ],
            },
            {
                "labelset": "fine",
                "cell_label": "Fib_D",
                "cell_set_accession": "F4",
                "parent_cell_set_accession": "B1",
                "n_cells": 30,
            },
            {
                "labelset": "fine",
                "cell_label": "Fib_E",
                "cell_set_accession": "F5",
                "parent_cell_set_accession": "B1",
                "n_cells": 30,
                "transferred_annotations": [
                    _transfer("Institute (no DOI)", "local_fib", 90, 90),
                ],
            },
        ],
    }


def _disagreeing() -> dict:
    """No hierarchy, and the two labelsets account for different numbers of cells."""
    cas = _cas()
    for annotation in cas["annotations"]:
        annotation.pop("parent_cell_set_accession", None)
    cas["annotations"][0]["n_cells"] = 700
    return cas


def _fine_labels() -> list[str]:
    return ["Fib_A", "Fib_B", "Fib_C", "Fib_D", "Fib_E"]


def _question(table: dict, paper_fragment: str, label: str) -> dict:
    for question in table["questions"]:
        if (
            paper_fragment in question["subatlas_paper"]
            and question["subatlas_cell_label"] == label
        ):
            return question
    raise AssertionError(f"no question for {paper_fragment} / {label}")


# ------------------------------------------------------------------
# folding labels
# ------------------------------------------------------------------


def test_fold_ignores_separators_and_case() -> None:
    assert normalise_label("ePV_2") == normalise_label("ePV2")
    assert normalise_label("Endo_cycling") == normalise_label("Endo_Cycling")
    assert normalise_label(" TIP ") == normalise_label("Tip")


def test_fold_keeps_a_marker_sign() -> None:
    assert normalise_label("PV-MYH11_CDKN1A+") != normalise_label("PV-MYH11_CDKN1A-")


def test_opposite_marker_state_is_not_a_synonym_match() -> None:
    table = build_table(_cas(), ["Fib_A"], min_overlap_cells=1)
    question = _question(table, "signs", "PV_CDKN1A-")
    claimant = question["atlas_cell_sets"][0]
    assert "named_as_synonym" not in claimant


# ------------------------------------------------------------------
# the atlas-wide denominator
# ------------------------------------------------------------------


def test_denominator_comes_from_the_leaves_of_the_hierarchy() -> None:
    totals, basis = subatlas_label_totals(_cas())
    assert basis["basis"] == "hierarchy_leaves"
    assert basis["total_cells"] == 900
    # Summed across the five leaves, not across the parent as well.
    assert totals[("DOI:10.1000/fine", "FibA")] == 60 + 140 + 5


def test_denominator_prefers_a_registry_where_the_document_has_one() -> None:
    cas = _cas()
    cas["source"]["subatlas_papers"] = [
        {"label": "DOI:10.1000/fine", "cell_sets": [{"cell_label": "FibA", "n_cells": 1000}]}
    ]
    totals, basis = subatlas_label_totals(cas)
    assert basis["basis"] == "registry"
    assert totals[("DOI:10.1000/fine", "FibA")] == 1000


def test_disagreeing_labelsets_with_no_hierarchy_are_refused() -> None:
    totals, basis = subatlas_label_totals(_disagreeing())
    assert basis["basis"] == "none"
    assert "labelset totals" in basis["reason"]
    assert totals == {}


def test_a_missing_denominator_leaves_the_share_out_rather_than_guessing() -> None:
    table = build_table(_disagreeing(), ["Fib_A"])
    claimant = _question(table, "coarse", "mesenchyme")["atlas_cell_sets"][0]
    assert "share_of_subatlas_label" not in claimant
    assert claimant["share_of_contribution"] == 1.0


# ------------------------------------------------------------------
# resolving the request
# ------------------------------------------------------------------


def test_a_label_used_at_two_levels_is_refused_not_resolved() -> None:
    cas = _cas()
    cas["annotations"][1]["cell_label"] = "Fibroblasts"
    with pytest.raises(RoutingError, match="ask by accession"):
        resolve_requested(cas, ["Fibroblasts"])


def test_an_accession_resolves_a_label_used_at_two_levels() -> None:
    cas = _cas()
    cas["annotations"][1]["cell_label"] = "Fibroblasts"
    got = resolve_requested(cas, None, ["F1"])
    assert [a["cell_set_accession"] for a in got] == ["F1"]


def test_an_unknown_label_is_refused() -> None:
    with pytest.raises(RoutingError, match="no cell set labelled"):
        resolve_requested(_cas(), ["Nothing"])


# ------------------------------------------------------------------
# the two numbers
# ------------------------------------------------------------------


def test_share_of_contribution_divides_by_what_that_study_contributed() -> None:
    table = build_table(_cas(), ["Fib_B"])
    claimant = _question(table, "fine", "FibA")["atlas_cell_sets"][0]
    # 140 of the 190 cells that study put into Fib_B, not 140 of the set's 300.
    assert claimant["share_of_contribution"] == pytest.approx(140 / 190, abs=1e-4)


def test_share_of_the_label_divides_by_the_whole_atlas() -> None:
    table = build_table(_cas(), ["Fib_B"])
    claimant = _question(table, "fine", "FibA")["atlas_cell_sets"][0]
    assert claimant["share_of_subatlas_label"] == pytest.approx(140 / 205, abs=1e-4)


def test_contribution_falls_back_to_the_transfers_where_it_is_not_stated() -> None:
    cas = _cas()
    for transfer in cas["annotations"][1]["transferred_annotations"]:
        transfer.pop("subatlas_contribution_cells", None)
    table = build_table(cas, ["Fib_A"])
    claimant = _question(table, "coarse", "mesenchyme")["atlas_cell_sets"][0]
    assert claimant["share_of_contribution"] == 1.0


# ------------------------------------------------------------------
# the floor, and what the synonym exemption is for
# ------------------------------------------------------------------


def test_the_floor_drops_a_small_contribution() -> None:
    table = build_table(_cas(), _fine_labels(), min_overlap_cells=50)
    # Fib_C's 5 cells are gone; the question survives through the larger claimants.
    served = [c["cell_label"] for c in _question(table, "fine", "FibA")["atlas_cell_sets"]]
    assert "Fib_C" not in served
    assert served == ["Fib_B", "Fib_A"]


def test_a_dropped_contribution_is_rolled_up_not_lost() -> None:
    table = build_table(_cas(), ["Fib_C"], min_overlap_cells=50)
    assert table["questions"] == []
    assert {d["subatlas_paper"] for d in table["dropped"]} == {
        "DOI:10.1000/coarse",
        "DOI:10.1000/fine",
    }
    assert sum(d["overlap_cells"] for d in table["dropped"]) == 12


def test_a_synonym_survives_the_floor_however_small() -> None:
    cas = _cas()
    # The study's label is named as a synonym of Fib_A and contributes 30 cells.
    table = build_table(cas, ["Fib_A"], min_overlap_cells=50)
    question = _question(table, "fine", "FibA")
    assert question["atlas_cell_sets"][0]["named_as_synonym"] is True
    assert question["atlas_cell_sets"][0]["overlap_cells"] == 60


def test_a_label_that_is_not_a_synonym_does_not_survive_the_floor() -> None:
    cas = _cas()
    cas["annotations"][1]["synonyms"] = []
    table = build_table(cas, ["Fib_A"], min_overlap_cells=100)
    assert [q["subatlas_cell_label"] for q in table["questions"]] == ["mesenchyme"]


# ------------------------------------------------------------------
# the inversion
# ------------------------------------------------------------------


def test_one_question_lists_every_cell_set_that_label_fed() -> None:
    table = build_table(_cas(), _fine_labels())
    served = [c["cell_label"] for c in _question(table, "coarse", "mesenchyme")["atlas_cell_sets"]]
    assert served == ["Fib_A", "Fib_B"]


def test_claimants_are_ordered_by_size() -> None:
    table = build_table(_cas(), _fine_labels())
    cells = [
        c["overlap_cells"] for c in _question(table, "coarse", "mesenchyme")["atlas_cell_sets"]
    ]
    assert cells == sorted(cells, reverse=True)


def test_a_parent_is_carried_only_when_it_was_also_asked_for() -> None:
    with_parent = build_table(_cas(), ["Fibroblasts", "Fib_A"])
    assert with_parent["requested"][1]["parent"] == "Fibroblasts"
    without = build_table(_cas(), ["Fib_A"])
    assert "parent" not in without["requested"][0]


# ------------------------------------------------------------------
# accounting for every requested cell set
# ------------------------------------------------------------------


def test_no_provenance_at_all_is_atlas_only() -> None:
    table = build_table(_cas(), _fine_labels())
    reasons = {a["cell_label"]: a["reason"] for a in table["atlas_only"]}
    assert reasons["Fib_D"] == "no_provenance"


def test_contributions_all_below_the_floor_are_atlas_only_with_the_cells_recorded() -> None:
    table = build_table(_cas(), _fine_labels(), min_overlap_cells=50)
    entry = next(a for a in table["atlas_only"] if a["cell_label"] == "Fib_C")
    assert entry["reason"] == "all_below_floor"
    assert entry["overlap_cells_dropped"] == 12


def test_a_source_with_no_doi_is_atlas_only_and_reported_as_unreadable() -> None:
    table = build_table(_cas(), _fine_labels())
    entry = next(a for a in table["atlas_only"] if a["cell_label"] == "Fib_E")
    assert entry["reason"] == "no_readable_source"
    unreadable = table["unreadable"][0]
    assert unreadable["subatlas_paper"] == "Institute (no DOI)"
    assert unreadable["overlap_cells"] == 90
    assert unreadable["n_atlas_cell_sets"] == 1


def test_an_unreadable_source_is_never_offered_as_a_question() -> None:
    table = build_table(_cas(), _fine_labels())
    assert all("no DOI" not in q["subatlas_paper"] for q in table["questions"])


def test_every_requested_cell_set_is_served_or_accounted_for() -> None:
    table = build_table(_cas(), _fine_labels(), min_overlap_cells=50)
    served = {c["cell_label"] for q in table["questions"] for c in q["atlas_cell_sets"]}
    accounted = served | {a["cell_label"] for a in table["atlas_only"]}
    assert accounted == set(_fine_labels())


# ------------------------------------------------------------------
# the shape as written out
# ------------------------------------------------------------------


def test_the_table_conforms_to_its_schema() -> None:
    table = build_table(_cas(), _fine_labels(), cas_source="cas.json")
    jsonschema.Draft202012Validator(load_schema("subatlas_routing_table.schema.json")).validate(
        table
    )


def test_cli_writes_the_table_and_reports_what_it_came_to(tmp_path, capsys) -> None:
    cas_path = tmp_path / "cas.json"
    cas_path.write_text(json.dumps(_cas()), encoding="utf-8")
    out = tmp_path / "routing_table.json"
    code = main(["--cas", str(cas_path), "--label", "Fib_A", "--out", str(out)])
    assert code == 0
    written = json.loads(out.read_text())
    assert written["cas_source"] == str(cas_path)
    assert written["atlas_doi"] == "10.1000/atlas"
    assert "questions across" in capsys.readouterr().out


def test_cli_refuses_an_unresolvable_request(tmp_path) -> None:
    cas_path = tmp_path / "cas.json"
    cas_path.write_text(json.dumps(_cas()), encoding="utf-8")
    assert main(["--cas", str(cas_path), "--label", "Nothing"]) == 2


def test_the_plan_fixture_conforms_to_its_schema() -> None:
    fixture = (
        Path(__file__).parent / "fixtures" / "routing" / "routing_plan.good.json"
    ).read_text()
    jsonschema.Draft202012Validator(load_schema("subatlas_routing_plan.schema.json")).validate(
        json.loads(fixture)
    )
