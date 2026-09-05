"""Schema + hook regression for subatlas_consistency.

The schema pins the shape; the hook pins the cross-field rules that carry the
design intent. Each rule below guards a specific way this step can produce
something that reads like an answer but isn't: a bare verdict with no attempt at
explanation, a confident judgement made without reading the paper, an inferred
upstream definition, or a quietly dropped awkward contributor.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

pytestmark = pytest.mark.unit

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).parent / "fixtures" / "subatlas"
HOOK = REPO_ROOT / ".claude" / "hooks" / "check_subatlas_consistency.py"
SCHEMA = json.loads(
    (REPO_ROOT / "src/atlas_chat/atlas_chat/schemas/subatlas_consistency.schema.json").read_text()
)


def _good() -> dict:
    return json.loads((FIXTURES / "consistency.good.json").read_text())


def _schema_errors(doc: object) -> list[str]:
    return [e.message for e in Draft202012Validator(SCHEMA).iter_errors(doc)]


def _run_hook(doc: object, *, tmp_path: Path | None = None, with_sibling: bool = False):
    """Drive the hook. Optionally place the sibling contributors file next to it.

    The hook reads that sibling to cross-check purity, so tests that exercise the
    purity rule need it present at the written path.
    """
    if tmp_path is not None:
        file_path = tmp_path / "subatlas_consistency.json"
        if with_sibling:
            shutil.copy(
                FIXTURES / "contributors.good.json", tmp_path / "subatlas_contributors.json"
            )
    else:
        file_path = Path("out/subatlas_consistency.json")
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps({"tool_input": {"file_path": str(file_path), "content": json.dumps(doc)}}),
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


# ---------------------------------------------------------------- schema


def test_the_good_fixture_validates():
    assert _schema_errors(_good()) == []


def test_the_good_fixture_passes_the_hook_with_its_sibling(tmp_path):
    result = _run_hook(_good(), tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 0, result.stderr


def test_match_type_vocabulary_is_closed():
    doc = _good()
    doc["contributors"][0]["match_type"] = "sort of matches"
    assert _schema_errors(doc)


def test_additional_properties_are_rejected():
    doc = _good()
    doc["contributors"][0]["vibes"] = "good"
    assert _schema_errors(doc)


def test_working_definition_is_required():
    doc = _good()
    del doc["working_definition"]
    assert _schema_errors(doc)


def test_an_evidence_quote_needs_a_paper_identifier():
    doc = _good()
    doc["contributors"][0]["evidence_quotes"][0]["source_paper"] = {"role": "subatlas"}
    assert _schema_errors(doc)


# ---------------------------------------------------------------- SKOS pairing


def test_hook_rejects_a_mismatched_skos_predicate(tmp_path):
    doc = _good()
    doc["contributors"][0]["skos_mapping"] = "skos:exactMatch"
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "disagree" in result.stderr


@pytest.mark.parametrize(
    ("match_type", "skos"),
    [
        ("exact match", "skos:exactMatch"),
        ("broad match", "skos:broadMatch"),
        ("narrow match", "skos:narrowMatch"),
        ("related match", "skos:relatedMatch"),
        ("no match", "skos:noMatch"),
    ],
)
def test_every_match_type_has_its_predicate(match_type, skos, tmp_path):
    doc = _good()
    verdict = doc["contributors"][0]
    verdict["match_type"] = match_type
    verdict["skos_mapping"] = skos
    if match_type == "exact match":
        verdict.pop("explanation", None)
    assert _run_hook(doc, tmp_path=tmp_path, with_sibling=True).returncode == 0


# ---------------------------------------------------------------- explanation


def test_hook_requires_an_explanation_for_any_inexact_match(tmp_path):
    """The functional spec asks for the attempt at explaining, not just the verdict."""
    doc = _good()
    del doc["contributors"][0]["explanation"]
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "an explanation is required" in result.stderr


def test_an_exact_match_needs_no_explanation(tmp_path):
    doc = _good()
    verdict = doc["contributors"][0]
    verdict.update(match_type="exact match", skos_mapping="skos:exactMatch")
    verdict.pop("explanation")
    assert _run_hook(doc, tmp_path=tmp_path, with_sibling=True).returncode == 0


# ---------------------------------------------------------------- unreachable text


def test_hook_forces_low_confidence_when_the_paper_was_never_read(tmp_path):
    doc = _good()
    verdict = doc["contributors"][0]
    verdict["evidence_status"] = "unreachable"
    verdict["confidence"] = "high"
    verdict.pop("upstream_definition")
    verdict.pop("evidence_quotes")
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "confidence must be 'low'" in result.stderr


def test_hook_rejects_an_upstream_definition_that_could_not_have_been_read(tmp_path):
    """Inferring a definition from a label string is the failure this step prevents."""
    doc = _good()
    verdict = doc["contributors"][0]
    verdict["evidence_status"] = "no_publication"
    verdict["confidence"] = "low"
    verdict.pop("evidence_quotes")
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "inferring one from the label string" in result.stderr


def test_an_honest_unreachable_verdict_passes(tmp_path):
    doc = _good()
    verdict = doc["contributors"][0]
    verdict.update(
        match_type="no match",
        skos_mapping="skos:noMatch",
        confidence="low",
        evidence_status="unreachable",
        explanation=(
            "Could not compare: the contributing paper's text was not retrievable, so "
            "its definition of the label is unknown. A retrieval limit, not a disagreement."
        ),
    )
    verdict.pop("upstream_definition")
    verdict.pop("evidence_quotes")
    assert _run_hook(doc, tmp_path=tmp_path, with_sibling=True).returncode == 0


def test_hook_requires_quotes_when_text_was_retrieved(tmp_path):
    doc = _good()
    doc["contributors"][0].pop("evidence_quotes")
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "no evidence_quotes" in result.stderr


def test_hook_rejects_a_contributor_quote_tagged_as_the_atlas(tmp_path):
    doc = _good()
    doc["contributors"][0]["evidence_quotes"][0]["source_paper"]["role"] = "atlas"
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "role 'subatlas'" in result.stderr


# ---------------------------------------------------------------- purity


def test_hook_requires_a_purity_caveat_for_an_impure_contributor(tmp_path):
    """Ulrich's purity is 0.59 in the sibling file: one verdict understates it."""
    doc = _good()
    del doc["contributors"][1]["purity_caveat"]
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "purity_caveat is" in result.stderr


def test_no_purity_caveat_needed_for_a_pure_contributor(tmp_path):
    doc = _good()
    # Weigert's purity is 1.0 and it carries no caveat; that is correct.
    assert "purity_caveat" not in doc["contributors"][0]
    assert _run_hook(doc, tmp_path=tmp_path, with_sibling=True).returncode == 0


def test_the_purity_rule_is_skipped_without_the_sibling_file(tmp_path):
    """The hook does not invent a purity it cannot read."""
    doc = _good()
    del doc["contributors"][1]["purity_caveat"]
    assert _run_hook(doc, tmp_path=tmp_path, with_sibling=False).returncode == 0


# ---------------------------------------------------------------- completeness


def test_hook_catches_a_dropped_contributor(tmp_path):
    """The easiest way to make a report look clean is to omit the awkward one."""
    doc = _good()
    doc["contributors"] = doc["contributors"][:1]
    doc["primacy"] = {"call": "atlas_primary", "reason": "..."}
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "celltype_Ulrich2024" in result.stderr


# ---------------------------------------------------------------- primacy


def test_hook_requires_a_named_paper_for_subatlas_primacy(tmp_path):
    doc = _good()
    doc["primacy"] = {"call": "subatlas_primary", "reason": "..."}
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "no primary_paper is named" in result.stderr


def test_hook_rejects_a_primary_paper_that_was_never_judged(tmp_path):
    doc = _good()
    doc["primacy"] = {
        "call": "subatlas_primary",
        "primary_paper": "celltype_SomethingElse",
        "reason": "...",
    }
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "not one of the contributors judged" in result.stderr


def test_hook_rejects_empty_co_equal_papers(tmp_path):
    doc = _good()
    doc["primacy"] = {"call": "co_equal", "reason": "..."}
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "co_equal_papers is empty" in result.stderr


def test_hook_rejects_subatlas_primacy_when_nothing_cleared_the_cutoff(tmp_path):
    doc = _good()
    doc["no_dominant_contributor"] = True
    doc["primacy"] = {
        "call": "subatlas_primary",
        "primary_paper": "celltype_Ulrich2024",
        "reason": "...",
    }
    result = _run_hook(doc, tmp_path=tmp_path, with_sibling=True)
    assert result.returncode == 2
    assert "cannot be 'subatlas_primary'" in result.stderr


def test_a_pooled_cell_set_with_no_contributors_is_valid(tmp_path):
    doc = {
        "cell_label": "AUTONOMIC_NCCS_SCPS",
        "labelset": "refined_celltype",
        "atlas_doi": "10.1/atlas",
        "working_definition": "An expert-pooled neural-crest / Schwann-cell-precursor compartment.",
        "contributors": [],
        "no_dominant_contributor": True,
        "primacy": {
            "call": "atlas_primary",
            "reason": "No contributor cleared the cutoff; an expert pool over many studies.",
        },
    }
    assert _schema_errors(doc) == []
    assert _run_hook(doc, tmp_path=tmp_path).returncode == 0


# ---------------------------------------------------------------- plumbing


def test_hook_ignores_other_files():
    result = subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps({"tool_input": {"file_path": "out/cl_mapping.json", "content": "{}"}}),
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    assert result.returncode == 0


def test_hook_rejects_invalid_json():
    result = subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(
            {"tool_input": {"file_path": "out/subatlas_consistency.json", "content": "{oops"}}
        ),
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    assert result.returncode == 2
    assert "not valid JSON" in result.stderr
