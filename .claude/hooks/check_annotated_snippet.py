#!/usr/bin/env python
"""Claude Code hook: validate annotated_snippet output against JSON Schema.

Fires as a PostToolUse hook on Write/Edit to the raw traversal records —
``annotated_snippets_hop<n>.json`` (an array) or any ``*annotated_snippet.json``
(a single record). Validates against ``annotated_snippet.schema.json``.

Exit codes:
    0 — valid, or file is not an annotated-snippet file, or jsonschema unavailable
    2 — validation failed (Claude sees stderr and self-corrects)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCHEMA_PATH = Path("src/atlas_chat/atlas_chat/schemas/annotated_snippet.schema.json")


def _targets(file_path: str) -> bool:
    name = Path(file_path).name
    return name.startswith("annotated_snippets_hop") or name.endswith("annotated_snippet.json")


def _errors(data: object, schema: dict) -> list[str]:
    import jsonschema

    validator = jsonschema.Draft202012Validator(schema)
    items = data if isinstance(data, list) else [data]
    errors: list[str] = []
    for i, item in enumerate(items):
        prefix = f"[{i}]" if isinstance(data, list) else ""
        for err in sorted(validator.iter_errors(item), key=lambda e: list(e.path)):
            path = ".".join(str(p) for p in err.absolute_path)
            loc = f"{prefix}.{path}" if path else (prefix or "(root)")
            errors.append(f"{loc}: {err.message}")
    return errors


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

    if not SCHEMA_PATH.exists():
        return 0
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        print("jsonschema not available — skipping annotated_snippet check", file=sys.stderr)
        return 0

    errors = _errors(data, json.loads(SCHEMA_PATH.read_text()))
    if not errors:
        return 0

    print("ANNOTATED_SNIPPET VALIDATION FAILED", file=sys.stderr)
    print(f"Fix these issues and rewrite {Path(file_path).name}:", file=sys.stderr)
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
