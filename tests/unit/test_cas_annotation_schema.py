"""Regression tests for the CAS-shaped annotation schema (local extension).

Pins the target shape from the big-bang CAS migration
(planning/plan_cas_migration_bigbang_and_prog_agentic_split_2026-06-24.md and
mockup_cas_cxg_annotations_2026-06-24.md — composition Variant B):

  * labelsets carry rank (0 = most granular) + role;
  * annotations are CLOSED (no drift) — arbitrary obs -> author_annotation_fields,
    descriptor distributions -> composition;
  * integration provenance reuses transferred_annotations (+ cell_count/cell_ratio);
  * composition is the cell-set-level form of CxG cell-level fields.

Two golden fixtures on real data: HDCA_neurons (integrated) and fetal_skin
(non-integrated). The non-integrated fixture is the over-fit guard — it MUST
validate AND carry no transferred_annotations.

Additive: does not touch cell_type_annotation.schema.json or its readers.
"""

from __future__ import annotations

import copy

import pytest

jsonschema = pytest.importorskip("jsonschema")

from atlas_chat.schemas import load_schema  # noqa: E402

# --- integrated atlas: real HDCA_neurons AMACRINE_CELL --------------------------
VALID_HDCA_INTEGRATED: dict = {
    "title": "HDCA v2 — neurons",
    "matrix_file_id": "https://cellatlas.io/hdca_v2_20260311_f2.zarr",
    "cellannotation_schema_version": "0.1.0",
    "source": {
        "doi": "10.64898/2026.03.30.714220",
        "title": "Human Developmental Cell Atlas (HDCA) v2",
        "data_provenance": {
            "source_type": "published_zarr",
            "obs_column": "refined_celltype",
            "n_cells_total": 4679782,
            "extracted_at": "2026-05-19T00:00:00Z",
        },
        "subatlas_papers": [
            {
                "label": "Sridhar_et_al_2020_CellPress",
                "first_author": "Sridhar",
                "year": 2020,
                "doi": "10.1016/j.celrep.2020.108023",
                "status": "asta",
            }
        ],
    },
    "labelsets": [
        {"name": "refined_celltype", "annotation_method": "manual", "rank": 0, "role": "author_cell_type"},
        {"name": "broad_celltype", "annotation_method": "manual", "rank": 1, "role": "author_cell_type"},
    ],
    "annotations": [
        {
            "labelset": "refined_celltype",
            "cell_label": "AMACRINE_CELL",
            "cell_fullname": "amacrine cell",
            "cell_ontology_term_id": "CL:0000561",
            "cell_ontology_term": "amacrine cell",
            "cell_set_accession": "HDCA:refined:AMACRINE_CELL",
            "parent_cell_set_accession": "HDCA:broad:AUDIOVISUAL_NEURONAL",
            "n_cells": 78,
            "rationale": "Retinal interneuron (Sridhar et al., 2020).",
            "rationale_dois": ["10.1016/j.celrep.2020.108023"],
            "marker_gene_evidence": ["TFAP2A", "GAD1"],
            "transferred_annotations": [
                {
                    "transferred_cell_label": "AC",
                    "source_taxonomy": "DOI:10.1016/j.celrep.2020.108023",
                    "cell_count": 77,
                    "cell_ratio": 0.987,
                    "comment": "Integration provenance (not algorithmic transfer): author label from contributing study.",
                },
                {
                    "transferred_cell_label": "imGlia",
                    "source_taxonomy": "DOI:10.1016/j.celrep.2020.108023",
                    "cell_count": 1,
                    "cell_ratio": 0.013,
                    "comment": "Integration provenance.",
                },
            ],
            "composition": {
                "tissue": {
                    "author_field_name": "organ",
                    "values": [
                        {
                            "author_value": "Retina",
                            "value": "retina",
                            "ontology_term_id": "UBERON:0000966",
                            "cell_count": 78,
                            "cell_ratio": 1.0,
                        }
                    ],
                },
                "development_stage": {
                    "author_field_name": "development_stage",
                    "values": [
                        {"author_value": "unknown", "cell_ratio": 0.808},
                        {"author_value": "HsapDv:0000048", "ontology_term_id": "HsapDv:0000048", "cell_ratio": 0.103},
                        {"author_value": "HsapDv:0000054", "ontology_term_id": "HsapDv:0000054", "cell_ratio": 0.09},
                    ],
                },
                "germ_layer": {
                    "author_field_name": "germlayer",
                    "values": [{"author_value": "ECTODERM", "cell_count": 78, "cell_ratio": 1.0}],
                },
            },
            "author_annotation_fields": {"scope": "fetal"},
        }
    ],
}

# --- non-integrated atlas: fetal_skin C_Melanocyte (the over-fit guard) ---------
VALID_FETAL_SKIN_NON_INTEGRATED: dict = {
    "title": "A prenatal skin atlas",
    "source": {"doi": "10.1038/s41586-024-08002-x", "title": "A prenatal skin atlas"},
    "labelsets": [
        {"name": "cell_type", "annotation_method": "manual", "rank": 0, "role": "author_cell_type"}
    ],
    "annotations": [
        {
            "labelset": "cell_type",
            "cell_label": "C_Melanocyte",
            "cell_fullname": "melanocyte",
            "cell_ontology_term_id": "CL:0000148",
            "composition": {
                "tissue": {
                    "author_field_name": "tissue",
                    "values": [{"author_value": "skin", "ontology_term_id": "UBERON:0002097", "cell_ratio": 1.0}],
                }
            },
        }
    ],
}


@pytest.fixture(scope="module")
def validator():
    schema = load_schema("cas_annotation.schema.json")
    return jsonschema.Draft202012Validator(schema)


@pytest.mark.unit
@pytest.mark.parametrize("doc", [VALID_HDCA_INTEGRATED, VALID_FETAL_SKIN_NON_INTEGRATED])
def test_valid_documents_pass(validator, doc):
    assert list(validator.iter_errors(doc)) == []


@pytest.mark.unit
def test_non_integrated_has_no_transferred_annotations():
    """Over-fit guard: a non-integrated atlas must not sprout HDCA-only structure."""
    for ann in VALID_FETAL_SKIN_NON_INTEGRATED["annotations"]:
        assert "transferred_annotations" not in ann


# --- closed Annotation: reject drift --------------------------------------------


@pytest.mark.unit
def test_annotation_rejects_unknown_field(validator):
    doc = copy.deepcopy(VALID_FETAL_SKIN_NON_INTEGRATED)
    doc["annotations"][0]["organ"] = "skin"  # inline covariate is the OLD shape — must be rejected
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_annotation_requires_cell_label(validator):
    doc = copy.deepcopy(VALID_FETAL_SKIN_NON_INTEGRATED)
    del doc["annotations"][0]["cell_label"]
    assert list(validator.iter_errors(doc))


# --- composition (Variant B) shape ----------------------------------------------


@pytest.mark.unit
def test_composition_value_requires_author_value(validator):
    doc = copy.deepcopy(VALID_HDCA_INTEGRATED)
    doc["annotations"][0]["composition"]["tissue"]["values"][0] = {"value": "retina"}
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_composition_value_rejects_unknown_key(validator):
    doc = copy.deepcopy(VALID_HDCA_INTEGRATED)
    doc["annotations"][0]["composition"]["tissue"]["values"][0]["nonsense"] = 1
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_composition_cell_ratio_out_of_range_fails(validator):
    doc = copy.deepcopy(VALID_HDCA_INTEGRATED)
    doc["annotations"][0]["composition"]["tissue"]["values"][0]["cell_ratio"] = 1.5
    assert list(validator.iter_errors(doc))


# --- transferred_annotations extension ------------------------------------------


@pytest.mark.unit
def test_transferred_requires_label(validator):
    doc = copy.deepcopy(VALID_HDCA_INTEGRATED)
    del doc["annotations"][0]["transferred_annotations"][0]["transferred_cell_label"]
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_transferred_cell_ratio_out_of_range_fails(validator):
    doc = copy.deepcopy(VALID_HDCA_INTEGRATED)
    doc["annotations"][0]["transferred_annotations"][0]["cell_ratio"] = 2.0
    assert list(validator.iter_errors(doc))


# --- top-level / source ---------------------------------------------------------


@pytest.mark.unit
def test_missing_source_doi_fails(validator):
    doc = copy.deepcopy(VALID_FETAL_SKIN_NON_INTEGRATED)
    del doc["source"]["doi"]
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_labelset_rank_must_be_non_negative(validator):
    doc = copy.deepcopy(VALID_FETAL_SKIN_NON_INTEGRATED)
    doc["labelsets"][0]["rank"] = -1
    assert list(validator.iter_errors(doc))
