#!/usr/bin/env python3
"""Stage 1 — ranking, not retrieval. Throwaway test harness.

For each item and each arm, produce an ordering over the paper's text and measure how
many tokens must be read, in that order, before the gold span is covered.

Arms: document (publication order), lexical (BM25), local (MiniLM dense), asta
(snippet_search scoped to the paper). Chance is a permutation null computed offline.
"""
from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from corpus import chunks  # noqa: E402
from norm import norm_loc as norm  # noqa: E402

HERE = Path(__file__).parent
RESULTS = HERE / "results"

STOP = set("""a an the of in on at to for from by with and or is are was were be been being
what which who whom whose where when how why do does did this that these those it its as
into within during their there here can could may might will would should than then
about above after again against all am any because before below between both each few
further had has have having he her hers him his i if into me more most my no nor not now
only other our out over own same she so some such too under until up very we you your
""".split())


def keywords(question: str) -> str:
    toks = re.findall(r"[A-Za-z0-9+\-]{2,}", question)
    keep = [t for t in toks if t.lower() not in STOP]
    return " ".join(keep)


# ---------------------------------------------------------------- lexical (BM25)

def bm25_order(chs: list[dict], query: str, k1: float = 1.5, b: float = 0.75) -> list[int]:
    docs = [re.findall(r"[a-z0-9+\-]+", c["text"].lower()) for c in chs]
    N = len(docs)
    avgdl = sum(len(d) for d in docs) / N
    df: Counter = Counter()
    for d in docs:
        for t in set(d):
            df[t] += 1
    q = [t for t in re.findall(r"[a-z0-9+\-]+", query.lower()) if t not in STOP]
    scores = []
    for i, d in enumerate(docs):
        tf = Counter(d)
        s = 0.0
        for t in q:
            if t not in tf:
                continue
            idf = math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5))
            s += idf * tf[t] * (k1 + 1) / (tf[t] + k1 * (1 - b + b * len(d) / avgdl))
        scores.append(s)
    return sorted(range(N), key=lambda i: -scores[i])


# ---------------------------------------------------------------- local (dense)

_MODEL = None
_EMB: dict[str, object] = {}


def _model():
    global _MODEL
    if _MODEL is None:
        from sentence_transformers import SentenceTransformer

        _MODEL = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _MODEL


def dense_order(paper: str, chs: list[dict], query: str) -> list[int]:
    import numpy as np

    if paper not in _EMB:
        _EMB[paper] = _model().encode(
            [c["text"] for c in chs], normalize_embeddings=True, show_progress_bar=False
        )
    mat = _EMB[paper]
    qv = _model().encode([query], normalize_embeddings=True)[0]
    sims = np.asarray(mat) @ qv
    return sorted(range(len(chs)), key=lambda i: -sims[i])


# ---------------------------------------------------------------- asta

PAPER_DOI = {
    "gopee2024": "DOI:10.1038/s41586-024-08002-x",
    "suo2022": "DOI:10.1126/science.abo0510",
}


def asta_snippets(paper: str, query: str, limit: int = 100) -> list[dict]:
    import asta_probe

    payload = asta_probe.call_tool(
        "snippet_search",
        {"query": query, "paper_ids": PAPER_DOI[paper], "limit": limit},
    )
    rows = asta_probe._rows(payload)
    out = []
    for r in rows:
        txt = (r.get("text") or (r.get("snippet") or {}).get("text") or "")
        if txt:
            out.append({"text": txt, "n_tokens": max(1, len(txt) // 4),
                        "score": r.get("score")})
    return out


# ---------------------------------------------------------------- scoring

def _grams(text: str, n: int = 5) -> set[tuple[str, ...]]:
    w = norm(text).split()
    if len(w) < n:
        return {tuple(w)} if w else set()
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def cost_to_answer(ordered_texts: list[dict], span: str,
                   threshold: float = 0.8) -> tuple[int | None, int]:
    """(rank at which the span becomes available, tokens read to that point).

    Availability = the fraction of the span's word 5-grams present in everything read so
    far reaches `threshold`. Two reasons not to use exact substring matching:

    - A span split across two retrieved chunks is available to a reader who has both, but
      the chunks arrive separated in rank order, so a joined string is not contiguous.
      An n-gram measure loses only the few grams spanning the seam.
    - Sources render the same sentence differently (ASTA vs PMC JATS), so exact matching
      penalises an arm for text it never had.
    """
    want = _grams(span)
    if not want:
        return None, 0
    have: set = set()
    read = 0
    for rank, c in enumerate(ordered_texts, start=1):
        read += c["n_tokens"]
        have |= _grams(c["text"])
        if len(want & have) / len(want) >= threshold:
            return rank, read
    return None, read


def permutation_null(chs: list[dict], hit_idx: list[int], n: int = 2000) -> dict:
    """Null distribution of tokens-to-answer under random ordering."""
    import numpy as np

    rng = np.random.default_rng(0)
    toks = np.array([c["n_tokens"] for c in chs])
    hits = set(hit_idx)
    out = []
    for _ in range(n):
        perm = rng.permutation(len(chs))
        read = 0
        for i in perm:
            read += toks[i]
            if i in hits:
                break
        out.append(read)
    a = np.array(out)
    return {"mean": float(a.mean()), "median": float(np.median(a)),
            "p05": float(np.percentile(a, 5)), "samples": a.tolist()}


# ---------------------------------------------------------------- hybrid

def rrf_order(paper: str, chs: list[dict], query: str, k: int = 60) -> list[int]:
    """Reciprocal rank fusion of BM25 and dense. No score calibration needed: each arm
    contributes 1/(k + rank), so only the orderings matter, not their score scales."""
    lex = bm25_order(chs, query)
    den = dense_order(paper, chs, query)
    score = {i: 0.0 for i in range(len(chs))}
    for order in (lex, den):
        for rank, i in enumerate(order, start=1):
            score[i] += 1.0 / (k + rank)
    return sorted(range(len(chs)), key=lambda i: -score[i])
