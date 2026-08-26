"""Reading contributing studies from CAS+ transferred_annotations.

CAS+ supersedes ``label_provenance.json``, which held only marginals. These pin
the precedence and the leaf-only summing.
"""

from __future__ import annotations

import json

import pytest

from atlas_chat.services import subatlas_resolver as sr

pytestmark = pytest.mark.unit


def _write(path, doc):
    path.write_text(json.dumps(doc))


def _cas(annotations, subatlas_papers=None):
    source = {"doi": "10.1/atlas"}
    if subatlas_papers is not None:
        source["subatlas_papers"] = subatlas_papers
    return {"title": "t", "source": source, "labelsets": [], "annotations": annotations}


def test_reads_transferred_annotations_and_lifts_the_doi(tmp_path):
    _write(
        tmp_path / "cas.json",
        _cas(
            [
                {
                    "labelset": "author",
                    "cell_label": "aPCV",
                    "transferred_annotations": [
                        {
                            "transferred_cell_label": "Capillary",
                            "subatlas_paper": "celltype_Ulrich2024",
                            "source_taxonomy": "DOI:10.1073/pnas.2404775121",
                            "cell_count": 197,
                        }
                    ],
                }
            ]
        ),
    )
    labels = sr.read_provenance_labels(tmp_path)
    assert len(labels) == 1
    assert labels[0].raw == "celltype_Ulrich2024"
    assert labels[0].doi == "10.1073/pnas.2404775121"
    assert labels[0].total_cells == 197


def test_sums_over_leaves_not_every_level(tmp_path):
    ta = lambda n: [  # noqa: E731
        {"transferred_cell_label": "X", "subatlas_paper": "src", "cell_count": n}
    ]
    _write(
        tmp_path / "cas.json",
        _cas(
            [
                {
                    "labelset": "L1",
                    "cell_label": "parent",
                    "cell_set_accession": "P",
                    "parent_cell_set_accession": None,
                    "transferred_annotations": ta(30),
                },
                {
                    "labelset": "L2",
                    "cell_label": "kid a",
                    "cell_set_accession": "A",
                    "parent_cell_set_accession": "P",
                    "transferred_annotations": ta(20),
                },
                {
                    "labelset": "L2",
                    "cell_label": "kid b",
                    "cell_set_accession": "B",
                    "parent_cell_set_accession": "P",
                    "transferred_annotations": ta(10),
                },
            ]
        ),
    )
    labels = sr.read_provenance_labels(tmp_path)
    assert [(x.raw, x.total_cells) for x in labels] == [("src", 30)]


def test_registry_metadata_beats_a_parsed_label(tmp_path):
    _write(
        tmp_path / "cas.json",
        _cas(
            [
                {
                    "labelset": "author",
                    "cell_label": "aPCV",
                    "transferred_annotations": [
                        {
                            "transferred_cell_label": "X",
                            "subatlas_paper": "celltype_HECA",
                            "cell_count": 5,
                        }
                    ],
                }
            ],
            subatlas_papers=[
                {
                    "label": "celltype_HECA",
                    "doi": "10.1038/s41588-024-01873-w",
                    "first_author": "Suo",
                    "year": 2024,
                    "venue": "Nat Genet",
                }
            ],
        ),
    )
    label = sr.read_provenance_labels(tmp_path)[0]
    # "celltype_HECA" parses to nothing useful; the registry entry fills it in.
    assert (label.first_author, label.year, label.venue) == ("Suo", 2024, "Nat Genet")
    assert label.doi == "10.1038/s41588-024-01873-w"


def test_non_paper_contributors_are_skipped(tmp_path):
    _write(
        tmp_path / "cas.json",
        _cas(
            [
                {
                    "labelset": "author",
                    "cell_label": "aPCV",
                    "transferred_annotations": [
                        {
                            "transferred_cell_label": "X",
                            "subatlas_paper": "whole_embryo",
                            "cell_count": 900,
                        },
                        {
                            "transferred_cell_label": "Y",
                            "subatlas_paper": "real_paper",
                            "cell_count": 5,
                        },
                    ],
                }
            ]
        ),
    )
    assert [x.raw for x in sr.read_provenance_labels(tmp_path)] == ["real_paper"]


def test_falls_back_to_label_provenance_when_cas_has_no_transfers(tmp_path):
    _write(tmp_path / "cas.json", _cas([{"labelset": "author", "cell_label": "AMACRINE_CELL"}]))
    _write(
        tmp_path / "label_provenance.json",
        {
            "AMACRINE_CELL": {
                "n_cells": 78,
                "studies": [["Sridhar_et_al_2020_CellPress", 78, 1.0]],
                "top_author_labels": [["AC", 77, 0.987]],
            }
        },
    )
    labels = sr.read_provenance_labels(tmp_path)
    assert [(x.raw, x.first_author, x.year, x.total_cells) for x in labels] == [
        ("Sridhar_et_al_2020_CellPress", "Sridhar", 2020, 78)
    ]
    # The legacy file carries no DOI, so discovery still has to guess.
    assert labels[0].doi is None


def test_cas_transfers_win_over_a_stale_provenance_file(tmp_path):
    _write(
        tmp_path / "cas.json",
        _cas(
            [
                {
                    "labelset": "author",
                    "cell_label": "aPCV",
                    "transferred_annotations": [
                        {
                            "transferred_cell_label": "X",
                            "subatlas_paper": "from_cas",
                            "cell_count": 1,
                        }
                    ],
                }
            ]
        ),
    )
    _write(
        tmp_path / "label_provenance.json",
        {"aPCV": {"n_cells": 1, "studies": [["from_legacy_file", 1, 1.0]]}},
    )
    assert [x.raw for x in sr.read_provenance_labels(tmp_path)] == ["from_cas"]


def test_no_provenance_at_all_is_empty_not_an_error(tmp_path):
    _write(tmp_path / "cas.json", _cas([{"labelset": "author", "cell_label": "x"}]))
    assert sr.read_provenance_labels(tmp_path) == []
