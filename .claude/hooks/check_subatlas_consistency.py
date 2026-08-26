#!/usr/bin/env python
"""Claude Code hook: validate subatlas_consistency output against JSON Schema.

Fires as a PostToolUse hook on Write/Edit to ``subatlas_consistency.json``.

Beyond the schema, enforces the cross-field rules that carry the actual design
intent — each one guards a specific way this step can produce something that
looks like an answer but isn't:

* ``match_type`` <-> ``skos_mapping`` agree (same rule as check_cl_mapping.py).
* ``explanation`` is present whenever ``match_type`` is not "exact match". A bare
  verdict of disagreement is not what the functional spec asks for; the attempt
  at explaining it is the deliverable.
* ``purity_caveat`` is present whenever the sibling ``subatlas_contributors.json``
  puts this contributor's purity below 0.8 — because then "what did this paper
  call these cells" has more than one answer and one verdict understates it.
* a verdict without the paper's own text (``evidence_status`` of ``unreachable`` /
  ``abstract_only`` / ``no_publication``) must be ``confidence: low`` and carry no
  ``upstream_definition``. Inferring an upstream definition from a label string is
  the failure mode this file exists to prevent.
* ``evidence_quotes`` from a contributor are tagged ``role: subatlas``, not
  ``atlas``.
* ``primacy.primary_paper`` is set when the call is ``subatlas_primary``, and names
  a contributor that is actually in the file.
* every contributor in the sibling ``subatlas_contributors.json`` has a verdict —
  silently dropping the awkward one is the easiest way to make this look clean.

Exit codes:
    0 — valid, or file is not a consistency file, or jsonschema unavailable
    2 — validation failed (Claude sees stderr and self-corrects)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCHEMA_PATH = Path("src/atlas_chat/atlas_chat/schemas/subatlas_consistency.schema.json")

MATCH_TO_SKOS = {
    "exact match": "skos:exactMatch",
    "broad match": "skos:broadMatch",
    "narrow match": "skos:narrowMatch",
    "related match": "skos:relatedMatch",
    "no match": "skos:noMatch",
}
NO_TEXT_STATUSES = {"unreachable", "abstract_only", "no_publication"}
IMPURE_BELOW = 0.8


def _targets(file_path: str) -> bool:
    return Path(file_path).name == "subatlas_consistency.json"


def _schema_errors(data: object, schema: dict) -> list[str]:
    import jsonschema

    validator = jsonschema.Draft202012Validator(schema)
    errors = []
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        path = ".".join(str(p) for p in err.absolute_path) or "(root)"
        errors.append(f"{path}: {err.message}")
    return errors


def _sibling_contributors(file_path: str) -> dict[str, dict] | None:
    """Read subatlas_contributors.json next to the consistency file, if present.

    The two are written into the same per-cell-type traversal directory. Absent is
    tolerated (the file may be produced elsewhere), but where it is present it is
    the authority on which contributors exist and how pure each one is.
    """
    sibling = Path(file_path).with_name("subatlas_contributors.json")
    if not sibling.exists():
        return None
    try:
        doc = json.loads(sibling.read_text())
    except (json.JSONDecodeError, OSError):
        return None
    if isinstance(doc, list):  # whole-project pass; not per-cell-type
        return None
    return {c["subatlas_paper"]: c for c in doc.get("contributors", []) if c.get("subatlas_paper")}


def _cross_field_errors(data: dict, contributors: dict[str, dict] | None) -> list[str]:
    errors: list[str] = []
    verdicts = data.get("contributors", [])
    seen: set[str] = set()

    for i, verdict in enumerate(verdicts):
        paper = verdict.get("subatlas_paper", "?")
        where = f"contributors[{i}] ({paper})"
        seen.add(paper)

        match_type = verdict.get("match_type", "")
        skos = verdict.get("skos_mapping", "")
        expected = MATCH_TO_SKOS.get(match_type)
        if expected and skos and expected != skos:
            errors.append(
                f"{where}: match_type {match_type!r} and skos_mapping {skos!r} disagree "
                f"(expected {expected!r})"
            )

        if match_type != "exact match" and not verdict.get("explanation"):
            errors.append(
                f"{where}: match_type is {match_type!r}, so an explanation is required — "
                "attempt to account for the difference from markers, resolution or context, "
                "or say explicitly that markers cannot explain it"
            )

        status = verdict.get("evidence_status", "text_retrieved")
        if status in NO_TEXT_STATUSES:
            if verdict.get("confidence") != "low":
                errors.append(
                    f"{where}: evidence_status is {status!r}, so confidence must be 'low' — "
                    "the paper's own account of its label was never read"
                )
            if verdict.get("upstream_definition"):
                errors.append(
                    f"{where}: evidence_status is {status!r} but an upstream_definition is "
                    "given. Leave it absent rather than inferring one from the label string"
                )
        elif not verdict.get("evidence_quotes"):
            errors.append(
                f"{where}: evidence_status is {status!r} (text was retrieved) but there are "
                "no evidence_quotes to ground the upstream definition"
            )

        for j, quote in enumerate(verdict.get("evidence_quotes", [])):
            role = (quote.get("source_paper") or {}).get("role")
            if role != "subatlas":
                errors.append(
                    f"{where}.evidence_quotes[{j}]: source_paper.role is {role!r}; a quote "
                    "supporting a contributor's own definition comes from that contributor "
                    "(role 'subatlas')"
                )

        if contributors is not None and paper in contributors:
            purity = contributors[paper].get("purity")
            if purity is not None and purity < IMPURE_BELOW and not verdict.get("purity_caveat"):
                errors.append(
                    f"{where}: purity is {purity} (< {IMPURE_BELOW}), so a purity_caveat is "
                    "required — this paper split its contribution across several labels, so "
                    "one verdict understates what it called these cells"
                )

    if contributors is not None:
        missing = sorted(set(contributors) - seen)
        if missing:
            errors.append(
                "every contributor over the cutoff needs a verdict; missing: "
                + ", ".join(missing)
            )

    primacy = data.get("primacy", {})
    call = primacy.get("call")
    if call == "subatlas_primary":
        primary = primacy.get("primary_paper")
        if not primary:
            errors.append("primacy.call is 'subatlas_primary' but no primary_paper is named")
        elif primary not in seen:
            errors.append(
                f"primacy.primary_paper {primary!r} is not one of the contributors judged "
                "in this file"
            )
    if call == "co_equal" and not primacy.get("co_equal_papers"):
        errors.append("primacy.call is 'co_equal' but co_equal_papers is empty")
    if data.get("no_dominant_contributor") and call == "subatlas_primary":
        errors.append(
            "no_dominant_contributor is true, so no contributor cleared the cutoff — "
            "primacy cannot be 'subatlas_primary'"
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
        print("jsonschema not available — skipping subatlas_consistency check", file=sys.stderr)
        return 0

    errors = _schema_errors(data, json.loads(SCHEMA_PATH.read_text()))
    if not errors and isinstance(data, dict):
        errors = _cross_field_errors(data, _sibling_contributors(file_path))

    if not errors:
        return 0

    print("SUBATLAS_CONSISTENCY VALIDATION FAILED", file=sys.stderr)
    print(f"Fix these issues and rewrite {Path(file_path).name}:", file=sys.stderr)
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
