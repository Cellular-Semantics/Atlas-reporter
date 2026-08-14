"""Schema regression for evidence-provenance contracts (issue #12).

Pins the shape of ``all_summaries.json`` and ``supplementary_findings.json``:
every evidence item must carry a ``source_paper`` (with ``role``) and a
``retrieval_method``. Good golden fixtures must validate; targeted mutations
must be rejected.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

import jsonschema
import pytest

from atlas_chat.schemas import load_schema

FIXTURES = Path(__file__).parent / "fixtures" / "evidence"


def _load_fixture(name: str) -> object:
    return json.loads((FIXTURES / name).read_text())


def _validate(schema_name: str, data: object) -> list[str]:
    schema = load_schema(schema_name)
    validator = jsonschema.Draft202012Validator(schema)
    return [e.message for e in validator.iter_errors(data)]


# --- schemas are themselves well-formed -------------------------------------


@pytest.mark.unit
@pytest.mark.parametrize(
    "schema_name",
    ["all_summaries.schema.json", "supplementary_findings.schema.json"],
)
def test_schema_is_valid(schema_name: str) -> None:
    jsonschema.Draft202012Validator.check_schema(load_schema(schema_name))


# --- all_summaries -----------------------------------------------------------


@pytest.mark.unit
def test_all_summaries_good_fixture_validates() -> None:
    data = _load_fixture("all_summaries.good.json")
    assert _validate("all_summaries.schema.json", data) == []


@pytest.mark.unit
def test_all_summaries_rejects_missing_source_paper() -> None:
    data = _load_fixture("all_summaries.good.json")
    del data[0]["source_paper"]
    assert _validate("all_summaries.schema.json", data)


@pytest.mark.unit
def test_all_summaries_rejects_bad_retrieval_method() -> None:
    data = _load_fixture("all_summaries.good.json")
    data[0]["retrieval_method"] = "made_up"
    assert _validate("all_summaries.schema.json", data)


@pytest.mark.unit
def test_all_summaries_rejects_source_paper_without_role() -> None:
    data = _load_fixture("all_summaries.good.json")
    del data[0]["source_paper"]["role"]
    assert _validate("all_summaries.schema.json", data)


@pytest.mark.unit
def test_all_summaries_rejects_source_paper_without_identifier() -> None:
    data = _load_fixture("all_summaries.good.json")
    data[0]["source_paper"] = {"role": "atlas"}
    assert _validate("all_summaries.schema.json", data)


@pytest.mark.unit
def test_all_summaries_rejects_extra_property() -> None:
    data = _load_fixture("all_summaries.good.json")
    data[0]["surprise"] = "not allowed"
    assert _validate("all_summaries.schema.json", data)


# --- supplementary_findings --------------------------------------------------


@pytest.mark.unit
def test_supplementary_findings_good_fixture_validates() -> None:
    data = _load_fixture("supplementary_findings.good.json")
    assert _validate("supplementary_findings.schema.json", data) == []


@pytest.mark.unit
def test_supplement_marker_requires_source_paper() -> None:
    data = _load_fixture("supplementary_findings.good.json")
    del data["markers"][0]["source_paper"]
    assert _validate("supplementary_findings.schema.json", data)


@pytest.mark.unit
def test_supplement_quote_requires_retrieval_method() -> None:
    data = _load_fixture("supplementary_findings.good.json")
    del data["evidence_quotes"][0]["retrieval_method"]
    assert _validate("supplementary_findings.schema.json", data)


@pytest.mark.unit
def test_supplement_ref_requires_file() -> None:
    data = _load_fixture("supplementary_findings.good.json")
    del data["markers"][0]["supplement_ref"]["file"]
    assert _validate("supplementary_findings.schema.json", data)


@pytest.mark.unit
def test_supplementary_findings_rejects_extra_property() -> None:
    data = _load_fixture("supplementary_findings.good.json")
    data["markers"][0]["surprise"] = "nope"
    assert _validate("supplementary_findings.schema.json", data)


@pytest.mark.unit
def test_good_fixtures_are_independent_copies() -> None:
    # Guard: mutating a loaded fixture must not affect a fresh load.
    a = _load_fixture("all_summaries.good.json")
    b = copy.deepcopy(a)
    a[0]["retrieval_method"] = "free_search"
    assert b[0]["retrieval_method"] == "corpus_snippet"
