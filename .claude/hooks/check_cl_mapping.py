#!/usr/bin/env python
"""Claude Code hook: validate cl_mapping.json against JSON Schema.

Invoked as a PostToolUse hook when a Write tool targets a file named
``cl_mapping.json``.  Validates the output against the canonical schema at
``src/atlas_chat/atlas_chat/schemas/cl_mapping.schema.json``.

Exit codes:
    0 — valid, or file is not a cl_mapping.json
    2 — validation failed (Claude sees stderr and self-corrects)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Resolve schema path relative to repo root (hook is run from repo root)
SCHEMA_PATH = Path("src/atlas_chat/atlas_chat/schemas/cl_mapping.schema.json")


def _load_schema() -> dict:
    """Load the JSON Schema, falling back to inline validation if missing."""
    if SCHEMA_PATH.exists():
        return json.loads(SCHEMA_PATH.read_text())
    # If schema file is missing, return None to signal inline fallback
    return None


def validate_with_jsonschema(data: dict, schema: dict) -> list[str]:
    """Validate using jsonschema library if available."""
    try:
        import jsonschema
    except ImportError:
        return validate_inline(data)

    errors = []
    validator = jsonschema.Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        path = ".".join(str(p) for p in error.absolute_path) or "(root)"
        errors.append(f"{path}: {error.message}")
    return errors


def validate_inline(data: dict) -> list[str]:
    """Fallback validation without jsonschema library."""
    errors: list[str] = []

    VALID_MATCH_TYPES = {"exact match", "broad match", "narrow match"}
    VALID_SKOS = {"skos:exactMatch", "skos:broadMatch", "skos:narrowMatch"}
    VALID_CONFIDENCE = {"high", "medium", "low"}

    # Required top-level string fields
    for field in [
        "cell_type_label",
        "working_definition",
        "justification",
        "recommendation",
    ]:
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"Missing or empty required field: '{field}'")

    # searches_performed
    sp = data.get("searches_performed")
    if not isinstance(sp, list) or len(sp) == 0:
        errors.append("'searches_performed' must be a non-empty list of strings")
    elif not all(isinstance(s, str) for s in sp):
        errors.append("'searches_performed' must contain only strings")

    # new_term_needed
    if not isinstance(data.get("new_term_needed"), bool):
        errors.append("'new_term_needed' must be a boolean")

    # other_candidates
    oc = data.get("other_candidates")
    if not isinstance(oc, list):
        errors.append("'other_candidates' must be a list (may be empty)")
    else:
        for i, cand in enumerate(oc):
            if not isinstance(cand, dict):
                errors.append(f"other_candidates[{i}] must be an object")
                continue
            for f in ["cl_term", "cl_id", "cl_definition", "reason_rejected"]:
                if not isinstance(cand.get(f), str) or not cand[f].strip():
                    errors.append(f"other_candidates[{i}] missing field: '{f}'")
            cl_id = cand.get("cl_id", "")
            if cl_id and not cl_id.startswith("CL:"):
                errors.append(
                    f"other_candidates[{i}].cl_id '{cl_id}' must start with 'CL:'"
                )
            # Reject extra fields
            extra = set(cand.keys()) - {"cl_term", "cl_id", "cl_definition", "reason_rejected"}
            if extra:
                errors.append(f"other_candidates[{i}] has extra fields: {extra}")

    # Reject extra top-level fields
    allowed_top = {
        "cell_type_label", "working_definition", "searches_performed",
        "best_match", "justification", "other_candidates",
        "recommendation", "new_term_needed",
    }
    extra_top = set(data.keys()) - allowed_top
    if extra_top:
        errors.append(f"Extra top-level fields not allowed: {extra_top}")

    # best_match — null is allowed (no match)
    bm = data.get("best_match")
    if bm is None:
        if data.get("new_term_needed") is not True:
            errors.append(
                "When best_match is null, 'new_term_needed' must be true"
            )
        return errors

    if not isinstance(bm, dict):
        errors.append("'best_match' must be an object or null")
        return errors

    # best_match fields
    for f in ["cl_term", "cl_id", "cl_definition", "match_type", "skos_mapping", "confidence"]:
        if not isinstance(bm.get(f), str) or not bm[f].strip():
            errors.append(f"best_match missing field: '{f}'")

    # Reject extra best_match fields
    allowed_bm = {"cl_term", "cl_id", "cl_definition", "match_type", "skos_mapping", "confidence"}
    extra_bm = set(bm.keys()) - allowed_bm
    if extra_bm:
        errors.append(f"best_match has extra fields not allowed: {extra_bm}")

    cl_id = bm.get("cl_id", "")
    if cl_id and not cl_id.startswith("CL:"):
        errors.append(f"best_match.cl_id '{cl_id}' must start with 'CL:'")

    mt = bm.get("match_type", "")
    if mt and mt not in VALID_MATCH_TYPES:
        errors.append(
            f"best_match.match_type '{mt}' must be one of: {VALID_MATCH_TYPES}"
        )

    skos = bm.get("skos_mapping", "")
    if skos and skos not in VALID_SKOS:
        errors.append(
            f"best_match.skos_mapping '{skos}' must be one of: {VALID_SKOS}"
        )

    conf = bm.get("confidence", "")
    if conf and conf not in VALID_CONFIDENCE:
        errors.append(
            f"best_match.confidence '{conf}' must be one of: {VALID_CONFIDENCE}"
        )

    # Cross-check: match_type ↔ skos_mapping consistency
    type_to_skos = {
        "exact match": "skos:exactMatch",
        "broad match": "skos:broadMatch",
        "narrow match": "skos:narrowMatch",
    }
    if mt in type_to_skos and skos and type_to_skos[mt] != skos:
        errors.append(
            f"match_type '{mt}' and skos_mapping '{skos}' are inconsistent"
        )

    # Cross-check: new_term_needed
    ntn = data.get("new_term_needed")
    if isinstance(ntn, bool):
        if mt == "exact match" and ntn is True:
            errors.append("'new_term_needed' should be false for exact match")
        if mt in ("broad match", "narrow match") and ntn is False:
            errors.append(f"'new_term_needed' should be true for {mt}")

    return errors


def main() -> int:
    try:
        hook_input = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, OSError):
        return 0

    tool_input = hook_input.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if not file_path or not file_path.endswith("cl_mapping.json"):
        return 0

    # Read the content from hook input
    content = tool_input.get("content", "")
    if not content:
        print("cl_mapping.json is empty", file=sys.stderr)
        return 2

    try:
        data = json.loads(content)
    except json.JSONDecodeError as exc:
        print(f"cl_mapping.json is not valid JSON: {exc}", file=sys.stderr)
        return 2

    # Try schema-based validation first, fall back to inline
    schema = _load_schema()
    if schema is not None:
        errors = validate_with_jsonschema(data, schema)
    else:
        errors = validate_inline(data)

    if not errors:
        return 0

    print("CL MAPPING VALIDATION FAILED", file=sys.stderr)
    print("Fix these issues and rewrite cl_mapping.json:", file=sys.stderr)
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
