"""PostToolUse hook regression for check_pdf_text_extract.py.

Drives the hook via subprocess, like the other hook regressions: a valid
sidecar exits 0, a drifted one exits 2, and anything not named
``*.extract.json`` is ignored.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
HOOK = REPO_ROOT / ".claude" / "hooks" / "check_pdf_text_extract.py"

VALID: dict[str, Any] = {
    "extract_version": 1,
    "retrieval_method": "pdf_text",
    "source": {
        "filename": "paper.pdf",
        "path": "store/paper.pdf",
        "sha256": "a" * 64,
        "n_bytes": 1024,
        "n_pages": 12,
    },
    "extractor": {
        "name": "pymupdf4llm",
        "version": "0.0.17",
        "extracted_at": "2026-08-01T10:00:00+00:00",
    },
    "outputs": {
        "text_file": "paper.text.txt",
        "figure_text_file": None,
        "n_chars": 40000,
        "n_figure_chars": 0,
        "n_segments": 120,
        "n_figure_segments": 0,
    },
    "segments": [{"index": 0, "section": "Results", "char_start": 0, "char_end": 42}],
    "figure_segments": [],
}


def _run_hook(file_path: str, payload: object) -> subprocess.CompletedProcess:
    hook_input = json.dumps(
        {"tool_input": {"file_path": file_path, "content": json.dumps(payload)}}
    )
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=hook_input,
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


@pytest.mark.unit
def test_hook_accepts_a_valid_sidecar() -> None:
    assert _run_hook("out/paper.extract.json", VALID).returncode == 0


@pytest.mark.unit
def test_hook_rejects_an_unknown_field() -> None:
    drifted = {**VALID, "notes": "hand-added"}
    result = _run_hook("out/paper.extract.json", drifted)
    assert result.returncode == 2
    assert "VALIDATION FAILED" in result.stderr


@pytest.mark.unit
def test_hook_rejects_a_wrong_retrieval_method() -> None:
    # The whole point of the field: PDF text must not be labelled as JATS.
    wrong = {**VALID, "retrieval_method": "jats"}
    assert _run_hook("out/paper.extract.json", wrong).returncode == 2


@pytest.mark.unit
def test_hook_ignores_other_json() -> None:
    assert _run_hook("out/manifest.json", {"anything": True}).returncode == 0
