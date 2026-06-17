"""Unit tests for the corpus model (multi-paper layout + migration).

Avoids the embedding step by direct manifest manipulation. Tests are
network-free.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest
from atlas_chat.services import local_snippet_index as lsi

# ---------------------------------------------------------------------------
# paper_slug
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_paper_slug_basic() -> None:
    assert lsi.paper_slug("10.1126/science.adf1226") == "10.1126_science.adf1226"
    assert lsi.paper_slug("10.1101/2024.03.20.123456") == "10.1101_2024.03.20.123456"


@pytest.mark.unit
def test_paper_slug_handles_uppercase_and_unsafe() -> None:
    s = lsi.paper_slug("10.1234/Foo Bar(Baz)")
    assert "/" not in s
    assert " " not in s
    assert "(" not in s
    assert s.startswith("10.1234_foo")


@pytest.mark.unit
def test_paper_slug_pathological_falls_back_to_hash() -> None:
    long_doi = "10.1234/" + "x" * 200
    s = lsi.paper_slug(long_doi)
    assert s.startswith("doi-") or len(s) <= 80


# ---------------------------------------------------------------------------
# Corpus init + upsert
# ---------------------------------------------------------------------------


def _write_paper_files(
    project_dir: Path,
    slug: str,
    doi: str,
    role: str,
    chunks: list[dict],
    embeddings: np.ndarray,
) -> dict:
    p_dir = project_dir / "local_index" / "papers" / slug
    (p_dir / "chunks").mkdir(parents=True, exist_ok=True)
    (p_dir / "snippet_index").mkdir(parents=True, exist_ok=True)
    with (p_dir / "chunks" / "chunks.jsonl").open("w") as fh:
        for c in chunks:
            fh.write(json.dumps(c) + "\n")
    np.save(p_dir / "chunks" / "embeddings.npy", embeddings)
    paper_meta = {
        "corpus_id": lsi._local_corpus_id(doi),
        "title": f"Paper {slug}",
        "authors": "Test, A.",
        "year": 2024,
        "doi": doi,
        "url": f"https://doi.org/{doi}",
    }
    snippets = [
        {
            "chunk_id": c["chunk_id"],
            "paper": paper_meta,
            "snippet": {
                "text": c["text"],
                "section": c["section"],
                "annotations": {"refMentions": []},
            },
        }
        for c in chunks
    ]
    (p_dir / "snippet_index" / "snippets.json").write_text(json.dumps(snippets))
    manifest = {
        "version": lsi.MANIFEST_VERSION,
        "slug": slug,
        "doi": doi,
        "role": role,
        "source_type": "jats",
        "citation_graph": False,
        "hash": "deadbeef",
        "embedding_model": lsi.EMBED_MODEL,
        "n_chunks": len(chunks),
        "n_sentences": 0,
        "n_refs": 0,
        "n_corpus_ids_resolved": 0,
        "resolution_methods": {},
        "paper": paper_meta,
    }
    (p_dir / "manifest.json").write_text(json.dumps(manifest))
    return manifest


@pytest.mark.unit
def test_upsert_creates_corpus_json(tmp_path: Path) -> None:
    manifest = _write_paper_files(
        tmp_path,
        "10.1234_atlas",
        "10.1234/atlas",
        "atlas",
        [{"chunk_id": 0, "section": "BODY", "char_start": 0, "char_end": 10, "text": "hello"}],
        np.array([[1.0, 0.0]]),
    )
    lsi._upsert_corpus_entry(tmp_path, "10.1234_atlas", manifest)
    corpus = json.loads((tmp_path / "local_index" / "corpus.json").read_text())
    assert corpus["atlas_doi"] == "10.1234/atlas"
    assert corpus["use_in_fanout"] is False
    assert len(corpus["papers"]) == 1
    assert corpus["papers"][0]["role"] == "atlas"


@pytest.mark.unit
def test_upsert_keeps_atlas_first(tmp_path: Path) -> None:
    atlas_m = _write_paper_files(
        tmp_path,
        "atlas-slug",
        "10.1234/atlas",
        "atlas",
        [{"chunk_id": 0, "section": "BODY", "char_start": 0, "char_end": 5, "text": "atlas"}],
        np.array([[1.0, 0.0]]),
    )
    sub_m = _write_paper_files(
        tmp_path,
        "sub-slug",
        "10.1234/sub",
        "subatlas",
        [{"chunk_id": 0, "section": "BODY", "char_start": 0, "char_end": 6, "text": "subref"}],
        np.array([[0.0, 1.0]]),
    )
    lsi._upsert_corpus_entry(tmp_path, "atlas-slug", atlas_m)
    lsi._upsert_corpus_entry(tmp_path, "sub-slug", sub_m)
    corpus = json.loads((tmp_path / "local_index" / "corpus.json").read_text())
    assert [p["role"] for p in corpus["papers"]] == ["atlas", "subatlas"]


# ---------------------------------------------------------------------------
# Migration from legacy single-paper layout
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_migration_moves_legacy_files(tmp_path: Path) -> None:
    idx = tmp_path / "local_index"
    (idx / "source").mkdir(parents=True)
    (idx / "chunks").mkdir()
    (idx / "snippet_index").mkdir()
    (idx / "source" / "paper.jats.xml").write_text("<article/>")
    (idx / "chunks" / "chunks.jsonl").write_text(
        '{"chunk_id":0,"section":"BODY","char_start":0,"char_end":3,"text":"abc"}\n'
    )
    np.save(idx / "chunks" / "embeddings.npy", np.array([[1.0, 0.0]]))
    (idx / "snippet_index" / "snippets.json").write_text("[]")
    legacy_manifest = {
        "version": 1,
        "doi": "10.1234/legacy",
        "hash": "abc",
        "embedding_model": lsi.EMBED_MODEL,
        "n_chunks": 1,
        "n_sentences": 0,
        "n_refs": 0,
        "n_corpus_ids_resolved": 0,
        "resolution_methods": {},
        "paper": {"title": "Legacy", "doi": "10.1234/legacy", "corpus_id": "CorpusId:local_x"},
    }
    (idx / "manifest.json").write_text(json.dumps(legacy_manifest))

    lsi._migrate_legacy_layout_if_needed(tmp_path)

    slug = lsi.paper_slug("10.1234/legacy")
    p_dir = idx / "papers" / slug
    assert p_dir.is_dir()
    assert (p_dir / "manifest.json").is_file()
    assert (p_dir / "source" / "paper.jats.xml").is_file()
    assert not (idx / "manifest.json").exists()
    assert (idx / "corpus.json").is_file()
    corpus = json.loads((idx / "corpus.json").read_text())
    assert corpus["atlas_doi"] == "10.1234/legacy"
    new_manifest = json.loads((p_dir / "manifest.json").read_text())
    assert new_manifest["role"] == "atlas"
    assert new_manifest["version"] == lsi.MANIFEST_VERSION


@pytest.mark.unit
def test_migration_idempotent(tmp_path: Path) -> None:
    # Run on a tree that already has corpus.json — should be a no-op.
    idx = tmp_path / "local_index"
    idx.mkdir(parents=True)
    (idx / "corpus.json").write_text(json.dumps(lsi._empty_corpus()))
    lsi._migrate_legacy_layout_if_needed(tmp_path)
    assert (idx / "corpus.json").exists()


# ---------------------------------------------------------------------------
# use_in_fanout flag
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_use_in_fanout_default_false(tmp_path: Path) -> None:
    idx = tmp_path / "local_index"
    idx.mkdir()
    (idx / "corpus.json").write_text(json.dumps(lsi._empty_corpus("10.1/x")))
    assert lsi.use_in_fanout(tmp_path) is False


@pytest.mark.unit
def test_use_in_fanout_true_when_flag_set(tmp_path: Path) -> None:
    idx = tmp_path / "local_index"
    idx.mkdir()
    corpus = lsi._empty_corpus("10.1/x")
    corpus["use_in_fanout"] = True
    (idx / "corpus.json").write_text(json.dumps(corpus))
    assert lsi.use_in_fanout(tmp_path) is True


@pytest.mark.unit
def test_needs_pdf_subatlas_lists_only_needs_pdf(tmp_path: Path) -> None:
    cfg = {
        "source": {
            "doi": "10.1/atlas",
            "subatlas_papers": [
                {"label": "Foo_et_al_2023_X", "doi": "10.1/a", "status": "asta"},
                {"label": "Bar_et_al_2024_Y", "doi": "10.1/b", "status": "needs_pdf"},
                {"label": "Baz_et_al_2024_Z", "doi": "", "status": "unresolved"},
            ],
        }
    }
    (tmp_path / "cell_type_annotations.json").write_text(json.dumps(cfg))
    missing = lsi.needs_pdf_subatlas(tmp_path)
    assert len(missing) == 1
    assert missing[0]["doi"] == "10.1/b"


# ---------------------------------------------------------------------------
# remove_paper + list_papers
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_remove_paper_drops_dir_and_corpus_entry(tmp_path: Path) -> None:
    doi = "10.1234/rm"
    slug = lsi.paper_slug(doi)
    m = _write_paper_files(
        tmp_path,
        slug,
        doi,
        "subatlas",
        [{"chunk_id": 0, "section": "BODY", "char_start": 0, "char_end": 3, "text": "abc"}],
        np.array([[1.0, 0.0]]),
    )
    lsi._upsert_corpus_entry(tmp_path, slug, m)
    assert (tmp_path / "local_index" / "papers" / slug).exists()
    removed = lsi.remove_paper(tmp_path, doi)
    assert removed is True
    assert not (tmp_path / "local_index" / "papers" / slug).exists()
    papers = lsi.list_papers(tmp_path)
    assert not any(p["doi"] == doi for p in papers)


# ---------------------------------------------------------------------------
# Multi-paper retrieval (filter by role, by paper)
# ---------------------------------------------------------------------------


class _FakeEmbedder:
    """Encodes a 'query' to a 2-d vector via simple keyword counting against
    a known token vocabulary. Used to make the search test deterministic
    without loading sentence-transformers."""

    def encode(self, texts, convert_to_numpy=True, show_progress_bar=False):  # noqa: D401
        out = []
        for t in texts:
            t_low = t.lower()
            out.append([float("atlas" in t_low), float("sub" in t_low)])
        return np.array(out)


@pytest.fixture
def multi_paper_project(tmp_path, monkeypatch):
    # Atlas paper: text matches the 'atlas' axis.
    _write_paper_files(
        tmp_path,
        "atlas-slug",
        "10.1234/atlas",
        "atlas",
        [
            {
                "chunk_id": 0,
                "section": "BODY",
                "char_start": 0,
                "char_end": 20,
                "text": "Atlas-specific content about cells",
            },
        ],
        np.array([[1.0, 0.0]]),
    )
    _write_paper_files(
        tmp_path,
        "sub-slug",
        "10.1234/sub",
        "subatlas",
        [
            {
                "chunk_id": 0,
                "section": "BODY",
                "char_start": 0,
                "char_end": 20,
                "text": "Sub-atlas reference content",
            },
        ],
        np.array([[0.0, 1.0]]),
    )
    # Manually write corpus.json (skips upsert reorder logic).
    corpus = lsi._empty_corpus("10.1234/atlas")
    corpus["papers"] = [
        {
            "slug": "atlas-slug",
            "doi": "10.1234/atlas",
            "role": "atlas",
            "source_type": "jats",
            "title": "Atlas",
            "n_chunks": 1,
        },
        {
            "slug": "sub-slug",
            "doi": "10.1234/sub",
            "role": "subatlas",
            "source_type": "pdf",
            "title": "Sub",
            "n_chunks": 1,
        },
    ]
    (tmp_path / "local_index" / "corpus.json").write_text(json.dumps(corpus))

    # Inject a fake sentence_transformers module so the optional [local-index]
    # dep is not required during unit tests.
    import sys
    import types

    fake_st = types.ModuleType("sentence_transformers")
    fake_st.SentenceTransformer = lambda *args, **kwargs: _FakeEmbedder()  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "sentence_transformers", fake_st)
    lsi._load_index.cache_clear()
    return tmp_path


@pytest.mark.unit
def test_search_returns_both_papers_default(multi_paper_project: Path) -> None:
    hits = lsi.search(multi_paper_project, "atlas sub", k=5)
    slugs = {h["paper_slug"] for h in hits}
    assert slugs == {"atlas-slug", "sub-slug"}


@pytest.mark.unit
def test_search_filter_by_role(multi_paper_project: Path) -> None:
    hits = lsi.search(multi_paper_project, "atlas sub", k=5, roles=["subatlas"])
    assert all(h["paper_role"] == "subatlas" for h in hits)
    assert all(h["paper_slug"] == "sub-slug" for h in hits)


@pytest.mark.unit
def test_search_filter_by_doi(multi_paper_project: Path) -> None:
    hits = lsi.search(multi_paper_project, "atlas sub", k=5, papers=["10.1234/atlas"])
    assert all(h["doi"] == "10.1234/atlas" for h in hits)


@pytest.mark.unit
def test_search_empty_corpus_returns_empty(tmp_path: Path) -> None:
    assert lsi.search(tmp_path, "anything", k=5) == []
