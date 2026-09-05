"""Unit tests for the PDF → text-on-disk service.

The extractor is injected, so these run without pymupdf4llm: what is under test
is the assembly (offsets, file layout, sidecar shape, gap reporting), not
pymupdf's parsing, which ``test_pdf_parser.py`` and the integration test cover.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from atlas_chat.services._pdf_parser import PdfSegment
from atlas_chat.services.pdf_text import (
    PdfTextError,
    assemble_text,
    extract_pdf_text,
    find_gaps,
    main,
    validate_sidecar,
)

BODY = [
    PdfSegment(section="Introduction", text="Prenatal skin harbours four macrophage subsets."),
    PdfSegment(section="Results", text="Iron-recycling macrophages express SLC40A1 and CD5L."),
]
FIGURES = [PdfSegment(section="IN_FIGURE", text="UMAP1 UMAP2 HRG SLC40A1 CD5L")]


def _fake_pdf(tmp_path: Path, name: str = "paper.pdf") -> Path:
    pdf = tmp_path / name
    pdf.write_bytes(b"%PDF-1.7 not really a pdf")
    return pdf


def _extract(segments: list[PdfSegment]):
    return lambda _path: list(segments)


@pytest.mark.unit
def test_offsets_locate_each_paragraph_exactly() -> None:
    text, records = assemble_text(BODY)
    for record, segment in zip(records, BODY, strict=True):
        assert text[record["char_start"] : record["char_end"]] == segment.text
    assert records[0]["section"] == "Introduction"


@pytest.mark.unit
def test_empty_input_gives_empty_text() -> None:
    text, records = assemble_text([])
    assert text == ""
    assert records == []


@pytest.mark.unit
def test_writes_text_figure_and_sidecar(tmp_path: Path) -> None:
    pdf = _fake_pdf(tmp_path)
    out = tmp_path / "out"

    result = extract_pdf_text(pdf, out, extractor=_extract(BODY + FIGURES))

    assert result.text_path.name == "paper.text.txt"
    assert result.figure_text_path is not None
    body_text = result.text_path.read_text()
    assert "SLC40A1 and CD5L" in body_text
    # Figure text is kept out of the body file — it is not quotable prose.
    assert "UMAP1" not in body_text
    assert "UMAP1" in result.figure_text_path.read_text()

    sidecar = json.loads(result.sidecar_path.read_text())
    assert sidecar["retrieval_method"] == "pdf_text"
    assert sidecar["outputs"]["n_segments"] == 2
    assert sidecar["outputs"]["n_figure_segments"] == 1
    assert sidecar["source"]["sha256"] and len(sidecar["source"]["sha256"]) == 64
    validate_sidecar(sidecar)


@pytest.mark.unit
def test_no_figure_text_flag_drops_figures(tmp_path: Path) -> None:
    result = extract_pdf_text(
        _fake_pdf(tmp_path),
        tmp_path / "out",
        include_figure_text=False,
        extractor=_extract(BODY + FIGURES),
    )
    assert result.figure_text_path is None
    assert result.sidecar["outputs"]["figure_text_file"] is None
    assert not (tmp_path / "out" / "paper.figure_text.txt").exists()


@pytest.mark.unit
def test_stem_overrides_output_names(tmp_path: Path) -> None:
    result = extract_pdf_text(
        _fake_pdf(tmp_path), tmp_path / "out", stem="supp1", extractor=_extract(BODY)
    )
    assert result.text_path.name == "supp1.text.txt"
    assert result.sidecar_path.name == "supp1.extract.json"


@pytest.mark.unit
def test_image_only_pdf_reports_a_gap_not_an_empty_success(tmp_path: Path) -> None:
    result = extract_pdf_text(_fake_pdf(tmp_path), tmp_path / "out", extractor=_extract([]))
    assert not result.has_body_text
    assert [g["kind"] for g in result.gaps] == ["no_text_extracted"]
    validate_sidecar(result.sidecar)


@pytest.mark.unit
def test_figure_text_only_is_called_out() -> None:
    kinds = [g["kind"] for g in find_gaps([], FIGURES, n_pages=3)]
    assert kinds == ["figure_text_only", "no_text_extracted"]


@pytest.mark.unit
def test_thin_extraction_flagged_as_short_text() -> None:
    thin = [PdfSegment(section="BODY", text="x" * 100)]
    assert [g["kind"] for g in find_gaps(thin, [], n_pages=10)] == ["short_text"]
    assert find_gaps(thin, [], n_pages=0) == []


@pytest.mark.unit
def test_missing_pdf_is_an_error(tmp_path: Path) -> None:
    with pytest.raises(PdfTextError, match="no such PDF"):
        extract_pdf_text(tmp_path / "nope.pdf", tmp_path / "out", extractor=_extract(BODY))


@pytest.mark.unit
def test_sidecar_rejects_drift() -> None:
    with pytest.raises(PdfTextError, match="invalid at"):
        validate_sidecar({"extract_version": 1})


@pytest.mark.unit
def test_cli_exits_2_when_nothing_came_out(tmp_path: Path, monkeypatch) -> None:
    pdf = _fake_pdf(tmp_path)
    monkeypatch.setattr(
        "atlas_chat.services.pdf_text._default_extractor", lambda _path: [], raising=True
    )
    assert main(["--pdf", str(pdf), "--out", str(tmp_path / "out"), "--quiet"]) == 2


@pytest.mark.unit
def test_cli_exits_0_and_prints_the_sidecar(tmp_path: Path, capsys, monkeypatch) -> None:
    pdf = _fake_pdf(tmp_path)
    monkeypatch.setattr(
        "atlas_chat.services.pdf_text._default_extractor", lambda _path: list(BODY), raising=True
    )
    assert main(["--pdf", str(pdf), "--out", str(tmp_path / "out")]) == 0
    printed = json.loads(capsys.readouterr().out)
    assert printed["outputs"]["n_segments"] == 2


@pytest.mark.unit
def test_cli_reports_a_missing_dependency_rather_than_degrading(
    tmp_path: Path, capsys, monkeypatch
) -> None:
    def _boom(_path: Path) -> list[PdfSegment]:
        raise PdfTextError("pymupdf4llm is not installed — uv sync --extra text-access")

    monkeypatch.setattr("atlas_chat.services.pdf_text._default_extractor", _boom, raising=True)
    assert main(["--pdf", str(_fake_pdf(tmp_path)), "--out", str(tmp_path / "out")]) == 1
    assert "text-access" in capsys.readouterr().err
