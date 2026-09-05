"""PostToolUse hook regression for check_subatlas_contributors.py.

The contributors file is *derived*, so the hook checks arithmetic the schema
cannot express. A hand-edited or invented file shows up as internally
inconsistent rather than as plausible-looking numbers.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.unit

REPO_ROOT = Path(__file__).resolve().parents[2]
HOOK = REPO_ROOT / ".claude" / "hooks" / "check_subatlas_contributors.py"


def _run(file_path: str, payload: object) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps({"tool_input": {"file_path": file_path, "content": json.dumps(payload)}}),
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


def _good():
    return {
        "cell_label": "aPCV",
        "labelset": "L4",
        "n_cells": 1000,
        "thresholds": {
            "min_contribution": 0.05,
            "min_source_cells": 50,
            "primary_contribution": 0.2,
            "min_within_source_share": 0.02,
        },
        "contributors": [
            {
                "subatlas_paper": "P",
                "doi": "10.1/p",
                "tier": "primary",
                "from_source_cells": 300,
                "contribution": 0.3,
                "purity": 0.6,
                "dominant_label": "Capillary",
                "labels": [
                    {
                        "transferred_cell_label": "Capillary",
                        "cell_count": 180,
                        "within_source_share": 0.6,
                        "share_of_set": 0.18,
                    },
                    {
                        "transferred_cell_label": "tPCV",
                        "cell_count": 110,
                        "within_source_share": 0.3667,
                        "share_of_set": 0.11,
                    },
                ],
                "n_tail_labels": 2,
                "tail_cells": 10,
            }
        ],
        "tail": {"n_papers": 0, "cell_count": 0, "contribution": 0.0, "papers": []},
    }


def test_accepts_a_consistent_file():
    result = _run("out/subatlas_contributors.json", _good())
    assert result.returncode == 0, result.stderr


def test_accepts_an_array_from_the_whole_project_pass():
    assert _run("out/subatlas_contributors.json", [_good(), _good()]).returncode == 0


def test_ignores_other_files():
    assert _run("out/all_summaries.json", {"nonsense": True}).returncode == 0


def test_rejects_a_schema_violation():
    doc = _good()
    doc["contributors"][0]["tier"] = "tertiary"
    result = _run("out/subatlas_contributors.json", doc)
    assert result.returncode == 2
    assert "tertiary" in result.stderr


def test_rejects_a_contribution_that_does_not_match_the_counts():
    doc = _good()
    doc["contributors"][0]["contribution"] = 0.9
    result = _run("out/subatlas_contributors.json", doc)
    assert result.returncode == 2
    assert "contribution 0.9" in result.stderr


def test_rejects_a_purity_that_is_not_the_dominant_share():
    doc = _good()
    doc["contributors"][0]["purity"] = 0.99
    result = _run("out/subatlas_contributors.json", doc)
    assert result.returncode == 2
    assert "purity 0.99" in result.stderr


def test_rejects_a_dominant_label_that_is_not_the_largest():
    doc = _good()
    doc["contributors"][0]["dominant_label"] = "tPCV"
    doc["contributors"][0]["purity"] = 110 / 300
    result = _run("out/subatlas_contributors.json", doc)
    assert result.returncode == 2
    assert "highest-count label is 'Capillary'" in result.stderr


def test_rejects_cells_that_do_not_add_up():
    """The tail exists to account for what is not listed; it must actually do so."""
    doc = _good()
    doc["contributors"][0]["tail_cells"] = 999
    result = _run("out/subatlas_contributors.json", doc)
    assert result.returncode == 2
    assert "from_source_cells = 300" in result.stderr


def test_rejects_no_dominant_contributor_alongside_contributors():
    doc = _good()
    doc["no_dominant_contributor"] = True
    result = _run("out/subatlas_contributors.json", doc)
    assert result.returncode == 2
    assert "no_dominant_contributor is true" in result.stderr


def test_accepts_a_genuinely_empty_result():
    doc = _good()
    doc["contributors"] = []
    doc["no_dominant_contributor"] = True
    doc["tail"] = {"n_papers": 3, "cell_count": 40, "contribution": 0.04, "papers": ["a", "b", "c"]}
    assert _run("out/subatlas_contributors.json", doc).returncode == 0


def test_rejects_invalid_json():
    result = subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(
            {"tool_input": {"file_path": "out/subatlas_contributors.json", "content": "{oops"}}
        ),
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    assert result.returncode == 2
    assert "not valid JSON" in result.stderr


def test_points_at_the_generator_rather_than_asking_for_a_hand_fix():
    doc = _good()
    doc["contributors"][0]["contribution"] = 0.9
    result = _run("out/subatlas_contributors.json", doc)
    assert "cli_contributors" in result.stderr


def test_real_generator_output_passes_the_hook():
    cas = REPO_ROOT / "projects/test_projects/hca_reproductive/cas.json"
    if not cas.exists():  # pragma: no cover - project data is committed
        pytest.skip("reference project not present")
    from atlas_chat.services import subatlas_contributors as sc

    doc = json.loads(cas.read_text())
    rows = sc.summarise_all(doc)
    assert len(rows) == 303
    assert _run("out/subatlas_contributors.json", rows).returncode == 0
