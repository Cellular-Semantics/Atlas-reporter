"""Regression tests for the cell_type_annotation collection schema.

Pins the design contract:
  * ``scope``/``granularity`` are free text (NO enum) — real upstream values like
    ``"embryonic"`` must validate.
  * diverse co-annotations are inline siblings on the annotation object and
    conform to one ``Covariate`` shape (scalar or distribution of
    ``CovariateValue``), with covariate KEYS left open.
  * Part-0 source additions (``subatlas_papers``, ``data_provenance``,
    ``local_text_path``) and annotation ``n_cells``.
Also guards backward compatibility with the shipped project config.
Mirrors the good/bad golden-fixture pattern in ``test_cl_mapping_schema.py``.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

jsonschema = pytest.importorskip("jsonschema")

from atlas_chat.schemas import load_schema  # noqa: E402

_PROJECT_ROOT = Path(__file__).resolve().parents[2]


VALID_MINIMAL: dict = {
    "source": {"doi": "10.1038/s41586-024-08002-x", "title": "A prenatal skin atlas"},
    "annotations": [
        {"label": "C_Melanocyte", "granularity": "fine", "scope": "adult"},
    ],
}

# Mirrors a real HDCA_neurons annotation: inline scalar + distribution covariates,
# free-text scope, a value that is already a CURIE, and the Part-0 source blocks.
VALID_HDCA_SHAPED: dict = {
    "source": {
        "doi": "10.64898/2026.03.30.714220",
        "title": "Human developmental cell atlas",
        "local_text_path": "projects/HDCA_neurons/atlas.pdf",
        "subatlas_papers": [
            {
                "label": "Sridhar_et_al_2020_CellPress",
                "first_author": "Sridhar",
                "year": 2020,
                "venue": "CellPress",
                "total_cells": 78,
                "doi": "10.1016/j.celrep.2020.01.007",
                "status": "needs_pdf",
                "proposed_doi": "10.1016/j.celrep.2020.01.007",
                "proposed": [
                    {
                        "doi": "10.1016/j.celrep.2020.01.007",
                        "title": "Single-cell transcriptomic ...",
                        "year": 2020,
                        "corpus_id": "210116",
                        "venue": "Cell Reports",
                    }
                ],
            }
        ],
        "data_provenance": {
            "source_type": "cellxgene",
            "dataset_id": "abc-123",
            "obs_column": "refined_celltype",
            "n_cells_total": 500000,
            "extracted_at": "2026-06-23T00:00:00Z",
        },
    },
    "annotations": [
        {
            "label": "AUTONOMIC_NCCS_SCPS",
            "granularity": "fine",
            "scope": "embryonic",
            "n_cells": 15860,
            "broad_celltype": "PNS_NCC",
            "germlayer": "ECTODERM",
            "organ": [
                {"value": "whole_embryo", "share": 0.673},
                {"value": "Gut ", "share": 0.075},
            ],
            "development_stage": [
                {
                    "value": "HsapDv:0000023",
                    "share": 0.473,
                    "curie": "HsapDv:0000023",
                    "ontology": "HsapDv",
                },
                {"value": "unknown", "share": 0.123},
            ],
        }
    ],
}


@pytest.fixture(scope="module")
def validator():
    schema = load_schema("cell_type_annotation.schema.json")
    return jsonschema.Draft202012Validator(schema)


@pytest.mark.unit
@pytest.mark.parametrize("doc", [VALID_MINIMAL, VALID_HDCA_SHAPED])
def test_valid_documents_pass_schema(validator, doc):
    assert list(validator.iter_errors(doc)) == []


@pytest.mark.unit
def test_existing_project_config_still_validates(validator):
    """Backward compatibility: the shipped fetal_skin_atlas config must validate."""
    cfg_path = _PROJECT_ROOT / "projects" / "fetal_skin_atlas" / "cell_type_annotations.json"
    if not cfg_path.exists():
        pytest.skip("fetal_skin_atlas config not present")
    doc = json.loads(cfg_path.read_text())
    assert list(validator.iter_errors(doc)) == []


# --- free-text scope/granularity (NO enum) ----------------------------------


@pytest.mark.unit
@pytest.mark.parametrize("scope", ["embryonic", "fetal", "adult", "organoid", "p7 postnatal"])
def test_scope_is_free_text(validator, scope):
    doc = copy.deepcopy(VALID_MINIMAL)
    doc["annotations"][0]["scope"] = scope
    assert list(validator.iter_errors(doc)) == []


@pytest.mark.unit
def test_scope_must_be_string(validator):
    doc = copy.deepcopy(VALID_MINIMAL)
    doc["annotations"][0]["scope"] = 7
    assert list(validator.iter_errors(doc))


# --- Covariate shape --------------------------------------------------------


@pytest.mark.unit
def test_scalar_and_distribution_covariates_validate(validator):
    doc = copy.deepcopy(VALID_MINIMAL)
    doc["annotations"][0]["germlayer"] = "ECTODERM"
    doc["annotations"][0]["organ"] = [{"value": "Retina", "share": 1.0}]
    assert list(validator.iter_errors(doc)) == []


@pytest.mark.unit
def test_covariate_distribution_item_requires_value(validator):
    doc = copy.deepcopy(VALID_MINIMAL)
    doc["annotations"][0]["organ"] = [{"share": 0.5}]  # missing 'value'
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_covariate_value_rejects_unknown_key(validator):
    doc = copy.deepcopy(VALID_MINIMAL)
    doc["annotations"][0]["organ"] = [{"value": "Retina", "nonsense": 1}]
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_covariate_share_out_of_range_fails(validator):
    doc = copy.deepcopy(VALID_MINIMAL)
    doc["annotations"][0]["organ"] = [{"value": "Retina", "share": 1.5}]
    assert list(validator.iter_errors(doc))


# --- source / Part-0 additions ----------------------------------------------


@pytest.mark.unit
def test_missing_doi_fails_schema(validator):
    doc = copy.deepcopy(VALID_MINIMAL)
    del doc["source"]["doi"]
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_bad_doi_pattern_fails_schema(validator):
    doc = copy.deepcopy(VALID_MINIMAL)
    doc["source"]["doi"] = "not-a-doi"
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_bad_data_provenance_source_type_fails_schema(validator):
    doc = copy.deepcopy(VALID_HDCA_SHAPED)
    doc["source"]["data_provenance"]["source_type"] = "carrier_pigeon"
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_data_provenance_requires_source_type(validator):
    doc = copy.deepcopy(VALID_HDCA_SHAPED)
    del doc["source"]["data_provenance"]["source_type"]
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_bad_subatlas_status_enum_fails_schema(validator):
    doc = copy.deepcopy(VALID_HDCA_SHAPED)
    doc["source"]["subatlas_papers"][0]["status"] = "made_up"
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_negative_n_cells_fails_schema(validator):
    doc = copy.deepcopy(VALID_HDCA_SHAPED)
    doc["annotations"][0]["n_cells"] = -5
    assert list(validator.iter_errors(doc))
