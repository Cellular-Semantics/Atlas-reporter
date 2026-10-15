"""Integration test: live ASTA snippet_search -> annotate -> follow-set.

Hits the real ASTA MCP endpoint. Fails hard (not skips) if ASTA_API_KEY is
missing, per the project's integration-test policy.
"""

from __future__ import annotations

import asyncio
import os
import re

import pytest
from atlas_chat.cli_annotate import _fetch_raw

from atlas_chat.services import snippet_annotator as sa

SEED = "CorpusId:273400864"  # Gopee et al. 2024 prenatal skin atlas
TOKEN_RE = re.compile(r"\[CorpusId:(\d+)\]")


@pytest.mark.integration
def test_live_snippet_search_annotates_and_gates_follow_set() -> None:
    assert os.getenv("ASTA_API_KEY"), "ASTA_API_KEY must be set for integration tests"

    raw = asyncio.run(
        _fetch_raw("TREM2 microglia-like macrophages markers location function", SEED, 10)
    )
    records = sa.project_response(
        raw, source_paper={"role": "atlas"}, retrieval_method="corpus_snippet"
    )
    assert records, "expected at least one snippet from the seed paper"

    for record in records:
        assert record["text"], "text must be present and verbatim"
        real = {m["corpus_id"] for m in record["refMentions"] if m["corpus_id"]}
        # Every inline token in annotated_text corresponds to a real refMention id.
        for corpus_num in TOKEN_RE.findall(record["annotated_text"]):
            assert f"CorpusId:{corpus_num}" in real

    # An injected fake id is never followed.
    result = sa.resolve_follow_set(records, ["CorpusId:99999999"])
    assert result["follow_set"] == []
    assert result["rejected"][0]["reason"] == "not_in_refmentions"
