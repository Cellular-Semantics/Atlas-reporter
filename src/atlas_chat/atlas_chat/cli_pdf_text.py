"""CLI for PDF text extraction.

Thin entry point so a PDF can be turned into text without a Claude Code
session:

.. code-block:: bash

    python -m atlas_chat.cli_pdf_text --pdf paper.pdf --out ./text
    atlas-pdf-text --pdf supp1.pdf --out ./text --no-figure-text

Exit codes: 0 on text extracted, 2 when the PDF yielded none (the sidecar
records the gap), 1 on error.

The implementation lives in :mod:`atlas_chat.services.pdf_text`.
"""

from __future__ import annotations

from atlas_chat.services.pdf_text import build_parser, main

__all__ = ["build_parser", "main"]

if __name__ == "__main__":
    raise SystemExit(main())
