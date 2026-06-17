"""Regression tests for the cl_term_request orchestration output contract.

Two layers are pinned:

1. **JSON Schema conformance** — structure, CURIE patterns, enums, and
   ``additionalProperties: false`` from ``cl_term_request.schema.json``.
2. **Semantic checks** — definition word count (80-120), no self-naming,
   and required ntr_markdown sections. These are enforced by the
   ``_semantic_checks`` function in ``check_cl_term_request.py``.

The golden fixture is derived from the real Iron-recycling macrophage run.
"""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

import pytest

jsonschema = pytest.importorskip("jsonschema")

from atlas_chat.schemas import load_schema  # noqa: E402

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_HOOK_PATH = _PROJECT_ROOT / ".claude" / "hooks" / "check_cl_term_request.py"


def _load_hook_module():
    spec = importlib.util.spec_from_file_location("check_cl_term_request", _HOOK_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALID: dict = {
    "cell_type_label": "Iron-recycling macrophage",
    "suggested_label": "iron-recycling macrophage of skin",
    "definition": (
        "A tissue-resident macrophage that is part of the skin, found in humans during "
        "prenatal development (7-17 post-conception weeks), characterised by expression "
        "of SLC40A1 (ferroportin), CD5L, APOE, VCAM1, and TIMD4 (PMID:39415002). "
        "This cell co-localises with endothelial cells in neurovascular microenvironments "
        "and contributes to angiogenesis through endothelial cell chemotaxis (PMID:39415002). "
        "Transcriptionally related to erythrophagocytic macrophages of the adult spleen and "
        "liver, representing a conserved prenatal macrophage identity (PMID:35549310)."
    ),
    "parent_term": {"cl_id": "CL:0000864", "cl_term": "tissue-resident macrophage"},
    "anatomical_location": {"uberon_id": "UBERON:0002097", "uberon_term": "skin of body"},
    "logical_axioms": [
        {
            "relation": "part of",
            "relation_id": "BFO:0000050",
            "filler": "skin of body",
            "filler_id": "UBERON:0002097",
        }
    ],
    "synonyms": [{"value": "iron recycling macrophage", "scope": "exact"}],
    "references": [{"citation": "Gopee et al. (2024)", "supports": "Identity and markers."}],
    "justification": "No CL term exists for an iron-recycling macrophage in skin.",
    "ntr_markdown": (
        "**Preferred term label**\niron-recycling macrophage of skin\n"
        "**Synonyms** (add reference(s), please)\niron recycling macrophage\n"
        "**Definition** (free text, with reference(s), please. PubMed ID format is PMID:XXXXXX)\n"
        "A tissue-resident macrophage...\n"
        "**Parent cell type term** (check the hierarchy here https://www.ebi.ac.uk/ols4/ontologies/cl)\n"
        "tissue-resident macrophage (CL:0000864)\n"
        "**Anatomical structure where the cell type is found** (check Uberon ...)\n"
        "skin of body (UBERON:0002097)\n"
    ),
}


@pytest.fixture(scope="module")
def validator():
    schema = load_schema("cl_term_request.schema.json")
    return jsonschema.Draft202012Validator(schema)


@pytest.mark.unit
def test_valid_document_passes_schema(validator):
    assert list(validator.iter_errors(VALID)) == []


@pytest.mark.unit
def test_extra_top_level_field_fails(validator):
    doc = copy.deepcopy(VALID)
    doc["unexpected"] = "nope"
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_missing_required_field_fails(validator):
    doc = copy.deepcopy(VALID)
    del doc["definition"]
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_bad_cl_id_pattern_fails(validator):
    doc = copy.deepcopy(VALID)
    doc["parent_term"]["cl_id"] = "CL:123"  # too few digits
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_bad_uberon_id_pattern_fails(validator):
    doc = copy.deepcopy(VALID)
    doc["anatomical_location"]["uberon_id"] = "UBERON:123"
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_bad_synonym_scope_fails(validator):
    doc = copy.deepcopy(VALID)
    doc["synonyms"][0]["scope"] = "fuzzy"
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_empty_logical_axioms_fails(validator):
    doc = copy.deepcopy(VALID)
    doc["logical_axioms"] = []
    assert list(validator.iter_errors(doc))


# --- Semantic checks (hook _semantic_checks) --------------------------------


@pytest.mark.unit
def test_semantic_definition_too_short_is_flagged():
    module = _load_hook_module()
    doc = copy.deepcopy(VALID)
    doc["definition"] = "A macrophage in skin."  # 4 words
    errors = module._semantic_checks(doc)
    assert any("words" in e for e in errors), errors


@pytest.mark.unit
def test_semantic_definition_self_naming_is_flagged():
    module = _load_hook_module()
    doc = copy.deepcopy(VALID)
    # Definition starts with the suggested_label
    doc["definition"] = "iron-recycling macrophage of skin is a macrophage " * 10
    errors = module._semantic_checks(doc)
    assert any("naming" in e.lower() or "start" in e.lower() for e in errors), errors


@pytest.mark.unit
def test_semantic_ntr_markdown_missing_section_is_flagged():
    module = _load_hook_module()
    doc = copy.deepcopy(VALID)
    doc["ntr_markdown"] = "no sections here"
    errors = module._semantic_checks(doc)
    assert len(errors) >= 3, errors  # should flag multiple missing sections


@pytest.mark.unit
def test_semantic_valid_has_no_errors():
    module = _load_hook_module()
    assert module._semantic_checks(copy.deepcopy(VALID)) == []
