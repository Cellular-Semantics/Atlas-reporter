#!/usr/bin/env python
"""Claude Code hook: validate subatlas_contributors output against JSON Schema.

Fires as a PostToolUse hook on Write/Edit to ``subatlas_contributors.json``,
which holds either one cell set's contributors view or an array of them (the
whole-project pass). Validates against ``subatlas_contributors.schema.json``.

Beyond the schema, checks the arithmetic the schema cannot express — the ratios
are derived, so a hand-edited or hallucinated file shows up here as internally
inconsistent rather than as plausible-looking numbers:

* ``contribution`` == ``from_source_cells`` / ``n_cells``
* ``purity`` == the dominant label's ``within_source_share``
* ``dominant_label`` is in fact the highest-count label
* listed labels + ``tail_cells`` account for ``from_source_cells``
* ``no_dominant_contributor`` agrees with ``contributors`` being empty

Exit codes:
    0 — valid, or file is not a contributors file, or jsonschema unavailable
    2 — validation failed (Claude sees stderr and self-corrects)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCHEMA_PATH = Path("src/atlas_chat/atlas_chat/schemas/subatlas_contributors.schema.json")

# Ratios are rounded to 4 dp on write, so allow a shade more than half a unit in
# the last place.
TOLERANCE = 1e-4


def _targets(file_path: str) -> bool:
    return Path(file_path).name == "subatlas_contributors.json"


def _schema_errors(data: object, schema: dict) -> list[str]:
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


def _arithmetic_errors(record: dict, prefix: str = "") -> list[str]:
    errors: list[str] = []
    n_cells = record.get("n_cells", 0)
    contributors = record.get("contributors", [])

    has_none = bool(record.get("no_dominant_contributor"))
    if has_none and contributors:
        errors.append(
            f"{prefix}no_dominant_contributor is true but {len(contributors)} "
            "contributor(s) are listed"
        )
    if contributors and not n_cells:
        errors.append(f"{prefix}contributors are listed but n_cells is 0")

    for i, contributor in enumerate(contributors):
        where = f"{prefix}contributors[{i}] ({contributor.get('subatlas_paper')})"
        from_source = contributor.get("from_source_cells", 0)
        labels = contributor.get("labels", [])

        if n_cells:
            expected = from_source / n_cells
            if abs(contributor.get("contribution", -1) - expected) > TOLERANCE:
                errors.append(
                    f"{where}: contribution {contributor.get('contribution')} != "
                    f"from_source_cells/n_cells ({from_source}/{n_cells} = {expected:.4f})"
                )
        if not labels:
            continue

        top = max(labels, key=lambda item: item.get("cell_count", 0))
        if contributor.get("dominant_label") != top.get("transferred_cell_label"):
            errors.append(
                f"{where}: dominant_label is {contributor.get('dominant_label')!r} but "
                f"the highest-count label is {top.get('transferred_cell_label')!r}"
            )
        if from_source:
            expected_purity = top.get("cell_count", 0) / from_source
            if abs(contributor.get("purity", -1) - expected_purity) > TOLERANCE:
                errors.append(
                    f"{where}: purity {contributor.get('purity')} != the dominant "
                    f"label's within_source_share ({expected_purity:.4f})"
                )
        accounted = sum(item.get("cell_count", 0) for item in labels) + contributor.get(
            "tail_cells", 0
        )
        if accounted != from_source:
            errors.append(
                f"{where}: listed labels + tail_cells = {accounted}, but "
                f"from_source_cells = {from_source}"
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
        data = json.loads(content)
    except json.JSONDecodeError as exc:
        print(f"{Path(file_path).name} is not valid JSON: {exc}", file=sys.stderr)
        return 2

    if not SCHEMA_PATH.exists():
        return 0
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        print("jsonschema not available — skipping subatlas_contributors check", file=sys.stderr)
        return 0

    errors = _schema_errors(data, json.loads(SCHEMA_PATH.read_text()))
    if not errors:
        records = data if isinstance(data, list) else [data]
        for i, record in enumerate(records):
            prefix = f"[{i}]." if isinstance(data, list) else ""
            errors.extend(_arithmetic_errors(record, prefix))

    if not errors:
        return 0

    print("SUBATLAS_CONTRIBUTORS VALIDATION FAILED", file=sys.stderr)
    print(
        "This file is derived, not authored — regenerate it with "
        "`python -m atlas_chat.cli_contributors` rather than hand-editing:",
        file=sys.stderr,
    )
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
