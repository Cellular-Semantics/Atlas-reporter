"""Local snippet index for fresh-preprint atlases.

Builds a project-wide chunk store + sentence-citation graph + ASTA-shape
snippet index from a single JATS XML file. The `search()` API returns dicts
shaped like `citation_traverser._snippet_to_dict(AstaSnippet(...))` so the
downstream `_summarize_snippets` / `validate_report` machinery consumes them
unchanged.

The index is gated by `local_index/manifest.json` — if absent, the pipeline
falls through to ASTA-only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_TARGET_CHARS = 2800
CHUNK_OVERLAP_CHARS = 200
MANIFEST_VERSION = 1


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


# ------------------------------------------------------------------
# JATS normalisation (bioRxiv quirks)
# ------------------------------------------------------------------


def _normalize_biorxiv_jats(xml: str) -> str:
    """Make bioRxiv JATS digestible by `_jats_parser.parse_jats_citations`.

    Two fixes:
      1. Strip `hwp:*` namespaced attributes that get aliased to `id` after
         namespace strip, overwriting the real `<ref id="cNN">` value.
      2. Rename `<citation>` (Highwire convention) to `<element-citation>`
         (JATS standard) so the parser's ref-detail extractor matches.
    """
    # Remove hwp:* attributes from any element. Match on attribute name to
    # avoid pulling in unrelated namespaces.
    xml = re.sub(r'\s+hwp:[\w:-]+="[^"]*"', "", xml)
    xml = re.sub(r'\s+xmlns:hw="[^"]*"', "", xml)
    # Rename <citation ...> → <element-citation ...> only when it carries
    # publication-type (the JATS-ish citation, not other uses of <citation>).
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


@dataclass
class _BodySegment:
    section: str
    text: str  # paragraph text (whitespace collapsed)


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
    ``[12-15]`` rather than a bare ``12-15`` run (which would otherwise
    appear glued to surrounding words and make blockquote validation
    against `parse_jats_citations`'s sentence output — which already
    bracket-wraps — impossible).
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

    # Abstract first
    for abs_el in root.iter("abstract"):
        for p in abs_el.iter("p"):
            txt = re.sub(r"\s+", " ", _text_of(p)).strip()
            if txt:
                segments.append(_BodySegment("ABSTRACT", txt))

    # Body sections (recursive)
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
    # Top-level <p> inside body (no sec wrapper)
    for p in body.findall("p"):
        txt = re.sub(r"\s+", " ", _text_of(p)).strip()
        if txt:
            segments.append(_BodySegment("BODY", txt))

    return segments


# ------------------------------------------------------------------
# Chunking
# ------------------------------------------------------------------


def chunk_segments(
    segments: list[_BodySegment],
    target_chars: int = CHUNK_TARGET_CHARS,
    overlap_chars: int = CHUNK_OVERLAP_CHARS,
) -> tuple[str, list[Chunk]]:
    """Build paragraph-aware chunks. Returns (concatenated_fulltext, chunks).

    Adjacent paragraphs from the same section are concatenated up to target
    size. Section boundaries flush the current chunk. Overlap is added by
    re-emitting the tail of the previous chunk if the next paragraph would
    otherwise start a fresh chunk.
    """
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

        # New section → flush current
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
            # Carry overlap from end of the previous chunk
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
# Sentence-level citation graph
# ------------------------------------------------------------------


def build_sentence_rows(
    xml: str,
    fulltext: str,
) -> tuple[list[SentenceRow], dict[str, Any]]:
    """Run the vendored `_jats_parser.parse_jats_citations` and align each cited sentence
    to a char offset in `fulltext`. Returns (rows, refs_dict).

    `refs_dict` is the full {ref_id → ResolvedRef} mapping from the parser —
    callers can read `.doi`, `.title`, `.year`, `.first_author` for downstream
    resolution (DOI batch + title-match fallback).
    """
    from atlas_chat.services._jats_parser import parse_jats_citations

    cited, refs = parse_jats_citations(xml)

    ref_id_to_doi = {rid: r.doi for rid, r in refs.items() if r.doi}

    rows: list[SentenceRow] = []
    for cs in cited:
        # parse_jats_citations emits sentence text with bracketed citation
        # markers like [12-15]. The body chunker now also bracket-wraps
        # bibr xrefs, so the sentence text should match the fulltext
        # directly. Fall back to a bracket-stripped form for any cases the
        # two extractors render differently.
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
    """Batch-resolve DOIs to Semantic Scholar CorpusIds.

    Retries on 429 with exponential backoff (3 attempts, 2-4-8 second sleeps)."""
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
    """Single-paper title-match via Semantic Scholar.

    Returns (corpus_id, doi) — both None if no confident match. Uses S2's
    /paper/search/match endpoint, which returns the single best title match
    (or empty data if confidence is too low). Retries once on 429.
    """
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
                return None, None  # no match
            if resp.status_code != 200:
                return None, None
            data = resp.json().get("data", [])
            if not data:
                return None, None
            best = data[0]
            # Year guard: discard matches more than 2 years off if year was supplied.
            if year and best.get("year") and abs(int(best["year"]) - year) > 2:
                return None, None
            # Author guard: require first-author surname appears in the matched
            # author list when both are present.
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
    """Resolve every ref to a CorpusId, using DOI batch first then title-match.

    Returns a dict keyed by ref_id with shape:
        {"corpus_id": str | None, "doi": str | None,
         "method": "doi" | "title" | "none"}

    `refs` is the dict returned by `parse_jats_citations` — values have `.doi`,
    `.title`, `.year`, `.first_author` attributes (ResolvedRef dataclass)."""
    import httpx

    out: dict[str, dict[str, str | None]] = {}

    # Phase 1: DOI batch resolution for refs that carry a DOI.
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

    # Phase 2: title-match for refs without DOIs (or whose DOI didn't resolve).
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
# bioRxiv metadata
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


# ------------------------------------------------------------------
# Build orchestrator
# ------------------------------------------------------------------


def _local_corpus_id(doi: str) -> str:
    """Stable atlas CorpusId for an unindexed preprint.

    Format `CorpusId:local_<sha1[:10]>` — the `local_` token has no digits so
    it sidesteps the legacy `CorpusId:\\d+` validation regex in
    `report_checker.py::check_references` while preserving shape parity."""
    h = hashlib.sha1(doi.encode("utf-8")).hexdigest()[:10]
    return f"CorpusId:local_{h}"


def _manifest_hash(xml_bytes: bytes, parser_version: int = 1) -> str:
    h = hashlib.sha256()
    h.update(xml_bytes)
    h.update(f"|emb={EMBED_MODEL}|p={parser_version}|m={MANIFEST_VERSION}".encode())
    return h.hexdigest()


def build_local_index(
    project_dir: Path,
    doi: str,
    jats_path: Path | None = None,
    force: bool = False,
) -> dict[str, Any]:
    """Build (or refresh) the local snippet index for a project.

    If `jats_path` is None, `services.fetch_preprint.fetch_preprint` is called
    to populate it. Otherwise the existing JATS file is used as-is.
    Idempotent: a re-run with unchanged JATS short-circuits unless force=True.
    Returns the manifest dict.
    """
    project_dir = Path(project_dir)
    idx_dir = project_dir / "local_index"
    source_dir = idx_dir / "source"
    chunks_dir = idx_dir / "chunks"
    citations_dir = idx_dir / "citations"
    snippet_dir = idx_dir / "snippet_index"
    for d in (idx_dir, source_dir, chunks_dir, citations_dir, snippet_dir):
        d.mkdir(parents=True, exist_ok=True)

    # 1. Resolve JATS path
    if jats_path is None:
        jats_path = source_dir / "paper.jats.xml"
        if not jats_path.exists() or force:
            from atlas_chat.services.fetch_preprint import fetch_preprint

            fetched = fetch_preprint(doi, source_dir)
            jats_path = fetched.jats_path
    else:
        # Copy / link into source dir for self-containment
        target = source_dir / "paper.jats.xml"
        if jats_path.resolve() != target.resolve():
            target.write_bytes(jats_path.read_bytes())
            jats_path = target

    raw_xml_bytes = jats_path.read_bytes()
    manifest_path = idx_dir / "manifest.json"
    expected_hash = _manifest_hash(raw_xml_bytes)
    if manifest_path.exists() and not force:
        try:
            existing = json.loads(manifest_path.read_text())
            if existing.get("hash") == expected_hash:
                logger.info("Local index already up to date (manifest hash match).")
                return existing
        except Exception:
            pass

    xml = raw_xml_bytes.decode("utf-8")
    normalized = _normalize_biorxiv_jats(xml)

    # 2. Body text + paragraph segments → chunks
    segments = extract_body_segments(normalized)
    fulltext, chunks = chunk_segments(segments)
    (chunks_dir / "chunks.fulltext.txt").write_text(fulltext)
    with (chunks_dir / "chunks.jsonl").open("w") as fh:
        for c in chunks:
            fh.write(json.dumps(asdict(c)) + "\n")

    # 3. Embeddings
    embeddings_path = chunks_dir / "embeddings.npy"
    _embed_and_save([c.text for c in chunks], embeddings_path)

    # 4. Sentence-level citation graph (and full refs dict)
    sent_rows, refs_full = build_sentence_rows(normalized, fulltext)
    with (citations_dir / "sentences.jsonl").open("w") as fh:
        for r in sent_rows:
            fh.write(json.dumps(asdict(r)) + "\n")

    # 5. Resolve EVERY cited ref to a CorpusId — DOI batch first, then title-match
    #    for refs without a DOI (or whose DOI didn't resolve).
    ref_resolution = _resolve_refs_to_corpus_ids(refs_full)
    (citations_dir / "ref_resolution.json").write_text(json.dumps(ref_resolution, indent=2))
    ref_id_to_corpus = {
        rid: entry["corpus_id"] for rid, entry in ref_resolution.items() if entry["corpus_id"]
    }

    # 6. Atlas-paper metadata (for ASTA-shape paper field)
    meta = _biorxiv_meta(doi) or {}
    paper_meta = {
        "title": meta.get("title", ""),
        "authors": meta.get("authors", ""),
        "year": int(re.match(r"(\d{4})", meta.get("date", "") or "").group(1))
        if re.match(r"(\d{4})", meta.get("date", "") or "")
        else None,
        "doi": doi,
        "corpus_id": _local_corpus_id(doi),
        "url": f"https://www.biorxiv.org/content/{doi}v{meta.get('version', 1)}",
    }

    # 7. Merge chunks ↔ sentences → ASTA-shape snippet index
    snippets = _merge_snippets(chunks, sent_rows, ref_id_to_corpus, paper_meta)
    (snippet_dir / "snippets.json").write_text(json.dumps(snippets, indent=2))

    manifest = {
        "version": MANIFEST_VERSION,
        "doi": doi,
        "hash": expected_hash,
        "embedding_model": EMBED_MODEL,
        "n_chunks": len(chunks),
        "n_sentences": len(sent_rows),
        "n_refs": len(refs_full),
        "n_corpus_ids_resolved": len(ref_id_to_corpus),
        "resolution_methods": _resolution_breakdown(ref_resolution),
        "paper": paper_meta,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2))
    logger.info(
        "Built local_index: %d chunks, %d cited sentences, %d/%d refs resolved (%s)",
        len(chunks),
        len(sent_rows),
        len(ref_id_to_corpus),
        len(refs_full),
        manifest["resolution_methods"],
    )
    return manifest


def _embed_and_save(texts: list[str], out_path: Path) -> None:
    import numpy as np
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(EMBED_MODEL)
    vecs = model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
    # Normalise for cosine similarity at search time
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    vecs = vecs / norms
    np.save(out_path, vecs)


def _resolution_breakdown(ref_resolution: dict[str, dict[str, str | None]]) -> dict[str, int]:
    """Count refs by resolution method for the manifest."""
    counts: dict[str, int] = {}
    for entry in ref_resolution.values():
        m = entry.get("method") or "none"
        counts[m] = counts.get(m, 0) + 1
    return counts


def _merge_snippets(
    chunks: list[Chunk],
    sent_rows: list[SentenceRow],
    ref_id_to_corpus: dict[str, str],
    paper_meta: dict,
) -> list[dict]:
    """Emit one ASTA-shape snippet per chunk with refMentions baked in.

    refMentions are emitted per `ref_id` (not per DOI), so refs resolved via
    title-match (no DOI) still produce mentions."""
    # Index sentences by char_start for fast lookup
    sent_rows_sorted = sorted(sent_rows, key=lambda r: r.char_start)
    snippets: list[dict] = []
    for c in chunks:
        ref_mentions: list[dict] = []
        for r in sent_rows_sorted:
            if r.char_start >= c.char_end:
                break
            if r.char_end <= c.char_start:
                continue
            # Only keep sentences fully inside the chunk (loss-tolerant)
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
# Retrieval API (Phase 3)
# ------------------------------------------------------------------


@lru_cache(maxsize=8)
def _load_index(project_dir_str: str) -> dict[str, Any]:
    project_dir = Path(project_dir_str)
    idx_dir = project_dir / "local_index"
    manifest = json.loads((idx_dir / "manifest.json").read_text())
    chunks: list[dict] = []
    with (idx_dir / "chunks" / "chunks.jsonl").open() as fh:
        for line in fh:
            chunks.append(json.loads(line))
    snippets = json.loads((idx_dir / "snippet_index" / "snippets.json").read_text())
    snippet_by_chunk = {s["chunk_id"]: s for s in snippets}

    import numpy as np

    embeddings = np.load(idx_dir / "chunks" / "embeddings.npy")
    return {
        "manifest": manifest,
        "chunks": chunks,
        "snippets_by_chunk": snippet_by_chunk,
        "embeddings": embeddings,
    }


def search(project_dir: Path, query: str, k: int = 20) -> list[dict[str, Any]]:
    """Local snippet search returning ASTA-shape dicts compatible with
    `_summarize_snippets` and `_snippet_to_dict(AstaSnippet)`.
    """
    import numpy as np
    from sentence_transformers import SentenceTransformer

    state = _load_index(str(Path(project_dir).resolve()))
    embeddings = state["embeddings"]
    manifest = state["manifest"]

    model = SentenceTransformer(EMBED_MODEL)
    q_vec = model.encode([query], convert_to_numpy=True)[0]
    q_vec = q_vec / max(np.linalg.norm(q_vec), 1e-9)
    scores = embeddings @ q_vec
    top_idx = np.argsort(-scores)[:k].tolist()

    paper_meta = manifest["paper"]
    out: list[dict[str, Any]] = []
    for i in top_idx:
        chunk = state["chunks"][i]
        snippet_entry = state["snippets_by_chunk"].get(chunk["chunk_id"], {})
        ref_mentions = (
            snippet_entry.get("snippet", {}).get("annotations", {}).get("refMentions", [])
        )
        out.append(
            {
                # Fields required by _snippet_to_dict + snippet_summarizer prompt:
                "snippet": chunk["text"],
                "paper_id": paper_meta["corpus_id"],
                "corpus_id": paper_meta["corpus_id"],
                "title": paper_meta["title"],
                "authors": paper_meta["authors"],
                "year": paper_meta["year"],
                "url": paper_meta["url"],
                "score": float(scores[i]),
                # Extras for downstream / debugging:
                "doi": paper_meta.get("doi", ""),
                "section": chunk["section"],
                "chunk_id": chunk["chunk_id"],
                "annotations": {"refMentions": ref_mentions},
                "source_method": "local_snippet",
            }
        )
    return out


def has_local_index(project_dir: Path) -> bool:
    return (Path(project_dir) / "local_index" / "manifest.json").exists()


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", maxsplit=1)[0])
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_build = sub.add_parser("build", help="Build / refresh the local index")
    p_build.add_argument("--project", required=True, type=Path)
    p_build.add_argument("--doi", required=True)
    p_build.add_argument("--jats", type=Path, default=None, help="Use existing JATS XML")
    p_build.add_argument("--force", action="store_true")

    p_search = sub.add_parser("search", help="Query the local index")
    p_search.add_argument("--project", required=True, type=Path)
    p_search.add_argument("--query", required=True)
    p_search.add_argument("-k", type=int, default=10)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    if args.cmd == "build":
        manifest = build_local_index(args.project, args.doi, args.jats, args.force)
        print(json.dumps(manifest, indent=2))
        return 0
    if args.cmd == "search":
        results = search(args.project, args.query, k=args.k)
        print(json.dumps(results, indent=2))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
