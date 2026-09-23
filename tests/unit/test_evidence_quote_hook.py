"""Regression for the quote half of check_evidence_summary.py.

Drives the hook via subprocess. The shape check is covered elsewhere; what is
pinned here is that a quote is looked for in the text it came from, that a
quote found nowhere is rejected, and that the check says so rather than passing
silently when there is nothing to search.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.unit

REPO_ROOT = Path(__file__).resolve().parents[2]
HOOK = REPO_ROOT / ".claude" / "hooks" / "check_evidence_summary.py"

JOB = {
    "narrative": {"text": "The population sits in the outer cortex of the ovary."},
    "legends": [{"label": "Fig. 1", "text": "Sections profiled by spatial transcriptomics."}],
}


def _item(*quotes: str, found: bool = True) -> dict:
    return {
        "cell_label": "Mesen_OvarianFibs_Outcor",
        "source_paper": {"doi": "10.1/x", "role": "atlas"},
        "retrieval_method": "corpus_snippet",
        "aspect": "location",
        "found": found,
        "summary": "The population sits in the outer cortex.",
        "quotes": list(quotes),
    }


def _run(
    out_dir: Path, payload: object, name: str = "all_summaries.json"
) -> subprocess.CompletedProcess:
    target = out_dir / name
    hook_input = json.dumps(
        {"tool_input": {"file_path": str(target), "content": json.dumps(payload)}}
    )
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=hook_input,
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


def _with_job(tmp_path: Path) -> Path:
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "atlas.json").write_text(json.dumps(JOB))
    return tmp_path


def test_a_quote_present_in_the_source_passes(tmp_path):
    out = _with_job(tmp_path)
    assert _run(out, [_item("sits in the outer cortex")]).returncode == 0


def test_a_quote_from_a_legend_passes(tmp_path):
    out = _with_job(tmp_path)
    assert _run(out, [_item("profiled by spatial transcriptomics")]).returncode == 0


def test_an_invented_quote_is_rejected(tmp_path):
    out = _with_job(tmp_path)
    result = _run(out, [_item("The cells glowed faintly in the dark.")])
    assert result.returncode == 2
    assert "not found in any source" in result.stderr


def test_a_spliced_quote_is_rejected(tmp_path):
    """Two real fragments joined are not something the author wrote."""
    out = _with_job(tmp_path)
    spliced = "outer cortex of the ovary. Sections profiled by spatial transcriptomics."
    assert _run(out, [_item(spliced)]).returncode == 2


def test_an_assertion_with_no_quote_is_rejected(tmp_path):
    """The failing that motivated the check: a claim with nothing behind it."""
    out = _with_job(tmp_path)
    result = _run(out, [_item()])
    assert result.returncode == 2


def test_a_decline_needs_no_quote(tmp_path):
    out = _with_job(tmp_path)
    assert _run(out, [_item(found=False)]).returncode == 0


def test_without_a_job_file_the_check_says_it_could_not_run(tmp_path):
    """No local source text means nothing to search — but silence about that
    would read as a pass."""
    result = _run(tmp_path, [_item("anything at all")])
    assert result.returncode == 0
    assert "not checked" in result.stderr


def test_a_job_file_shared_by_several_cell_types_is_found(tmp_path):
    """One read covers several cell types and produces one job file, so the
    paper sits above the per-cell-type output directories rather than being
    copied into each of them."""
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "atlas.json").write_text(json.dumps(JOB))
    out = tmp_path / "Immune_uftLAM"
    out.mkdir()
    assert _run(out, [_item("sits in the outer cortex")]).returncode == 0
    assert _run(out, [_item("never written anywhere")]).returncode == 2


def test_an_evidence_file_is_recognised_by_its_new_name(tmp_path):
    """`*.evidence.json` is what a producer writes now. The hook and the
    collector share one rule for which files that is."""
    out = _with_job(tmp_path)
    result = _run(out, [_item("nothing like this appears")], name="Immune_oLAM.evidence.json")
    assert result.returncode == 2


def test_a_job_file_in_the_same_directory_is_found(tmp_path):
    """A paper read files its evidence next to the paper it quoted, so the job
    file is neither in a `papers/` subdirectory nor one level up."""
    out = tmp_path / "papers" / "celltype_Lorenzi2025"
    out.mkdir(parents=True)
    (out / "paper.json").write_text(json.dumps(JOB))
    result = _run(out, [_item("sits in the outer cortex")], name="Immune_oLAM.evidence.json")
    assert result.returncode == 0


def test_evidence_beside_evidence_is_not_mistaken_for_a_source(tmp_path):
    """A quote must be found in a paper, not in another item's prose. Searching
    the output's own directory means the files beside it are candidates, so
    evidence files have to be excluded from the sources."""
    out = tmp_path / "papers" / "celltype_Lorenzi2025"
    out.mkdir(parents=True)
    (out / "paper.json").write_text(json.dumps(JOB))
    (out / "Immune_uftLAM.evidence.json").write_text(
        json.dumps([_item("The cells glowed faintly in the dark.")])
    )
    result = _run(
        out, [_item("The cells glowed faintly in the dark.")], name="Immune_oLAM.evidence.json"
    )
    assert result.returncode == 2
