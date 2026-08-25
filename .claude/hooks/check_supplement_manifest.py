#!/usr/bin/env python
"""Claude Code hook: validate a supplement store manifest.json.

Runs as a PostToolUse hook on Write/Edit. Fires only for a ``manifest.json``
under a ``supplements/`` path, so it does not collide with the local-index
manifests (which live under ``local_index/``).

Both checks come from the service rather than being restated here — the schema
is the source of truth and the cross-field rules live next to the code that
writes manifests:

* :func:`atlas_chat.services.supplement_store.validate_manifest` — shape.
* :func:`atlas_chat.services.supplement_store.cross_check_manifest` — the rules
  a schema cannot express, e.g. a table pointing at a file that isn't present.

Exit codes:
    0 — valid, or not a supplement manifest
    2 — validation failed (Claude sees stderr and self-corrects)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def _is_supplement_manifest(file_path: str) -> bool:
    path = Path(file_path)
    if path.name != "manifest.json":
        return False
    return "supplements" in path.parts


def main() -> int:
    try:
        hook_input = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, OSError):
        return 0

    tool_input = hook_input.get("tool_input", {})
    file_path = tool_input.get("file_path", "")
    if not file_path or not _is_supplement_manifest(file_path):
        return 0

    # Prefer what is on disk: PostToolUse runs after the write, and an Edit
    # carries no full content in tool_input.
    raw = tool_input.get("content", "")
    path = Path(file_path)
    if path.exists():
        raw = path.read_text(encoding="utf-8")
    if not raw.strip():
        print("supplement manifest is empty", file=sys.stderr)
        return 2

    try:
        manifest = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"supplement manifest is not valid JSON: {exc}", file=sys.stderr)
        return 2

    try:
        from atlas_chat.services.supplement_store import (
            SupplementStoreError,
            cross_check_manifest,
            validate_manifest,
        )
    except ImportError as exc:  # pragma: no cover - environment guard
        print(f"cannot import supplement_store to validate: {exc}", file=sys.stderr)
        return 0

    errors: list[str] = []
    try:
        validate_manifest(manifest)
    except SupplementStoreError as exc:
        errors.append(str(exc))
    else:
        errors.extend(cross_check_manifest(manifest))

    if not errors:
        return 0

    print("SUPPLEMENT MANIFEST VALIDATION FAILED", file=sys.stderr)
    print(f"Fix these issues in {file_path}:", file=sys.stderr)
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
