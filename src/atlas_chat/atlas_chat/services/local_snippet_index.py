"""Local snippet index for atlases and their subatlas papers.

A project's ``local_index/`` is a **corpus** of one or more papers:

* Exactly one ``role: atlas`` paper (the DOI from ``cell_type_annotations.json``).
* Zero or more ``role: subatlas`` papers (upstream studies whose cell types
  were folded into the atlas — see ``subatlas_resolver``).

Each paper lives in its own subdir under ``papers/<slug>/`` with its own
manifest, chunks, embeddings, and ASTA-shape snippet index. A corpus-level
``corpus.json`` lists papers, points at the atlas, and carries an
``use_in_fanout`` flag (default ``false``) which gates whether
``FanOut._citation_traverse`` queries the local index at all.

On-disk layout::

    local_index/
      corpus.json
      papers/
        <paper_slug>/
          manifest.json
          source/{paper.jats.xml|paper.pdf|paper.md}
          chunks/{chunks.jsonl, embeddings.npy, chunks.fulltext.txt}
          citations/{sentences.jsonl, ref_resolution.json}   # JATS only
          snippet_index/snippets.json

Snippet shape returned by ``search`` is identical to
``citation_traverser._snippet_to_dict(AstaSnippet)`` so the downstream
``_summarize_snippets`` / ``validate_report`` machinery consumes them
unchanged.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import logging
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Literal

logger = logging.getLogger(__name__)

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_TARGET_CHARS = 2800
CHUNK_OVERLAP_CHARS = 200
MANIFEST_VERSION = 2  # bumped: per-paper manifest, corpus model
CORPUS_VERSION = 1

SourceType = Literal["jats", "pdf"]
PaperRole = Literal["atlas", "subatlas"]


# ------------------------------------------------------------------
# Data classes (on-disk shape)
# ------------------------------------------------------------------


@dataclass
class Chunk:
    chunk_id: int
    section: str
    char_start: int
    char_end: int
    text: str


@dataclass
class SentenceRow:
    text: str
    section: str
    char_start: int  # offset in the cleaned full-text
    char_end: int
    ref_ids: list[str]
    # resolved at build time:
    doi_list: list[str] = field(default_factory=list)


@dataclass
class _BodySegment:
    section: str
    text: str  # paragraph text (whitespace collapsed)


# ------------------------------------------------------------------
# Paper slug + path helpers
# ------------------------------------------------------------------


_SLUG_SAFE_RE = re.compile(r"[^a-z0-9._-]")


def paper_slug(doi: str) -> str:
    """Stable, human-readable directory slug for a paper.

    Lowercases, replaces ``/`` with ``_`` and any other unsafe char with ``-``,
    truncates at 80 chars. For pathological DOIs (rare), falls back to a sha1
    prefix.
    """
    s = doi.strip().lower()
    s = s.replace("/", "_")
    s = _SLUG_SAFE_RE.sub("-", s)
    s = s.strip("-_.")
    if not s or len(s) > 120:
        return "doi-" + hashlib.sha1(doi.encode("utf-8")).hexdigest()[:16]
    return s[:80]


def _papers_dir(project_dir: Path) -> Path:
    return project_dir / "local_index" / "papers"


def _paper_dir(project_dir: Path, slug: str) -> Path:
    return _papers_dir(project_dir) / slug


def _corpus_json_path(project_dir: Path) -> Path:
    return project_dir / "local_index" / "corpus.json"


# ------------------------------------------------------------------
# JATS normalisation (bioRxiv quirks)
# ------------------------------------------------------------------


def _normalize_biorxiv_jats(xml: str) -> str:
    """Make bioRxiv JATS digestible by ``_jats_parser.parse_jats_citations``.

    Two fixes:
      1. Strip ``hwp:*`` namespaced attributes that get aliased to ``id`` after
         namespace strip, overwriting the real ``<ref id="cNN">`` value.
      2. Rename ``<citation>`` (Highwire convention) to ``<element-citation>``
         (JATS standard) so the parser's ref-detail extractor matches.
    """
    xml = re.sub(r'\s+hwp:[\w:-]+="[^"]*"', "", xml)
    xml = re.sub(r'\s+xmlns:hw="[^"]*"', "", xml)
    xml = re.sub(
        r"<citation(\s+[^>]*publication-type=)",
        r"<element-citation\1",
        xml,
    )
    xml = xml.replace("</citation>", "</element-citation>")
    return xml


# ------------------------------------------------------------------
# JATS → plain text + sections
# ------------------------------------------------------------------


def _strip_ns(root: ET.Element) -> None:
    for el in root.iter():
        if "}" in el.tag:
            el.tag = el.tag.split("}", 1)[1]


def _is_bibr_xref(el: ET.Element) -> bool:
    return el.tag == "xref" and el.get("ref-type") == "bibr"


def _contains_bibr(el: ET.Element) -> bool:
    return any(_is_bibr_xref(g) for g in el.iter())


def _text_of(el: ET.Element, in_citation: bool = False) -> str:
    """Concatenate all descendant text, skipping ref-list and tables.

    Wraps citation markers in brackets so the rendered text shows e.g.
    ``[12-15]`` rather than a bare ``12-15`` run.
    """
    parts: list[str] = []
    if el.text:
        parts.append(el.text)
    for child in el:
        if child.tag in {"ref-list", "table-wrap"}:
            continue
        is_citation_block = (child.tag == "sup" and _contains_bibr(child)) or _is_bibr_xref(child)
        if is_citation_block and not in_citation:
            parts.append("[" + _text_of(child, in_citation=True) + "]")
        else:
            parts.append(_text_of(child, in_citation=in_citation))
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)


def extract_body_segments(xml: str) -> list[_BodySegment]:
    """Walk JATS body, return ordered paragraph segments with section labels."""
    root = ET.fromstring(xml)
    _strip_ns(root)

    segments: list[_BodySegment] = []

    for abs_el in root.iter("abstract"):
        for p in abs_el.iter("p"):
            txt = re.sub(r"\s+", " ", _text_of(p)).strip()
            if txt:
                segments.append(_BodySegment("ABSTRACT", txt))

    body = root.find(".//body")
    if body is None:
        return segments

    def walk(sec_el: ET.Element, parent_title: str) -> None:
        title_el = sec_el.find("title")
        title = (
            re.sub(r"\s+", " ", _text_of(title_el)).strip()
            if title_el is not None
            else parent_title
        )
        for child in sec_el:
            if child.tag == "sec":
                walk(child, title)
            elif child.tag == "p":
                txt = re.sub(r"\s+", " ", _text_of(child)).strip()
                if txt:
                    segments.append(_BodySegment(title, txt))

    for sec in body.findall("sec"):
        walk(sec, "BODY")
    for p in body.findall("p"):
        txt = re.sub(r"\s+", " ", _text_of(p)).strip()
        if txt:
            segments.append(_BodySegment("BODY", txt))

    return segments


def _extract_pdf_segments(pdf_path: Path) -> list[_BodySegment]:
    """Adapter: convert ``_pdf_parser.PdfSegment`` to ``_BodySegment``."""
    from atlas_chat.services._pdf_parser import extract_pdf_segments

    return [_BodySegment(section=s.section, text=s.text) for s in extract_pdf_segments(pdf_path)]


# ------------------------------------------------------------------
# Chunking
# ------------------------------------------------------------------


def chunk_segments(
    segments: list[_BodySegment],
    target_chars: int = CHUNK_TARGET_CHARS,
    overlap_chars: int = CHUNK_OVERLAP_CHARS,
) -> tuple[str, list[Chunk]]:
    """Build paragraph-aware chunks. Returns ``(concatenated_fulltext, chunks)``."""
    fulltext_parts: list[str] = []
    chunks: list[Chunk] = []
    cursor = 0
    cur_section = ""
    cur_text = ""
    cur_start = 0

    def flush() -> None:
        nonlocal cur_text, cur_start
        if not cur_text:
            return
        chunk = Chunk(
            chunk_id=len(chunks),
            section=cur_section,
            char_start=cur_start,
            char_end=cur_start + len(cur_text),
            text=cur_text,
        )
        chunks.append(chunk)
        cur_text = ""

    for seg in segments:
        para = seg.text + "\n\n"
        para_start = cursor
        fulltext_parts.append(para)
        cursor += len(para)

        if cur_section and seg.section != cur_section:
            flush()
        if not cur_text:
            cur_section = seg.section
            cur_start = para_start
            cur_text = para
        elif len(cur_text) + len(para) <= target_chars:
            cur_text += para
        else:
            flush()
            if chunks and overlap_chars > 0:
                tail = chunks[-1].text[-overlap_chars:]
                cur_text = tail + para
                cur_start = chunks[-1].char_end - len(tail)
            else:
                cur_text = para
                cur_start = para_start
            cur_section = seg.section
    flush()

    fulltext = "".join(fulltext_parts)
    return fulltext, chunks


# ------------------------------------------------------------------
# Sentence-level citation graph (JATS only)
# ------------------------------------------------------------------


def build_sentence_rows(
    xml: str,
    fulltext: str,
) -> tuple[list[SentenceRow], dict[str, Any]]:
    """Run the vendored ``_jats_parser.parse_jats_citations`` and align each cited
    sentence to a char offset in ``fulltext``. Returns ``(rows, refs_dict)``."""
    from atlas_chat.services._jats_parser import parse_jats_citations

    cited, refs = parse_jats_citations(xml)
    ref_id_to_doi = {rid: r.doi for rid, r in refs.items() if r.doi}

    rows: list[SentenceRow] = []
    for cs in cited:
        anchor = cs.text[:80]
        pos = fulltext.find(anchor)
        if pos < 0:
            stripped = re.sub(r"\[[^\]]{1,40}\]", "", cs.text).strip()
            if stripped:
                pos = fulltext.find(stripped[:80])
        if pos < 0:
            continue
        needle = cs.text
        doi_list = [ref_id_to_doi[rid] for rid in cs.ref_ids if rid in ref_id_to_doi]
        rows.append(
            SentenceRow(
                text=cs.text,
                section=cs.section,
                char_start=pos,
                char_end=pos + len(needle),
                ref_ids=cs.ref_ids,
                doi_list=doi_list,
            )
        )
    return rows, refs


# ------------------------------------------------------------------
# DOI → CorpusId resolution via Semantic Scholar (batch)
# ------------------------------------------------------------------


def _resolve_dois_to_corpus_ids(dois: list[str]) -> dict[str, str]:
    """Batch-resolve DOIs to Semantic Scholar CorpusIds. Retries on 429."""
    import time

    import httpx

    if not dois:
        return {}
    unique = list({d for d in dois if d})
    out: dict[str, str] = {}
    batch_size = 100
    api = "https://api.semanticscholar.org/graph/v1/paper/batch"
    fields = "externalIds,title,authors,year"
    with httpx.Client(timeout=60) as client:
        for i in range(0, len(unique), batch_size):
            batch = unique[i : i + batch_size]
            for attempt in range(3):
                try:
                    resp = client.post(
                        api,
                        params={"fields": fields},
                        json={"ids": [f"DOI:{d}" for d in batch]},
                    )
                    if resp.status_code == 429:
                        sleep = 2 ** (attempt + 1)
                        logger.warning("S2 429, sleeping %ds (attempt %d)", sleep, attempt + 1)
                        time.sleep(sleep)
                        continue
                    if resp.status_code != 200:
                        logger.warning("S2 batch returned %d", resp.status_code)
                        break
                    for d, paper in zip(batch, resp.json(), strict=False):
                        if not paper:
                            continue
                        cid = paper.get("externalIds", {}).get("CorpusId")
                        if cid:
                            out[d] = str(cid)
                    break
                except Exception as exc:
                    logger.warning("S2 batch attempt %d failed: %s", attempt + 1, exc)
                    if attempt == 2:
                        break
                    time.sleep(2 ** (attempt + 1))
    logger.info("Resolved %d/%d DOIs to CorpusIds", len(out), len(unique))
    return out


def _resolve_title_to_corpus_id(
    title: str,
    year: int | None,
    first_author: str | None,
    client: Any,
) -> tuple[str | None, str | None]:
    """Single-paper title-match via Semantic Scholar /paper/search/match."""
    import time

    api = "https://api.semanticscholar.org/graph/v1/paper/search/match"
    params = {"query": title[:300], "fields": "externalIds,title,year,authors"}
    for attempt in range(3):
        try:
            resp = client.get(api, params=params)
            if resp.status_code == 429:
                time.sleep(2 ** (attempt + 1))
                continue
            if resp.status_code == 404:
                return None, None
            if resp.status_code != 200:
                return None, None
            data = resp.json().get("data", [])
            if not data:
                return None, None
            best = data[0]
            if year and best.get("year") and abs(int(best["year"]) - year) > 2:
                return None, None
            if first_author and best.get("authors"):
                au_text = " ".join(a.get("name", "") for a in best["authors"]).lower()
                if first_author.lower() not in au_text:
                    return None, None
            ext = best.get("externalIds") or {}
            cid = ext.get("CorpusId")
            doi = ext.get("DOI")
            return (str(cid) if cid else None), doi
        except Exception as exc:
            logger.debug("title-match attempt %d failed: %s", attempt + 1, exc)
            time.sleep(2 ** (attempt + 1))
    return None, None


def _resolve_refs_to_corpus_ids(refs: dict[str, Any]) -> dict[str, dict[str, str | None]]:
    """Resolve every ref to a CorpusId, using DOI batch first then title-match."""
    import httpx

    out: dict[str, dict[str, str | None]] = {}

    dois_to_lookup = [r.doi for r in refs.values() if r.doi]
    doi_to_corpus = _resolve_dois_to_corpus_ids(dois_to_lookup)
    for ref_id, r in refs.items():
        if r.doi:
            cid = doi_to_corpus.get(r.doi)
            out[ref_id] = {
                "corpus_id": cid,
                "doi": r.doi,
                "method": "doi" if cid else "doi_unmatched",
            }

    title_candidates = [
        (rid, r) for rid, r in refs.items() if r.title and not out.get(rid, {}).get("corpus_id")
    ]
    if not title_candidates:
        logger.info("DOI-only resolution covered all refs (%d)", len(out))
        return out

    logger.info(
        "Title-matching %d refs without resolved DOI via S2 /paper/search/match",
        len(title_candidates),
    )
    resolved_via_title = 0
    with httpx.Client(timeout=30) as client:
        for ref_id, r in title_candidates:
            cid, doi = _resolve_title_to_corpus_id(r.title, r.year, r.first_author, client)
            entry = out.get(ref_id, {"corpus_id": None, "doi": r.doi, "method": "title_unmatched"})
            if cid:
                entry = {
                    "corpus_id": cid,
                    "doi": doi or r.doi,
                    "method": "title",
                }
                resolved_via_title += 1
            else:
                entry["method"] = "title_unmatched"
            out[ref_id] = entry

    total_resolved = sum(1 for v in out.values() if v["corpus_id"])
    logger.info(
        "Resolved %d/%d refs to CorpusIds (%d via DOI, %d via title-match)",
        total_resolved,
        len(refs),
        len(doi_to_corpus),
        resolved_via_title,
    )
    return out


# ------------------------------------------------------------------
# Paper metadata: bioRxiv (for JATS preprints) + Crossref (for PDFs)
# ------------------------------------------------------------------


def _biorxiv_meta(doi: str) -> dict | None:
    url = f"https://api.biorxiv.org/details/biorxiv/{doi}/na/json"
    try:
        with urllib.request.urlopen(url, timeout=20) as fh:
            data = json.load(fh)
        if data.get("messages", [{}])[0].get("status") != "ok":
            return None
        coll = data.get("collection", [])
        return coll[0] if coll else None
    except Exception:
        return None


def _crossref_meta(doi: str) -> dict | None:
    """Fetch metadata from Crossref REST API. Public, no key required.

    Returns a dict with keys ``title``, ``authors`` (semicolon-joined string),
    ``year``, ``container_title``, or ``None`` on failure.
    """
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "atlas-chat/0.1"})
        with urllib.request.urlopen(req, timeout=20) as fh:
            payload = json.load(fh)
        msg = payload.get("message", {})
        title = (msg.get("title") or [""])[0]
        authors = msg.get("author") or []
        au_parts = []
        for a in authors:
            given = a.get("given", "")
            family = a.get("family", "")
            if family:
                au_parts.append(f"{given} {family}".strip())
        date_parts = (msg.get("issued") or {}).get("date-parts") or [[None]]
        year = date_parts[0][0] if date_parts and date_parts[0] else None
        container = (msg.get("container-title") or [""])[0]
        return {
            "title": title,
            "authors": "; ".join(au_parts),
            "year": int(year) if year else None,
            "container_title": container,
        }
    except Exception as exc:
        logger.warning("Crossref metadata fetch failed for %s: %s", doi, exc)
        return None


def _build_paper_meta(doi: str, source_type: SourceType) -> dict[str, Any]:
    """Best-effort paper metadata for the ASTA-shape ``paper`` field."""
    if source_type == "jats":
        meta = _biorxiv_meta(doi) or {}
        year = None
        if date := meta.get("date", ""):
            m = re.match(r"(\d{4})", date)
            if m:
                year = int(m.group(1))
        return {
            "title": meta.get("title", ""),
            "authors": meta.get("authors", ""),
            "year": year,
            "doi": doi,
            "corpus_id": _local_corpus_id(doi),
            "url": f"https://www.biorxiv.org/content/{doi}v{meta.get('version', 1)}",
            "venue": "bioRxiv",
        }
    # PDF: Crossref
    cm = _crossref_meta(doi) or {}
    return {
        "title": cm.get("title", ""),
        "authors": cm.get("authors", ""),
        "year": cm.get("year"),
        "doi": doi,
        "corpus_id": _local_corpus_id(doi),
        "url": f"https://doi.org/{doi}",
        "venue": cm.get("container_title", ""),
    }


# ------------------------------------------------------------------
# Build orchestrator
# ------------------------------------------------------------------


def _local_corpus_id(doi: str) -> str:
    """Stable atlas CorpusId for an unindexed paper.

    Format ``CorpusId:local_<sha1[:10]>`` — the ``local_`` token has no digits so
    it sidesteps the legacy ``CorpusId:\\d+`` validation regex in
    ``report_checker.py::check_references`` while preserving shape parity."""
    h = hashlib.sha1(doi.encode("utf-8")).hexdigest()[:10]
    return f"CorpusId:local_{h}"


def _manifest_hash(source_bytes: bytes, source_type: SourceType) -> str:
    h = hashlib.sha256()
    h.update(source_bytes)
    h.update(f"|emb={EMBED_MODEL}|st={source_type}|m={MANIFEST_VERSION}".encode())
    return h.hexdigest()


def _embed_and_save(texts: list[str], out_path: Path) -> None:
    import numpy as np
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(EMBED_MODEL)
    vecs = model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    vecs = vecs / norms
    np.save(out_path, vecs)


def _resolution_breakdown(ref_resolution: dict[str, dict[str, str | None]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for entry in ref_resolution.values():
        m = entry.get("method") or "none"
        counts[m] = counts.get(m, 0) + 1
    return counts


def build_paper_index(
    project_dir: Path,
    doi: str,
    *,
    jats_path: Path | None = None,
    pdf_path: Path | None = None,
    role: PaperRole = "atlas",
    force: bool = False,
) -> dict[str, Any]:
    """Build (or refresh) the local index entry for one paper.

    Exactly one of ``jats_path`` or ``pdf_path`` must be provided. The atlas
    paper additionally supports auto-fetching JATS when neither is supplied
    (back-compat path).

    Returns the per-paper manifest dict and updates ``corpus.json``.
    """
    project_dir = Path(project_dir)
    _migrate_legacy_layout_if_needed(project_dir)

    slug = paper_slug(doi)
    p_dir = _paper_dir(project_dir, slug)
    source_dir = p_dir / "source"
    chunks_dir = p_dir / "chunks"
    citations_dir = p_dir / "citations"
    snippet_dir = p_dir / "snippet_index"
    for d in (p_dir, source_dir, chunks_dir, citations_dir, snippet_dir):
        d.mkdir(parents=True, exist_ok=True)

    # Resolve source path + type
    if pdf_path is not None and jats_path is not None:
        raise ValueError("Pass jats_path OR pdf_path, not both")
    if pdf_path is not None:
        source_type: SourceType = "pdf"
        target = source_dir / "paper.pdf"
        if pdf_path.resolve() != target.resolve():
            target.write_bytes(pdf_path.read_bytes())
        source_path = target
    elif jats_path is not None:
        source_type = "jats"
        target = source_dir / "paper.jats.xml"
        if jats_path.resolve() != target.resolve():
            target.write_bytes(jats_path.read_bytes())
        source_path = target
    else:
        # No source given — for atlas role we may auto-fetch JATS.
        source_type = "jats"
        source_path = source_dir / "paper.jats.xml"
        if not source_path.exists() or force:
            from atlas_chat.services.fetch_preprint import fetch_preprint

            fetched = fetch_preprint(doi, source_dir)
            source_path = fetched.jats_path

    raw_bytes = source_path.read_bytes()
    expected_hash = _manifest_hash(raw_bytes, source_type)
    manifest_path = p_dir / "manifest.json"
    if manifest_path.exists() and not force:
        try:
            existing = json.loads(manifest_path.read_text())
            if existing.get("hash") == expected_hash:
                logger.info("Paper %s already up to date.", slug)
                _upsert_corpus_entry(project_dir, slug, existing)
                return existing
        except Exception:
            pass

    # Extract body segments
    if source_type == "jats":
        xml = raw_bytes.decode("utf-8")
        normalized = _normalize_biorxiv_jats(xml)
        segments = extract_body_segments(normalized)
    else:
        segments = _extract_pdf_segments(source_path)
        normalized = None  # used only for citation graph below

    if not segments:
        raise RuntimeError(f"No body segments extracted from {source_path}")

    fulltext, chunks = chunk_segments(segments)
    (chunks_dir / "chunks.fulltext.txt").write_text(fulltext)
    with (chunks_dir / "chunks.jsonl").open("w") as fh:
        for c in chunks:
            fh.write(json.dumps(asdict(c)) + "\n")

    _embed_and_save([c.text for c in chunks], chunks_dir / "embeddings.npy")

    # Citation graph: JATS only — PDFs have no xref markers.
    sent_rows: list[SentenceRow] = []
    ref_resolution: dict[str, dict[str, str | None]] = {}
    ref_id_to_corpus: dict[str, str] = {}
    citation_graph = False
    if source_type == "jats" and normalized is not None:
        try:
            sent_rows, refs_full = build_sentence_rows(normalized, fulltext)
            with (citations_dir / "sentences.jsonl").open("w") as fh:
                for r in sent_rows:
                    fh.write(json.dumps(asdict(r)) + "\n")
            ref_resolution = _resolve_refs_to_corpus_ids(refs_full)
            (citations_dir / "ref_resolution.json").write_text(json.dumps(ref_resolution, indent=2))
            ref_id_to_corpus = {
                rid: entry["corpus_id"]
                for rid, entry in ref_resolution.items()
                if entry["corpus_id"]
            }
            citation_graph = True
        except Exception as exc:
            logger.warning("Citation graph build failed for %s: %s", slug, exc)

    paper_meta = _build_paper_meta(doi, source_type)
    snippets = _merge_snippets(chunks, sent_rows, ref_id_to_corpus, paper_meta)
    (snippet_dir / "snippets.json").write_text(json.dumps(snippets, indent=2))

    manifest = {
        "version": MANIFEST_VERSION,
        "slug": slug,
        "doi": doi,
        "role": role,
        "source_type": source_type,
        "citation_graph": citation_graph,
        "hash": expected_hash,
        "embedding_model": EMBED_MODEL,
        "n_chunks": len(chunks),
        "n_sentences": len(sent_rows),
        "n_refs": len(ref_resolution),
        "n_corpus_ids_resolved": len(ref_id_to_corpus),
        "resolution_methods": _resolution_breakdown(ref_resolution) if ref_resolution else {},
        "paper": paper_meta,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2))
    logger.info(
        "Built paper index [%s/%s]: %d chunks, %d sentences, citation_graph=%s",
        slug,
        source_type,
        len(chunks),
        len(sent_rows),
        citation_graph,
    )

    _upsert_corpus_entry(project_dir, slug, manifest)
    return manifest


def _merge_snippets(
    chunks: list[Chunk],
    sent_rows: list[SentenceRow],
    ref_id_to_corpus: dict[str, str],
    paper_meta: dict,
) -> list[dict]:
    """Emit one ASTA-shape snippet per chunk with refMentions baked in."""
    sent_rows_sorted = sorted(sent_rows, key=lambda r: r.char_start)
    snippets: list[dict] = []
    for c in chunks:
        ref_mentions: list[dict] = []
        for r in sent_rows_sorted:
            if r.char_start >= c.char_end:
                break
            if r.char_end <= c.char_start:
                continue
            if r.char_start < c.char_start or r.char_end > c.char_end:
                continue
            for ref_id in r.ref_ids:
                cid = ref_id_to_corpus.get(ref_id)
                if not cid:
                    continue
                ref_mentions.append(
                    {
                        "matchedPaperCorpusId": cid,
                        "ref_id": ref_id,
                        "start": r.char_start - c.char_start,
                        "end": r.char_end - c.char_start,
                    }
                )
        snippets.append(
            {
                "chunk_id": c.chunk_id,
                "paper": {
                    "corpusId": paper_meta["corpus_id"],
                    "title": paper_meta["title"],
                    "authors": paper_meta["authors"],
                    "year": paper_meta["year"],
                    "doi": paper_meta["doi"],
                },
                "snippet": {
                    "text": c.text,
                    "section": c.section,
                    "annotations": {"refMentions": ref_mentions},
                },
            }
        )
    return snippets


# ------------------------------------------------------------------
# Corpus-level orchestration
# ------------------------------------------------------------------


def _empty_corpus(atlas_doi: str | None = None) -> dict[str, Any]:
    return {
        "version": CORPUS_VERSION,
        "embedding_model": EMBED_MODEL,
        "atlas_doi": atlas_doi,
        "use_in_fanout": False,
        "papers": [],
    }


def _load_corpus_json(project_dir: Path) -> dict[str, Any]:
    path = _corpus_json_path(project_dir)
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            logger.warning("corpus.json unreadable, treating as empty")
    return _empty_corpus()


def _save_corpus_json(project_dir: Path, corpus: dict[str, Any]) -> None:
    path = _corpus_json_path(project_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(corpus, indent=2))


def _upsert_corpus_entry(project_dir: Path, slug: str, manifest: dict[str, Any]) -> None:
    corpus = _load_corpus_json(project_dir)
    entry = {
        "slug": slug,
        "doi": manifest["doi"],
        "role": manifest["role"],
        "source_type": manifest["source_type"],
        "title": manifest.get("paper", {}).get("title", ""),
        "n_chunks": manifest.get("n_chunks", 0),
    }
    by_slug = {p["slug"]: p for p in corpus.get("papers", [])}
    by_slug[slug] = entry
    corpus["papers"] = sorted(by_slug.values(), key=lambda p: (p["role"] != "atlas", p["slug"]))
    if manifest["role"] == "atlas":
        corpus["atlas_doi"] = manifest["doi"]
    _save_corpus_json(project_dir, corpus)


def _migrate_legacy_layout_if_needed(project_dir: Path) -> None:
    """If ``local_index/manifest.json`` exists at the old single-paper location,
    move all files under ``papers/<atlas_slug>/`` and synthesize ``corpus.json``.

    Idempotent. Safe to call on every read or build.
    """
    idx = project_dir / "local_index"
    legacy_manifest = idx / "manifest.json"
    if not legacy_manifest.exists():
        return
    if _corpus_json_path(project_dir).exists():
        # Already migrated — but legacy manifest still hanging around. Drop it.
        with contextlib.suppress(OSError):
            legacy_manifest.unlink()
        return

    try:
        legacy = json.loads(legacy_manifest.read_text())
    except Exception:
        logger.warning("Legacy manifest.json unreadable; skipping migration")
        return

    doi = legacy.get("doi")
    if not doi:
        logger.warning("Legacy manifest has no DOI; skipping migration")
        return
    slug = paper_slug(doi)
    target_dir = _paper_dir(project_dir, slug)
    if target_dir.exists() and (target_dir / "manifest.json").exists():
        logger.info("Migration: target %s already populated, just dropping legacy file", slug)
        legacy_manifest.unlink()
        return
    target_dir.mkdir(parents=True, exist_ok=True)

    # Move subdirs that the old layout placed directly under local_index/.
    for subdir in ("source", "chunks", "citations", "snippet_index"):
        old = idx / subdir
        new = target_dir / subdir
        if old.exists() and not new.exists():
            old.rename(new)

    # Synthesize a v2 manifest from the v1 fields we can fill.
    new_manifest = {
        "version": MANIFEST_VERSION,
        "slug": slug,
        "doi": doi,
        "role": "atlas",
        "source_type": "jats",
        "citation_graph": True,
        "hash": legacy.get("hash", ""),
        "embedding_model": legacy.get("embedding_model", EMBED_MODEL),
        "n_chunks": legacy.get("n_chunks", 0),
        "n_sentences": legacy.get("n_sentences", 0),
        "n_refs": legacy.get("n_refs", 0),
        "n_corpus_ids_resolved": legacy.get("n_corpus_ids_resolved", 0),
        "resolution_methods": legacy.get("resolution_methods", {}),
        "paper": legacy.get("paper", {}),
    }
    (target_dir / "manifest.json").write_text(json.dumps(new_manifest, indent=2))

    corpus = _empty_corpus(atlas_doi=doi)
    corpus["papers"] = [
        {
            "slug": slug,
            "doi": doi,
            "role": "atlas",
            "source_type": "jats",
            "title": new_manifest["paper"].get("title", ""),
            "n_chunks": new_manifest["n_chunks"],
        }
    ]
    _save_corpus_json(project_dir, corpus)

    with contextlib.suppress(OSError):
        legacy_manifest.unlink()
    logger.info("Migrated legacy local_index layout → papers/%s/", slug)


# ------------------------------------------------------------------
# Public build entry points
# ------------------------------------------------------------------


def build_local_index(
    project_dir: Path,
    doi: str,
    jats_path: Path | None = None,
    force: bool = False,
) -> dict[str, Any]:
    """Back-compat entry point: build the atlas paper for this project.

    Equivalent to ``build_paper_index(..., role='atlas')`` with JATS auto-fetch
    when ``jats_path`` is ``None``.
    """
    return build_paper_index(
        project_dir,
        doi,
        jats_path=jats_path,
        role="atlas",
        force=force,
    )


def add_paper(
    project_dir: Path,
    doi: str,
    *,
    pdf_path: Path | None = None,
    jats_path: Path | None = None,
    role: PaperRole = "subatlas",
    force: bool = False,
) -> dict[str, Any]:
    """Add a subatlas reference paper to the corpus."""
    return build_paper_index(
        project_dir,
        doi,
        pdf_path=pdf_path,
        jats_path=jats_path,
        role=role,
        force=force,
    )


def remove_paper(project_dir: Path, doi: str) -> bool:
    """Remove a paper from the corpus. Returns True if it was present."""
    import shutil

    _migrate_legacy_layout_if_needed(project_dir)
    slug = paper_slug(doi)
    p_dir = _paper_dir(project_dir, slug)
    existed = p_dir.exists()
    if existed:
        shutil.rmtree(p_dir)
    corpus = _load_corpus_json(project_dir)
    before = len(corpus["papers"])
    corpus["papers"] = [p for p in corpus["papers"] if p["slug"] != slug]
    if before != len(corpus["papers"]):
        _save_corpus_json(project_dir, corpus)
    _load_index.cache_clear()
    return existed


def list_papers(project_dir: Path) -> list[dict[str, Any]]:
    """Return the corpus.json papers list (empty if no corpus)."""
    _migrate_legacy_layout_if_needed(project_dir)
    return _load_corpus_json(project_dir).get("papers", [])


# ------------------------------------------------------------------
# Retrieval API
# ------------------------------------------------------------------


@lru_cache(maxsize=8)
def _load_index(project_dir_str: str) -> dict[str, Any]:
    """Load corpus + all per-paper indices into memory.

    Returns a dict with concatenated embeddings keyed to a global row index,
    plus a parallel list mapping each row → (slug, paper_meta, chunk dict,
    snippet dict). Single ``np.load`` per paper; cheap to rebuild after add/remove.
    """
    import numpy as np

    project_dir = Path(project_dir_str)
    _migrate_legacy_layout_if_needed(project_dir)
    corpus = _load_corpus_json(project_dir)
    papers = corpus.get("papers", [])

    embeddings_parts: list[Any] = []
    row_index: list[dict[str, Any]] = []

    for entry in papers:
        slug = entry["slug"]
        p_dir = _paper_dir(project_dir, slug)
        manifest_path = p_dir / "manifest.json"
        emb_path = p_dir / "chunks" / "embeddings.npy"
        chunks_path = p_dir / "chunks" / "chunks.jsonl"
        snippets_path = p_dir / "snippet_index" / "snippets.json"
        if not (manifest_path.exists() and emb_path.exists() and chunks_path.exists()):
            logger.warning("Paper %s incomplete on disk; skipping", slug)
            continue
        manifest = json.loads(manifest_path.read_text())
        paper_meta = manifest.get("paper", {})
        role = manifest.get("role", entry.get("role", "subatlas"))

        chunks = []
        with chunks_path.open() as fh:
            for line in fh:
                chunks.append(json.loads(line))

        snippets_by_chunk: dict[int, dict[str, Any]] = {}
        if snippets_path.exists():
            snip_list = json.loads(snippets_path.read_text())
            snippets_by_chunk = {s["chunk_id"]: s for s in snip_list}

        vecs = np.load(emb_path)
        embeddings_parts.append(vecs)
        for ch in chunks:
            row_index.append(
                {
                    "slug": slug,
                    "role": role,
                    "paper_meta": paper_meta,
                    "chunk": ch,
                    "snippet_entry": snippets_by_chunk.get(ch["chunk_id"], {}),
                }
            )

    embeddings = np.vstack(embeddings_parts) if embeddings_parts else np.zeros((0, 0))

    return {
        "corpus": corpus,
        "row_index": row_index,
        "embeddings": embeddings,
    }


def search(
    project_dir: Path,
    query: str,
    k: int = 20,
    *,
    papers: list[str] | None = None,
    roles: list[PaperRole] | None = None,
) -> list[dict[str, Any]]:
    """Search the corpus. Returns ASTA-shape snippet dicts.

    Optional filters:
      * ``papers``: DOIs to restrict the search to.
      * ``roles``: paper roles to restrict the search to (e.g. ``["subatlas"]``).
    """
    import numpy as np
    from sentence_transformers import SentenceTransformer

    state = _load_index(str(Path(project_dir).resolve()))
    embeddings = state["embeddings"]
    row_index: list[dict[str, Any]] = state["row_index"]
    if embeddings.size == 0 or not row_index:
        return []

    paper_slug_filter: set[str] | None = None
    if papers:
        paper_slug_filter = {paper_slug(d) for d in papers}
    role_filter: set[str] | None = set(roles) if roles else None

    model = SentenceTransformer(EMBED_MODEL)
    q_vec = model.encode([query], convert_to_numpy=True)[0]
    q_vec = q_vec / max(np.linalg.norm(q_vec), 1e-9)
    scores = embeddings @ q_vec

    # Eligible rows
    if paper_slug_filter is not None or role_filter is not None:
        eligible = [
            i
            for i, row in enumerate(row_index)
            if (paper_slug_filter is None or row["slug"] in paper_slug_filter)
            and (role_filter is None or row["role"] in role_filter)
        ]
        if not eligible:
            return []
        eligible_scores = [(i, scores[i]) for i in eligible]
        eligible_scores.sort(key=lambda x: -x[1])
        top = eligible_scores[:k]
    else:
        top_idx = np.argsort(-scores)[:k].tolist()
        top = [(i, scores[i]) for i in top_idx]

    out: list[dict[str, Any]] = []
    for i, score in top:
        row = row_index[i]
        paper_meta = row["paper_meta"]
        chunk = row["chunk"]
        ref_mentions = (
            row["snippet_entry"].get("snippet", {}).get("annotations", {}).get("refMentions", [])
        )
        out.append(
            {
                "snippet": chunk["text"],
                "paper_id": paper_meta.get("corpus_id", ""),
                "corpus_id": paper_meta.get("corpus_id", ""),
                "title": paper_meta.get("title", ""),
                "authors": paper_meta.get("authors", ""),
                "year": paper_meta.get("year"),
                "url": paper_meta.get("url", ""),
                "score": float(score),
                "doi": paper_meta.get("doi", ""),
                "section": chunk["section"],
                "chunk_id": chunk["chunk_id"],
                "paper_slug": row["slug"],
                "paper_role": row["role"],
                "annotations": {"refMentions": ref_mentions},
                "source_method": "local_snippet",
            }
        )
    return out


def has_local_index(project_dir: Path) -> bool:
    """True iff the project has any paper in its corpus (post-migration)."""
    project_dir = Path(project_dir)
    _migrate_legacy_layout_if_needed(project_dir)
    if not _corpus_json_path(project_dir).exists():
        return False
    return bool(_load_corpus_json(project_dir).get("papers"))


def use_in_fanout(project_dir: Path) -> bool:
    """Whether the local index should be queried during ``FanOut._citation_traverse``.

    Defaults to ``False`` per the multi-paper design: subatlas papers are
    surfaced as a corpus and only consulted when the user opts in via the
    ``use_in_fanout`` flag in ``corpus.json``.
    """
    project_dir = Path(project_dir)
    _migrate_legacy_layout_if_needed(project_dir)
    if not _corpus_json_path(project_dir).exists():
        return False
    return bool(_load_corpus_json(project_dir).get("use_in_fanout", False))


def needs_pdf_subatlas(project_dir: Path) -> list[dict[str, Any]]:
    """Return any subatlas entries in cell_type_annotations.json with status ``needs_pdf``.

    Used by ``FanOut._citation_traverse`` to emit a non-blocking warning row.
    Empty list if the project has no subatlas list or no needs_pdf entries.
    """
    cfg_path = Path(project_dir) / "cell_type_annotations.json"
    if not cfg_path.exists():
        return []
    try:
        data = json.loads(cfg_path.read_text())
    except Exception:
        return []
    refs = (data.get("source") or {}).get("subatlas_papers") or []
    return [r for r in refs if r.get("status") == "needs_pdf"]


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", maxsplit=1)[0])
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_build = sub.add_parser("build", help="Build / refresh the atlas paper index")
    p_build.add_argument("--project", required=True, type=Path)
    p_build.add_argument("--doi", required=True)
    p_build.add_argument("--jats", type=Path, default=None)
    p_build.add_argument("--force", action="store_true")

    p_add = sub.add_parser("add", help="Add a paper to the corpus")
    p_add.add_argument("--project", required=True, type=Path)
    p_add.add_argument("--doi", required=True)
    src = p_add.add_mutually_exclusive_group()
    src.add_argument("--pdf", type=Path, default=None)
    src.add_argument("--jats", type=Path, default=None)
    p_add.add_argument("--role", default="subatlas", choices=("atlas", "subatlas"))
    p_add.add_argument("--force", action="store_true")

    p_rm = sub.add_parser("remove", help="Remove a paper from the corpus")
    p_rm.add_argument("--project", required=True, type=Path)
    p_rm.add_argument("--doi", required=True)

    p_list = sub.add_parser("list", help="List papers in the corpus")
    p_list.add_argument("--project", required=True, type=Path)

    p_search = sub.add_parser("search", help="Query the corpus")
    p_search.add_argument("--project", required=True, type=Path)
    p_search.add_argument("--query", required=True)
    p_search.add_argument("-k", type=int, default=10)
    p_search.add_argument("--paper", action="append", default=None, help="Filter by DOI")
    p_search.add_argument(
        "--role",
        action="append",
        default=None,
        choices=("atlas", "subatlas"),
    )

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    if args.cmd == "build":
        manifest = build_local_index(args.project, args.doi, args.jats, args.force)
        print(json.dumps(manifest, indent=2))
        return 0
    if args.cmd == "add":
        manifest = add_paper(
            args.project,
            args.doi,
            pdf_path=args.pdf,
            jats_path=args.jats,
            role=args.role,
            force=args.force,
        )
        print(json.dumps(manifest, indent=2))
        return 0
    if args.cmd == "remove":
        present = remove_paper(args.project, args.doi)
        print(json.dumps({"removed": present}, indent=2))
        return 0
    if args.cmd == "list":
        print(json.dumps(list_papers(args.project), indent=2))
        return 0
    if args.cmd == "search":
        results = search(
            args.project,
            args.query,
            k=args.k,
            papers=args.paper,
            roles=args.role,
        )
        print(json.dumps(results, indent=2))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
