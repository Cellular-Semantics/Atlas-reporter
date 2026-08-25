"""Integration test: the ASTA index-depth probe against the real endpoint.

These are the acceptance criteria of #22, stated as papers rather than
thresholds. The old ``_probe_asta`` returned True for every one of them; the
probe passes only if it now separates them.

Hits the real ASTA MCP endpoint. Fails hard (not skips) if ASTA_API_KEY is
missing, per the project's integration-test policy.
"""

from __future__ import annotations

import asyncio
import os

import pytest

from atlas_chat.services import asta_indexing

#: Gopee et al. 2024, prenatal skin atlas — 72 indexed chunks across 30 sections.
FULLY_INDEXED = "CorpusId:273400864"

#: Papers ASTA holds no body text for, each of which the CorpusId check passed.
#: The last two are the ones that silently carried report claims: Wang et al.
#: 2023 (the only morphology evidence for TML macrophages) and Goh et al. (the
#: yolk-sac origin claim, resting on 4 abstract-only snippets).
NOT_FULLY_INDEXED = [
    "CorpusId:261701324",
    "CorpusId:43817583",
    "CorpusId:5707329",
    "CorpusId:266222435",
    "CorpusId:260956290",
]


def _probe(paper_id: str) -> asta_indexing.IndexingReport:
    assert os.getenv("ASTA_API_KEY"), "ASTA_API_KEY must be set for integration tests"
    return asyncio.run(asta_indexing.probe(paper_id))


@pytest.mark.integration
def test_fully_indexed_paper_is_band_full() -> None:
    report = _probe(FULLY_INDEXED)
    assert report.band == "full", report.reason
    assert report.servable
    # The two decisive signals, both well clear of their thresholds.
    assert report.sections >= asta_indexing.MIN_SECTIONS
    assert report.ref_mentions > 0
    assert report.snippets >= asta_indexing.PARTIAL_SNIPPETS
    assert report.chars >= asta_indexing.PARTIAL_CHARS


@pytest.mark.integration
@pytest.mark.parametrize("paper_id", NOT_FULLY_INDEXED)
def test_papers_with_no_body_text_are_not_band_full(paper_id: str) -> None:
    """The regression: each of these used to pass the CorpusId check."""
    report = _probe(paper_id)
    assert report.band != "full", f"{paper_id} classified full: {report.reason}"
    assert not report.servable
    assert report.band in asta_indexing.BANDS


@pytest.mark.integration
def test_the_band_does_not_depend_on_the_query() -> None:
    """A paper-scoped search returns the whole chunk set, so the band is stable.

    This is the assumption that lets one call per paper stand in for a full
    audit. If it ever stops holding, every band becomes query-dependent and the
    caching in :func:`asta_indexing.probe_cached` is unsound.
    """
    baseline = _probe(FULLY_INDEXED)
    other = asyncio.run(asta_indexing.probe(FULLY_INDEXED, query="mitochondrial ribosome assembly"))
    assert other.snippets == baseline.snippets
    assert other.chars == baseline.chars
    assert other.band == baseline.band


@pytest.mark.integration
def test_a_paper_absent_from_semantic_scholar_is_not_in_s2() -> None:
    """The #13 case: distinct from registered-but-unindexed, and must not raise."""
    report = asyncio.run(asta_indexing.probe("DOI:10.1126/science.adx0659"))
    assert report.band in ("not_in_s2", "unindexed"), report.reason
    assert not report.servable
    assert report.dead
