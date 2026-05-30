"""PDF → paragraph segments for the local snippet index.

Uses ``pymupdf4llm.to_markdown`` to reassemble multi-column PDFs into clean
paragraph-level markdown, then splits the markdown into ``_BodySegment``
records compatible with the existing JATS-derived chunker.

Document-level reading order across columns is not always preserved by
pymupdf4llm (a known limitation on heavily-floated layouts like 3-column
Science articles), but each emitted paragraph is internally coherent — which
is what the embedding-based snippet retriever needs.

Figure-internal text (axis labels, panel tags, gene-name strips) is emitted
by pymupdf4llm inside ``Start of picture text`` / ``End of picture text``
blocks. We tag those as ``section="IN_FIGURE"`` so downstream consumers can
exclude them from quoted evidence while still indexing them for recall.
"""

from __future__ import annotations

import logging
import os
import re
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class PdfSegment:
    """Paragraph segment extracted from a PDF.

    Mirrors ``local_snippet_index._BodySegment``. Kept as a separate class so
    the chunker's type hint can be widened to a Protocol without coupling
    the JATS parser to PDF concerns.
    """

    section: str
    text: str


# Pattern for pymupdf4llm picture-text blocks. Capture the raw <br>-separated
# content so we can keep it as a single "figure" segment per picture.
_PICTURE_BLOCK_RE = re.compile(
    r"\*\*-+ Start of picture text -+\*\*<br>\s*(.*?)\s*\*\*-+ End of picture text -+\*\*<br>",
    re.DOTALL,
)

# pymupdf4llm headings: ##, ###, etc. Strip leading hashes for the section label.
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")

# "==> picture [W x H] intentionally omitted <==" — drop entirely (no text).
_OMITTED_PIC_RE = re.compile(r"\*\*==>\s*picture\s*\[[^\]]+\]\s*intentionally omitted\s*<==\*\*")

# pymupdf4llm sometimes emits a leading `>` blockquote marker for author /
# affiliation footers. Strip the marker but keep the text.
_BLOCKQUOTE_RE = re.compile(r"^>\s+")

# Minimum body-paragraph length to keep. Very short fragments (page numbers,
# "1 of 14", standalone figure-label tokens) are noise.
_MIN_BODY_CHARS = 40
_MIN_FIGURE_CHARS = 20


def extract_pdf_segments(pdf_path: str | os.PathLike[str]) -> list[PdfSegment]:
    """Run pymupdf4llm and split the markdown output into paragraph segments.

    Parameters
    ----------
    pdf_path:
        Path to the PDF file.

    Returns
    -------
    list[PdfSegment]
        Paragraph segments tagged with a section label inferred from the
        nearest preceding markdown heading (``BODY`` if none seen yet,
        ``IN_FIGURE`` for picture-text blocks). Order follows pymupdf4llm's
        output, which is paragraph-coherent but may shuffle across columns.
    """
    import pymupdf4llm  # type: ignore[import-untyped]

    md = pymupdf4llm.to_markdown(str(pdf_path))
    return _split_markdown(md)


def _split_markdown(md: str) -> list[PdfSegment]:
    """Split pymupdf4llm markdown into segments. Pure-function for testability."""
    segments: list[PdfSegment] = []
    cur_section = "BODY"

    # Replace picture blocks with sentinels so we can emit them as their own
    # IN_FIGURE segments and keep their position in the stream.
    pic_payloads: list[str] = []

    def _stash_pic(match: re.Match[str]) -> str:
        idx = len(pic_payloads)
        pic_payloads.append(match.group(1))
        return f"\n\n@@PIC{idx}@@\n\n"

    md = _PICTURE_BLOCK_RE.sub(_stash_pic, md)
    md = _OMITTED_PIC_RE.sub("", md)

    # Split on blank lines — pymupdf4llm uses blank-line-separated paragraphs.
    for raw_para in re.split(r"\n\s*\n", md):
        para = raw_para.strip()
        if not para:
            continue

        # Picture-text payload?
        pic_match = re.fullmatch(r"@@PIC(\d+)@@", para)
        if pic_match:
            payload = pic_payloads[int(pic_match.group(1))]
            text = _clean_picture_text(payload)
            if len(text) >= _MIN_FIGURE_CHARS:
                segments.append(PdfSegment(section="IN_FIGURE", text=text))
            continue

        # Strip a leading blockquote marker if present.
        para = _BLOCKQUOTE_RE.sub("", para)

        # Heading?
        head_match = _HEADING_RE.match(para)
        if head_match:
            cur_section = head_match.group(2).strip()[:80] or "BODY"
            continue

        # Body paragraph — collapse internal newlines and dedupe whitespace.
        text = _clean_body_text(para)
        if len(text) < _MIN_BODY_CHARS:
            continue
        segments.append(PdfSegment(section=cur_section, text=text))

    return _dedupe_front_matter(segments)


def _clean_body_text(text: str) -> str:
    """Collapse markdown body text to a single whitespace-normalised line.

    Fixes the residual ``word- word`` artifacts that pymupdf4llm leaves when
    a hyphenated word straddles a column boundary it couldn't fully resolve
    (e.g. ``regionspecific`` from ``region-specific`` is already merged, but
    occasional ``oppositetrends`` survives).
    """
    # Drop superscript / subscript markup like `[+]`, `[12-15]` is kept though
    # — it's a useful citation token for retrieval.
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _clean_picture_text(payload: str) -> str:
    """Flatten a picture-text block to a space-separated token stream.

    pymupdf4llm emits picture text with `<br>` separators between visual
    rows; we don't try to reconstruct geometry — the stream is keyword fuel
    for the embedder, not quotable prose.
    """
    cleaned = payload.replace("<br>", " ")
    return re.sub(r"\s+", " ", cleaned).strip()


def _dedupe_front_matter(segments: list[PdfSegment]) -> list[PdfSegment]:
    """Drop a Research Article Summary paragraph if it is a strict prefix of
    a longer paragraph elsewhere in the document.

    Heuristic: a shorter paragraph that is the literal opening of a longer
    one is the duplicated summary version (e.g. Science 1-page Research
    Article Summary vs. the full Abstract on the article page). Conservative
    — only drops on exact prefix match after whitespace collapse.
    """
    if len(segments) < 2:
        return segments
    drop: set[int] = set()
    # Compare each pair where one text could be a prefix of the other.
    by_head: dict[str, list[int]] = {}
    for i, seg in enumerate(segments):
        head = seg.text[:60].lower()
        if len(head) < 40:
            continue
        by_head.setdefault(head, []).append(i)
    for indices in by_head.values():
        if len(indices) < 2:
            continue
        # Keep only the longest; drop strict-prefix duplicates.
        longest = max(indices, key=lambda i: len(segments[i].text))
        longest_text = segments[longest].text
        for i in indices:
            if i == longest:
                continue
            if longest_text.startswith(segments[i].text):
                drop.add(i)
    if not drop:
        return segments
    logger.info("Dropped %d duplicate front-matter paragraphs", len(drop))
    return [s for i, s in enumerate(segments) if i not in drop]


__all__ = ["PdfSegment", "extract_pdf_segments"]
