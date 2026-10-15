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

#: Yao et al. 2023, "A high-resolution transcriptomic and spatial atlas of cell
#: types in the whole mouse brain" (Nature). One of the papers that motivated
#: this work, and the sharpest counter-example to the signals we rejected: open
#: access, in PMC, 118 references in the metadata graph — and 3 title/abstract
#: snippets in ASTA, no body text at all. Nothing short of probing distinguishes
#: it from a fully indexed paper.
YAO_2023 = "CorpusId:266222435"
YAO_2023_DOI = "DOI:10.1038/s41586-023-06812-z"

#: Goh et al. 2023, yolk sac cell atlas — the paper the TML macrophage report's
#: yolk-sac origin claim silently rested on, with 4 abstract-only snippets.
GOH_2023 = "CorpusId:260956290"

#: Wang et al. 2023 — carried the only morphology evidence for TML macrophages,
#: and was reachable only second-hand via two 2026 reviews that cite it.
WANG_2023 = "CorpusId:261701324"

#: Papers ASTA holds no body text for, each of which the CorpusId check passed.
NOT_FULLY_INDEXED = [
    WANG_2023,
    "CorpusId:43817583",
    "CorpusId:5707329",
    YAO_2023,
    GOH_2023,
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
def test_yao_2023_is_abstract_only_despite_looking_fully_available() -> None:
    """The motivating case, and the reason the rejected signals are rejected.

    Yao et al. 2023 is open access, sits in PMC, and its metadata graph carries
    118 references — every surface signal says "this paper is available". ASTA's
    snippet index holds only the title and abstract. `isOpenAccess`,
    `openAccessPdf` and `referenceCount` would all wave it through; only the
    section/refMention probe catches it.

    **If this test fails because the band is now `full` or `partial`, ASTA has
    started indexing the paper — that is good news, not a bug here.** Move it out
    of ``NOT_FULLY_INDEXED``, pick another abstract-only paper for this test, and
    note the change; do not loosen the assertion to keep it passing.
    """
    report = _probe(YAO_2023)
    assert report.band == "abstract_only", (
        f"expected abstract_only, got {report.band} — if ASTA now indexes this "
        f"paper's body text, update the fixture rather than the threshold. "
        f"{report.reason}"
    )
    assert report.snippets > 0, "abstract_only means thin, not absent"
    assert report.sections == 0, "no section names — nothing but title/abstract"
    assert report.ref_mentions == 0, "no bibliography in the index"
    # Not dead: the reference edges are still recoverable from the graph API
    # (116 of 118 carry a paperId), just without the character offsets that make
    # sentence-level gating possible. That is the deferred follow-up.
    assert not report.dead
    assert not report.servable


@pytest.mark.integration
def test_yao_2023_bands_identically_by_doi_and_corpus_id() -> None:
    """Either identifier must reach the same verdict — the audit CLI takes both."""
    by_corpus = _probe(YAO_2023)
    by_doi = _probe(YAO_2023_DOI)
    assert by_doi.band == by_corpus.band
    assert by_doi.snippets == by_corpus.snippets
    assert by_doi.corpus_id == YAO_2023


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
