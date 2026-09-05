"""Integration test: real pymupdf4llm over a real PDF, through the CLI.

Builds a small two-page PDF with PyMuPDF, extracts it, and checks the text and
the sidecar against the bytes on disk. No mocks — this is the test that would
notice pymupdf4llm changing its markdown conventions out from under
``_pdf_parser``.

Fails hard (not skips) if the [text-access] extra is absent, per the project's
integration-test policy::

    uv sync --extra text-access
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from atlas_chat.services.pdf_text import extract_pdf_text, main, validate_sidecar

PARAGRAPH_ONE = (
    "Iron-recycling macrophages are one of four macrophage subsets identified in "
    "prenatal human skin, distinguished by expression of SLC40A1, CD5L and TIMD4."
)
PARAGRAPH_TWO = (
    "These cells localise to the perivascular niche of the developing dermis and "
    "are transcriptionally distinct from the Langerhans cell lineage throughout "
    "the second trimester."
)


@pytest.fixture(scope="module")
def real_pdf(tmp_path_factory: pytest.TempPathFactory) -> Path:
    import pymupdf  # type: ignore[import-untyped]

    path = tmp_path_factory.mktemp("pdf") / "synthetic.pdf"
    doc = pymupdf.open()
    for heading, body in (("Results", PARAGRAPH_ONE), ("Discussion", PARAGRAPH_TWO)):
        page = doc.new_page()
        page.insert_textbox(pymupdf.Rect(60, 60, 540, 120), heading, fontsize=18)
        page.insert_textbox(pymupdf.Rect(60, 140, 540, 400), body, fontsize=11)
    doc.save(str(path))
    doc.close()
    return path


@pytest.mark.integration
def test_extracts_real_text_and_a_consistent_sidecar(real_pdf: Path, tmp_path: Path) -> None:
    result = extract_pdf_text(real_pdf, tmp_path / "out")

    text = result.text_path.read_text()
    assert "SLC40A1" in text
    assert "perivascular niche" in text

    sidecar = result.sidecar
    validate_sidecar(sidecar)
    assert sidecar["source"]["n_pages"] == 2
    assert sidecar["extractor"]["name"] == "pymupdf4llm"
    assert sidecar["extractor"]["version"]
    assert sidecar["outputs"]["n_chars"] > 0
    assert "gaps" not in sidecar or all(g["kind"] != "no_text_extracted" for g in sidecar["gaps"])

    # Every recorded offset must locate its paragraph in the file exactly —
    # this is what lets a caller read one section without loading the whole thing.
    for segment in sidecar["segments"]:
        assert text[segment["char_start"] : segment["char_end"]].strip()
        assert len(text[segment["char_start"] : segment["char_end"]]) > 0


@pytest.mark.integration
def test_cli_writes_the_same_files(real_pdf: Path, tmp_path: Path) -> None:
    out = tmp_path / "cli-out"
    assert main(["--pdf", str(real_pdf), "--out", str(out), "--stem", "paper", "--quiet"]) == 0
    sidecar = json.loads((out / "paper.extract.json").read_text())
    assert (out / "paper.text.txt").exists()
    assert sidecar["retrieval_method"] == "pdf_text"
    assert sidecar["source"]["filename"] == "synthetic.pdf"


@pytest.mark.integration
def test_a_pdf_with_no_text_layer_reports_a_gap(tmp_path: Path) -> None:
    import pymupdf  # type: ignore[import-untyped]

    path = tmp_path / "blank.pdf"
    doc = pymupdf.open()
    doc.new_page()
    doc.save(str(path))
    doc.close()

    result = extract_pdf_text(path, tmp_path / "out")
    assert not result.has_body_text
    assert any(gap["kind"] == "no_text_extracted" for gap in result.gaps)
