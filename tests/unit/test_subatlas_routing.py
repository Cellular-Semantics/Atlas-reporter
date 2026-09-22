"""Unit tests for arranging cell-set provenance by the read.

The fixture is a miniature of the shape the real documents have: a two-level
hierarchy, several contributing studies, one of them unpublished, a registry,
a label the atlas records as a synonym, and a marker-sign pair that a careless
fold would merge.

Nothing here should ever assert that a measure was *computed*. The measures are
counted at ingest and stored in CAS+; this carries them through, and a test that
recomputed one would be pinning the behaviour we removed.
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
    summarise,
)

from atlas_chat.schemas import load_schema

pytestmark = pytest.mark.unit


def _transfer(
    paper: str,
    label: str,
    cells: int,
    contribution: int,
    label_total: int | None = None,
    n_cells: int | None = None,
) -> dict:
    """A transfer carrying the measures an ingest pass would have stored."""
    out: dict = {
        "transferred_cell_label": label,
        "source_labelset": paper,
        "cell_count": cells,
        "subatlas_contribution_cells": contribution,
        "share_of_subatlas_contribution": round(cells / contribution, 4),
    }
    if label_total is not None:
        out["subatlas_label_total_cells"] = label_total
        out["share_of_subatlas_label"] = round(cells / label_total, 4)
    if n_cells:
        out["cell_ratio"] = round(cells / n_cells, 4)
    return out


def _cas() -> dict:
    """One parent, five leaves, four contributing studies, a registry."""
    return {
        "source": {
            "doi": "10.1000/atlas",
            "title": "A test atlas",
            "subatlas_papers": [
                {
                    "label": "coarse",
                    "doi": "10.1000/coarse",
                    "first_author": "Brunel",
                    "year": 2021,
                    "title": "One big mesenchyme",
                    "total_cells": 1200,
                    "cell_sets": [{"cell_label": "mesenchyme", "n_cells": 607}],
                },
                {
                    "label": "fine",
                    "doi": "10.1000/fine",
                    "first_author": "Franklin",
                    "year": 2023,
                    "title": "Fibroblasts in detail",
                    "total_cells": 400,
                    "cell_sets": [{"cell_label": "FibA", "n_cells": 205}],
                },
                {"label": "signs", "doi": "10.1000/signs", "first_author": "Hodgkin"},
                {"label": "institute", "status": "unresolved"},
            ],
        },
        "labelsets": [{"name": "broad"}, {"name": "fine"}],
        "annotations": [
            {
                "labelset": "broad",
                "cell_label": "Fibroblasts",
                "cell_set_accession": "B1",
                "n_cells": 970,
                "transferred_annotations": [
                    _transfer("coarse", "mesenchyme", 600, 620, 607, 970),
                    _transfer("fine", "FibA", 200, 280, 205, 970),
                    _transfer("institute", "local_fib", 80, 80, None, 970),
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
                    _transfer("coarse", "mesenchyme", 400, 400, 607, 500),
                    _transfer("fine", "FibA", 60, 90, 205, 500),
                    _transfer("signs", "PV_CDKN1A-", 30, 30, 90, 500),
                ],
            },
            {
                "labelset": "fine",
                "cell_label": "Fib_B",
                "cell_set_accession": "F2",
                "parent_cell_set_accession": "B1",
                "n_cells": 300,
                "transferred_annotations": [
                    _transfer("coarse", "mesenchyme", 200, 220, 607, 300),
                    _transfer("fine", "FibA", 140, 190, 205, 300),
                ],
            },
            {
                "labelset": "fine",
                "cell_label": "Fib_C",
                "cell_set_accession": "F3",
                "parent_cell_set_accession": "B1",
                "n_cells": 40,
                "transferred_annotations": [
                    _transfer("fine", "FibA", 5, 12, 205, 40),
                    _transfer("coarse", "mesenchyme", 7, 7, 607, 40),
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
                "n_cells": 100,
                "transferred_annotations": [
                    _transfer("institute", "local_fib", 90, 90, None, 100),
                ],
            },
        ],
    }


def _unenriched() -> dict:
    """The same document before the registry pass: no atlas-wide denominator."""
    cas = _cas()
    cas["source"].pop("subatlas_papers")
    for annotation in cas["annotations"]:
        for transfer in annotation.get("transferred_annotations") or []:
            transfer.pop("subatlas_label_total_cells", None)
            transfer.pop("share_of_subatlas_label", None)
            if transfer["source_labelset"] != "institute":
                transfer["source_taxonomy"] = "DOI:10.1000/" + transfer["source_labelset"]
    return cas


def _fine_labels() -> list[str]:
    return ["Fib_A", "Fib_B", "Fib_C", "Fib_D", "Fib_E"]


def _question(table: dict, paper: str, label: str) -> dict:
    for question in table["questions"]:
        if question["subatlas_paper"] == paper and question["subatlas_cell_label"] == label:
            return question
    raise AssertionError(f"no question for {paper} / {label}")


def _paper(table: dict, paper: str) -> dict:
    return next(p for p in table["papers"] if p["subatlas_paper"] == paper)


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
    claimant = _question(table, "signs", "PV_CDKN1A-")["atlas_cell_sets"][0]
    assert "named_as_synonym" not in claimant


# ------------------------------------------------------------------
# the measures are carried, never computed
# ------------------------------------------------------------------


def test_all_three_measures_come_through_unchanged() -> None:
    table = build_table(_cas(), ["Fib_B"])
    claimant = _question(table, "fine", "FibA")["atlas_cell_sets"][0]
    assert claimant["share_of_subatlas_contribution"] == pytest.approx(140 / 190, abs=1e-4)
    assert claimant["share_of_subatlas_label"] == pytest.approx(140 / 205, abs=1e-4)
    assert claimant["share_of_atlas_cell_set"] == pytest.approx(140 / 300, abs=1e-4)


def test_a_stored_measure_is_carried_verbatim_not_recalculated() -> None:
    """A wrong stored value is the CAS+ hook's business, not this module's."""
    cas = _cas()
    cas["annotations"][2]["transferred_annotations"][1]["share_of_subatlas_label"] = 0.9999
    table = build_table(cas, ["Fib_B"])
    claimant = _question(table, "fine", "FibA")["atlas_cell_sets"][0]
    assert claimant["share_of_subatlas_label"] == 0.9999


def test_an_unenriched_document_still_finds_a_doi_to_read() -> None:
    """Without a registry the study key is an obs column; the DOI is on the transfer."""
    table = build_table(_unenriched(), ["Fib_A"])
    assert _paper(table, "coarse")["doi"] == "10.1000/coarse"
    assert table["unreadable"] == [] if "unreadable" in table else True


def test_an_unenriched_document_yields_no_recall_side_rather_than_an_estimate() -> None:
    table = build_table(_unenriched(), ["Fib_A"])
    claimant = _question(table, "coarse", "mesenchyme")["atlas_cell_sets"][0]
    assert "share_of_subatlas_label" not in claimant
    assert claimant["share_of_subatlas_contribution"] == 1.0


def test_an_unenriched_document_says_so_in_the_summary() -> None:
    assert "registry is not populated" in summarise(build_table(_unenriched(), ["Fib_A"]))


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
    assert [a["cell_set_accession"] for a in resolve_requested(cas, None, ["F1"])] == ["F1"]


def test_an_unknown_label_is_refused() -> None:
    with pytest.raises(RoutingError, match="no cell set labelled"):
        resolve_requested(_cas(), ["Nothing"])


# ------------------------------------------------------------------
# the floor, and what the synonym exemption is for
# ------------------------------------------------------------------


def test_the_floor_drops_a_small_contribution() -> None:
    table = build_table(_cas(), _fine_labels(), min_overlap_cells=50)
    served = [c["cell_label"] for c in _question(table, "fine", "FibA")["atlas_cell_sets"]]
    assert "Fib_C" not in served
    assert served == ["Fib_B", "Fib_A"]


def test_a_dropped_contribution_is_rolled_up_not_lost() -> None:
    table = build_table(_cas(), ["Fib_C"], min_overlap_cells=50)
    assert table["questions"] == []
    assert {d["subatlas_paper"] for d in table["dropped"]} == {"coarse", "fine"}
    assert sum(d["overlap_cells"] for d in table["dropped"]) == 12


def test_a_synonym_survives_the_floor_however_small() -> None:
    table = build_table(_cas(), ["Fib_A"], min_overlap_cells=50)
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


def test_a_claimant_does_not_repeat_the_labelset_its_cell_set_already_carries() -> None:
    table = build_table(_cas(), _fine_labels())
    claimant = _question(table, "coarse", "mesenchyme")["atlas_cell_sets"][0]
    assert "labelset" not in claimant
    assert claimant["cell_set_accession"] == "F1"
    assert {r["cell_label"]: r["labelset"] for r in table["requested"]}["Fib_A"] == "fine"


# ------------------------------------------------------------------
# papers, which is what a plan ranks
# ------------------------------------------------------------------


def test_a_paper_appears_once_however_many_of_its_labels_are_asked_about() -> None:
    table = build_table(_cas(), _fine_labels(), min_overlap_cells=1)
    assert [p["subatlas_paper"] for p in table["papers"]].count("fine") == 1
    assert _paper(table, "fine")["n_questions"] == 1


def test_a_paper_carries_the_identity_the_registry_holds() -> None:
    paper = _paper(build_table(_cas(), ["Fib_A"]), "coarse")
    assert paper["first_author"] == "Brunel"
    assert paper["title"] == "One big mesenchyme"
    assert paper["doi"] == "10.1000/coarse"


def test_a_question_carries_no_identity_of_its_own() -> None:
    question = _question(build_table(_cas(), ["Fib_A"]), "coarse", "mesenchyme")
    assert not {"doi", "first_author", "year", "title"} & set(question)


def test_a_paper_counts_what_it_reached_and_what_it_gave_the_whole_atlas() -> None:
    paper = _paper(build_table(_cas(), _fine_labels()), "coarse")
    assert paper["cells_contributed"] == 600
    assert paper["n_atlas_cell_sets_reached"] == 2
    assert paper["total_cells_in_atlas"] == 1200


def test_papers_are_ordered_by_what_they_contributed_to_this_selection() -> None:
    table = build_table(_cas(), _fine_labels(), min_overlap_cells=1)
    contributed = [p["cells_contributed"] for p in table["papers"]]
    assert contributed == sorted(contributed, reverse=True)


# ------------------------------------------------------------------
# what a requested cell set is described with
# ------------------------------------------------------------------


def test_children_are_carried_so_an_atlas_subdivision_is_visible() -> None:
    table = build_table(_cas(), ["Fibroblasts"])
    assert table["requested"][0]["children"] == ["Fib_A", "Fib_B", "Fib_C", "Fib_D", "Fib_E"]


def test_sampling_context_is_left_out() -> None:
    cas = _cas()
    cas["annotations"][1]["composition"] = {
        "organ": {"category": "tissue", "values": [{"author_value": "Uterus", "cell_ratio": 1.0}]}
    }
    assert "context" not in build_table(cas, ["Fib_A"])["requested"][0]


def test_the_atlas_paper_is_named() -> None:
    table = build_table(_cas(), ["Fib_A"])
    assert table["atlas_paper"] == {"doi": "10.1000/atlas", "title": "A test atlas"}


# ------------------------------------------------------------------
# accounting for every requested cell set
# ------------------------------------------------------------------


def test_no_provenance_at_all_is_atlas_only() -> None:
    table = build_table(_cas(), _fine_labels())
    assert {a["cell_label"]: a["reason"] for a in table["atlas_only"]}["Fib_D"] == "no_provenance"


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
    assert unreadable["subatlas_paper"] == "institute"
    assert unreadable["overlap_cells"] == 90
    assert unreadable["n_atlas_cell_sets"] == 1


def test_an_unreadable_source_is_never_offered_as_a_question() -> None:
    table = build_table(_cas(), _fine_labels())
    assert "institute" not in {q["subatlas_paper"] for q in table["questions"]}
    assert "institute" not in {p["subatlas_paper"] for p in table["papers"]}


def test_every_requested_cell_set_is_served_or_accounted_for() -> None:
    table = build_table(_cas(), _fine_labels(), min_overlap_cells=50)
    served = {c["cell_label"] for q in table["questions"] for c in q["atlas_cell_sets"]}
    assert served | {a["cell_label"] for a in table["atlas_only"]} == set(_fine_labels())


# ------------------------------------------------------------------
# the shape as written out
# ------------------------------------------------------------------


def test_the_table_conforms_to_its_schema() -> None:
    table = build_table(_cas(), _fine_labels(), cas_source="cas.json")
    jsonschema.Draft202012Validator(load_schema("subatlas_routing_table.schema.json")).validate(
        table
    )


def test_an_unenriched_table_also_conforms() -> None:
    table = build_table(_unenriched(), _fine_labels())
    jsonschema.Draft202012Validator(load_schema("subatlas_routing_table.schema.json")).validate(
        table
    )


def test_the_plan_fixture_conforms_to_its_schema() -> None:
    fixture = (
        Path(__file__).parent / "fixtures" / "routing" / "routing_plan.good.json"
    ).read_text()
    jsonschema.Draft202012Validator(load_schema("subatlas_routing_plan.schema.json")).validate(
        json.loads(fixture)
    )


def test_cli_writes_the_table_and_reports_what_it_came_to(tmp_path, capsys) -> None:
    cas_path = tmp_path / "cas.json"
    cas_path.write_text(json.dumps(_cas()), encoding="utf-8")
    out = tmp_path / "routing_table.json"
    assert main(["--cas", str(cas_path), "--label", "Fib_A", "--out", str(out)]) == 0
    written = json.loads(out.read_text())
    assert written["cas_source"] == str(cas_path)
    assert written["atlas_paper"]["doi"] == "10.1000/atlas"
    assert "questions across" in capsys.readouterr().out


def test_cli_refuses_an_unresolvable_request(tmp_path) -> None:
    cas_path = tmp_path / "cas.json"
    cas_path.write_text(json.dumps(_cas()), encoding="utf-8")
    assert main(["--cas", str(cas_path), "--label", "Nothing"]) == 2
