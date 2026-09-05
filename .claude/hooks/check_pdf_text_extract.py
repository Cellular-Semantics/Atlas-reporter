#!/usr/bin/env python
"""Claude Code hook: validate a PDF text-extraction sidecar.

Runs as a PostToolUse hook on Write/Edit. Fires only for files named
``*.extract.json``, which is what
:func:`atlas_chat.services.pdf_text.extract_pdf_text` writes.

The schema is the source of truth and the check comes from the service rather
than being restated here:
:func:`atlas_chat.services.pdf_text.validate_sidecar`.

Exit codes:
    0 — valid, or not an extraction sidecar
    2 — validation failed (Claude sees stderr and self-corrects)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def _is_extract_sidecar(file_path: str) -> bool:
    return file_path.endswith(".extract.json")


def main() -> int:
    try:
        hook_input = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, OSError):
        return 0

    tool_input = hook_input.get("tool_input", {})
    file_path = tool_input.get("file_path", "")
    if not file_path or not _is_extract_sidecar(file_path):
        return 0

    # Prefer what is on disk: PostToolUse runs after the write, and an Edit
    # carries no full content in tool_input.
    raw = tool_input.get("content", "")
    path = Path(file_path)
    if path.exists():
        raw = path.read_text(encoding="utf-8")
    if not raw.strip():
        print("extraction sidecar is empty", file=sys.stderr)
        return 2

    try:
        sidecar = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"extraction sidecar is not valid JSON: {exc}", file=sys.stderr)
        return 2

    try:
        from atlas_chat.services.pdf_text import PdfTextError, validate_sidecar
    except ImportError as exc:  # pragma: no cover - environment guard
        print(f"cannot import pdf_text to validate: {exc}", file=sys.stderr)
        return 0

    try:
        validate_sidecar(sidecar)
    except PdfTextError as exc:
        print("PDF EXTRACT SIDECAR VALIDATION FAILED", file=sys.stderr)
        print(f"Fix this issue in {file_path}:", file=sys.stderr)
        print(f"  - {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
