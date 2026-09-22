#!/usr/bin/env python
"""Claude Code hook: validate a project's CAS+ document against JSON Schema.

Fires as a PostToolUse hook on Write/Edit to a project's CAS+ config —
``cas.json`` — validating against ``cas_annotation.schema.json``. The generate-cas
skill produces this file (it is agent output), so schema compliance is enforced
here.

It also recomputes the three subatlas overlap measures on every transferred
annotation. They are stored rather than derived on read, so that the file can be
read directly by a person or an agent without arithmetic; storing them is only
safe if something checks them, and this is that something.

Exit codes:
    0 — valid, or file is not a cas.json, or jsonschema unavailable
    2 — validation failed (Claude sees stderr and self-corrects)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCHEMA_PATH = Path("src/atlas_chat/atlas_chat/schemas/cas_annotation.schema.json")


def _targets(file_path: str) -> bool:
    return Path(file_path).name == "cas.json"


#: Stored ratios are rounded, so a recomputed value is compared within this.
TOLERANCE = 5e-4

#: measure -> (numerator field, denominator field). cell_ratio divides by the
#: cell set's own n_cells, which lives on the annotation rather than the transfer.
MEASURES = {
    "share_of_subatlas_contribution": ("cell_count", "subatlas_contribution_cells"),
    "share_of_subatlas_label": ("cell_count", "subatlas_label_total_cells"),
    "cell_ratio": ("cell_count", None),
}


def _measure_errors(data: object) -> list[str]:
    """Recompute each stored overlap measure from the counts beside it.

    A measure whose denominator is absent is skipped rather than failed: the
    counting and registry passes write at different times, and a transfer that
    has not reached the later one yet is not wrong.
    """
    if not isinstance(data, dict):
        return []
    errors: list[str] = []
    for annotation in data.get("annotations") or []:
        if not isinstance(annotation, dict):
            continue
        label = annotation.get("cell_label", "?")
        for transfer in annotation.get("transferred_annotations") or []:
            if not isinstance(transfer, dict):
                continue
            for measure, (num_field, den_field) in MEASURES.items():
                stored = transfer.get(measure)
                if stored is None:
                    continue
                numerator = transfer.get(num_field)
                denominator = (
                    annotation.get("n_cells") if den_field is None else transfer.get(den_field)
                )
                if numerator is None or not denominator:
                    continue
                expected = numerator / denominator
                if abs(expected - stored) > TOLERANCE:
                    where = f"{label} / {transfer.get('transferred_cell_label', '?')}"
                    errors.append(
                        f"{where}: {measure} is {stored}, but "
                        f"{num_field} / {den_field or 'n_cells'} = "
                        f"{numerator}/{denominator} = {expected:.4f}"
                    )
    return errors


def _errors(data: object, schema: dict) -> list[str]:
    import jsonschema

    validator = jsonschema.Draft202012Validator(schema)
    errors: list[str] = []
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
        return 0
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        print("jsonschema not available — skipping cas_annotation check", file=sys.stderr)
        return 0

    errors = _errors(data, json.loads(SCHEMA_PATH.read_text()))
    errors.extend(_measure_errors(data))
    if not errors:
        return 0

    print("CAS_ANNOTATION VALIDATION FAILED", file=sys.stderr)
    print(f"Fix these issues and rewrite {Path(file_path).name}:", file=sys.stderr)
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
