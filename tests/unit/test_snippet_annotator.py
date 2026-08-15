"""Unit tests for services.snippet_annotator (splice + follow-set).

Covers the deterministic core the agent relies on: right-to-left ref splicing,
quote integrity, unresolved tokens, id normalisation, payload nesting, schema
conformance, and the follow-set intersection / anti-hallucination check.
"""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

from atlas_chat.schemas import load_schema
from atlas_chat.services import snippet_annotator as sa

FIXTURES = Path(__file__).parent / "fixtures" / "evidence"
SOURCE = {"role": "external"}

EXPECTED_ANNOTATED = (
    "TML macrophages support angiogenesis [CorpusId:234484741]. "
    "They also guide axons [CorpusId:41350702],[CorpusId:unresolved]."
)


def _raw() -> dict:
    return json.loads((FIXTURES / "asta_snippet_search.raw.json").read_text())


def _records() -> list[dict]:
    return sa.project_response(_raw(), source_paper=SOURCE, retrieval_method="citation_traversal")


# --- splicing ----------------------------------------------------------------


@pytest.mark.unit
def test_splice_right_to_left_and_unresolved_token() -> None:
    text = "TML macrophages support angiogenesis 3. They also guide axons 4,5."
    refs = [
        {"start": 37, "end": 38, "matchedPaperCorpusId": "234484741"},
        {"start": 62, "end": 63, "matchedPaperCorpusId": "41350702"},
        {"start": 64, "end": 65, "matchedPaperCorpusId": None},
    ]
    assert sa._splice_refs(text, refs) == EXPECTED_ANNOTATED


@pytest.mark.unit
def test_splice_adjacent_run_preserves_separators() -> None:
    text = "effect 6,7,8,9 end"
    refs = [
        {"start": 7, "end": 8, "matchedPaperCorpusId": "100"},
        {"start": 9, "end": 10, "matchedPaperCorpusId": "200"},
        {"start": 11, "end": 12, "matchedPaperCorpusId": "300"},
        {"start": 13, "end": 14, "matchedPaperCorpusId": "400"},
    ]
    assert sa._splice_refs(text, refs) == (
        "effect [CorpusId:100],[CorpusId:200],[CorpusId:300],[CorpusId:400] end"
    )


@pytest.mark.unit
def test_splice_no_refs_returns_text_unchanged() -> None:
    assert sa._splice_refs("plain text with no cites", []) == "plain text with no cites"


@pytest.mark.unit
@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("234484741", "[CorpusId:234484741]"),
        (234484741, "[CorpusId:234484741]"),
        ("CorpusId:234484741", "[CorpusId:234484741]"),
        (None, sa.UNRESOLVED_TOKEN),
        ("", sa.UNRESOLVED_TOKEN),
        ("not-a-number", sa.UNRESOLVED_TOKEN),
    ],
)
def test_corpus_token_normalisation(value: object, expected: str) -> None:
    assert sa._corpus_token(value) == expected  # type: ignore[arg-type]


# --- projection --------------------------------------------------------------


@pytest.mark.unit
def test_project_snippet_preserves_text_verbatim() -> None:
    raw_item = _raw()["result"]["data"][0]
    record = sa.project_snippet(
        raw_item, source_paper=SOURCE, retrieval_method="citation_traversal"
    )
    assert record["text"] == raw_item["snippet"]["text"]
    assert record["annotated_text"] == EXPECTED_ANNOTATED
    assert record["annotated_text"] != record["text"]


@pytest.mark.unit
def test_project_snippet_maps_provenance_and_refmentions() -> None:
    record = _records()[0]
    assert record["source_paper"] == {"role": "external", "corpus_id": "CorpusId:252635104"}
    assert record["retrieval_method"] == "citation_traversal"
    assert record["refMentions"][0] == {
        "start": 37,
        "end": 38,
        "corpus_id": "CorpusId:234484741",
        "resolved": True,
    }
    assert record["refMentions"][2] == {
        "start": 64,
        "end": 65,
        "corpus_id": None,
        "resolved": False,
    }


@pytest.mark.unit
def test_project_response_payload_nesting_tolerance() -> None:
    full = _raw()
    data = full["result"]["data"]
    a = sa.project_response(full, source_paper=SOURCE, retrieval_method="citation_traversal")
    b = sa.project_response(
        {"data": data}, source_paper=SOURCE, retrieval_method="citation_traversal"
    )
    c = sa.project_response(data, source_paper=SOURCE, retrieval_method="citation_traversal")
    assert a == b == c
    assert len(a) == 1


@pytest.mark.unit
def test_project_response_score_threshold_drops_low_scores() -> None:
    assert (
        sa.project_response(
            _raw(),
            source_paper=SOURCE,
            retrieval_method="citation_traversal",
            score_threshold=0.9,
        )
        == []
    )


@pytest.mark.unit
def test_projected_records_validate_against_schema() -> None:
    validator = jsonschema.Draft202012Validator(load_schema("annotated_snippet.schema.json"))
    for record in _records():
        assert list(validator.iter_errors(record)) == []


# --- follow-set --------------------------------------------------------------


@pytest.mark.unit
def test_follow_set_drops_hallucinated_id() -> None:
    result = sa.resolve_follow_set(_records(), ["CorpusId:234484741", "CorpusId:999999"], hop=1)
    assert result["follow_set"] == ["CorpusId:234484741"]
    assert result["rejected"] == [{"corpus_id": "CorpusId:999999", "reason": "not_in_refmentions"}]
    assert result["hop"] == 1


@pytest.mark.unit
def test_follow_set_dedup_preserves_order() -> None:
    result = sa.resolve_follow_set(
        _records(),
        ["CorpusId:41350702", "CorpusId:41350702", "CorpusId:234484741"],
    )
    assert result["follow_set"] == ["CorpusId:41350702", "CorpusId:234484741"]
    assert "hop" not in result


@pytest.mark.unit
def test_follow_set_rejects_malformed_id() -> None:
    result = sa.resolve_follow_set(_records(), ["12345"])
    assert result["follow_set"] == []
    assert result["rejected"] == [{"corpus_id": "12345", "reason": "malformed"}]


@pytest.mark.unit
def test_unresolved_mention_is_not_a_real_target() -> None:
    # The null-corpus refMention contributes no followable id.
    assert sa._real_corpus_ids(_records()) == {
        "CorpusId:234484741",
        "CorpusId:41350702",
    }


@pytest.mark.unit
def test_follow_set_output_validates_against_schema() -> None:
    result = sa.resolve_follow_set(_records(), ["CorpusId:234484741", "CorpusId:999999"], hop=1)
    validator = jsonschema.Draft202012Validator(load_schema("follow_set.schema.json"))
    assert list(validator.iter_errors(result)) == []
