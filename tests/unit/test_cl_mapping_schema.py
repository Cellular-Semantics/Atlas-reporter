"""Regression tests for the cl_mapping orchestration output contract.

Two layers are pinned here, both used by the ``check_cl_mapping.py`` PostToolUse
hook:

1. **JSON Schema conformance** — structure, CURIE patterns, enums, and
   ``additionalProperties: false`` from ``cl_mapping.schema.json``.
2. **Cross-field consistency** — the ``match_type ↔ skos_mapping`` and
   ``new_term_needed`` rules. NOTE: these rules currently live only in the hook's
   ``validate_inline`` fallback (the JSON Schema does not encode them), so they are
   asserted by calling that function directly. This makes the consistency contract
   explicit regardless of which validation path the hook takes.

This is the regression baseline for the CL-mapping contract; extend the same
pattern (good/bad golden fixtures) for new orchestration output schemas.
"""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

import pytest

jsonschema = pytest.importorskip("jsonschema")

from atlas_chat.schemas import load_schema  # noqa: E402

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_HOOK_PATH = _PROJECT_ROOT / ".claude" / "hooks" / "check_cl_mapping.py"


def _load_hook_module():
    spec = importlib.util.spec_from_file_location("check_cl_mapping", _HOOK_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALID_EXACT: dict = {
    "cell_type_label": "basal cell of epidermis",
    "working_definition": (
        "A keratinocyte residing in the basal layer of the epidermis, "
        "attached to the basement membrane and capable of proliferation."
    ),
    "searches_performed": ["basal cell of epidermis", "basal keratinocyte"],
    "best_match": {
        "cl_term": "basal cell of epidermis",
        "cl_id": "CL:0002187",
        "cl_definition": "An epidermal cell of the basal layer of the epidermis.",
        "match_type": "exact match",
        "skos_mapping": "skos:exactMatch",
        "confidence": "high",
    },
    "justification": "The CL definition matches the working definition on layer and lineage.",
    "other_candidates": [],
    "recommendation": "Use CL:0002187.",
    "new_term_needed": False,
}

VALID_NO_MATCH: dict = {
    "cell_type_label": "iron-recycling macrophage",
    "working_definition": "A macrophage specialised in iron recycling in prenatal skin.",
    "searches_performed": ["iron-recycling macrophage", "HRG+ macrophage"],
    "best_match": None,
    "justification": "No CL term captures the iron-recycling specialisation.",
    "other_candidates": [],
    "recommendation": "New CL term needed for iron-recycling macrophage.",
    "new_term_needed": True,
}


@pytest.fixture(scope="module")
def validator():
    schema = load_schema("cl_mapping.schema.json")
    return jsonschema.Draft202012Validator(schema)


@pytest.mark.unit
@pytest.mark.parametrize("doc", [VALID_EXACT, VALID_NO_MATCH])
def test_valid_documents_pass_schema(validator, doc):
    assert list(validator.iter_errors(doc)) == []


@pytest.mark.unit
def test_bad_cl_id_pattern_fails_schema(validator):
    doc = copy.deepcopy(VALID_EXACT)
    doc["best_match"]["cl_id"] = "CL:123"  # too few digits
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_extra_top_level_field_fails_schema(validator):
    doc = copy.deepcopy(VALID_EXACT)
    doc["unexpected"] = "nope"
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_bad_match_type_enum_fails_schema(validator):
    doc = copy.deepcopy(VALID_EXACT)
    doc["best_match"]["match_type"] = "fuzzy match"
    assert list(validator.iter_errors(doc))


@pytest.mark.unit
def test_missing_required_field_fails_schema(validator):
    doc = copy.deepcopy(VALID_EXACT)
    del doc["recommendation"]
    assert list(validator.iter_errors(doc))


# --- Cross-field consistency rules (hook validate_inline) -------------------


@pytest.mark.unit
def test_consistency_inconsistent_skos_is_rejected():
    module = _load_hook_module()
    doc = copy.deepcopy(VALID_EXACT)
    doc["best_match"]["skos_mapping"] = "skos:broadMatch"  # contradicts exact match
    errors = module.validate_inline(doc)
    assert any("inconsistent" in e for e in errors), errors


@pytest.mark.unit
def test_consistency_exact_match_must_not_need_new_term():
    module = _load_hook_module()
    doc = copy.deepcopy(VALID_EXACT)
    doc["new_term_needed"] = True
    errors = module.validate_inline(doc)
    assert any("new_term_needed" in e for e in errors), errors


@pytest.mark.unit
def test_consistency_broad_match_requires_new_term():
    module = _load_hook_module()
    doc = copy.deepcopy(VALID_EXACT)
    doc["best_match"]["match_type"] = "broad match"
    doc["best_match"]["skos_mapping"] = "skos:broadMatch"
    doc["new_term_needed"] = False
    errors = module.validate_inline(doc)
    assert any("new_term_needed" in e for e in errors), errors


@pytest.mark.unit
def test_consistency_valid_exact_has_no_inline_errors():
    module = _load_hook_module()
    assert module.validate_inline(copy.deepcopy(VALID_EXACT)) == []
