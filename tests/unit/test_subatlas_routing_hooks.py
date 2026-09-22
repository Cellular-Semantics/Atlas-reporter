"""PostToolUse hook regressions for the routing table and plan.

Driven by subprocess like the other hook regressions. The plan checks are the
point of the pair: a plan is the one artefact here written by an agent, and the
failures worth catching are a question the table does not carry, a cell set
claimed for a reading that does not reach it, and a requested cell set that
ends up in neither the plan's papers nor its atlas_only list.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).parent / "fixtures" / "routing"
TABLE_HOOK = REPO_ROOT / ".claude" / "hooks" / "check_subatlas_routing_table.py"
PLAN_HOOK = REPO_ROOT / ".claude" / "hooks" / "check_subatlas_routing_plan.py"

pytestmark = pytest.mark.unit


def _load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text())


def _run(hook: Path, file_path: str, payload: object) -> subprocess.CompletedProcess:
    hook_input = json.dumps(
        {"tool_input": {"file_path": file_path, "content": json.dumps(payload)}}
    )
    return subprocess.run(
        [sys.executable, str(hook)],
        input=hook_input,
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


# ------------------------------------------------------------------
# the table
# ------------------------------------------------------------------


def test_table_hook_accepts_a_generated_table() -> None:
    result = _run(TABLE_HOOK, "projects/x/routing_table.json", _load("routing_table.good.json"))
    assert result.returncode == 0, result.stderr


def test_table_hook_rejects_a_share_outside_its_range() -> None:
    result = _run(
        TABLE_HOOK,
        "projects/x/routing_table.json",
        _load("routing_table.bad_share_out_of_range.json"),
    )
    assert result.returncode == 2
    assert "share_of_contribution" in result.stderr


def test_table_hook_points_at_regeneration_rather_than_hand_editing() -> None:
    result = _run(
        TABLE_HOOK,
        "projects/x/routing_table.json",
        _load("routing_table.bad_share_out_of_range.json"),
    )
    assert "cli_route" in result.stderr


def test_table_hook_ignores_other_files() -> None:
    assert _run(TABLE_HOOK, "projects/x/notes.json", {"anything": True}).returncode == 0


# ------------------------------------------------------------------
# the plan
# ------------------------------------------------------------------


def test_plan_hook_accepts_a_plan_that_matches_its_table() -> None:
    result = _run(PLAN_HOOK, "projects/x/routing_plan.json", _load("routing_plan.good.json"))
    assert result.returncode == 0, result.stderr


def test_plan_hook_rejects_a_question_the_table_does_not_carry() -> None:
    result = _run(
        PLAN_HOOK,
        "projects/x/routing_plan.json",
        _load("routing_plan.bad_invented_question.json"),
    )
    assert result.returncode == 2
    assert "Fibroblast A" in result.stderr


def test_plan_hook_rejects_a_reading_claimed_for_a_cell_set_it_does_not_reach() -> None:
    result = _run(
        PLAN_HOOK,
        "projects/x/routing_plan.json",
        _load("routing_plan.bad_serves_a_non_claimant.json"),
    )
    assert result.returncode == 2
    assert "does not feed" in result.stderr


def test_plan_hook_rejects_a_requested_cell_set_that_fell_out_of_both() -> None:
    result = _run(
        PLAN_HOOK,
        "projects/x/routing_plan.json",
        _load("routing_plan.bad_unaccounted_cell_set.json"),
    )
    assert result.returncode == 2
    assert "Fib_D" in result.stderr


def test_plan_hook_rejects_a_plan_with_no_table_to_check_against() -> None:
    plan = _load("routing_plan.good.json")
    del plan["table_source"]
    result = _run(PLAN_HOOK, "projects/x/routing_plan.json", plan)
    assert result.returncode == 2
    assert "table_source" in result.stderr


def test_plan_hook_ignores_other_files() -> None:
    assert _run(PLAN_HOOK, "projects/x/notes.json", {"anything": True}).returncode == 0
