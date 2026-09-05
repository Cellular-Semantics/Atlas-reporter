"""The parts of supplementary-prose handling that must not drift.

Characterising a document is pure and pinned directly. The rest is the boundary
with whoever reads it: a document that comes back without a verdict must become
a recorded gap, never a silently absent pointer.
"""

from __future__ import annotations

import json

import jsonschema
import pytest
from atlas_chat.services.supplement_prose import (
    SAMPLE_BUDGET,
    AssessResult,
    SupplementProseError,
    Unit,
    apply_verdicts,
    labels_from_cas,
    merge_sections,
    outline_sections,
    record_cas_uptake,
    render_evidence,
    roster_block,
    sample_text,
    write_into_manifest,
)

from atlas_chat.schemas import load_schema

pytestmark = pytest.mark.unit


def _verdict(**kwargs):
    return {
        "description": "Legends for the supplementary tables.",
        "mentions_cell_types": True,
        "mentions_cell_types_note": "Table 22's legend names four macrophage subsets",
        **kwargs,
    }


def _unit(unit_id="p1", evidence="full_text", n_chars=1000, **pointer):
    base = {
        "file_id": "f1",
        "text_file": "text/a.txt",
        "n_chars": n_chars,
        "extractor": "docx",
        "evidence": evidence,
    }
    return Unit(unit_id=unit_id, pointer={**base, **pointer}, evidence_block="...")


# ------------------------------------------------------------------
# Outlines
# ------------------------------------------------------------------


def test_sections_are_merged_once_each_in_document_order():
    # The parser tags every paragraph with the heading above it, so a section
    # with three paragraphs arrives three times.
    segments = [
        ("Supplementary Methods", "aaa"),
        ("Supplementary Methods", "bb"),
        ("Cell state annotation", "cccc"),
        ("Supplementary Methods", "d"),
    ]
    assert merge_sections(segments) == [
        ("Supplementary Methods", 6),
        ("Cell state annotation", 4),
    ]


def test_unheaded_and_figure_text_are_left_out_of_an_outline():
    segments = [("BODY", "preamble"), ("IN_FIGURE", "axis label"), ("Methods", "text")]
    assert merge_sections(segments) == [("Methods", 4)]


def test_an_outline_with_no_headings_is_empty_not_a_fake_section():
    assert merge_sections([("BODY", "all of it")]) == []


def test_outline_renders_headings_with_their_sizes():
    block = outline_sections([("Supplementary Methods", 40_000), ("Cell state annotation", 900)])
    assert "Supplementary Methods — 40000 chars" in block
    assert "Cell state annotation — 900 chars" in block


def test_a_long_outline_keeps_the_biggest_sections_in_document_order():
    # A real PDF yields a heading per run-in bold line — one had 119 — and a
    # hundred-line outline is no longer a cheap characterisation.
    sections = [(f"tiny_{i}", 10) for i in range(50)]
    sections.insert(20, ("Supplementary Methods", 40_000))
    sections.append(("Cell state annotation", 9_000))

    block = outline_sections(sections, cap=2)
    lines = [ln for ln in block.splitlines() if ln.startswith("  ")]

    assert len(lines) == 2
    assert "Supplementary Methods" in lines[0]
    assert "Cell state annotation" in lines[1]
    assert "tiny_0" not in block


def test_a_capped_outline_says_what_it_dropped():
    # A silently truncated outline reads as a complete one, and a reader would
    # conclude a section is absent when it was only omitted.
    sections = [("Methods", 40_000)] + [(f"tiny_{i}", 100) for i in range(9)]
    block = outline_sections(sections, cap=1)

    assert "10 in total" in block
    assert "9 smallest are omitted" in block
    assert "900 chars" in block


def test_no_headings_is_stated_not_left_blank():
    assert "none" in outline_sections([])


# ------------------------------------------------------------------
# Sampling
# ------------------------------------------------------------------


def test_short_text_samples_to_itself():
    assert sample_text("short") == "short"


def test_sampling_takes_head_middle_and_tail_not_a_prefix():
    # A legends document lists its tables in order; a prefix would characterise
    # the first few and say nothing about the rest.
    text = "HEAD" + ("x" * SAMPLE_BUDGET) + "MIDDLE" + ("y" * SAMPLE_BUDGET) + "TAIL"
    shown = sample_text(text)

    assert shown.startswith("HEAD")
    assert shown.endswith("TAIL")
    assert "MIDDLE" in shown
    assert len(shown) < len(text)


# ------------------------------------------------------------------
# What the reader is told
# ------------------------------------------------------------------


@pytest.mark.parametrize(
    ("evidence", "expected"),
    [
        ("full_text", "the complete text"),
        ("outline", "OUTLINE ONLY"),
        ("sampled_text", "SAMPLE"),
    ],
)
def test_the_evidence_block_says_which_view_it_is(evidence, expected):
    # A reader told nothing about truncation reports absence as a finding.
    block = render_evidence("methods.pdf", "body", evidence, 40_000)
    assert expected in block
    assert "methods.pdf" in block


def test_a_partial_view_states_the_true_document_size():
    block = render_evidence("methods.pdf", "body", "outline", 40_000)
    assert "40000" in block


def test_roster_is_listed_when_short_and_generalised_when_long():
    listed = roster_block(["Macrophage", "LC_1"])
    assert "- Macrophage" in listed
    assert "- LC_1" in listed

    generalised = roster_block([f"label_{i}" for i in range(200)], cap=150)
    assert "label_0" not in generalised
    assert "200" in generalised
    assert "general biological grounds" in generalised


def test_roster_block_without_labels_still_asks_the_question():
    assert "general biological grounds" in roster_block([])


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


def test_readable_whole_distinguishes_a_document_from_a_stand_in():
    assert _unit(evidence="full_text").readable_whole is True
    assert _unit(evidence="outline").readable_whole is False
    assert _unit(evidence="sampled_text").readable_whole is False


def test_the_task_tells_a_caller_which_view_it_is_getting():
    # This is what routes a document to a subagent or to the agent itself.
    task = _unit(evidence="outline", n_chars=40_000).as_task()
    assert task["evidence_kind"] == "outline"
    assert task["n_chars"] == 40_000
    assert set(task) == {"unit_id", "evidence_kind", "n_chars", "evidence"}


# ------------------------------------------------------------------
# Taking verdicts back
# ------------------------------------------------------------------


def test_a_verdict_lands_on_the_pointer():
    result = apply_verdicts([_unit("p1")], {"p1": _verdict()})

    assert result.gaps == []
    assert len(result.prose) == 1
    assert result.prose[0]["mentions_cell_types"] is True
    assert result.prose[0]["description"] == "Legends for the supplementary tables."


def test_a_document_with_no_verdict_becomes_a_gap():
    # An unread document must not vanish from the manifest, where its absence
    # reads as "there is nothing here".
    result = apply_verdicts([_unit("p1")], {})

    assert result.prose == []
    assert len(result.gaps) == 1
    assert "not empty" in result.gaps[0]["reason"]
    assert result.gaps[0]["file_id"] == "f1"
    assert "text/a.txt" in result.gaps[0]["action"]


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
    result = apply_verdicts([_unit("p1")], {"p1": verdict})
    assert result.prose == []
    assert len(result.gaps) == 1


def test_one_bad_verdict_does_not_lose_the_good_ones():
    result = apply_verdicts([_unit("p1"), _unit("p2", text_file="text/b.txt")], {"p2": _verdict()})

    assert len(result.prose) == 1
    assert result.prose[0]["text_file"] == "text/b.txt"
    assert len(result.gaps) == 1


def test_a_verdict_under_the_wrong_id_is_not_silently_accepted():
    # A reader that mangles the unit_id loses its document. That has to surface.
    result = apply_verdicts([_unit("p1")], {"P1": _verdict()})
    assert result.prose == []
    assert len(result.gaps) == 1


# ------------------------------------------------------------------
# Writing back
# ------------------------------------------------------------------

DOI = "10.1038/s41586-024-08002-x"


def _manifest(tmp_path, **extra):
    from atlas_chat.services.supplement_store import write_manifest

    write_manifest(
        tmp_path,
        DOI,
        {
            "manifest_version": 1,
            "paper": {"doi": DOI},
            "files": [{"file_id": "f1", "media_type": "docx", "status": "present"}],
            **extra,
        },
    )
    return DOI


def _prose_pointer(**extra):
    return {
        "file_id": "f1",
        "text_file": "text/legends.txt",
        "n_chars": 10_995,
        "extractor": "docx",
        "description": "Legends for the supplementary tables.",
        "mentions_cell_types": True,
        "evidence": "full_text",
        **extra,
    }


def _table_pointer(**extra):
    return {
        "file_id": "f1",
        "locator": "Sheet1",
        "content_type": "cluster_annotation",
        "description": "Cluster-to-name mapping.",
        "evidence": "rows_read",
        **extra,
    }


def test_recording_prose_leaves_the_tables_index_alone(tmp_path):
    # Tables are the indexing agent's, written from the store's own outline and
    # slice. Nothing here has looked at a spreadsheet.
    doi = _manifest(tmp_path, tables=[_table_pointer()])

    path = write_into_manifest(tmp_path, doi, AssessResult(prose=[_prose_pointer()]))
    written = json.loads(path.read_text())

    assert written["tables"] == [_table_pointer()]
    assert len(written["prose"]) == 1


def test_an_existing_cas_uptake_note_survives_a_re_record(tmp_path):
    # Uptake records something a later step did. This pass knows nothing about
    # it and must not erase it.
    uptake = {"at": "2026-09-05T00:00:00+00:00", "note": "synonyms taken into CAS+"}
    doi = _manifest(tmp_path, prose=[_prose_pointer(description="old", cas_uptake=uptake)])

    path = write_into_manifest(
        tmp_path, doi, AssessResult(prose=[_prose_pointer(description="new")])
    )
    written = json.loads(path.read_text())

    assert written["prose"][0]["description"] == "new"
    assert written["prose"][0]["cas_uptake"] == uptake


def test_the_written_manifest_validates(tmp_path):
    doi = _manifest(tmp_path)
    result = AssessResult(
        prose=[_prose_pointer(evidence="outline", n_chars=120_000)],
        gaps=[{"file_id": "f1", "reason": "not characterised: no verdict was returned for it"}],
    )

    path = write_into_manifest(tmp_path, doi, result)
    jsonschema.validate(
        json.loads(path.read_text()), load_schema("supplement_manifest.schema.json")
    )


def test_cas_uptake_stamps_a_prose_pointer(tmp_path):
    doi = _manifest(tmp_path, prose=[_prose_pointer()])

    path = record_cas_uptake(
        tmp_path, doi, "prose|f1|", "legends used for CAS+ synonyms", "2026-09-05T00:00:00+00:00"
    )
    written = json.loads(path.read_text())

    assert written["prose"][0]["cas_uptake"]["note"] == "legends used for CAS+ synonyms"
    jsonschema.validate(written, load_schema("supplement_manifest.schema.json"))


def test_cas_uptake_stamps_a_table_pointer_too(tmp_path):
    # A cluster-to-name sheet is the commonest thing to take into CAS+.
    doi = _manifest(tmp_path, tables=[_table_pointer()])

    path = record_cas_uptake(
        tmp_path, doi, "table|f1||Sheet1", "cluster names taken", "2026-09-05T00:00:00+00:00"
    )
    written = json.loads(path.read_text())

    assert written["tables"][0]["cas_uptake"]["note"] == "cluster names taken"


def test_cas_uptake_against_an_unknown_unit_is_an_error(tmp_path):
    doi = _manifest(tmp_path, prose=[_prose_pointer()])
    with pytest.raises(SupplementProseError, match="no pointer with id"):
        record_cas_uptake(tmp_path, doi, "prose|nope|", "x", "2026-09-05T00:00:00+00:00")
