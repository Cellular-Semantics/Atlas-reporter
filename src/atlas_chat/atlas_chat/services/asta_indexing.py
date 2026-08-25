"""ASTA snippet-index depth probe.

Answers one question: *how much of this paper does ASTA's snippet index actually
hold?* Semantic Scholar's metadata graph and the snippet index are separate
systems, so a paper can carry a ``CorpusId``, an abstract and 118 references
while ``snippet_search`` returns nothing at all for it. There is no API field
that reports snippet coverage — probing is the only instrument.

The bands, and what each one can support:

===============  ==================  ==========================================
band             quotable snippets   citation traversal route
===============  ==================  ==========================================
``full``         yes                 ``refMentions`` — gated and positioned
``partial``      thin                ``refMentions``, but below the full-text floor
``abstract_only``no                  ``get_paper --fields references`` (edges only)
``unindexed``    no                  none via ASTA → local index
``not_in_s2``    no                  none via ASTA → local index
===============  ==================  ==========================================

Only ``full`` may be served from ASTA; every other band must fall through the
``jats → needs_pdf`` waterfall in :mod:`atlas_chat.services.subatlas_resolver`.

Calibration
-----------
Measured 2026-08-21 over 21 papers from the fetal_skin_atlas run, at
``limit 100`` per paper. The three observed bands separated with no overlap:

===============  ========  ================  ========  ============  ===
band             snippets  chars             sections  refMentions   n
===============  ========  ================  ========  ============  ===
``UNINDEXED``    0         0                 0         0             6
``ABSTRACT_ONLY``2..4      1,219..6,312      0         0             3
``FULL``         15..72    18,802..105,876   9..30     50..361       12
===============  ========  ================  ========  ============  ===

Distinct section names and refMention counts are the two decisive signals, and
they are orthogonal: body chunks carry section names, and only a body carries a
bibliography. The gaps are wide (0 vs >=9 sections; 0 vs >=50 refMentions), so
the thresholds are not finely tuned.

Signals deliberately **not** used, each tested and rejected:

* ``externalIds.CorpusId`` — fires for 21/21 including all 6 unindexed papers.
  This was the original bug (see #22).
* ``isOpenAccess`` / ``openAccessPdf`` — 3 of 6 unindexed papers are open
  access; one fully indexed paper is not.
* ``referenceCount`` — 21/21 non-zero and the ranges fully overlap (unindexed
  30..116 vs full 26..289); it comes from publisher metadata, not full text.
* ``publicationTypes`` — no signal.
* ``chars / abstract_length`` — breaks both ways: 0.0 for a paper with 6,312
  indexed chars (missing abstract), 426 for a 118-char truncated abstract.

A paper-scoped ``snippet_search`` returns that paper's **entire** indexed chunk
set regardless of the query — verified by running unrelated queries against the
same paper and getting identical counts. So the probe query is arbitrary (it
only affects ordering) and one call per paper suffices.

The exploratory prototype these constants came from is kept as the calibration
record at ``experiments/asta_probe.py`` (``audit`` subcommand).
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

#: Bands in descending order of usefulness. Only ``full`` is ASTA-servable.
BANDS = ("full", "partial", "abstract_only", "unindexed", "not_in_s2")

#: The band that may be served from ASTA without a local index.
SERVABLE_BAND = "full"

#: Bands with no retrievable text *and* no traversable references — dispatching
#: a citation hop to one of these cannot produce evidence.
DEAD_BANDS = ("unindexed", "not_in_s2")

MIN_SECTIONS = 1  # >=1 distinct section name means body text is indexed
PARTIAL_SNIPPETS = 10  # below the observed FULL floor of 15
PARTIAL_CHARS = 15_000  # below the observed FULL floor of 18,802

#: The probe query is arbitrary (see module docstring) — it only affects the
#: order of the returned chunk set, never its size.
AUDIT_QUERY = "cell types methods results discussion"

#: The paper's whole indexed chunk set is returned, so the limit only needs to
#: exceed the largest observed chunk count (72).
AUDIT_LIMIT = 100


@dataclass
class IndexingReport:
    """One paper's snippet-index depth.

    Serializes to the ``asta_indexing`` block of a CAS+ ``SubatlasPaper``.
    """

    band: str
    snippets: int = 0
    chars: int = 0
    sections: int = 0
    ref_mentions: int = 0
    corpus_id: str | None = None
    reason: str = ""
    probed_at: str = field(default_factory=lambda: datetime.now(UTC).isoformat())

    @property
    def servable(self) -> bool:
        """Whether ASTA can serve this paper's text without a local index."""
        return self.band == SERVABLE_BAND

    @property
    def dead(self) -> bool:
        """Whether a citation hop to this paper is guaranteed to return nothing."""
        return self.band in DEAD_BANDS

    def to_dict(self) -> dict[str, Any]:
        """Render the ``asta_indexing`` object for the CAS+ config."""
        out: dict[str, Any] = {
            "band": self.band,
            "snippets": self.snippets,
            "chars": self.chars,
            "sections": self.sections,
            "ref_mentions": self.ref_mentions,
            "probed_at": self.probed_at,
        }
        if self.corpus_id:
            out["corpus_id"] = self.corpus_id
        if self.reason:
            out["reason"] = self.reason
        return out

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> IndexingReport:
        """Rehydrate a cached ``asta_indexing`` block."""
        return cls(
            band=data["band"],
            snippets=int(data.get("snippets") or 0),
            chars=int(data.get("chars") or 0),
            sections=int(data.get("sections") or 0),
            ref_mentions=int(data.get("ref_mentions") or 0),
            corpus_id=data.get("corpus_id"),
            reason=data.get("reason") or "",
            probed_at=data.get("probed_at") or "",
        )


def _count_signals(rows: list[dict[str, Any]]) -> tuple[int, set[str], int, str | None]:
    """Extract (chars, distinct sections, refMention count, corpus id) from rows.

    ``refMentions`` live at ``snippet.annotations.refMentions`` and the key may be
    absent or explicitly ``null``. Section names are ``null`` for title/abstract
    pseudo-chunks, which is precisely the signal that separates a body from an
    abstract — so only non-null names are counted.
    """
    chars = 0
    sections: set[str] = set()
    ref_mentions = 0
    corpus_id: str | None = None
    for row in rows:
        snippet = row.get("snippet") or {}
        paper = row.get("paper") or {}
        chars += len(snippet.get("text") or "")
        section = snippet.get("section")
        if section:
            sections.add(section)
        annotations = snippet.get("annotations") or {}
        ref_mentions += len(annotations.get("refMentions") or [])
        if corpus_id is None:
            raw_id = paper.get("corpusId") or paper.get("corpus_id")
            if raw_id:
                corpus_id = f"CorpusId:{raw_id}" if str(raw_id).isdigit() else str(raw_id)
    return chars, sections, ref_mentions, corpus_id


def classify_rows(rows: list[dict[str, Any]]) -> IndexingReport:
    """Classify a paper's indexing band from its raw ``snippet_search`` rows.

    Pure: no I/O. This is the whole decision, and the unit tests pin it at each
    boundary of the calibration table in the module docstring.

    Args:
        rows: The ``data`` array of a paper-scoped ``snippet_search`` response.

    Returns:
        An :class:`IndexingReport`.

    .. code-block:: python

        >>> classify_rows([]).band
        'unindexed'
    """
    chars, sections, ref_mentions, corpus_id = _count_signals(rows)
    count = len(rows)

    if count == 0:
        band = "unindexed"
        reason = "0 snippets — ASTA holds nothing for this paper"
    elif len(sections) < MIN_SECTIONS and ref_mentions == 0:
        band = "abstract_only"
        reason = (
            f"{count} snippets, no section names, no refMentions — "
            "title/abstract only, no body text"
        )
    elif count < PARTIAL_SNIPPETS or chars < PARTIAL_CHARS or ref_mentions == 0:
        band = "partial"
        reason = (
            f"{count} snippets / {chars:,} chars / {ref_mentions} refMentions — "
            "below the observed full-text floor; treat as needing a local index"
        )
    else:
        band = "full"
        reason = f"{count} snippets across {len(sections)} sections"

    return IndexingReport(
        band=band,
        snippets=count,
        chars=chars,
        sections=len(sections),
        ref_mentions=ref_mentions,
        corpus_id=corpus_id,
        reason=reason,
    )


#: Phrases in an ASTA tool error that mean "no such paper" rather than "the call
#: failed". The tool reports a missing paper as a generic ``isError`` payload
#: with no distinguishable code, so the message is the only signal available —
#: hence phrases rather than a substring like "404", which would also match a
#: fault mentioning a paper id such as ``CorpusId:1404567``. The wording below is
#: verbatim from the live endpoint and pinned by the integration test.
_MISSING_PAPER_PHRASES = (
    "no papers matching",
    "no such paper",
    "paper not found",
    "does not exist",
)


def _is_missing_paper_error(exc: Exception) -> bool:
    """Whether an ASTA failure means "no such paper" rather than a fault.

    A paper absent from Semantic Scholar entirely is the ``not_in_s2`` band
    (#13); anything else is a real failure and must propagate rather than be
    recorded as a band, which would silently turn an outage into a corpus of
    unindexed papers.

    Two shapes reach here. An HTTP-level failure arrives as
    :class:`httpx.HTTPStatusError` and carries a status code, so it is judged
    structurally. An MCP tool error arrives as :class:`ValueError` from
    ``AstaProvider._call_tool`` with the message as its only content; ASTA's
    wording for a missing paper, verified against ``DOI:10.1126/science.adx0659``,
    is::

        No papers matching the provided paper ids ([...]) were found. Please
        double check the paper ids provided.
    """
    import httpx

    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code == 404

    text = str(exc).lower()
    return any(phrase in text for phrase in _MISSING_PAPER_PHRASES)


async def probe(
    paper_id: str, *, limit: int = AUDIT_LIMIT, query: str = AUDIT_QUERY
) -> IndexingReport:
    """Probe one paper's snippet-index depth with a single ASTA call.

    Args:
        paper_id: ``CorpusId:NNNN`` or ``DOI:...``.
        limit: Snippet limit; only needs to exceed the paper's chunk count.
        query: Arbitrary — a paper-scoped search returns the whole chunk set.

    Returns:
        An :class:`IndexingReport`. A paper absent from Semantic Scholar yields
        band ``not_in_s2``; any other transport or tool failure propagates.

    Raises:
        ValueError: On an ASTA tool or transport error unrelated to a missing
            paper (including a missing ``ASTA_API_KEY``).
    """
    import httpx

    from atlas_chat.services import snippet_annotator
    from atlas_chat.services.citation_traverser import _make_provider

    provider = _make_provider()
    arguments: dict[str, Any] = {"query": query, "limit": limit, "paper_ids": paper_id}
    try:
        async with httpx.AsyncClient(timeout=180) as http_client:
            raw = await provider._call_tool(http_client, "snippet_search", arguments)
    except (ValueError, httpx.HTTPStatusError) as exc:
        if _is_missing_paper_error(exc):
            logger.info("ASTA has no record of %s: %s", paper_id, exc)
            return IndexingReport(
                band="not_in_s2",
                corpus_id=paper_id if paper_id.startswith("CorpusId:") else None,
                reason=f"snippet_search found no such paper: {exc}",
            )
        raise

    report = classify_rows(snippet_annotator._coerce_data_list(raw))
    if report.corpus_id is None and paper_id.startswith("CorpusId:"):
        report.corpus_id = paper_id
    logger.info("ASTA band for %s: %s (%s)", paper_id, report.band, report.reason)
    return report


# --------------------------------------------------------------------------
# caching
# --------------------------------------------------------------------------
# A band is a property of the paper, not of the query, so it never needs
# re-probing within a run. The long-term home for the cache is the per-paper
# materials manifest proposed in #21; until that exists the CAS+ config carries
# it, and this in-process map keeps a single run to one call per paper.
_MEMO: dict[str, IndexingReport] = {}


def config_path(project_dir: Path | str) -> Path:
    """Return the project's config file, preferring CAS+ over the legacy name.

    ``cas.json`` supersedes ``cell_type_annotations.json`` (see ``CLAUDE.md``);
    both are read so existing projects keep working.
    """
    project_dir = Path(project_dir)
    cas = project_dir / "cas.json"
    if cas.exists():
        return cas
    return project_dir / "cell_type_annotations.json"


def cached_bands(project_dir: Path | str) -> dict[str, IndexingReport]:
    """Read persisted ``asta_indexing`` blocks from a project's config.

    Keyed by both ``corpus_id`` and ``DOI:<doi>`` so a lookup succeeds with
    whichever identifier the caller holds.
    """
    path = config_path(project_dir)
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("Could not read %s: %s", path, exc)
        return {}

    out: dict[str, IndexingReport] = {}
    source = data.get("source") or {}
    entries = list(source.get("subatlas_papers") or [])
    if source.get("asta_indexing"):
        entries.append(source)
    for entry in entries:
        block = entry.get("asta_indexing")
        if not isinstance(block, dict) or "band" not in block:
            continue
        try:
            report = IndexingReport.from_dict(block)
        except (KeyError, TypeError, ValueError) as exc:
            logger.warning("Skipping malformed asta_indexing block: %s", exc)
            continue
        for key in (report.corpus_id, block.get("corpus_id")):
            if key:
                out[key] = report
        if entry.get("doi"):
            out[f"DOI:{entry['doi']}"] = report
    return out


async def probe_cached(
    paper_id: str,
    *,
    project_dir: Path | str | None = None,
    limit: int = AUDIT_LIMIT,
) -> IndexingReport:
    """Probe ``paper_id``, reusing a persisted or in-process band if there is one.

    Args:
        paper_id: ``CorpusId:NNNN`` or ``DOI:...``.
        project_dir: If given, persisted bands in the project's config are
            consulted before making a call.
        limit: Passed through to :func:`probe`.

    Returns:
        An :class:`IndexingReport`.
    """
    if paper_id in _MEMO:
        return _MEMO[paper_id]
    if project_dir is not None:
        persisted = cached_bands(project_dir).get(paper_id)
        if persisted is not None:
            _MEMO[paper_id] = persisted
            return persisted
    report = await probe(paper_id, limit=limit)
    _MEMO[paper_id] = report
    return report


def clear_cache() -> None:
    """Drop the in-process band memo (test helper; also useful after a re-probe)."""
    _MEMO.clear()
