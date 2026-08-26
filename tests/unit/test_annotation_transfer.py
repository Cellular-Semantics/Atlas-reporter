"""Unit tests for obs transfer columns -> CAS+ transferred_annotations."""

from __future__ import annotations

import json

import pytest

from atlas_chat.services import annotation_transfer as at

pytestmark = pytest.mark.unit


# A miniature of the HCA_repro case that motivates the whole feature: one atlas
# cell set whose cells two upstream studies annotated differently. "Weigert" is
# pure but coarse; "Ulrich" splits them three ways, and the label the atlas
# adopted (aPCV) is Ulrich's *minority* call.
CELL_TYPES = ["aPCV"] * 10 + ["Capillary EC"] * 4
ULRICH = (
    ["Capillary"] * 5 + ["tPCV"] * 3 + ["aPCV"] * 2 + ["Capillary"] * 2 + [None, "nan"]
)
WEIGERT = ["endothelial cell"] * 10 + ["endothelial cell", "", "NA", "unknown"]

SOURCES = [
    at.TransferSource(column="celltype_Ulrich2024", doi="10.1073/pnas.2404775121", year=2024),
    at.TransferSource(column="celltype_Weigert2025", doi="10.1038/s41467-024-55440-2"),
]


def test_crosstab_counts_and_set_sizes():
    counts, sizes = at.crosstab(CELL_TYPES, {"u": ULRICH, "w": WEIGERT})
    assert sizes == {"aPCV": 10, "Capillary EC": 4}
    assert counts["aPCV"]["u"] == {"Capillary": 5, "tPCV": 3, "aPCV": 2}
    # Only two of the four Capillary EC cells carry a Ulrich label; None and the
    # "nan" string are both absence, not a label.
    assert counts["Capillary EC"]["u"] == {"Capillary": 2}
    # "", "NA" and "unknown" are all absence too.
    assert counts["Capillary EC"]["w"] == {"endothelial cell": 1}


def test_crosstab_rejects_ragged_columns():
    with pytest.raises(ValueError, match="expected 14"):
        at.crosstab(CELL_TYPES, {"u": ULRICH[:-1]})


def test_crosstab_custom_drop_values():
    counts, sizes = at.crosstab(
        ["A", "A"], {"s": ["keep", "sentinel"]}, drop_values={"sentinel"}
    )
    assert counts["A"]["s"] == {"keep": 1}
    assert sizes == {"A": 2}


def test_build_orders_by_descending_count_and_ratios_use_the_set_size():
    counts, sizes = at.crosstab(
        CELL_TYPES, {"celltype_Ulrich2024": ULRICH, "celltype_Weigert2025": WEIGERT}
    )
    built = at.build_transferred_annotations(counts, sizes, SOURCES)
    ulrich = [t for t in built["aPCV"] if t["source_labelset"] == "celltype_Ulrich2024"]
    assert [t["transferred_cell_label"] for t in ulrich] == ["Capillary", "tPCV", "aPCV"]
    assert [t["cell_count"] for t in ulrich] == [5, 3, 2]
    # cell_ratio is a fraction of the atlas cell set (10 cells), not of the cells
    # Ulrich contributed to it.
    assert [t["cell_ratio"] for t in ulrich] == [0.5, 0.3, 0.2]
    assert ulrich[0]["source_taxonomy"] == "DOI:10.1073/pnas.2404775121"
    assert ulrich[0]["subatlas_paper"] == "celltype_Ulrich2024"


def test_build_skips_columns_without_a_declared_source():
    counts, sizes = at.crosstab(CELL_TYPES, {"celltype_Ulrich2024": ULRICH, "mystery": WEIGERT})
    built = at.build_transferred_annotations(counts, sizes, SOURCES)
    assert {t["source_labelset"] for t in built["aPCV"]} == {"celltype_Ulrich2024"}


def test_build_flags_sources_with_no_publication():
    counts, sizes = at.crosstab(["A"], {"sanger": ["Endo_Cap"]})
    built = at.build_transferred_annotations(
        counts, sizes, [at.TransferSource(column="sanger")]
    )
    item = built["A"][0]
    assert "source_taxonomy" not in item
    assert "no publication" in item["comment"]


def test_build_uses_the_registry_label_when_it_differs_from_the_column():
    counts, sizes = at.crosstab(["A"], {"col": ["X"]})
    built = at.build_transferred_annotations(
        counts, sizes, [at.TransferSource(column="col", label="Ulrich2024", doi="10.1/x")]
    )
    assert built["A"][0]["source_labelset"] == "col"
    assert built["A"][0]["subatlas_paper"] == "Ulrich2024"


# ---------------------------------------------------------------- hierarchy


def _hierarchical_doc():
    """Two leaves under one parent, both carrying the same upstream label.

    The parent repeats its children's counts, which is exactly the double-count
    the leaf restriction exists to avoid.
    """
    return {
        "annotations": [
            {
                "labelset": "L1",
                "cell_label": "Endothelial",
                "cell_set_accession": "P",
                "parent_cell_set_accession": None,
                "transferred_annotations": [
                    {
                        "transferred_cell_label": "Capillary",
                        "source_labelset": "u",
                        "cell_count": 30,
                    }
                ],
            },
            {
                "labelset": "L2",
                "cell_label": "aPCV",
                "cell_set_accession": "C1",
                "parent_cell_set_accession": "P",
                "transferred_annotations": [
                    {
                        "transferred_cell_label": "Capillary",
                        "source_labelset": "u",
                        "cell_count": 20,
                    }
                ],
            },
            {
                "labelset": "L2",
                "cell_label": "tPCV",
                "cell_set_accession": "C2",
                "parent_cell_set_accession": "P",
                "transferred_annotations": [
                    {
                        "transferred_cell_label": "Capillary",
                        "source_labelset": "u",
                        "cell_count": 10,
                    }
                ],
            },
        ]
    }


def test_leaf_accessions_excludes_parents():
    doc = _hierarchical_doc()
    assert at.leaf_accessions(doc["annotations"]) == {"C1", "C2"}


def test_backfill_totals_sums_over_leaves_only():
    doc = _hierarchical_doc()
    n = at.backfill_source_label_totals(doc)
    assert n == 3
    # 20 + 10 from the leaves; the parent's own 30 must not be added again.
    totals = {
        a["cell_label"]: a["transferred_annotations"][0]["source_label_cell_count"]
        for a in doc["annotations"]
    }
    assert totals == {"Endothelial": 30, "aPCV": 30, "tPCV": 30}
    # The reverse share is now computable: this leaf holds 2/3 of Ulrich's
    # Capillary cells.
    leaf = doc["annotations"][1]["transferred_annotations"][0]
    assert leaf["cell_count"] / leaf["source_label_cell_count"] == pytest.approx(2 / 3)


def test_backfill_totals_on_a_flat_document_treats_every_set_as_a_leaf():
    doc = {
        "annotations": [
            {
                "labelset": "author",
                "cell_label": ct,
                "transferred_annotations": [
                    {"transferred_cell_label": "X", "source_labelset": "u", "cell_count": n}
                ],
            }
            for ct, n in [("A", 7), ("B", 3)]
        ]
    }
    at.backfill_source_label_totals(doc)
    assert all(
        a["transferred_annotations"][0]["source_label_cell_count"] == 10
        for a in doc["annotations"]
    )


def test_subatlas_registry_status_and_totals():
    doc = _hierarchical_doc()
    entries = at.subatlas_registry(
        [
            at.TransferSource(column="u", doi="10.1/x", first_author="Ulrich", year=2024),
            at.TransferSource(column="absent"),
        ],
        doc,
    )
    by_label = {e["label"]: e for e in entries}
    assert by_label["u"]["status"] == "candidate"
    assert by_label["u"]["total_cells"] == 30
    assert by_label["u"]["first_author"] == "Ulrich"
    # No DOI to confirm, and no cells under this column, so no total either.
    assert by_label["absent"]["status"] == "unresolved"
    assert "total_cells" not in by_label["absent"]


# ---------------------------------------------------------------- apply_to_cas


def test_apply_to_cas_matches_on_labelset_and_label():
    doc = {
        "annotations": [
            {"labelset": "L4", "cell_label": "aPCV"},
            {"labelset": "L3", "cell_label": "aPCV"},
        ]
    }
    n, unmatched = at.apply_to_cas(
        doc, {"aPCV": [{"transferred_cell_label": "X"}]}, labelset="L4"
    )
    assert (n, unmatched) == (1, [])
    assert "transferred_annotations" in doc["annotations"][0]
    assert "transferred_annotations" not in doc["annotations"][1]


def test_apply_to_cas_reports_labels_the_document_does_not_have():
    doc = {"annotations": [{"labelset": "L4", "cell_label": "aPCV"}]}
    n, unmatched = at.apply_to_cas(
        doc,
        {"aPCV": [{"transferred_cell_label": "X"}], "new thing": [{"transferred_cell_label": "Y"}]},
        labelset="L4",
    )
    assert (n, unmatched) == (1, ["new thing"])


def test_apply_to_cas_replaces_by_default_and_appends_on_request():
    doc = {
        "annotations": [
            {
                "labelset": "L4",
                "cell_label": "aPCV",
                "transferred_annotations": [{"transferred_cell_label": "old"}],
            }
        ]
    }
    at.apply_to_cas(doc, {"aPCV": [{"transferred_cell_label": "new"}]}, labelset="L4")
    assert [t["transferred_cell_label"] for t in doc["annotations"][0]["transferred_annotations"]] == [
        "new"
    ]
    at.apply_to_cas(
        doc, {"aPCV": [{"transferred_cell_label": "second"}]}, labelset="L4", replace=False
    )
    assert [
        t["transferred_cell_label"] for t in doc["annotations"][0]["transferred_annotations"]
    ] == ["new", "second"]


# ---------------------------------------------------------------- CLI plumbing


@pytest.mark.parametrize(
    ("spec", "expected"),
    [
        ("col", at.TransferSource(column="col")),
        ("col=10.1/x", at.TransferSource(column="col", doi="10.1/x")),
        (
            "col=10.1/x;Ulrich;2024",
            at.TransferSource(column="col", doi="10.1/x", first_author="Ulrich", year=2024),
        ),
        ("col;Ulrich", at.TransferSource(column="col", first_author="Ulrich")),
    ],
)
def test_parse_sources(spec, expected):
    assert at.parse_sources([spec]) == [expected]


def test_parse_sources_rejects_a_non_numeric_year():
    with pytest.raises(ValueError, match="bad year"):
        at.parse_sources(["col=10.1/x;Ulrich;last year"])


def test_read_delimited_infers_tab_for_tsv(tmp_path):
    path = tmp_path / "obs.tsv"
    path.write_text("cell_type\tsource\nA\tX\nB\tY\n")
    data, n = at.read_delimited(path, ["cell_type", "source"])
    assert n == 2
    assert data["source"] == ["X", "Y"]


def test_read_delimited_names_the_missing_column(tmp_path):
    path = tmp_path / "obs.csv"
    path.write_text("cell_type\nA\n")
    with pytest.raises(ValueError, match="no column\\(s\\): source"):
        at.read_delimited(path, ["cell_type", "source"])


def test_cli_transfer_end_to_end(tmp_path):
    obs = tmp_path / "obs.csv"
    rows = ["cell_type,celltype_Ulrich2024"]
    rows += [f"aPCV,{v or ''}" for v in ULRICH[:10]]
    obs.write_text("\n".join(rows) + "\n")

    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps({"annotations": [{"labelset": "L4", "cell_label": "aPCV"}]}))

    rc = at.main(
        [
            "transfer",
            "--cas", str(cas),
            "--obs", str(obs),
            "--cell-type-col", "cell_type",
            "--labelset", "L4",
            "--source", "celltype_Ulrich2024=10.1073/pnas.2404775121;Ulrich;2024",
        ]
    )
    assert rc == 0
    doc = json.loads(cas.read_text())
    items = doc["annotations"][0]["transferred_annotations"]
    assert [t["transferred_cell_label"] for t in items] == ["Capillary", "tPCV", "aPCV"]
    assert items[0]["source_label_cell_count"] == 5
    assert doc["source"]["subatlas_papers"][0]["doi"] == "10.1073/pnas.2404775121"


def test_cli_transfer_dry_run_writes_nothing(tmp_path):
    obs = tmp_path / "obs.csv"
    obs.write_text("cell_type,src\naPCV,X\n")
    cas = tmp_path / "cas.json"
    original = json.dumps({"annotations": [{"labelset": "L4", "cell_label": "aPCV"}]})
    cas.write_text(original)
    at.main(
        [
            "transfer", "--cas", str(cas), "--obs", str(obs),
            "--cell-type-col", "cell_type", "--labelset", "L4",
            "--source", "src=10.1/x", "--dry-run",
        ]
    )
    assert cas.read_text() == original


def test_cli_transfer_keeps_a_confirmed_doi_in_the_registry(tmp_path):
    obs = tmp_path / "obs.csv"
    obs.write_text("cell_type,src\naPCV,X\n")
    cas = tmp_path / "cas.json"
    cas.write_text(
        json.dumps(
            {
                "source": {
                    "subatlas_papers": [
                        {"label": "src", "doi": "10.9/confirmed", "status": "local"}
                    ]
                },
                "annotations": [{"labelset": "L4", "cell_label": "aPCV"}],
            }
        )
    )
    at.main(
        [
            "transfer", "--cas", str(cas), "--obs", str(obs),
            "--cell-type-col", "cell_type", "--labelset", "L4",
            "--source", "src=10.1/proposed",
        ]
    )
    entry = json.loads(cas.read_text())["source"]["subatlas_papers"][0]
    # The resolver already confirmed this one; a fresh cross-tab must not reset
    # its DOI or knock its status back to "candidate".
    assert entry["doi"] == "10.9/confirmed"
    assert entry["status"] == "local"
    assert entry["total_cells"] == 1


# ---------------------------------------------------------------- joint input


JOINT_DOC = {
    "source": {"obs_column": "cell_type"},
    "cell_sets": {
        "aPCV": {
            "n_cells": 10,
            "from_source": {"celltype_Ulrich2024": 10},
            "transfers": {
                "celltype_Ulrich2024": [
                    {"value": "Capillary", "n": 5, "share_of_set": 0.5, "share_of_source": 0.5},
                    {"value": "tPCV", "n": 3, "share_of_set": 0.3, "share_of_source": 0.3},
                    {"value": "aPCV", "n": 2, "share_of_set": 0.2, "share_of_source": 0.2},
                ]
            },
        },
        "Lymphatic": {"n_cells": 4, "transfers": {}},
    },
}


def test_counts_from_joint_round_trips_to_the_crosstab_shape():
    counts, sizes = at.counts_from_joint(JOINT_DOC)
    assert counts == {"aPCV": {"celltype_Ulrich2024": {"Capillary": 5, "tPCV": 3, "aPCV": 2}}}
    # A set with no upstream labels still contributes its size, so a later
    # cross-tab against a different column has the right denominator.
    assert sizes == {"aPCV": 10, "Lymphatic": 4}


def test_counts_from_joint_rejects_the_wrong_file():
    with pytest.raises(ValueError, match="no 'cell_sets' key"):
        at.counts_from_joint({"annotations": []})


def test_cli_transfer_accepts_the_joint_file(tmp_path):
    transfers = tmp_path / "label_transfers__cell_type.json"
    transfers.write_text(json.dumps(JOINT_DOC))
    cas = tmp_path / "cas.json"
    cas.write_text(
        json.dumps(
            {
                "annotations": [
                    {"labelset": "L4", "cell_label": "aPCV"},
                    {"labelset": "L4", "cell_label": "Lymphatic"},
                ]
            }
        )
    )
    rc = at.main(
        [
            "transfer",
            "--cas", str(cas),
            "--transfers", str(transfers),
            "--labelset", "L4",
            "--source", "celltype_Ulrich2024=10.1073/pnas.2404775121",
        ]
    )
    assert rc == 0
    doc = json.loads(cas.read_text())
    by_label = {a["cell_label"]: a for a in doc["annotations"]}
    assert [t["cell_count"] for t in by_label["aPCV"]["transferred_annotations"]] == [5, 3, 2]
    assert "transferred_annotations" not in by_label["Lymphatic"]


def test_cli_transfer_requires_cell_type_col_with_obs(tmp_path):
    obs = tmp_path / "obs.csv"
    obs.write_text("cell_type,src\nA,X\n")
    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps({"annotations": []}))
    rc = at.main(
        ["transfer", "--cas", str(cas), "--obs", str(obs), "--labelset", "L4", "--source", "src"]
    )
    assert rc == 2


def test_cli_transfer_rejects_both_inputs_at_once(tmp_path):
    with pytest.raises(SystemExit):
        at.main(
            [
                "transfer", "--cas", "c.json", "--obs", "o.csv",
                "--transfers", "t.json", "--labelset", "L4", "--source", "src",
            ]
        )
