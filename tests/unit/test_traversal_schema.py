"""Schema + hook regression for ASTA-native citation traversal (issue #14).

Pins the two pipeline schemas (annotated_snippet -> evidence_summary), the
sentence-gated traversal fields (reached_from.hop, refMention.corpus_id nullable),
the all_summaries <-> evidence_summary mirror, and the PostToolUse validator hooks.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import jsonschema
import pytest

from atlas_chat.schemas import load_schema

FIXTURES = Path(__file__).parent / "fixtures" / "evidence"
REPO_ROOT = Path(__file__).resolve().parents[2]


def _load_fixture(name: str) -> object:
    return json.loads((FIXTURES / name).read_text())


def _errors(schema_name: str, data: object) -> list[str]:
    validator = jsonschema.Draft202012Validator(load_schema(schema_name))
    return [e.message for e in validator.iter_errors(data)]


def _item_errors(schema_name: str, items: list) -> list[str]:
    validator = jsonschema.Draft202012Validator(load_schema(schema_name))
    out: list[str] = []
    for item in items:
        out += [e.message for e in validator.iter_errors(item)]
    return out


# --- schemas well-formed -----------------------------------------------------


@pytest.mark.unit
@pytest.mark.parametrize(
    "schema_name",
    [
        "annotated_snippet.schema.json",
        "evidence_summary.schema.json",
        "citation_traverse_input.schema.json",
        "follow_set.schema.json",
    ],
)
def test_schema_is_valid(schema_name: str) -> None:
    jsonschema.Draft202012Validator.check_schema(load_schema(schema_name))


# --- all_summaries mirrors evidence_summary ----------------------------------


@pytest.mark.unit
def test_all_summaries_item_mirrors_evidence_summary() -> None:
    es = load_schema("evidence_summary.schema.json")
    item = load_schema("all_summaries.schema.json")["$defs"]["EvidenceSummary"]
    assert set(item["properties"]) == set(es["properties"])
    assert set(item["required"]) == set(es["required"])


# --- evidence_summary --------------------------------------------------------


@pytest.mark.unit
def test_evidence_summary_good_fixture_validates() -> None:
    assert (
        _item_errors("evidence_summary.schema.json", _load_fixture("evidence_summary.good.json"))
        == []
    )


@pytest.mark.unit
def test_evidence_summary_reached_from_requires_hop() -> None:
    data = _load_fixture("evidence_summary.good.json")
    del data[1]["reached_from"]["hop"]
    assert _item_errors("evidence_summary.schema.json", data)


@pytest.mark.unit
def test_evidence_summary_rejects_traversal_machinery() -> None:
    # refMentions / sentences must not leak into the distilled item.
    data = _load_fixture("evidence_summary.good.json")
    data[0]["refMentions"] = []
    assert _item_errors("evidence_summary.schema.json", data)


@pytest.mark.unit
def test_evidence_summary_requires_quotes() -> None:
    data = _load_fixture("evidence_summary.good.json")
    del data[0]["quotes"]
    assert _item_errors("evidence_summary.schema.json", data)


# --- annotated_snippet -------------------------------------------------------


@pytest.mark.unit
def test_annotated_snippet_good_fixture_validates() -> None:
    assert (
        _item_errors("annotated_snippet.schema.json", _load_fixture("annotated_snippet.good.json"))
        == []
    )


@pytest.mark.unit
def test_annotated_snippet_allows_null_refmention_corpus_id() -> None:
    # An on-topic-but-unresolved edge (null CorpusId) is valid — logged, not dropped.
    data = _load_fixture("annotated_snippet.good.json")
    assert data[1]["refMentions"][0]["corpus_id"] is None
    assert _item_errors("annotated_snippet.schema.json", data) == []


@pytest.mark.unit
def test_annotated_snippet_rejects_bad_refmention_corpus_id() -> None:
    data = _load_fixture("annotated_snippet.good.json")
    data[0]["refMentions"][0]["corpus_id"] = "41350702"  # missing CorpusId: prefix
    assert _item_errors("annotated_snippet.schema.json", data)


@pytest.mark.unit
def test_annotated_snippet_requires_text_and_score() -> None:
    data = _load_fixture("annotated_snippet.good.json")
    del data[0]["text"]
    del data[0]["score"]
    assert len(_item_errors("annotated_snippet.schema.json", data)) >= 2


@pytest.mark.unit
def test_annotated_snippet_with_annotated_text_validates() -> None:
    # The spliced record (with annotated_text) is valid...
    data = _load_fixture("annotated_snippet_with_annotated_text.good.json")
    assert "annotated_text" in data[0]
    assert _item_errors("annotated_snippet.schema.json", data) == []


@pytest.mark.unit
def test_annotated_snippet_annotated_text_is_optional() -> None:
    # ...and legacy records without annotated_text still validate (back-compat).
    legacy = _load_fixture("annotated_snippet.good.json")
    assert all("annotated_text" not in item for item in legacy)
    assert _item_errors("annotated_snippet.schema.json", legacy) == []


# --- follow_set --------------------------------------------------------------


@pytest.mark.unit
def test_follow_set_good_fixture_validates() -> None:
    assert _errors("follow_set.schema.json", _load_fixture("follow_set.good.json")) == []


@pytest.mark.unit
def test_follow_set_bad_fixture_rejected() -> None:
    # Bare id in follow_set (missing CorpusId: prefix) + bad rejected reason enum.
    assert _errors("follow_set.schema.json", _load_fixture("follow_set.bad.json"))


# --- PostToolUse hooks -------------------------------------------------------


def _run_hook(hook: str, file_path: str, payload: object) -> subprocess.CompletedProcess:
    hook_input = json.dumps(
        {"tool_input": {"file_path": file_path, "content": json.dumps(payload)}}
    )
    return subprocess.run(
        [sys.executable, str(REPO_ROOT / ".claude" / "hooks" / hook)],
        input=hook_input,
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


@pytest.mark.unit
def test_evidence_summary_hook_accepts_good_all_summaries() -> None:
    r = _run_hook(
        "check_evidence_summary.py",
        "projects/x/traversal_output/ct/all_summaries.json",
        _load_fixture("evidence_summary.good.json"),
    )
    assert r.returncode == 0, r.stderr


@pytest.mark.unit
def test_evidence_summary_hook_rejects_bad_item() -> None:
    r = _run_hook(
        "check_evidence_summary.py",
        "projects/x/traversal_output/ct/all_summaries.json",
        [{"source_paper": {"role": "external"}, "retrieval_method": "nope", "summary": "x"}],
    )
    assert r.returncode == 2
    assert "VALIDATION FAILED" in r.stderr


@pytest.mark.unit
def test_evidence_summary_hook_ignores_other_files() -> None:
    r = _run_hook("check_evidence_summary.py", "projects/x/notes.txt", {"anything": 1})
    assert r.returncode == 0


@pytest.mark.unit
def test_annotated_snippet_hook_accepts_good_and_null_edge() -> None:
    r = _run_hook(
        "check_annotated_snippet.py",
        "projects/x/traversal_output/ct/annotated_snippets_hop1.json",
        _load_fixture("annotated_snippet.good.json"),
    )
    assert r.returncode == 0, r.stderr


@pytest.mark.unit
def test_annotated_snippet_hook_rejects_bad_record() -> None:
    r = _run_hook(
        "check_annotated_snippet.py",
        "projects/x/traversal_output/ct/annotated_snippets_hop0.json",
        [{"section": "Results", "source_paper": {"role": "atlas"}}],
    )
    assert r.returncode == 2
    assert "VALIDATION FAILED" in r.stderr


@pytest.mark.unit
def test_follow_set_hook_accepts_good() -> None:
    r = _run_hook(
        "check_follow_set.py",
        "projects/x/traversal_output/ct/follow_set_hop1.json",
        _load_fixture("follow_set.good.json"),
    )
    assert r.returncode == 0, r.stderr


@pytest.mark.unit
def test_follow_set_hook_rejects_bad() -> None:
    r = _run_hook(
        "check_follow_set.py",
        "projects/x/traversal_output/ct/follow_set_hop1.json",
        _load_fixture("follow_set.bad.json"),
    )
    assert r.returncode == 2
    assert "VALIDATION FAILED" in r.stderr


@pytest.mark.unit
def test_follow_set_hook_ignores_other_files() -> None:
    r = _run_hook("check_follow_set.py", "projects/x/notes.txt", {"anything": 1})
    assert r.returncode == 0
