"""Unit tests for the local snippet index.

Driven by a tiny synthetic JATS fixture so the test runs without network
and without the heavy ML stack — only the parser + chunker + merge layer
are exercised. The embedding step is bypassed via direct chunk inspection.
"""

from __future__ import annotations

import json
from textwrap import dedent

import atlas_chat.services.local_snippet_index as lsi
import pytest
from atlas_chat.services.local_snippet_index import (
    _cached_ref_resolution,
    _local_corpus_id,
    _manifest_hash,
    _merge_snippets,
    _normalize_biorxiv_jats,
    build_sentence_rows,
    chunk_segments,
    extract_body_segments,
    has_local_index,
    split_chunk_into_windows,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

# Minimal bioRxiv-flavoured JATS: uses <citation> + hwp:id (the two quirks the
# normaliser handles), one cited sentence, one ref-list entry with a DOI.
JATS_FIXTURE = dedent("""\
    <?xml version="1.0"?>
    <article xmlns:hw="org.highwire.hpp">
      <front>
        <article-meta>
          <abstract>
            <p>Abstract paragraph mentioning ILC3 cells in skin.</p>
          </abstract>
        </article-meta>
      </front>
      <body>
        <sec>
          <title>Introduction</title>
          <p>Prior work showed marker expression in skin<sup><xref
              ref-type="bibr" rid="c1">1</xref></sup>.</p>
          <p>Another paragraph without citations describing methods.</p>
        </sec>
        <sec>
          <title>Results</title>
          <p>We identified ILC3_CCL1+PTGDS+ cells localised to the superficial dermis.</p>
        </sec>
      </body>
      <back>
        <ref-list>
          <ref id="c1" hwp:id="ref-1">
            <citation publication-type="journal">
              <article-title>Reference paper title</article-title>
              <year>2021</year>
              <pub-id pub-id-type="doi">10.1234/example</pub-id>
            </citation>
          </ref>
        </ref-list>
      </back>
    </article>
""")


# ---------------------------------------------------------------------------
# _normalize_biorxiv_jats
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_normalize_strips_hwp_and_renames_citation() -> None:
    out = _normalize_biorxiv_jats(JATS_FIXTURE)
    assert "hwp:id" not in out
    assert "xmlns:hw=" not in out
    assert "<element-citation" in out
    # Plain <citation> on its own (without publication-type) is unchanged
    assert "<citation publication-type=" not in out


# ---------------------------------------------------------------------------
# extract_body_segments + chunk_segments
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_body_extraction_includes_sections() -> None:
    normalized = _normalize_biorxiv_jats(JATS_FIXTURE)
    segments = extract_body_segments(normalized)
    sections = {s.section for s in segments}
    assert "ABSTRACT" in sections
    assert "Introduction" in sections
    assert "Results" in sections
    # ref-list text should not appear in body extraction
    assert not any("Reference paper title" in s.text for s in segments)


@pytest.mark.unit
def test_chunking_produces_fulltext_with_consistent_offsets() -> None:
    normalized = _normalize_biorxiv_jats(JATS_FIXTURE)
    segments = extract_body_segments(normalized)
    fulltext, chunks = chunk_segments(segments)
    assert chunks, "expected at least one chunk"
    # Each chunk's slice of fulltext must equal its stored text
    for c in chunks:
        # Allow loose offsets when overlap is added, but text must be a
        # substring of fulltext.
        assert c.text in fulltext
        assert c.section
    # Re-assemble cleanly
    assert "ILC3_CCL1+PTGDS+" in fulltext
    # Every chunk must be embeddable: at least one window, none over budget (#23).
    for c in chunks:
        windows = split_chunk_into_windows(c.text, _count_words)
        assert windows
        assert all(_count_words(w) <= lsi.WINDOW_TARGET_TOKENS for w in windows)


# ---------------------------------------------------------------------------
# build_sentence_rows
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_sentence_rows_resolve_doi() -> None:
    normalized = _normalize_biorxiv_jats(JATS_FIXTURE)
    segments = extract_body_segments(normalized)
    fulltext, _ = chunk_segments(segments)
    rows, refs = build_sentence_rows(normalized, fulltext)
    # The single cited sentence references c1 → 10.1234/example
    assert "c1" in refs
    assert refs["c1"].doi == "10.1234/example"
    cited = [r for r in rows if "c1" in r.ref_ids]
    assert cited, "expected at least one cited sentence"
    assert all("10.1234/example" in r.doi_list for r in cited)


# ---------------------------------------------------------------------------
# _merge_snippets — ASTA-shape parity
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_merge_emits_asta_shape() -> None:
    normalized = _normalize_biorxiv_jats(JATS_FIXTURE)
    segments = extract_body_segments(normalized)
    fulltext, chunks = chunk_segments(segments)
    rows, _refs = build_sentence_rows(normalized, fulltext)
    paper_meta = {
        "corpus_id": "CorpusId:local_abc123",
        "title": "Test",
        "authors": "Test, A.",
        "year": 2026,
        "doi": "10.0000/test",
    }
    # Caller now supplies a ref_id → corpus_id map directly (supports refs
    # resolved via title-match as well as via DOI).
    ref_id_to_corpus = {"c1": "999999"}
    snippets = _merge_snippets(chunks, rows, ref_id_to_corpus, paper_meta)
    assert snippets
    s0 = snippets[0]
    # Top-level shape
    assert {"chunk_id", "paper", "snippet"} <= set(s0.keys())
    assert s0["paper"]["corpusId"] == "CorpusId:local_abc123"
    # snippet shape
    assert {"text", "section", "annotations"} <= set(s0["snippet"].keys())
    # At least one refMention with the resolved corpus_id
    all_refs = [rm for s in snippets for rm in s["snippet"]["annotations"]["refMentions"]]
    assert any(rm["matchedPaperCorpusId"] == "999999" for rm in all_refs)


# ---------------------------------------------------------------------------
# Misc
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_local_corpus_id_format() -> None:
    cid = _local_corpus_id("10.1101/foo")
    assert cid.startswith("CorpusId:local_")
    # Has no digits-only suffix → won't false-match the legacy `\d+` regex
    import re

    assert not re.match(r"^CorpusId:\d+$", cid)


@pytest.mark.unit
def test_has_local_index_false_for_missing(tmp_path) -> None:
    assert not has_local_index(tmp_path)


# ---------------------------------------------------------------------------
# Windowing for the embedding model (#23)
# ---------------------------------------------------------------------------


def _count_words(text: str) -> int:
    """Stand-in for the model tokeniser — predictable, so window sizes are exact."""
    return len(text.split())


@pytest.mark.unit
def test_short_chunk_is_a_single_window() -> None:
    text = "One short sentence about macrophages."
    assert split_chunk_into_windows(text, _count_words, target_tokens=50) == [text]


@pytest.mark.unit
def test_empty_chunk_yields_no_windows() -> None:
    assert split_chunk_into_windows("", _count_words) == []


@pytest.mark.unit
def test_long_chunk_windows_fit_the_budget_and_cover_the_text() -> None:
    sentences = [f"Sentence number {i} describes marker gene GENE{i} in detail." for i in range(40)]
    text = " ".join(sentences)
    windows = split_chunk_into_windows(text, _count_words, target_tokens=30, overlap_tokens=10)

    assert len(windows) > 1
    for w in windows:
        assert _count_words(w) <= 30
        assert w in text, "windows must be exact substrings of the chunk"
    # Nothing is dropped: every sentence lands in at least one window.
    joined = " ".join(windows)
    for sent in sentences:
        assert sent in joined
    # Consecutive windows overlap, so a claim spanning a boundary stays intact.
    assert windows[0].split()[-1] in windows[1]


@pytest.mark.unit
def test_single_over_long_sentence_is_split() -> None:
    """A table row or reference blob with no sentence break still fits."""
    text = " ".join(f"token{i}" for i in range(200))
    windows = split_chunk_into_windows(text, _count_words, target_tokens=25, overlap_tokens=5)
    assert len(windows) > 1
    assert all(_count_words(w) <= 25 for w in windows)


# ---------------------------------------------------------------------------
# Index invalidation
# ---------------------------------------------------------------------------


@pytest.mark.unit
@pytest.mark.parametrize(
    "const",
    [
        "MANIFEST_VERSION",
        "EMBED_MODEL",
        "CHUNK_TARGET_CHARS",
        "CHUNK_OVERLAP_CHARS",
        "WINDOW_TARGET_TOKENS",
        "WINDOW_OVERLAP_TOKENS",
    ],
)
def test_manifest_hash_changes_with_index_parameters(
    const: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Changing anything that changes the vectors must invalidate existing
    indexes, or a rebuild silently keeps serving stale ones."""
    baseline = _manifest_hash(b"source", "jats")
    original = getattr(lsi, const)
    changed = original + 1 if isinstance(original, int) else original + "-x"
    monkeypatch.setattr(lsi, const, changed)
    assert _manifest_hash(b"source", "jats") != baseline


@pytest.mark.unit
def test_manifest_hash_changes_with_source_bytes() -> None:
    assert _manifest_hash(b"source", "jats") != _manifest_hash(b"other", "jats")
    assert _manifest_hash(b"source", "jats") != _manifest_hash(b"source", "pdf")


# ---------------------------------------------------------------------------
# Cached reference resolution across rebuilds
# ---------------------------------------------------------------------------

RESOLUTION = {"c1": {"corpus_id": "CorpusId:1", "doi": "10.1234/x", "method": "doi"}}


def _refs_dir(tmp_path):
    d = tmp_path / "citations"
    d.mkdir()
    (d / "ref_resolution.json").write_text(json.dumps(RESOLUTION))
    return d


@pytest.mark.unit
def test_cached_refs_reused_when_source_unchanged(tmp_path) -> None:
    d = _refs_dir(tmp_path)
    assert _cached_ref_resolution(d, {"source_sha": "abc"}, "abc") == RESOLUTION


@pytest.mark.unit
def test_cached_refs_dropped_when_source_changed(tmp_path) -> None:
    d = _refs_dir(tmp_path)
    assert _cached_ref_resolution(d, {"source_sha": "abc"}, "def") is None


@pytest.mark.unit
def test_cached_refs_reused_for_manifests_predating_source_sha(tmp_path) -> None:
    """The pre-#23 corpora everyone has to rebuild have no source_sha, and
    re-resolving their references costs tens of minutes per paper."""
    d = _refs_dir(tmp_path)
    assert _cached_ref_resolution(d, {"version": 2, "hash": "old"}, "abc") == RESOLUTION


@pytest.mark.unit
def test_no_cached_refs_without_a_prior_manifest(tmp_path) -> None:
    d = _refs_dir(tmp_path)
    assert _cached_ref_resolution(d, {}, "abc") is None


@pytest.mark.unit
def test_no_cached_refs_when_file_missing_or_empty(tmp_path) -> None:
    d = tmp_path / "citations"
    d.mkdir()
    assert _cached_ref_resolution(d, {"source_sha": "abc"}, "abc") is None
    (d / "ref_resolution.json").write_text("{}")
    assert _cached_ref_resolution(d, {"source_sha": "abc"}, "abc") is None
    (d / "ref_resolution.json").write_text("not json")
    assert _cached_ref_resolution(d, {"source_sha": "abc"}, "abc") is None
