"""Regression for the source-tagging checks in report_checker (issue #12).

Covers ``check_source_tags`` directly and its integration into
``validate_report``: every evidence item must carry a resolvable
``source_paper`` + ``retrieval_method``; ``supplement`` items must resolve to an
``atlas``/``subatlas`` corpus member; every referenced paper must appear in the
catalogue.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from atlas_chat.validation.report_checker import check_source_tags, validate_report

FIXTURES = Path(__file__).parent / "fixtures" / "evidence"

# Catalogue containing every paper referenced by the good fixtures.
CATALOGUE: dict[str, object] = {
    "CorpusId:2762329": {"doi": "10.1038/s41586-024-08002-x", "title": "A prenatal skin atlas"},
    "CorpusId:252635104": {"doi": "", "title": "Ferroportin and iron export"},
    "CorpusId:231699447": {"doi": "", "title": "Citing paper"},
}


def _summaries() -> list[dict[str, object]]:
    return json.loads((FIXTURES / "all_summaries.good.json").read_text())


def _supp() -> dict[str, object]:
    return json.loads((FIXTURES / "supplementary_findings.good.json").read_text())


@pytest.mark.unit
def test_good_fixtures_pass() -> None:
    assert check_source_tags(_summaries(), _supp(), CATALOGUE) == []


@pytest.mark.unit
def test_missing_source_paper_flagged() -> None:
    summaries = _summaries()
    del summaries[0]["source_paper"]
    errors = check_source_tags(summaries, _supp(), CATALOGUE)
    # Schema-derived: "'source_paper' is a required property".
    assert any("source_paper" in e and "required" in e for e in errors)


@pytest.mark.unit
def test_invalid_retrieval_method_flagged() -> None:
    summaries = _summaries()
    summaries[0]["retrieval_method"] = "guesswork"
    errors = check_source_tags(summaries, _supp(), CATALOGUE)
    assert any("retrieval_method" in e for e in errors)


@pytest.mark.unit
def test_supplement_with_external_role_flagged() -> None:
    supp = _supp()
    supp["markers"][0]["source_paper"]["role"] = "external"
    errors = check_source_tags(_summaries(), supp, CATALOGUE)
    assert any("atlas/subatlas" in e for e in errors)


@pytest.mark.unit
def test_source_paper_not_in_catalogue_flagged() -> None:
    summaries = _summaries()
    summaries[0]["source_paper"] = {"corpus_id": "CorpusId:99999999", "role": "atlas"}
    errors = check_source_tags(summaries, _supp(), CATALOGUE)
    assert any("not found in paper_catalogue" in e for e in errors)


@pytest.mark.unit
def test_source_paper_resolved_by_doi() -> None:
    summaries = _summaries()
    # Drop the corpus_id; the DOI alone must still resolve against the catalogue.
    summaries[0]["source_paper"] = {"doi": "10.1038/s41586-024-08002-x", "role": "atlas"}
    assert check_source_tags(summaries, _supp(), CATALOGUE) == []


@pytest.mark.unit
def test_reached_from_not_in_catalogue_flagged() -> None:
    summaries = _summaries()
    summaries[1]["reached_from"]["corpus_id"] = "CorpusId:88888888"
    errors = check_source_tags(summaries, _supp(), CATALOGUE)
    assert any("reached_from" in e and "not found" in e for e in errors)


@pytest.mark.unit
def test_source_paper_without_identifier_flagged() -> None:
    summaries = _summaries()
    summaries[0]["source_paper"] = {"role": "atlas"}
    errors = check_source_tags(summaries, _supp(), CATALOGUE)
    # Schema-derived: source_paper fails the anyOf(doi|corpus_id) requirement.
    assert any("source_paper" in e for e in errors)


@pytest.mark.unit
def test_validate_report_runs_source_tag_checks(tmp_path: Path) -> None:
    traversal = tmp_path
    (traversal / "all_summaries.json").write_text(json.dumps(_summaries()))
    (traversal / "paper_catalogue.json").write_text(json.dumps(CATALOGUE))
    # Break one item so validate_report must surface a source-tag error.
    supp = _supp()
    del supp["markers"][0]["source_paper"]
    (traversal / "supplementary_findings.json").write_text(json.dumps(supp))

    report = tmp_path / "report.md"
    report.write_text("# Report\n\nNo quotes, no DOIs.\n")

    passed, errors = validate_report(report, traversal)
    assert not passed
    assert any("source_paper" in e and "required" in e for e in errors)
