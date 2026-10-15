#!/usr/bin/env python
"""Claude Code hook: validate a DEG document written by hand.

Fires as a PostToolUse hook on Write/Edit under a ``degs/`` directory.

It is a second line only. These documents are normally written by a conversion
script the agent wrote, and a file written by a script never passes through a
tool hook — which is why the skill requires ``cli_degs`` to be run over the
store afterwards. This catches the other case.

Exit codes:
    0 — valid, or not a DEG document, or jsonschema unavailable
    2 — invalid (Claude sees stderr and self-corrects)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def _targets(file_path: str) -> bool:
    path = Path(file_path)
    return path.suffix == ".json" and path.parent.name == "degs"


def main() -> int:
    try:
        hook_input = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, OSError):
        return 0

    tool_input = hook_input.get("tool_input", {})
    file_path = tool_input.get("file_path", "")
    if not file_path or not _targets(file_path):
        return 0

    content = tool_input.get("content", "")
    if not content:
        print(f"{Path(file_path).name} is empty", file=sys.stderr)
        return 2
    try:
        data = json.loads(content)
    except json.JSONDecodeError as exc:
        print(f"{Path(file_path).name} is not valid JSON: {exc}", file=sys.stderr)
        return 2

    try:
        from atlas_chat.services.degs import validate_document
    except ImportError:
        return 0
    try:
        errors = validate_document(data)
    except ImportError:
        print("jsonschema not available — skipping DEG check", file=sys.stderr)
        return 0
    if not errors:
        return 0

    print("DEG VALIDATION FAILED", file=sys.stderr)
    print(f"Fix these and rewrite {Path(file_path).name}:", file=sys.stderr)
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
