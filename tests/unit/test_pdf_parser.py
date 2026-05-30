"""Unit tests for the PDF → segment converter.

Operates on synthetic pymupdf4llm-flavoured markdown so no real PDF parse is
needed. The pymupdf4llm dependency is only exercised by the integration
test that ingests the actual Braun PDF.
"""

from __future__ import annotations

from textwrap import dedent

import pytest
from atlas_chat.services._pdf_parser import _split_markdown


@pytest.mark.unit
def test_headings_become_section_labels() -> None:
    md = dedent(
        """\
        ## Introduction

        This is the first body paragraph. It is long enough to survive the
        minimum-character filter applied to body paragraphs.

        ## Results

        We discovered that ILC3 cells localise to the dermis in fetal skin
        and express CCL1 plus PTGDS as defining markers.
        """
    )
    segs = _split_markdown(md)
    assert any(s.section == "Introduction" for s in segs)
    assert any(s.section == "Results" for s in segs)
    assert all(len(s.text) >= 40 for s in segs if s.section != "IN_FIGURE")


@pytest.mark.unit
def test_picture_blocks_become_in_figure_segments() -> None:
    md = (
        "**----- Start of picture text -----**<br>\n"
        "Panel A<br>Panel B<br>NEUROD6 SOX2 PAX5 EMX1<br>\n"
        "**----- End of picture text -----**<br>\n"
        "\n"
        "This is the figure caption describing what panels A and B show.\n"
    )
    segs = _split_markdown(md)
    fig_segs = [s for s in segs if s.section == "IN_FIGURE"]
    body_segs = [s for s in segs if s.section != "IN_FIGURE"]
    assert len(fig_segs) == 1
    # <br> markers collapsed to spaces.
    assert "<br>" not in fig_segs[0].text
    assert "NEUROD6" in fig_segs[0].text
    # The caption is body.
    assert body_segs and "figure caption" in body_segs[0].text.lower()


@pytest.mark.unit
def test_omitted_picture_blocks_dropped() -> None:
    md = (
        "**==> picture [400 x 200] intentionally omitted <==**\n"
        "\n"
        "Real paragraph that should survive the noise filter for body text.\n"
    )
    segs = _split_markdown(md)
    assert all("intentionally omitted" not in s.text for s in segs)
    assert any("Real paragraph" in s.text for s in segs)


@pytest.mark.unit
def test_short_fragments_dropped() -> None:
    md = (
        "## Title\n\nA\n\n"
        "Real body paragraph that comfortably exceeds the threshold for inclusion.\n"
    )
    segs = _split_markdown(md)
    # The 'A' fragment should be filtered out as too short.
    body = [s for s in segs if s.section != "IN_FIGURE"]
    assert all(s.text != "A" for s in body)
    assert any("Real body paragraph" in s.text for s in body)


@pytest.mark.unit
def test_blockquote_marker_stripped() -> None:
    md = (
        "> Author affiliations: Karolinska Institute, 171 65 Stockholm, "
        "Sweden, plus collaborators at KTH and Cambridge.\n"
    )
    segs = _split_markdown(md)
    assert segs
    assert not segs[0].text.startswith(">")
    assert "Karolinska" in segs[0].text


@pytest.mark.unit
def test_front_matter_duplicates_dropped() -> None:
    body1 = "This is the abstract paragraph that begins with a distinctive enough opener to dedupe."
    md = (
        f"{body1}\n\n"
        f"{body1} It also continues with additional detail in the longer copy of the paragraph.\n"
    )
    segs = _split_markdown(md)
    # Only one of the two near-duplicate paragraphs should survive
    surviving = [s for s in segs if s.text.startswith("This is the abstract paragraph")]
    assert len(surviving) == 1
    # The longer one wins.
    assert "additional detail" in surviving[0].text
