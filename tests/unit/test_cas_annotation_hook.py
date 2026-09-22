"""PostToolUse hook regression for check_cas_annotation.py.

Drives the hook via subprocess (like the other hook regressions): a valid
``cas.json`` exits 0, an invalid one exits 2, and a non-``cas.json`` file is
ignored. Reuses the CAS fixtures from test_cas_annotation_schema.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).parent / "fixtures" / "cas"
HOOK = REPO_ROOT / ".claude" / "hooks" / "check_cas_annotation.py"


def _load(name: str) -> object:
    return json.loads((FIXTURES / name).read_text())


def _run_hook(file_path: str, payload: object) -> subprocess.CompletedProcess:
    hook_input = json.dumps(
        {"tool_input": {"file_path": file_path, "content": json.dumps(payload)}}
    )
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=hook_input,
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


@pytest.mark.unit
def test_hook_accepts_valid_cas() -> None:
    r = _run_hook("projects/x/cas.json", _load("cas_annotation.minimal.good.json"))
    assert r.returncode == 0, r.stderr


@pytest.mark.unit
def test_hook_rejects_invalid_cas() -> None:
    r = _run_hook("projects/x/cas.json", _load("cas_annotation.bad.json"))
    assert r.returncode == 2
    assert "VALIDATION FAILED" in r.stderr


@pytest.mark.unit
def test_hook_ignores_non_cas_files() -> None:
    r = _run_hook("projects/x/notes.txt", {"anything": 1})
    assert r.returncode == 0


# ------------------------------------------------------------------
# Recomputing the stored overlap measures
# ------------------------------------------------------------------


def _worked_example() -> tuple[dict, dict]:
    data = _load("cas_annotation.good.json")
    annotation = next(a for a in data["annotations"] if a["cell_label"] == "bar")
    return data, annotation["transferred_annotations"][0]


@pytest.mark.unit
def test_hook_accepts_measures_that_recompute() -> None:
    data, _ = _worked_example()
    r = _run_hook("projects/x/cas.json", data)
    assert r.returncode == 0, r.stderr


@pytest.mark.unit
@pytest.mark.parametrize(
    ("measure", "wrong"),
    [
        ("share_of_subatlas_contribution", 0.24),  # the other share's value
        ("share_of_subatlas_label", 0.80),  # and vice versa
        ("cell_ratio", 0.80),
    ],
)
def test_hook_rejects_a_measure_that_does_not_recompute(measure: str, wrong: float) -> None:
    data, transfer = _worked_example()
    transfer[measure] = wrong
    r = _run_hook("projects/x/cas.json", data)
    assert r.returncode == 2
    assert measure in r.stderr
    assert "bar / fu" in r.stderr


@pytest.mark.unit
def test_hook_skips_a_measure_whose_denominator_has_not_been_counted_yet() -> None:
    """Absent is not wrong: the registry pass runs after the counting pass."""
    data, transfer = _worked_example()
    del transfer["subatlas_label_total_cells"]
    r = _run_hook("projects/x/cas.json", data)
    assert r.returncode == 0, r.stderr


@pytest.mark.unit
def test_hook_tolerates_the_rounding_the_stored_values_carry() -> None:
    data, transfer = _worked_example()
    transfer["share_of_subatlas_contribution"] = 0.7999
    r = _run_hook("projects/x/cas.json", data)
    assert r.returncode == 0, r.stderr
