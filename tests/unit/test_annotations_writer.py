"""Unit tests for the shared annotations_writer convergence point.

Covers the pure transform (``build_documents``), inline co-annotation handling,
CURIE self-population, provenance preservation, schema validation, and the
on-disk ``write_project`` behaviour. All offline.
"""

from __future__ import annotations

import json

import pytest

pytest.importorskip("jsonschema")

from atlas_chat.services import annotations_writer as aw  # noqa: E402

DOI = "10.1038/s41586-024-08002-x"


def _intermediate(**overrides):
    base = {
        "labels": [{"label": "C_Melanocyte", "n_cells": 1234, "granularity": "fine"}],
        "source_meta": {"doi": DOI, "title": "A prenatal skin atlas"},
    }
    base.update(overrides)
    return base


# --- build_documents + schema conformance -----------------------------------


@pytest.mark.unit
def test_build_documents_produces_schema_valid_annotations():
    bundle = aw.build_documents(_intermediate())
    assert aw.validate_annotations(bundle.annotations) == []
    assert bundle.annotations["source"]["doi"] == DOI
    assert bundle.annotations["annotations"][0] == {
        "label": "C_Melanocyte",
        "granularity": "fine",
        "n_cells": 1234,
    }


@pytest.mark.unit
def test_source_passthrough_fields_are_copied():
    meta = {
        "doi": DOI,
        "title": "T",
        "local_text_path": "projects/x/atlas.md",
        "subatlas_papers": [{"label": "Reynolds_et_al_2021_Science"}],
        "data_provenance": {"source_type": "spreadsheet", "file_path": "x.csv"},
        "ignored_extra": "dropped",
    }
    bundle = aw.build_documents(_intermediate(source_meta=meta))
    src = bundle.annotations["source"]
    assert src["local_text_path"] == "projects/x/atlas.md"
    assert src["subatlas_papers"][0]["label"] == "Reynolds_et_al_2021_Science"
    assert src["data_provenance"]["source_type"] == "spreadsheet"
    assert "ignored_extra" not in src


# --- free-text scope/granularity (preserved, no enforcement) ----------------


@pytest.mark.unit
def test_scope_preserved_verbatim_including_embryonic():
    inter = _intermediate(labels=[{"label": "M", "scope": "embryonic"}])
    bundle = aw.build_documents(inter)
    assert bundle.annotations["annotations"][0]["scope"] == "embryonic"
    assert aw.validate_annotations(bundle.annotations) == []


# --- inline co-annotations + CURIE self-population ---------------------------


@pytest.mark.unit
def test_covariates_written_inline_on_annotation():
    inter = _intermediate(
        labels=[
            {
                "label": "AUTONOMIC_NCCS_SCPS",
                "scope": "embryonic",
                "covariates": {
                    "germlayer": "ECTODERM",
                    "organ": [
                        {"value": "whole_embryo", "share": 0.673},
                        {"value": "Gut ", "share": 0.075},
                    ],
                },
            }
        ]
    )
    ann = aw.build_documents(inter).annotations["annotations"][0]
    assert ann["germlayer"] == "ECTODERM"  # scalar covariate inline
    assert ann["organ"][1]["value"] == "Gut "  # verbatim, trailing space preserved


@pytest.mark.unit
def test_curie_value_self_populates_ontology_slots():
    inter = _intermediate(
        labels=[
            {
                "label": "M",
                "covariates": {
                    "development_stage": [
                        {"value": "HsapDv:0000023", "share": 0.47},
                        {"value": "unknown", "share": 0.12},
                    ]
                },
            }
        ]
    )
    stages = aw.build_documents(inter).annotations["annotations"][0]["development_stage"]
    assert stages[0] == {
        "value": "HsapDv:0000023",
        "share": 0.47,
        "curie": "HsapDv:0000023",
        "ontology": "HsapDv",
    }
    assert "curie" not in stages[1]  # free text left for an explicit mapping step


@pytest.mark.unit
def test_existing_curie_not_overwritten():
    inter = _intermediate(
        labels=[
            {
                "label": "M",
                "covariates": {
                    "organ": [
                        {
                            "value": "Retina",
                            "curie": "UBERON:0000966",
                            "label": "retina",
                            "ontology": "UBERON",
                        }
                    ]
                },
            }
        ]
    )
    organ = aw.build_documents(inter).annotations["annotations"][0]["organ"][0]
    assert organ["curie"] == "UBERON:0000966"
    assert organ["label"] == "retina"


@pytest.mark.unit
def test_reserved_covariate_key_does_not_clobber_named_field():
    inter = _intermediate(
        labels=[{"label": "M", "scope": "adult", "covariates": {"scope": "junk"}}]
    )
    ann = aw.build_documents(inter).annotations["annotations"][0]
    assert ann["scope"] == "adult"


# --- error handling ----------------------------------------------------------


@pytest.mark.unit
def test_missing_doi_raises():
    with pytest.raises(ValueError, match="doi"):
        aw.build_documents(_intermediate(source_meta={"title": "no doi"}))


@pytest.mark.unit
def test_empty_labels_raises():
    with pytest.raises(ValueError, match="labels"):
        aw.build_documents(_intermediate(labels=[]))


@pytest.mark.unit
def test_blank_label_raises():
    with pytest.raises(ValueError, match="label"):
        aw.build_documents(_intermediate(labels=[{"label": "  "}]))


# --- label_provenance (source/author shares preserved verbatim) -------------


@pytest.mark.unit
def test_label_provenance_preserves_shares_and_author_labels():
    inter = _intermediate(
        labels=[
            {
                "label": "AUTONOMIC_NCCS_SCPS",
                "n_cells": 15860,
                "studies": [
                    ["whole_embryo", 10670, 0.673],
                    ["Suo_et_al_2022_Science", 1198, 0.076],
                ],
                "top_author_labels": [["AC", 77, 0.987], ["imGlia", 1, 0.013]],
            }
        ]
    )
    prov = aw.build_documents(inter).label_provenance
    assert prov is not None
    entry = prov["AUTONOMIC_NCCS_SCPS"]
    assert entry["n_cells"] == 15860
    assert entry["studies"][0] == ["whole_embryo", 10670, 0.673]  # share preserved
    assert entry["top_author_labels"][0] == ["AC", 77, 0.987]


@pytest.mark.unit
def test_label_provenance_omitted_without_source_breakdown():
    # n_cells alone is not provenance — no studies/top_author_labels -> no file.
    assert aw.build_documents(_intermediate()).label_provenance is None


# --- write_project -----------------------------------------------------------


@pytest.mark.unit
def test_write_project_writes_files_and_validates(tmp_path):
    inter = _intermediate(
        labels=[
            {
                "label": "Mac",
                "scope": "embryonic",
                "n_cells": 800,
                "covariates": {"organ": [{"value": "whole_embryo", "share": 1.0}]},
                "studies": [["whole_embryo", 800, 1.0]],
            }
        ]
    )
    written = aw.write_project(tmp_path, inter)

    assert (tmp_path / "cell_type_annotations.json").exists()
    assert (tmp_path / "label_provenance.json").exists()
    assert not (tmp_path / "co_annotations.json").exists()  # no split file
    assert set(written) == {"cell_type_annotations", "label_provenance"}

    doc = json.loads((tmp_path / "cell_type_annotations.json").read_text())
    assert aw.validate_annotations(doc) == []


@pytest.mark.unit
def test_write_project_omits_provenance_without_studies(tmp_path):
    aw.write_project(tmp_path, _intermediate())
    assert not (tmp_path / "label_provenance.json").exists()


@pytest.mark.unit
def test_write_project_rejects_invalid_doi(tmp_path):
    with pytest.raises(ValueError, match="schema-valid"):
        aw.write_project(tmp_path, _intermediate(source_meta={"doi": "bogus"}))
