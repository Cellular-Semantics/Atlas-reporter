"""Shared validation logic for cell-type reports.

Consumed by:
1. Claude Code hook (``.claude/hooks/check_report_refs.py``) — exits 2 on failure
2. PydanticAI graph — validation node routes failures back to synthesis
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def check_quotes(
    report_md: str,
    summaries: list[dict[str, object]],
    atlas_snippets: list[str],
) -> list[str]:
    """Return error messages for quotes in the report not found in evidence.

    Extracts all blockquote lines (``> "..."``), then checks each against the
    concatenated evidence corpus (traversal summaries + atlas snippets).

    Args:
        report_md: The full markdown report text.
        summaries: List of per-snippet summary dicts, each expected to contain
            a ``"quotes"`` key with a list of strings.
        atlas_snippets: Raw text snippets from the atlas paper / supplements.

    Returns:
        List of error strings.  Empty means all quotes verified.
    """
    errors: list[str] = []

    # Build evidence corpus from all summary quotes and atlas snippets
    evidence_texts: list[str] = list(atlas_snippets)
    for s in summaries:
        for q in s.get("quotes", []):  # type: ignore[union-attr]
            if isinstance(q, str):
                evidence_texts.append(q)
        # Also include the summary text itself as context
        if isinstance(s.get("summary"), str):
            evidence_texts.append(s["summary"])  # type: ignore[arg-type]
        # ASTA snippet search results use "snippet" key
        if isinstance(s.get("snippet"), str):
            evidence_texts.append(s["snippet"])  # type: ignore[arg-type]

    # Extract quoted text from blockquotes: > "some text"
    quote_pattern = re.compile(r'>\s*"([^"]+)"')
    for match in quote_pattern.finditer(report_md):
        quote = match.group(1)
        # Check if the quote appears as a substring in any evidence source
        if not _quote_in_evidence(quote, evidence_texts):
            errors.append(f'Quote not found in evidence: "{quote[:80]}..."')

    return errors


def _quote_in_evidence(quote: str, evidence_texts: list[str]) -> bool:
    """Check if a quote is a substring of any evidence text.

    Uses case-insensitive matching, normalises whitespace, and handles
    ellipsis (``...``) in quotes — each segment between ellipses must
    appear in the same evidence text in order.
    """
    # Split on ellipsis patterns: "...", "…", ". . ."
    segments = re.split(r"\.{3}|\u2026|\.\s\.\s\.", quote)
    segments = [s.strip() for s in segments if s.strip()]

    if not segments:
        return True  # empty quote

    for text in evidence_texts:
        norm_text = _normalise_for_match(text)
        # All segments must appear in order in the same evidence text
        pos = 0
        matched = True
        for seg in segments:
            norm_seg = _normalise_for_match(seg)
            if not norm_seg:
                continue
            idx = norm_text.find(norm_seg, pos)
            if idx == -1:
                matched = False
                break
            pos = idx + len(norm_seg)
        if matched:
            return True

    return False


def _normalise_for_match(text: str) -> str:
    """Normalise text for fuzzy substring matching.

    Collapses whitespace, lowercases, and strips characters that commonly
    differ between XML-derived full text and LLM-generated quotes (en-dash,
    em-dash, smart quotes, extra spaces around punctuation).
    """
    t = text.lower()
    # Normalise dashes and hyphens
    t = re.sub(r"[\u2013\u2014\u2015]", "-", t)
    # Normalise quotes
    t = re.sub(r"[\u2018\u2019\u201c\u201d]", "'", t)
    # Collapse whitespace
    t = re.sub(r"\s+", " ", t).strip()
    return t


def _normalise_ws(text: str) -> str:
    """Collapse runs of whitespace to single spaces."""
    return re.sub(r"\s+", " ", text).strip()


def check_references(
    report_md: str,
    catalogue: dict[str, object],
) -> list[str]:
    """Return error messages for DOIs in the report not found in the catalogue.

    Scans for DOI patterns (``10.NNNN/...``) in the report and verifies each
    against the DOIs in the paper catalogue.

    Also checks legacy ``CorpusId:NNN`` patterns for backwards compatibility.

    Args:
        report_md: The full markdown report text.
        catalogue: Paper catalogue dict, keyed by corpus ID string.

    Returns:
        List of error strings.  Empty means all references verified.
    """
    errors: list[str] = []

    # Build set of known DOIs from catalogue values
    known_dois: set[str] = set()
    for entry in catalogue.values():
        if isinstance(entry, dict):
            doi = entry.get("doi", "")
            if doi:
                known_dois.add(doi.lower().strip())

    # Build set of known CorpusIds (legacy support)
    known_corpus_ids: set[str] = set()
    for key in catalogue:
        clean = str(key).replace("CorpusId:", "").strip()
        known_corpus_ids.add(clean)

    # Find all DOIs in the report (standard DOI format: 10.NNNN/...)
    doi_pattern = re.compile(r"10\.\d{4,}/[^\s\)>\]]+")
    found_dois = {d.rstrip(".,;").lower() for d in doi_pattern.findall(report_md)}

    for doi in sorted(found_dois):
        if doi not in known_dois:
            errors.append(f"Unknown DOI {doi} — not in paper catalogue")

    # Legacy: also check any CorpusId references
    corpus_pattern = re.compile(r"CorpusId:(\d+)")
    found_corpus_ids = set(corpus_pattern.findall(report_md))
    for cid in sorted(found_corpus_ids):
        if cid not in known_corpus_ids:
            errors.append(f"Unknown reference CorpusId:{cid} — not in paper catalogue")

    return errors


VALID_ROLES = {"atlas", "subatlas", "external"}
VALID_RETRIEVAL_METHODS = {
    "corpus_snippet",
    "supplement",
    "citation_traversal",
    "free_search",
}
SUPPLEMENT_ROLES = {"atlas", "subatlas"}


def _catalogue_ids(catalogue: dict[str, object]) -> tuple[set[str], set[str]]:
    """Return (known_dois, known_corpus_ids) drawn from a paper catalogue.

    DOIs are lower-cased/stripped; CorpusIds are bare numeric strings (the
    ``CorpusId:`` prefix removed) collected from both the catalogue keys and any
    ``corpus_id`` values inside entries.
    """
    known_dois: set[str] = set()
    known_corpus_ids: set[str] = set()
    for key, entry in catalogue.items():
        known_corpus_ids.add(str(key).replace("CorpusId:", "").strip())
        if isinstance(entry, dict):
            doi = entry.get("doi", "")
            if isinstance(doi, str) and doi:
                known_dois.add(doi.lower().strip())
            cid = entry.get("corpus_id", "")
            if isinstance(cid, str) and cid:
                known_corpus_ids.add(cid.replace("CorpusId:", "").strip())
    return known_dois, known_corpus_ids


def _paper_ref_resolves(
    ref: dict[str, object],
    known_dois: set[str],
    known_corpus_ids: set[str],
) -> bool:
    """True if a source_paper/reached_from ref points at a catalogue member."""
    doi = ref.get("doi")
    if isinstance(doi, str) and doi.lower().strip() in known_dois:
        return True
    cid = ref.get("corpus_id")
    return isinstance(cid, str) and cid.replace("CorpusId:", "").strip() in known_corpus_ids


def check_source_tags(
    summaries: list[dict[str, object]],
    supp_data: dict[str, object],
    catalogue: dict[str, object],
) -> list[str]:
    """Return errors for evidence items with missing/invalid source provenance.

    Enforces the source-tagging contract from issue #12 on every evidence item
    across ``all_summaries.json`` and ``supplementary_findings.json``:

    1. Each item has a ``source_paper`` object carrying a valid ``role`` and at
       least one of ``doi`` / ``corpus_id``, plus a valid ``retrieval_method``.
    2. ``supplement`` items resolve to an ``atlas`` / ``subatlas`` corpus member
       (the implicit-atlas assumption is removed — the parent is now explicit).
    3. Every ``source_paper`` (and any ``reached_from``) DOI/CorpusId appears in
       ``paper_catalogue.json``.

    Args:
        summaries: Parsed ``all_summaries.json`` (list of evidence items).
        supp_data: Parsed ``supplementary_findings.json`` (markers /
            other_findings / evidence_quotes arrays).
        catalogue: Parsed ``paper_catalogue.json``.

    Returns:
        List of error strings.  Empty means every item is correctly tagged.
    """
    errors: list[str] = []
    known_dois, known_corpus_ids = _catalogue_ids(catalogue)

    def _check_item(item: object, where: str) -> None:
        if not isinstance(item, dict):
            errors.append(f"{where}: evidence item is not an object")
            return

        method = item.get("retrieval_method")
        if method not in VALID_RETRIEVAL_METHODS:
            errors.append(
                f"{where}: retrieval_method {method!r} missing or not one of "
                f"{sorted(VALID_RETRIEVAL_METHODS)}"
            )

        sp = item.get("source_paper")
        if not isinstance(sp, dict):
            errors.append(f"{where}: missing required source_paper object")
            return

        role = sp.get("role")
        if role not in VALID_ROLES:
            errors.append(
                f"{where}: source_paper.role {role!r} missing or not one of {sorted(VALID_ROLES)}"
            )

        if not (isinstance(sp.get("doi"), str) or isinstance(sp.get("corpus_id"), str)):
            errors.append(f"{where}: source_paper must have at least one of doi / corpus_id")
        elif not _paper_ref_resolves(sp, known_dois, known_corpus_ids):
            ident = sp.get("doi") or sp.get("corpus_id")
            errors.append(f"{where}: source_paper {ident!r} not found in paper_catalogue.json")

        if method == "supplement" and role not in SUPPLEMENT_ROLES:
            errors.append(
                f"{where}: supplement finding must resolve to an atlas/subatlas "
                f"paper, got role {role!r}"
            )

        reached = item.get("reached_from")
        if isinstance(reached, dict):
            if not (
                isinstance(reached.get("doi"), str) or isinstance(reached.get("corpus_id"), str)
            ):
                errors.append(f"{where}: reached_from must have at least one of doi / corpus_id")
            elif not _paper_ref_resolves(reached, known_dois, known_corpus_ids):
                ident = reached.get("doi") or reached.get("corpus_id")
                errors.append(f"{where}: reached_from {ident!r} not found in paper_catalogue.json")

    for i, item in enumerate(summaries):
        _check_item(item, f"all_summaries[{i}]")

    for array_name in ("markers", "other_findings", "evidence_quotes"):
        array = supp_data.get(array_name, [])
        if isinstance(array, list):
            for i, item in enumerate(array):
                _check_item(item, f"supplementary_findings.{array_name}[{i}]")

    return errors


def validate_report(
    report_path: Path,
    traversal_dir: Path,
) -> tuple[bool, list[str]]:
    """Full validation of a generated report against its evidence files.

    Args:
        report_path: Path to the markdown report file.
        traversal_dir: Directory containing traversal output files
            (``all_summaries.json``, ``paper_catalogue.json``).

    Returns:
        Tuple of ``(passed, errors)`` where *passed* is ``True`` when there
        are no validation errors.
    """
    report_md = report_path.read_text()

    # Load summaries
    summaries_path = traversal_dir / "all_summaries.json"
    summaries: list[dict[str, object]] = []
    if summaries_path.exists():
        summaries = json.loads(summaries_path.read_text())

    # Load paper catalogue
    catalogue_path = traversal_dir / "paper_catalogue.json"
    catalogue: dict[str, object] = {}
    if catalogue_path.exists():
        catalogue = json.loads(catalogue_path.read_text())

    # Load any atlas snippets (supplementary findings have evidence_quotes)
    atlas_snippets: list[str] = []
    supp_data: dict[str, Any] = {}
    supp_path = traversal_dir / "supplementary_findings.json"
    if supp_path.exists():
        supp_data = json.loads(supp_path.read_text())
        for eq in supp_data.get("evidence_quotes", []):
            if isinstance(eq, dict) and isinstance(eq.get("quote"), str):
                atlas_snippets.append(eq["quote"])
            elif isinstance(eq, str):
                atlas_snippets.append(eq)

    # Include atlas paper full text if saved during fetch step
    fulltext_path = traversal_dir / "atlas_full_text.txt"
    if fulltext_path.exists():
        atlas_snippets.append(fulltext_path.read_text())

    errors: list[str] = []
    errors.extend(check_quotes(report_md, summaries, atlas_snippets))
    errors.extend(check_references(report_md, catalogue))
    errors.extend(check_source_tags(summaries, supp_data, catalogue))

    return (len(errors) == 0, errors)
