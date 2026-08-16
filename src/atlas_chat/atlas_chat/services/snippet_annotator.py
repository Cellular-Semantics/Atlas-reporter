"""Programmatic ASTA snippet annotation and follow-set resolution.

This module keeps citation-traversal reference handling out of the agent's
context. It does two deterministic jobs, both pure (stdlib only) so they unit-test
offline:

1. **Projection + inline ref splicing** (:func:`project_snippet`,
   :func:`project_response`): turn a raw ASTA ``snippet_search`` response into slim
   ``annotated_snippet`` records. Each record keeps ``text`` verbatim (the
   exact-substring quote source) and adds ``annotated_text`` — the same text with
   every ``refMention`` span replaced *in place* by a standardized inline token
   (``[CorpusId:NNNN]`` or ``[CorpusId:unresolved]``). The agent reads
   ``annotated_text`` to gate sentences and propose ids; it never sees the raw
   payload.

2. **Follow-set resolution** (:func:`resolve_follow_set`): intersect the agent's
   proposed CorpusIds with the ids the annotator actually emitted, deduped. A
   proposed id the annotator never emitted (hallucinated or mistranscribed) is
   dropped to ``rejected`` — the agent is never the source of truth for an id.

The record shape matches ``schemas/annotated_snippet.schema.json``; the follow-set
shape matches ``schemas/follow_set.schema.json``.
"""

from __future__ import annotations

import re
from typing import Any

UNRESOLVED_TOKEN = "[CorpusId:unresolved]"
"""Inline token spliced in place of a refMention ASTA could not resolve."""

_CORPUS_ID_RE = re.compile(r"^CorpusId:\d+$")


def _normalize_corpus_id(matched: str | int | None) -> str | None:
    """Coerce an ASTA ``matchedPaperCorpusId`` to canonical ``CorpusId:NNNN`` form.

    Lenient — accepts what ASTA emits (bare integers) as well as already-prefixed
    strings. Use this for *response* data, not for agent-proposed ids (those are
    validated strictly in :func:`resolve_follow_set`).

    Args:
        matched: ``234484741``, ``"234484741"``, ``"CorpusId:234484741"``, or None.

    Returns:
        ``"CorpusId:NNNN"``, or None when the input is empty/None or not numeric.
    """
    if matched is None:
        return None
    text = str(matched).strip()
    if text.startswith("CorpusId:"):
        text = text[len("CorpusId:") :]
    if not text.isdigit():
        return None
    return f"CorpusId:{text}"


def _corpus_token(matched: str | int | None) -> str:
    """Return the inline token for a matched corpus id (or the unresolved token)."""
    corpus_id = _normalize_corpus_id(matched)
    return f"[{corpus_id}]" if corpus_id else UNRESOLVED_TOKEN


def _raw_matched(raw_rm: dict[str, Any]) -> str | int | None:
    """Read the matched corpus id from a refMention in either ASTA or schema shape."""
    if "matchedPaperCorpusId" in raw_rm:
        return raw_rm.get("matchedPaperCorpusId")
    return raw_rm.get("corpus_id")


def _splice_refs(text: str, ref_mentions: list[dict[str, Any]]) -> str:
    """Splice inline citation tokens into ``text`` at each refMention span.

    Replacement is deterministic and right-to-left: spans are processed by
    descending ``(start, end)`` so replacing one never shifts the offsets of those
    not yet processed. Only the ``[start, end)`` spans are replaced — any
    inter-mention punctuation (e.g. the commas in ``"6,7,8,9"``) is preserved.

    Args:
        text: The verbatim snippet text.
        ref_mentions: Raw ASTA refMentions (``start``/``end`` +
            ``matchedPaperCorpusId``) or schema refMentions (``corpus_id``).

    Returns:
        ``text`` with each refMention span replaced by its inline token. Equal to
        ``text`` when ``ref_mentions`` is empty.
    """
    ordered = sorted(
        (r for r in ref_mentions if "start" in r and "end" in r),
        key=lambda r: (int(r["start"]), int(r["end"])),
        reverse=True,
    )
    out = text
    for ref in ordered:
        start, end = int(ref["start"]), int(ref["end"])
        out = out[:start] + _corpus_token(_raw_matched(ref)) + out[end:]
    return out


def _to_ref_mention(raw_rm: dict[str, Any]) -> dict[str, Any]:
    """Map a raw ASTA refMention to the schema ``RefMention`` shape."""
    corpus_id = _normalize_corpus_id(_raw_matched(raw_rm))
    return {
        "start": int(raw_rm["start"]),
        "end": int(raw_rm["end"]),
        "corpus_id": corpus_id,
        "resolved": corpus_id is not None,
    }


def project_snippet(
    raw_item: dict[str, Any],
    *,
    source_paper: dict[str, Any],
    retrieval_method: str,
    reached_from: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build one slim ``annotated_snippet`` record from a raw ASTA data item.

    ``text`` is copied verbatim (quote integrity); ``annotated_text`` is the spliced
    copy. ``source_paper.role`` comes from the caller; the record's ``corpus_id`` is
    taken from the raw item's own ``paper.corpusId`` when present (so a multi-paper
    response tags each snippet with the paper it actually came from), otherwise from
    the caller's ``source_paper``.

    Args:
        raw_item: One element of the ASTA ``result.data`` array.
        source_paper: ``{"role": ..., "corpus_id"/"doi": ...}`` provenance; the role
            is authoritative, ids are a fallback.
        retrieval_method: One of the ``retrieval_method`` enum values.
        reached_from: Optional citation provenance for followed (hop >= 1) snippets.

    Returns:
        A dict validating against ``annotated_snippet.schema.json``.
    """
    snippet = raw_item.get("snippet", {}) or {}
    text = snippet.get("text", "") or ""
    annotations = snippet.get("annotations") or {}
    raw_refs = annotations.get("refMentions") or []
    raw_sentences = annotations.get("sentences") or []

    resolved_source = dict(source_paper)
    per_item_cid = _normalize_corpus_id((raw_item.get("paper") or {}).get("corpusId"))
    if per_item_cid and "doi" not in resolved_source:
        resolved_source["corpus_id"] = per_item_cid

    record: dict[str, Any] = {
        "text": text,
        "annotated_text": _splice_refs(text, raw_refs),
        "score": raw_item.get("score", 0.0),
        "source_paper": resolved_source,
        "retrieval_method": retrieval_method,
        "sentences": [{"start": int(s["start"]), "end": int(s["end"])} for s in raw_sentences],
        "refMentions": [_to_ref_mention(r) for r in raw_refs],
    }
    section = snippet.get("section")
    if section:
        record["section"] = section
    if reached_from is not None:
        record["reached_from"] = reached_from
    return record


def _coerce_data_list(response: Any) -> list[dict[str, Any]]:
    """Return the ``data`` array from any of the three ASTA payload nestings."""
    if isinstance(response, list):
        return response
    if isinstance(response, dict):
        result = response.get("result")
        if isinstance(result, dict):
            return result.get("data") or []
        if "data" in response:
            return response.get("data") or []
    return []


def project_response(
    response: Any,
    *,
    source_paper: dict[str, Any],
    retrieval_method: str,
    reached_from: dict[str, Any] | None = None,
    score_threshold: float = 0.0,
) -> list[dict[str, Any]]:
    """Project a full ASTA ``snippet_search`` response into slim records.

    Tolerates the three payload nestings the provider may return:
    ``{"result": {"data": [...]}}``, ``{"data": [...]}``, or ``[...]``. Items with
    ``score`` below ``score_threshold`` are dropped.

    Args:
        response: The raw ASTA response.
        source_paper: Provenance passed to :func:`project_snippet`.
        retrieval_method: One of the ``retrieval_method`` enum values.
        reached_from: Optional citation provenance for followed snippets.
        score_threshold: Coarse score floor applied before the sentence gate.

    Returns:
        A list of ``annotated_snippet`` dicts.
    """
    records: list[dict[str, Any]] = []
    for item in _coerce_data_list(response):
        if item.get("score", 0.0) < score_threshold:
            continue
        records.append(
            project_snippet(
                item,
                source_paper=source_paper,
                retrieval_method=retrieval_method,
                reached_from=reached_from,
            )
        )
    return records


def _real_corpus_ids(snippets: list[dict[str, Any]]) -> set[str]:
    """Union of every non-null ``refMentions[].corpus_id`` across the snippets.

    This is the ground truth of what ASTA actually returned inline — the only ids
    that may be followed.
    """
    ids: set[str] = set()
    for snippet in snippets:
        for ref in snippet.get("refMentions") or []:
            corpus_id = ref.get("corpus_id")
            if corpus_id:
                ids.add(corpus_id)
    return ids


def resolve_follow_set(
    snippets: list[dict[str, Any]],
    proposed_ids: list[str],
    *,
    hop: int | None = None,
) -> dict[str, Any]:
    """Compute the deduped follow-set as ``proposed ∩ real``, logging the rest.

    Anti-hallucination gate: the agent proposes CorpusIds it read inline; this
    intersects them with the ids the annotator emitted for these snippets. A
    proposal that is not a well-formed ``CorpusId:NNNN`` is rejected as
    ``malformed``; a well-formed proposal absent from the snippets' refMentions is
    rejected as ``not_in_refmentions``. Deduplication preserves first-seen order.

    Args:
        snippets: The projected ``annotated_snippet`` records (source of truth).
        proposed_ids: The agent's proposed CorpusIds to follow.
        hop: Optional hop number stamped on the output.

    Returns:
        A dict validating against ``follow_set.schema.json``:
        ``{"hop"?, "follow_set": [...], "rejected": [{"corpus_id", "reason"}]}``.
    """
    real = _real_corpus_ids(snippets)
    follow_set: list[str] = []
    rejected: list[dict[str, str]] = []
    seen: set[str] = set()
    for proposed in proposed_ids:
        candidate = str(proposed).strip()
        if not _CORPUS_ID_RE.match(candidate):
            rejected.append({"corpus_id": candidate, "reason": "malformed"})
            continue
        if candidate not in real:
            rejected.append({"corpus_id": candidate, "reason": "not_in_refmentions"})
            continue
        if candidate in seen:
            continue
        seen.add(candidate)
        follow_set.append(candidate)

    result: dict[str, Any] = {"follow_set": follow_set, "rejected": rejected}
    if hop is not None:
        result["hop"] = hop
    return result
