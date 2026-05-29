"""Parse JATS XML from EuropePMC to extract sentence-level citation associations.

JATS XML preserves inline citations (<xref ref-type="bibr"> or <xref ref-type="ref">)
cross-referenced to a structured <ref-list> with DOIs, PMIDs, and PMCIDs. This module
extracts that structure into dataclasses suitable for citation traversal pipelines.

Dependencies: stdlib only.

----------------------------------------------------------------------------
Vendored from Cellular-Semantics/paperqa2_cyberian @ 4d5d153 (Mar 2026).

paperqa2_cyberian is an experimental repo with no formal release line and
no LICENSE file. Rather than pin atlas_chat to a moving experimental
dependency (which also forces Python 3.13+ on a 3.10-3.12 CI matrix), the
parser is vendored here. Stdlib-only — re-syncing is a straight `cp` if the
upstream picks up new JATS dialect support.
----------------------------------------------------------------------------
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class ResolvedRef:
    ref_id: str  # e.g. "CR1"
    doi: str | None = None
    pmid: str | None = None
    pmcid: str | None = None
    title: str | None = None
    year: int | None = None
    first_author: str | None = None


@dataclass
class CitedSentence:
    text: str  # sentence with citation markers like [1-3]
    section: str  # section title
    ref_ids: list[str] = field(default_factory=list)  # ordered, deduplicated
    resolved_refs: list[ResolvedRef] = field(default_factory=list)


# ---------------------------------------------------------------------------
# XML cleanup
# ---------------------------------------------------------------------------


def _clean_xml(xml_string: str) -> str:
    """Strip DOCTYPE declarations that cause ET to choke on external entities."""
    return re.sub(r"<!DOCTYPE[^>]*>", "", xml_string, count=1)


def _strip_namespace_from_tree(root: ET.Element) -> None:
    """Remove xmlns prefixes in-place so we can use plain tag names."""
    for elem in root.iter():
        if "}" in elem.tag:
            elem.tag = elem.tag.split("}", 1)[1]
        for key in list(elem.attrib):
            if "}" in key:
                new_key = key.split("}", 1)[1]
                elem.attrib[new_key] = elem.attrib.pop(key)


# ---------------------------------------------------------------------------
# Reference list parsing
# ---------------------------------------------------------------------------


def _parse_single_ref(ref_elem: ET.Element) -> ResolvedRef:
    """Extract identifiers and metadata from one <ref> element."""
    ref_id = ref_elem.get("id", "")

    doi = pmid = pmcid = title = first_author = None
    year: int | None = None

    # Look in both element-citation and mixed-citation
    citation = ref_elem.find(".//element-citation")
    if citation is None:
        citation = ref_elem.find(".//mixed-citation")

    if citation is not None:
        # DOI / PMID / PMCID from pub-id elements
        for pub_id in citation.findall(".//pub-id"):
            pub_type = pub_id.get("pub-id-type", "")
            val = (pub_id.text or "").strip()
            if pub_type == "doi":
                doi = val
            elif pub_type == "pmid":
                pmid = val
            elif pub_type == "pmcid":
                pmcid = val

        # Title — article-title or chapter-title
        title_elem = citation.find("article-title")
        if title_elem is None:
            title_elem = citation.find("chapter-title")
        if title_elem is not None:
            title = "".join(title_elem.itertext()).strip()

        # Year
        year_elem = citation.find("year")
        if year_elem is not None:
            year_text = (year_elem.text or "").strip()
            m = re.search(r"\d{4}", year_text)
            if m:
                year = int(m.group())

        # First author
        name_elem = citation.find(".//name")
        if name_elem is not None:
            surname = name_elem.find("surname")
            if surname is not None:
                first_author = (surname.text or "").strip()

    return ResolvedRef(
        ref_id=ref_id,
        doi=doi,
        pmid=pmid,
        pmcid=pmcid,
        title=title,
        year=year,
        first_author=first_author,
    )


def _parse_ref_list(root: ET.Element) -> dict[str, ResolvedRef]:
    """Parse all <ref> elements into a lookup dict keyed by ref id."""
    refs: dict[str, ResolvedRef] = {}
    for ref_elem in root.iter("ref"):
        parsed = _parse_single_ref(ref_elem)
        if parsed.ref_id:
            refs[parsed.ref_id] = parsed
    return refs


# ---------------------------------------------------------------------------
# Range expansion
# ---------------------------------------------------------------------------


def _expand_ref_range(rid_start: str, rid_end: str) -> list[str]:
    """Expand "CR1"-"CR3" → ["CR1","CR2","CR3"].

    Works for any common prefix + numeric suffix pattern.
    """
    m_start = re.match(r"^(.*?)(\d+)$", rid_start)
    m_end = re.match(r"^(.*?)(\d+)$", rid_end)
    if not m_start or not m_end or m_start.group(1) != m_end.group(1):
        return [rid_start, rid_end]
    prefix = m_start.group(1)
    lo, hi = int(m_start.group(2)), int(m_end.group(2))
    if hi < lo:
        return [rid_start, rid_end]
    return [f"{prefix}{i}" for i in range(lo, hi + 1)]


# ---------------------------------------------------------------------------
# Text reconstruction with citation tracking
# ---------------------------------------------------------------------------

# ref-type values that indicate a bibliography citation
_BIBR_REF_TYPES = {"bibr", "ref"}

# Type alias: list of (character_position, list_of_ref_ids)
CitationPositions = list[tuple[int, list[str]]]


def _walk_node(
    node: ET.Element,
    parts: list[str],
    citations: CitationPositions,
    *,
    inside_sup: bool = False,
) -> None:
    """Recursively walk an element tree, rebuilding text and tracking citations.

    ``parts`` accumulates text fragments; ``citations`` accumulates
    (char_offset, [ref_ids]) pairs where char_offset is computed from
    the *current* length of the joined parts.
    """

    def _current_pos() -> int:
        return sum(len(p) for p in parts)

    if node.tag == "xref" and node.get("ref-type") in _BIBR_REF_TYPES:
        rid = node.get("rid", "")
        display = "".join(node.itertext()).strip()
        pos = _current_pos()
        if rid:
            citations.append((pos, [rid]))
        if display:
            parts.append(display)
        # tail handled by caller
    elif node.tag == "sup":
        # Collect all bibr xrefs in this <sup>, detect ranges
        bibr_children = [
            ch for ch in node if ch.tag == "xref" and ch.get("ref-type") in _BIBR_REF_TYPES
        ]
        all_children_are_bibr = len(bibr_children) == len(list(node))

        if bibr_children and all_children_are_bibr:
            parts.append("[")
            _process_sup_bibr(node, parts, citations)
            parts.append("]")
        else:
            # Mixed content <sup> — recurse normally
            if node.text:
                parts.append(node.text)
            for child in node:
                _walk_node(child, parts, citations, inside_sup=True)
                if child.tail:
                    parts.append(child.tail)
    elif node.tag == "xref":
        # Non-bibr xref (fig, table, etc.) — just include display text
        display = "".join(node.itertext()).strip()
        if display:
            parts.append(display)
    else:
        # Generic element (<italic>, <bold>, <ext-link>, etc.) — recurse
        if node.text:
            parts.append(node.text)
        for child in node:
            _walk_node(child, parts, citations, inside_sup=inside_sup)
            if child.tail:
                parts.append(child.tail)


def _process_sup_bibr(
    sup: ET.Element,
    parts: list[str],
    citations: CitationPositions,
) -> None:
    """Handle a <sup> that contains only bibr xrefs (possibly with range separators)."""
    children = list(sup)
    prev_rid: str | None = None

    for i, child in enumerate(children):
        if child.tag != "xref" or child.get("ref-type") not in _BIBR_REF_TYPES:
            continue

        rid = child.get("rid", "")
        display = "".join(child.itertext()).strip()

        # Check for range separator between this xref and the previous one
        separator = ""
        if i > 0:
            # Separator is the tail of the previous child, or text between
            prev = children[i - 1]
            sep_text = (prev.tail or "").strip()
            if not sep_text and i == 1:
                sep_text = (sup.text or "").strip()
            separator = sep_text

        is_range = separator in ("-", "\u2013", "\u2014")

        if is_range and prev_rid and rid:
            expanded = _expand_ref_range(prev_rid, rid)
            # The first ref was already recorded; record intermediate + last
            for expanded_rid in expanded[1:]:
                pos = sum(len(p) for p in parts)
                citations.append((pos, [expanded_rid]))
            parts.append("\u2013")
            parts.append(display)
        else:
            if prev_rid is not None:
                parts.append(",")
            pos = sum(len(p) for p in parts)
            if rid:
                citations.append((pos, [rid]))
            if display:
                parts.append(display)

        prev_rid = rid


def _reconstruct_paragraph(
    p_elem: ET.Element,
) -> tuple[str, CitationPositions]:
    """Reconstruct text from a <p> element, tracking citation positions."""
    parts: list[str] = []
    citations: CitationPositions = []

    if p_elem.text:
        parts.append(p_elem.text)

    for child in p_elem:
        _walk_node(child, parts, citations)
        if child.tail:
            parts.append(child.tail)

    text = "".join(parts).strip()
    return text, citations


# ---------------------------------------------------------------------------
# Sentence splitting
# ---------------------------------------------------------------------------

# Abbreviations that should not trigger sentence breaks
_ABBREV_SET = {
    "et al",
    "Fig",
    "Figs",
    "Ref",
    "Refs",
    "Eq",
    "Eqs",
    "vs",
    "i.e",
    "e.g",
    "Dr",
    "Mr",
    "Mrs",
    "Ms",
    "Prof",
    "Jr",
    "Sr",
    "St",
    "vol",
    "no",
    "approx",
}


def _split_sentences(text: str) -> list[tuple[str, int]]:
    """Split text into sentences, returning (sentence, start_offset) pairs.

    Uses a conservative approach: splits on sentence-ending punctuation
    followed by whitespace and an uppercase letter, but protects common
    abbreviations.
    """
    if not text:
        return []

    # Find candidate split points: ". X" / "? X" / "! X" where X is uppercase
    candidates: list[int] = []
    for m in re.finditer(r'[.?!]\s+(?=[A-Z\[\("\'"\u201c])', text):
        # Check if the period belongs to a known abbreviation
        end_pos = m.start()  # position of the punctuation
        # Look back up to 10 chars for an abbreviation
        prefix = text[max(0, end_pos - 10) : end_pos + 1]
        is_abbrev = False
        for ab in _ABBREV_SET:
            if prefix.endswith(ab + ".") or prefix.endswith(ab):
                is_abbrev = True
                break
        if not is_abbrev:
            # split at the start of the whitespace gap
            candidates.append(m.start() + 1)

    if not candidates:
        return [(text.strip(), 0)]

    result: list[tuple[str, int]] = []
    prev = 0
    for sp in candidates:
        chunk = text[prev:sp].strip()
        if chunk:
            idx = text.find(chunk, prev)
            result.append((chunk, idx if idx >= 0 else prev))
        prev = sp
    # Last segment
    chunk = text[prev:].strip()
    if chunk:
        idx = text.find(chunk, prev)
        result.append((chunk, idx if idx >= 0 else prev))
    return result


# ---------------------------------------------------------------------------
# Citation → sentence mapping
# ---------------------------------------------------------------------------


def _assign_citations_to_sentences(
    sentences: list[tuple[str, int]],
    citations: CitationPositions,
    section: str,
    ref_lookup: dict[str, ResolvedRef],
) -> list[CitedSentence]:
    """Map citation positions to the sentence they fall within."""
    if not sentences or not citations:
        return []

    result: list[CitedSentence] = []

    for sent_text, sent_start in sentences:
        sent_end = sent_start + len(sent_text)
        ref_ids: list[str] = []
        for cit_pos, cit_rids in citations:
            if sent_start <= cit_pos <= sent_end:
                for rid in cit_rids:
                    if rid not in ref_ids:
                        ref_ids.append(rid)

        if ref_ids:
            resolved = [ref_lookup[rid] for rid in ref_ids if rid in ref_lookup]
            result.append(
                CitedSentence(
                    text=sent_text,
                    section=section,
                    ref_ids=ref_ids,
                    resolved_refs=resolved,
                )
            )

    return result


# ---------------------------------------------------------------------------
# Section walking
# ---------------------------------------------------------------------------


def _get_section_title(sec_elem: ET.Element) -> str:
    """Extract section title from a <sec> element."""
    title_elem = sec_elem.find("title")
    if title_elem is not None:
        return "".join(title_elem.itertext()).strip()
    return ""


def _walk_sections(
    elem: ET.Element,
    ref_lookup: dict[str, ResolvedRef],
    section_title: str = "Main",
) -> list[CitedSentence]:
    """Recursively walk <sec> and <body> elements, extracting cited sentences."""
    results: list[CitedSentence] = []

    for child in elem:
        if child.tag == "sec":
            sub_title = _get_section_title(child) or section_title
            results.extend(_walk_sections(child, ref_lookup, sub_title))
        elif child.tag == "p":
            text, citations = _reconstruct_paragraph(child)
            if not citations:
                continue
            sentences = _split_sentences(text)
            results.extend(
                _assign_citations_to_sentences(sentences, citations, section_title, ref_lookup)
            )

    return results


def _extract_cited_sentences(
    root: ET.Element,
    ref_lookup: dict[str, ResolvedRef],
) -> list[CitedSentence]:
    """Extract all cited sentences from the document body and back matter."""
    results: list[CitedSentence] = []

    # Body
    body = root.find(".//body")
    if body is not None:
        results.extend(_walk_sections(body, ref_lookup))

    # Abstract (sometimes has citations)
    for abstract in root.iter("abstract"):
        results.extend(_walk_sections(abstract, ref_lookup, "Abstract"))

    return results


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def parse_jats_citations(
    xml_string: str,
) -> tuple[list[CitedSentence], dict[str, ResolvedRef]]:
    """Parse JATS XML and extract sentence-level citation associations.

    Args:
        xml_string: Raw JATS XML content.

    Returns:
        Tuple of (cited_sentences, ref_lookup) where ref_lookup maps ref_id
        to ResolvedRef.
    """
    cleaned = _clean_xml(xml_string)
    root = ET.fromstring(cleaned)
    _strip_namespace_from_tree(root)

    ref_lookup = _parse_ref_list(root)
    logger.info("Parsed %d references from ref-list", len(ref_lookup))

    cited_sentences = _extract_cited_sentences(root, ref_lookup)
    logger.info("Extracted %d cited sentences", len(cited_sentences))

    return cited_sentences, ref_lookup


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _fetch_jats_xml(pmcid: str) -> str:
    """Fetch JATS XML from EuropePMC for a given PMCID."""
    # Normalise: ensure PMC prefix
    if not pmcid.upper().startswith("PMC"):
        pmcid = f"PMC{pmcid}"

    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
    logger.info("Fetching %s", url)

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def cli_main() -> None:
    """CLI entry point: fetch JATS XML for a PMCID and output structured JSON."""
    parser = argparse.ArgumentParser(description="Parse JATS XML citations from EuropePMC")
    parser.add_argument("pmcid", help="PubMed Central ID (e.g. PMC10719114)")
    parser.add_argument(
        "--from-file",
        help="Read XML from a local file instead of fetching",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    if args.from_file:
        with open(args.from_file) as f:
            xml_string = f.read()
    else:
        xml_string = _fetch_jats_xml(args.pmcid)

    cited_sentences, ref_lookup = parse_jats_citations(xml_string)

    # Normalise PMCID for output
    pmcid = args.pmcid.upper()
    if not pmcid.startswith("PMC"):
        pmcid = f"PMC{pmcid}"

    # Build stats
    refs_with_doi = sum(1 for r in ref_lookup.values() if r.doi)
    refs_with_pmid = sum(1 for r in ref_lookup.values() if r.pmid)

    output = {
        "pmcid": pmcid,
        "refs": {k: asdict(v) for k, v in ref_lookup.items()},
        "cited_sentences": [
            {
                "text": cs.text,
                "section": cs.section,
                "ref_ids": cs.ref_ids,
            }
            for cs in cited_sentences
        ],
        "stats": {
            "total_refs": len(ref_lookup),
            "refs_with_doi": refs_with_doi,
            "refs_with_pmid": refs_with_pmid,
            "sentences_with_citations": len(cited_sentences),
        },
    }

    indent = 2 if args.pretty else None
    print(json.dumps(output, indent=indent, ensure_ascii=False))
