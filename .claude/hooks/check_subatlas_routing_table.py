#!/usr/bin/env python
"""Claude Code hook: validate a subatlas routing table against JSON Schema.

Fires as a PostToolUse hook on Write/Edit to ``*routing_table.json``. The table
is written by ``atlas_chat.cli_route`` and is not meant to be edited by hand:
the point of this check is to catch a table that has been, since the routing
plan is validated against it and a hand-loosened table would quietly widen what
a plan is allowed to claim.

Exit codes:
    0 — valid, or the file is not a routing table, or jsonschema is unavailable
    2 — validation failed (Claude sees stderr and self-corrects)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

#: The checkout this hook belongs to. Taken from the hook's own location,
#: because a hook runs with whatever working directory its agent had, and an
#: agent working in a subdirectory would otherwise find no schema and pass
#: everything it was given.
REPO_ROOT = Path(__file__).resolve().parents[2]

SCHEMA_PATH = REPO_ROOT / "src/atlas_chat/atlas_chat/schemas/subatlas_routing_table.schema.json"


def _targets(file_path: str) -> bool:
    return Path(file_path).name.endswith("routing_table.json")


def _errors(data: object, schema: dict) -> list[str]:
    import jsonschema

    validator = jsonschema.Draft202012Validator(schema)
    errors = []
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        path = ".".join(str(p) for p in err.absolute_path)
        errors.append(f"{path or '(root)'}: {err.message}")
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
        print(f"no schema at {SCHEMA_PATH} — not checked", file=sys.stderr)
        return 0
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        print("jsonschema not available — skipping routing table check", file=sys.stderr)
        return 0

    errors = _errors(data, json.loads(SCHEMA_PATH.read_text()))
    if not errors:
        return 0

    print("SUBATLAS ROUTING TABLE VALIDATION FAILED", file=sys.stderr)
    print(
        "Regenerate it with python -m atlas_chat.cli_route rather than editing it:",
        file=sys.stderr,
    )
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
