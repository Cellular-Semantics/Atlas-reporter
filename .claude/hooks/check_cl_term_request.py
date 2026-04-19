#!/usr/bin/env python
"""Claude Code hook: validate cl_term_request.json against JSON Schema.

Invoked as a PostToolUse hook when a Write tool targets a file named
``cl_term_request.json``.

Exit codes:
    0 — valid, or file is not a cl_term_request.json
    2 — validation failed (Claude sees stderr and self-corrects)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCHEMA_PATH = Path("src/atlas_chat/atlas_chat/schemas/cl_term_request.schema.json")


def main() -> int:
    try:
        hook_input = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, OSError):
        return 0

    tool_input = hook_input.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if not file_path or not file_path.endswith("cl_term_request.json"):
        return 0

    content = tool_input.get("content", "")
    if not content:
        print("cl_term_request.json is empty", file=sys.stderr)
        return 2

    try:
        data = json.loads(content)
    except json.JSONDecodeError as exc:
        print(f"cl_term_request.json is not valid JSON: {exc}", file=sys.stderr)
        return 2

    # Schema-based validation
    if SCHEMA_PATH.exists():
        try:
            import jsonschema

            schema = json.loads(SCHEMA_PATH.read_text())
            errors = []
            validator = jsonschema.Draft202012Validator(schema)
            for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
                path = ".".join(str(p) for p in error.absolute_path) or "(root)"
                errors.append(f"{path}: {error.message}")
        except ImportError:
            errors = _validate_inline(data)
    else:
        errors = _validate_inline(data)

    # Additional semantic checks beyond schema
    errors.extend(_semantic_checks(data))

    if not errors:
        return 0

    print("CL TERM REQUEST VALIDATION FAILED", file=sys.stderr)
    print("Fix these issues and rewrite cl_term_request.json:", file=sys.stderr)
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    return 2


def _semantic_checks(data: dict) -> list[str]:
    """Cross-field validation beyond what JSON Schema catches."""
    errors = []

    # Definition word count (80-120)
    defn = data.get("definition", "")
    if defn:
        word_count = len(defn.split())
        if word_count < 60:
            errors.append(
                f"Definition is {word_count} words; CL guidelines require 80-120. "
                "Consider adding more detail."
            )
        elif word_count > 150:
            errors.append(
                f"Definition is {word_count} words; CL guidelines require 80-120. "
                "Consider trimming."
            )

    # Definition should not start with the suggested label
    label = data.get("suggested_label", "").lower()
    if label and defn.lower().startswith(label):
        errors.append(
            "Definition must not start by naming the cell type being defined "
            "(CL guideline: start with general classification)."
        )

    # ntr_markdown should contain key sections
    ntr = data.get("ntr_markdown", "")
    if ntr:
        for section in [
            "Preferred term label",
            "Synonyms",
            "Definition",
            "Parent cell type term",
            "Anatomical structure",
        ]:
            if section not in ntr:
                errors.append(f"ntr_markdown missing section: '{section}'")

    return errors


def _validate_inline(data: dict) -> list[str]:
    """Fallback validation without jsonschema library."""
    errors = []

    for field in [
        "cell_type_label", "suggested_label", "definition",
        "justification", "ntr_markdown",
    ]:
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"Missing or empty required field: '{field}'")

    for obj_field, id_key, id_prefix in [
        ("parent_term", "cl_id", "CL:"),
        ("anatomical_location", "uberon_id", "UBERON:"),
    ]:
        obj = data.get(obj_field)
        if not isinstance(obj, dict):
            errors.append(f"'{obj_field}' must be an object")
        else:
            id_val = obj.get(id_key, "")
            if not id_val or not id_val.startswith(id_prefix):
                errors.append(f"{obj_field}.{id_key} must start with '{id_prefix}'")

    axioms = data.get("logical_axioms")
    if not isinstance(axioms, list) or len(axioms) == 0:
        errors.append("'logical_axioms' must be a non-empty list")

    refs = data.get("references")
    if not isinstance(refs, list) or len(refs) == 0:
        errors.append("'references' must be a non-empty list")

    synonyms = data.get("synonyms")
    if not isinstance(synonyms, list):
        errors.append("'synonyms' must be a list")

    allowed_top = {
        "cell_type_label", "suggested_label", "definition", "parent_term",
        "anatomical_location", "logical_axioms", "synonyms", "references",
        "justification", "ntr_markdown",
    }
    extra = set(data.keys()) - allowed_top
    if extra:
        errors.append(f"Extra top-level fields not allowed: {extra}")

    return errors


if __name__ == "__main__":
    sys.exit(main())
