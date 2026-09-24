"""Unit tests for finding a quote in the text it claims to come from."""

from __future__ import annotations

import json

import pytest
from atlas_chat.validation.quote_search import (
    check_items,
    load_sources,
    locate,
    normalise,
    sources_from_job,
)

pytestmark = pytest.mark.unit

JOB = {
    "narrative": {"text": "## Results\nThe population sits in the outer cortex."},
    "legends": [
        {"label": "Fig. 1", "text": "Sections profiled by spatial transcriptomics."},
        {"text": "An unlabelled caption."},
    ],
    "supplement_prose": [{"file_id": "s1.docx", "text": "Clusters were named by marker score."}],
}


def _item(*quotes: str, found: bool = True) -> dict:
    return {"aspect": "location", "found": found, "summary": "s", "quotes": list(quotes)}


def test_each_kind_of_text_is_a_source_of_its_own():
    """A quote from a caption must be known to have come from a caption."""
    assert set(sources_from_job(JOB)) == {
        "narrative",
        "legend:Fig. 1",
        "legend:1",
        "supplement:s1.docx",
    }


def test_an_empty_source_is_not_offered():
    assert sources_from_job({"narrative": {"text": "   "}}) == {}


def test_a_quote_is_located_to_the_source_holding_it():
    s = sources_from_job(JOB)
    assert locate("outer cortex", s) == ["narrative"]
    assert locate("spatial transcriptomics", s) == ["legend:Fig. 1"]
    assert locate("named by marker score", s) == ["supplement:s1.docx"]


def test_a_rewrapped_quote_still_matches():
    """Sources are re-wrapped from XML and from Word; the words are what matter."""
    assert locate("Results The population sits", sources_from_job(JOB)) == ["narrative"]


def test_an_invented_quote_is_found_nowhere():
    assert locate("The cells glowed faintly.", sources_from_job(JOB)) == []


def test_a_spliced_quote_is_found_nowhere():
    """Two real fragments joined are not something the author wrote."""
    spliced = "The population sits in the outer cortex. Clusters were named by marker score."
    assert locate(spliced, sources_from_job(JOB)) == []


def test_an_empty_quote_matches_nothing_rather_than_everything():
    assert locate("   ", sources_from_job(JOB)) == []


def test_normalise_collapses_runs_of_whitespace():
    assert normalise("a  \n b\t c ") == "a b c"


def test_items_pass_when_every_quote_is_found():
    s = sources_from_job(JOB)
    assert check_items([_item("outer cortex", "spatial transcriptomics")], s) == []


def test_an_unfindable_quote_is_reported_with_its_position():
    s = sources_from_job(JOB)
    problems = check_items([_item("outer cortex"), _item("never written")], s)
    assert len(problems) == 1
    assert problems[0].startswith("[1]")
    assert "never written" in problems[0]


def test_a_decline_carries_no_quotes_and_so_raises_nothing():
    assert check_items([_item(found=False)], sources_from_job(JOB)) == []


def test_sources_from_several_job_files_are_kept_apart(tmp_path):
    """Two papers may both use a phrase; which one it came from still matters."""
    d = tmp_path / "papers"
    d.mkdir()
    (d / "a.json").write_text(json.dumps({"narrative": {"text": "shared phrase, paper A"}}))
    (d / "b.json").write_text(json.dumps({"narrative": {"text": "shared phrase, paper B"}}))
    s = load_sources(sorted(d.glob("*.json")))
    assert set(s) == {"a/narrative", "b/narrative"}
    assert locate("shared phrase", s) == ["a/narrative", "b/narrative"]
    assert locate("paper B", s) == ["b/narrative"]


def test_an_unreadable_job_file_is_skipped_rather_than_raising(tmp_path):
    d = tmp_path / "papers"
    d.mkdir()
    (d / "broken.json").write_text("{not json")
    (d / "good.json").write_text(json.dumps({"narrative": {"text": "real text"}}))
    assert set(load_sources(sorted(d.glob("*.json")))) == {"good/narrative"}


# --- however the job file writes its text ------------------------------------

BLOCKS_JOB = {
    "narrative": {"blocks": ["## Results", "The population sits in the outer cortex."]},
    "legends": JOB["legends"],
    "supplement_prose": [
        {"file_id": "s1.docx", "blocks": ["Clusters were named by marker score."]}
    ],
}


def test_the_two_shapes_of_job_file_give_the_same_sources():
    """Text is written as blocks so a reader can page the file. `text` is what
    job files held before that, and is still read so evidence written beside one
    stays checkable without regenerating it."""
    assert sources_from_job(BLOCKS_JOB) == sources_from_job(JOB)


def test_a_quote_spanning_a_paragraph_break_is_still_found():
    """The property the split had to preserve. It holds because the split is on
    whitespace and matching normalises whitespace away."""
    assert locate("Results The population sits", sources_from_job(BLOCKS_JOB)) == ["narrative"]


def test_a_quote_the_paper_does_not_contain_is_not_found_either_way():
    """Strictness has to be preserved in both directions: the change must not
    make a quote verifiable that was not verifiable before."""
    invented = "The cells glowed faintly in the dark."
    assert locate(invented, sources_from_job(BLOCKS_JOB)) == []
    assert locate(invented, sources_from_job(JOB)) == []


def test_a_narrative_of_empty_blocks_is_no_source_at_all():
    assert sources_from_job({"narrative": {"blocks": []}}) == {}
