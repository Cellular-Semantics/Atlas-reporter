#!/usr/bin/env python
"""Claude Code hook: check a subatlas routing plan against its routing table.

Fires as a PostToolUse hook on Write/Edit to ``*routing_plan.json``. Validates
against ``subatlas_routing_plan.schema.json``, then checks the plan against the
table it names in ``table_source``:

* every paper-and-label pair the plan asks about exists in the table;
* every cell set a question claims to serve is listed as a claimant of that
  question in the table;
* every cell set the table was built for is either served or accounted for in
  ``atlas_only``.

The last is the one that matters most: a cell set falling out of both becomes a
report written with no upstream evidence and nothing saying why.

Exit codes:
    0 — valid, or the file is not a routing plan, or jsonschema is unavailable
    2 — validation failed (Claude sees stderr and self-corrects)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCHEMA_PATH = Path("src/atlas_chat/atlas_chat/schemas/subatlas_routing_plan.schema.json")


def _targets(file_path: str) -> bool:
    return Path(file_path).name.endswith("routing_plan.json")


def _schema_errors(data: object, schema: dict) -> list[str]:
    import jsonschema

    validator = jsonschema.Draft202012Validator(schema)
    errors = []
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        path = ".".join(str(p) for p in err.absolute_path)
        errors.append(f"{path or '(root)'}: {err.message}")
    return errors


def _table_errors(plan: dict, table: dict) -> list[str]:
    errors: list[str] = []
    claimants: dict[tuple[str, str], set[str]] = {}
    for question in table.get("questions") or []:
        key = (question["subatlas_paper"], question["subatlas_cell_label"])
        claimants[key] = {c["cell_label"] for c in question["atlas_cell_sets"]}

    served: set[str] = set()
    for paper in plan.get("papers") or []:
        study = paper["subatlas_paper"]
        for question in paper.get("questions") or []:
            key = (study, question["subatlas_cell_label"])
            if key not in claimants:
                errors.append(
                    f"{study} is not asked about {question['subatlas_cell_label']!r} "
                    "in the table — copy the label verbatim, or drop the question"
                )
                continue
            for label in question.get("serves") or []:
                if label not in claimants[key]:
                    errors.append(
                        f"{question['subatlas_cell_label']!r} does not feed {label!r} "
                        "in the table"
                    )
                else:
                    served.add(label)

    accounted = served | {a["cell_label"] for a in plan.get("atlas_only") or []}
    missing = [
        r["cell_label"] for r in table.get("requested") or [] if r["cell_label"] not in accounted
    ]
    if missing:
        errors.append(
            "requested but neither served nor listed as atlas_only: " + ", ".join(sorted(missing))
        )
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
        plan = json.loads(content)
    except json.JSONDecodeError as exc:
        print(f"{Path(file_path).name} is not valid JSON: {exc}", file=sys.stderr)
        return 2

    if not SCHEMA_PATH.exists():
        return 0
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        print("jsonschema not available — skipping routing plan check", file=sys.stderr)
        return 0

    errors = _schema_errors(plan, json.loads(SCHEMA_PATH.read_text()))

    table_source = plan.get("table_source")
    if not errors:
        if not table_source:
            errors.append("no table_source — the plan cannot be checked against its table")
        elif not Path(table_source).exists():
            errors.append(f"table_source {table_source} does not exist")
        else:
            errors.extend(
                _table_errors(plan, json.loads(Path(table_source).read_text(encoding="utf-8")))
            )

    if not errors:
        return 0

    print("SUBATLAS ROUTING PLAN VALIDATION FAILED", file=sys.stderr)
    print(f"Fix these issues and rewrite {Path(file_path).name}:", file=sys.stderr)
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
