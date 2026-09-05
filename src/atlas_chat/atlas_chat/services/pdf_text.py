"""Turn a PDF into plain text on disk.

Deliberately small. It writes three files next to each other and stops:

* ``<stem>.text.txt`` — body paragraphs, blank-line separated, no markup.
* ``<stem>.figure_text.txt`` — text found inside figures, kept apart.
* ``<stem>.extract.json`` — the sidecar described by
  ``pdf_text_extract.schema.json``: what was extracted, by what, from which
  bytes, where each paragraph sits in the text file, and what failed.

No citation extraction, no table reconstruction, no embedding. Whether to load
the result into a context window is the caller's decision, which is the whole
point of separating extraction from consumption.

Two things to know before trusting the output:

* Reading order across columns is not reliably preserved (see
  :mod:`atlas_chat.services._pdf_parser`). The sidecar therefore records
  ``retrieval_method: "pdf_text"`` — a quote spliced across a column boundary
  can pass a substring check against this text even though no human ever read
  those words in that order.
* A scanned PDF yields nothing. That is recorded as a gap, never as an empty
  success.

Requires the ``text-access`` extra::

    uv sync --extra text-access
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import sys
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from atlas_chat.services._pdf_parser import PdfSegment

logger = logging.getLogger(__name__)

EXTRACT_VERSION = 1

#: Paragraphs are joined by a blank line in the text files. Offsets recorded in
#: the sidecar assume exactly this separator.
_PARAGRAPH_SEP = "\n\n"

#: Below this many characters of body text per page, assume something went
#: unread — a mixed scan, a heavily-figured supplement — and record a gap.
_SHORT_TEXT_CHARS_PER_PAGE = 200

#: Extractor callable: takes a PDF path, returns paragraph segments. Injectable
#: so the assembly logic can be tested without a real PDF or pymupdf4llm.
SegmentExtractor = Callable[[Path], list[PdfSegment]]


class PdfTextError(RuntimeError):
    """Extraction could not be attempted or could not complete."""


@dataclass
class PdfTextResult:
    """Where the extraction landed and what the sidecar says about it."""

    text_path: Path
    figure_text_path: Path | None
    sidecar_path: Path
    sidecar: dict[str, Any]

    @property
    def gaps(self) -> list[dict[str, str]]:
        return list(self.sidecar.get("gaps", []))

    @property
    def has_body_text(self) -> bool:
        return self.sidecar["outputs"]["n_chars"] > 0


# ------------------------------------------------------------------
# Reading the PDF
# ------------------------------------------------------------------


def _require_pymupdf4llm() -> Any:
    """Import pymupdf4llm, or say plainly which extra is missing.

    A missing optional dependency must never degrade quietly into a worse
    retrieval path — the caller gets an error naming the fix.
    """
    try:
        import pymupdf4llm  # type: ignore[import-untyped]
    except ImportError as exc:
        raise PdfTextError(
            "pymupdf4llm is not installed — PDF text extraction is unavailable. "
            "Install it with: uv sync --extra text-access"
        ) from exc
    return pymupdf4llm


def _extractor_version() -> str | None:
    from importlib.metadata import PackageNotFoundError, version

    try:
        return version("pymupdf4llm")
    except PackageNotFoundError:  # pragma: no cover - environment guard
        return None


def _page_count(pdf_path: Path) -> int:
    """Page count from the PDF itself, independent of extracted text.

    Many pages plus almost no text is the signature of a scan, so this number
    is worth having even when extraction returns nothing.
    """
    try:
        import pymupdf  # type: ignore[import-untyped]
    except ImportError:  # pragma: no cover - pymupdf ships with pymupdf4llm
        return 0
    try:
        with pymupdf.open(str(pdf_path)) as doc:
            return int(doc.page_count)
    except Exception as exc:
        logger.warning("could not read page count from %s: %s", pdf_path, exc)
        return 0


def _default_extractor(pdf_path: Path) -> list[PdfSegment]:
    from atlas_chat.services._pdf_parser import extract_pdf_segments

    _require_pymupdf4llm()
    try:
        return extract_pdf_segments(pdf_path)
    except Exception as exc:
        raise PdfTextError(f"pymupdf4llm failed on {pdf_path}: {exc}") from exc


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


# ------------------------------------------------------------------
# Assembling the output (pure — no PDF, no filesystem reads)
# ------------------------------------------------------------------


def assemble_text(segments: Sequence[PdfSegment]) -> tuple[str, list[dict[str, Any]]]:
    """Join paragraphs into one string and record where each one landed.

    Returns:
        The text file's contents, and one sidecar segment record per paragraph
        such that ``text[char_start:char_end]`` is exactly that paragraph.
    """
    parts: list[str] = []
    records: list[dict[str, Any]] = []
    cursor = 0
    for index, segment in enumerate(segments):
        if index:
            cursor += len(_PARAGRAPH_SEP)
        records.append(
            {
                "index": index,
                "section": segment.section,
                "char_start": cursor,
                "char_end": cursor + len(segment.text),
            }
        )
        cursor += len(segment.text)
        parts.append(segment.text)
    text = _PARAGRAPH_SEP.join(parts)
    if text:
        text += "\n"
    return text, records


def find_gaps(
    body: Sequence[PdfSegment],
    figures: Sequence[PdfSegment],
    n_pages: int,
) -> list[dict[str, str]]:
    """Say what the extraction did not deliver, so silence is never ambiguous."""
    gaps: list[dict[str, str]] = []
    body_chars = sum(len(s.text) for s in body)

    if not body_chars:
        if figures:
            gaps.append(
                {
                    "kind": "figure_text_only",
                    "detail": (
                        f"No body prose extracted from {n_pages} page(s); the only text "
                        f"found was inside figures ({len(figures)} block(s)). Index it for "
                        "recall if you like, but it is not quotable prose."
                    ),
                }
            )
        gaps.append(
            {
                "kind": "no_text_extracted",
                "detail": (
                    f"No body text came out of {n_pages} page(s). Most likely a scanned or "
                    "image-only PDF; there is no OCR in this path. Treat the paper as "
                    "unread rather than as having no relevant content."
                ),
            }
        )
        return gaps

    if n_pages and body_chars < _SHORT_TEXT_CHARS_PER_PAGE * n_pages:
        gaps.append(
            {
                "kind": "short_text",
                "detail": (
                    f"Only {body_chars} characters of body text across {n_pages} page(s) "
                    f"(under {_SHORT_TEXT_CHARS_PER_PAGE}/page). Parts of the document are "
                    "probably images or an unreadable layout."
                ),
            }
        )
    return gaps


def build_sidecar(
    *,
    pdf_path: Path,
    sha256: str,
    n_bytes: int,
    n_pages: int,
    extractor_name: str,
    extractor_version: str | None,
    extracted_at: str,
    text_file: str,
    figure_text_file: str | None,
    body: Sequence[PdfSegment],
    figures: Sequence[PdfSegment],
    body_records: Sequence[dict[str, Any]],
    figure_records: Sequence[dict[str, Any]],
    gaps: Sequence[dict[str, str]],
) -> dict[str, Any]:
    """Build the sidecar object. Validated by the caller before it is written."""
    sidecar: dict[str, Any] = {
        "extract_version": EXTRACT_VERSION,
        "retrieval_method": "pdf_text",
        "source": {
            "filename": pdf_path.name,
            "path": str(pdf_path),
            "sha256": sha256,
            "n_bytes": n_bytes,
            "n_pages": n_pages,
        },
        "extractor": {
            "name": extractor_name,
            "version": extractor_version,
            "extracted_at": extracted_at,
        },
        "outputs": {
            "text_file": text_file,
            "figure_text_file": figure_text_file,
            "n_chars": sum(len(s.text) for s in body),
            "n_figure_chars": sum(len(s.text) for s in figures),
            "n_segments": len(body),
            "n_figure_segments": len(figures),
        },
        "segments": list(body_records),
        "figure_segments": list(figure_records),
    }
    if gaps:
        sidecar["gaps"] = list(gaps)
    return sidecar


def validate_sidecar(sidecar: dict[str, Any]) -> None:
    """Validate against ``pdf_text_extract.schema.json``.

    Raises:
        PdfTextError: On the first schema violation, with the JSON path.
    """
    import jsonschema  # type: ignore[import-untyped]

    from atlas_chat.schemas import load_schema

    try:
        jsonschema.validate(sidecar, load_schema("pdf_text_extract.schema.json"))
    except jsonschema.ValidationError as exc:
        location = "/".join(str(part) for part in exc.absolute_path) or "(root)"
        raise PdfTextError(f"extract sidecar invalid at {location}: {exc.message}") from exc


# ------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------


def extract_pdf_text(
    pdf_path: str | Path,
    out_dir: str | Path,
    *,
    stem: str | None = None,
    include_figure_text: bool = True,
    extractor: SegmentExtractor | None = None,
    extractor_name: str = "pymupdf4llm",
    extractor_version: str | None = None,
) -> PdfTextResult:
    """Extract a PDF's text to ``out_dir`` and return what was written.

    The output directory is an argument, never derived: nothing here knows
    about project layouts.

    Args:
        pdf_path: The PDF to read.
        out_dir: Directory to write into. Created if absent.
        stem: Base name for the output files. Defaults to the PDF's stem.
        include_figure_text: Write figure-internal text to its own file.
            Off means figure text is dropped, not folded into the body.
        extractor: Override the segment extractor (used by tests).
        extractor_name: Recorded in the sidecar.
        extractor_version: Recorded in the sidecar; looked up when omitted.

    Returns:
        PdfTextResult: Paths written and the sidecar object.

    Raises:
        PdfTextError: The PDF is missing, the dependency is absent, or the
            extractor failed. An unreadable *but valid* PDF is not an error —
            it produces an empty text file and a gap.
    """
    pdf = Path(pdf_path)
    if not pdf.is_file():
        raise PdfTextError(f"no such PDF: {pdf}")

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    base = stem or pdf.stem

    read_segments = extractor or _default_extractor
    if extractor is None:
        extractor_version = extractor_version or _extractor_version()

    segments = read_segments(pdf)
    body = [s for s in segments if s.section != "IN_FIGURE"]
    figures = [s for s in segments if s.section == "IN_FIGURE"]

    n_pages = _page_count(pdf) if extractor is None else 0

    text, body_records = assemble_text(body)
    text_name = f"{base}.text.txt"
    (out / text_name).write_text(text, encoding="utf-8")

    figure_name: str | None = None
    figure_records: list[dict[str, Any]] = []
    if include_figure_text and figures:
        figure_text, figure_records = assemble_text(figures)
        figure_name = f"{base}.figure_text.txt"
        (out / figure_name).write_text(figure_text, encoding="utf-8")
    elif not include_figure_text:
        figures = []

    sidecar = build_sidecar(
        pdf_path=pdf,
        sha256=sha256_of(pdf),
        n_bytes=pdf.stat().st_size,
        n_pages=n_pages,
        extractor_name=extractor_name,
        extractor_version=extractor_version,
        extracted_at=datetime.now(UTC).isoformat(timespec="seconds"),
        text_file=text_name,
        figure_text_file=figure_name,
        body=body,
        figures=figures,
        body_records=body_records,
        figure_records=figure_records,
        gaps=find_gaps(body, figures, n_pages),
    )
    validate_sidecar(sidecar)

    sidecar_path = out / f"{base}.extract.json"
    sidecar_path.write_text(json.dumps(sidecar, indent=2) + "\n", encoding="utf-8")

    logger.info(
        "extracted %d chars in %d paragraphs from %s -> %s",
        sidecar["outputs"]["n_chars"],
        sidecar["outputs"]["n_segments"],
        pdf.name,
        out / text_name,
    )
    return PdfTextResult(
        text_path=out / text_name,
        figure_text_path=(out / figure_name) if figure_name else None,
        sidecar_path=sidecar_path,
        sidecar=sidecar,
    )


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="atlas_chat.cli_pdf_text",
        description=(
            "Write a PDF's text to disk as plain text plus a sidecar JSON. "
            "Deciding whether to read the result is the caller's job."
        ),
    )
    parser.add_argument("--pdf", required=True, help="path to the PDF")
    parser.add_argument("--out", required=True, help="directory to write into")
    parser.add_argument("--stem", help="base name for output files (default: the PDF's stem)")
    parser.add_argument(
        "--no-figure-text",
        action="store_true",
        help="drop figure-internal text instead of writing it to its own file",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="print only the sidecar path, not the sidecar itself",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI. Returns 0 on text, 2 when the PDF yielded none, 1 on error."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = build_parser().parse_args(argv)
    try:
        result = extract_pdf_text(
            args.pdf,
            args.out,
            stem=args.stem,
            include_figure_text=not args.no_figure_text,
        )
    except PdfTextError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if args.quiet:
        print(result.sidecar_path)
    else:
        print(json.dumps(result.sidecar, indent=2))

    if not result.has_body_text:
        print(
            f"no body text extracted from {args.pdf} — see the gaps in {result.sidecar_path}",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())


__all__ = [
    "EXTRACT_VERSION",
    "PdfTextError",
    "PdfTextResult",
    "assemble_text",
    "build_parser",
    "build_sidecar",
    "extract_pdf_text",
    "find_gaps",
    "main",
    "sha256_of",
    "validate_sidecar",
]
