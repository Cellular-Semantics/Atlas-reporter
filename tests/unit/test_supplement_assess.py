"""The parts of the supplement assessment that must not drift.

The sampling and rendering helpers are pure, so they are pinned directly. The
rest is the boundary with the judging subagent: a unit that comes back without
a verdict must become a recorded gap, never a silently absent pointer.
"""

from __future__ import annotations

import json

import jsonschema
import pytest
from atlas_chat.services.supplement_assess import (
    PROSE_SAMPLE_THRESHOLD,
    AssessResult,
    SupplementAssessError,
    Unit,
    apply_verdicts,
    labels_from_cas,
    record_cas_uptake,
    render_prose,
    render_sheet,
    roster_block,
    sample_prose,
    write_into_manifest,
)

from atlas_chat.schemas import load_schema

pytestmark = pytest.mark.unit


def _verdict(**kwargs):
    return {
        "description": "A table of genes.",
        "mentions_cell_types": True,
        "mentions_cell_types_note": "cluster column present",
        **kwargs,
    }


def _unit(kind="table", unit_id="u1", **pointer):
    base = {"file_id": "f1", "content_type": "other", "relevance": "unknown"}
    if kind == "prose":
        base = {"file_id": "f1", "text_file": "text/a.txt", "evidence": "full_text"}
    return Unit(unit_id=unit_id, kind=kind, pointer={**base, **pointer}, evidence_block="...")


# ------------------------------------------------------------------
# Sampling
# ------------------------------------------------------------------


def test_short_prose_is_read_whole_not_sampled():
    text = "a" * (PROSE_SAMPLE_THRESHOLD - 1)
    shown, complete = sample_prose(text)
    assert complete is True
    assert shown == text


def test_long_prose_samples_head_middle_and_tail():
    # A legends document describes its tables in order, so a prefix would
    # characterise the first few and miss the rest.
    text = "HEAD" + ("x" * 60_000) + "MIDDLE" + ("y" * 60_000) + "TAIL"
    shown, complete = sample_prose(text)

    assert complete is False
    assert shown.startswith("HEAD")
    assert shown.endswith("TAIL")
    assert "MIDDLE" in shown
    assert len(shown) < len(text)


def test_sampled_prose_says_so_in_the_prompt():
    # A model told nothing about truncation will report absence as a finding.
    partial = render_prose("legends.docx", "text", complete=False)
    whole = render_prose("legends.docx", "text", complete=True)

    assert "SAMPLE" in partial
    assert "not shown" in partial
    assert "complete text" in whole


# ------------------------------------------------------------------
# Rendering
# ------------------------------------------------------------------


def test_sheet_render_states_true_dimensions_beside_the_sample():
    block = render_sheet(
        {
            "locator": "Table 12",
            "columns": [{"name": "gene"}, {"name": "cluster"}],
            "n_rows": 396_877,
            "n_columns": 8,
        },
        rows=[["HRG", "c1"]],
    )
    assert "396877" in block or "396,877" in block.replace(",", "")
    assert "Table 12" in block
    assert "gene, cluster" in block
    assert "HRG | c1" in block


def test_roster_is_listed_when_short_and_generalised_when_long():
    listed = roster_block(["Macrophage", "LC_1"])
    assert "- Macrophage" in listed
    assert "- LC_1" in listed

    generalised = roster_block([f"label_{i}" for i in range(200)], cap=150)
    assert "label_0" not in generalised
    assert "200" in generalised
    assert "general biological grounds" in generalised


def test_roster_block_without_labels_still_asks_the_question():
    block = roster_block([])
    assert "general biological grounds" in block


def test_labels_from_cas_reads_cell_label_and_dedupes():
    cas = {
        "annotations": [
            {"cell_label": "Macrophage"},
            {"cell_label": "Macrophage"},
            {"label": "LC_1"},
            {},
        ]
    }
    assert labels_from_cas(cas) == ["Macrophage", "LC_1"]


# ------------------------------------------------------------------
# Taking verdicts back
# ------------------------------------------------------------------


def test_verdicts_are_split_by_kind_and_land_on_the_pointer():
    units = [_unit("table", "t1", locator="S1"), _unit("prose", "p1")]
    result = apply_verdicts(units, {"t1": _verdict(), "p1": _verdict()})

    assert len(result.tables) == 1
    assert len(result.prose) == 1
    assert result.gaps == []
    assert result.tables[0]["mentions_cell_types"] is True
    assert result.tables[0]["description"] == "A table of genes."
    assert result.tables[0]["mentions_cell_types_note"] == "cluster column present"


def test_a_unit_with_no_verdict_becomes_a_gap():
    # The failure mode that matters: an unjudged unit must not simply vanish
    # from the manifest, where its absence reads as "nothing here".
    result = apply_verdicts([_unit("table", "t1", locator="S1")], {})

    assert result.tables == []
    assert len(result.gaps) == 1
    assert "not empty" in result.gaps[0]["reason"]
    assert result.gaps[0]["file_id"] == "f1"


@pytest.mark.parametrize(
    "verdict",
    [
        {"mentions_cell_types": True},
        {"description": "x"},
        {"description": "   ", "mentions_cell_types": True},
        "not an object",
    ],
    ids=["no-description", "no-verdict-flag", "blank-description", "not-an-object"],
)
def test_a_malformed_verdict_becomes_a_gap_not_a_pointer(verdict):
    result = apply_verdicts([_unit("table", "t1")], {"t1": verdict})
    assert result.tables == []
    assert len(result.gaps) == 1


def test_one_bad_verdict_does_not_lose_the_good_ones():
    units = [_unit("table", "t1", locator="S1"), _unit("table", "t2", locator="S2")]
    result = apply_verdicts(units, {"t2": _verdict()})

    assert len(result.tables) == 1
    assert result.tables[0]["locator"] == "S2"
    assert len(result.gaps) == 1


def test_a_verdict_under_the_wrong_id_is_not_silently_accepted():
    # A judge that mangles the unit_id loses its unit. That has to surface.
    result = apply_verdicts([_unit("table", "t1")], {"T1": _verdict()})
    assert result.tables == []
    assert len(result.gaps) == 1


def test_roster_reaches_the_task_payload():
    from atlas_chat.services.supplement_assess import roster_block

    assert "Iron-recycling macrophage" in roster_block(["Iron-recycling macrophage"])


def test_unit_task_carries_only_an_id_and_the_evidence():
    task = _unit("table", "t1", locator="S1").as_task()
    assert set(task) == {"unit_id", "kind", "evidence"}
    assert task["unit_id"] == "t1"


# ------------------------------------------------------------------
# Writing back
# ------------------------------------------------------------------


def _manifest(tmp_path, doi="10.1038/s41586-024-08002-x", **extra):
    from atlas_chat.services.supplement_store import write_manifest

    manifest = {
        "manifest_version": 1,
        "paper": {"doi": doi},
        "files": [{"file_id": "f1", "media_type": "xlsx", "status": "present"}],
        **extra,
    }
    write_manifest(tmp_path, doi, manifest)
    return doi


def _table_pointer(**extra):
    return {
        "file_id": "f1",
        "locator": "S1",
        "content_type": "cluster_annotation",
        "description": "Cluster-to-name mapping.",
        "evidence": "rows_read",
        "mentions_cell_types": True,
        **extra,
    }


def test_write_into_manifest_preserves_an_existing_cas_uptake_note(tmp_path):
    # Uptake records something a later step did. Re-running the assessment
    # knows nothing about it and must not erase it.
    uptake = {"at": "2026-09-05T00:00:00+00:00", "note": "synonyms taken into CAS+"}
    doi = _manifest(tmp_path, tables=[_table_pointer(description="old", cas_uptake=uptake)])

    path = write_into_manifest(
        tmp_path, doi, AssessResult(tables=[_table_pointer(description="new")])
    )
    written = json.loads(path.read_text())

    assert written["tables"][0]["description"] == "new"
    assert written["tables"][0]["cas_uptake"] == uptake


def test_written_manifest_validates_against_the_schema(tmp_path):
    doi = _manifest(tmp_path)
    result = AssessResult(
        tables=[_table_pointer(mentions_cell_types_note="cluster column")],
        prose=[
            {
                "file_id": "f1",
                "text_file": "text/legends.txt",
                "n_chars": 10_995,
                "extractor": "docx",
                "description": "Legends for the supplementary tables.",
                "mentions_cell_types": True,
                "evidence": "full_text",
            }
        ],
        gaps=[{"file_id": "f1", "reason": "not assessed: no verdict was returned for it"}],
    )

    path = write_into_manifest(tmp_path, doi, result)
    jsonschema.validate(
        json.loads(path.read_text()), load_schema("supplement_manifest.schema.json")
    )


def test_cas_uptake_is_recorded_against_the_matching_pointer(tmp_path):
    doi = _manifest(tmp_path, tables=[_table_pointer()])
    unit_id = "table|f1||S1"

    path = record_cas_uptake(
        tmp_path,
        doi,
        unit_id,
        "cluster names taken into CAS+ cell_fullname",
        "2026-09-05T00:00:00+00:00",
    )
    written = json.loads(path.read_text())

    assert written["tables"][0]["cas_uptake"]["note"].startswith("cluster names")
    jsonschema.validate(written, load_schema("supplement_manifest.schema.json"))


def test_cas_uptake_against_an_unknown_unit_is_an_error(tmp_path):
    doi = _manifest(tmp_path, tables=[_table_pointer()])
    with pytest.raises(SupplementAssessError, match="no pointer with id"):
        record_cas_uptake(tmp_path, doi, "table|f1||nope", "x", "2026-09-05T00:00:00+00:00")
