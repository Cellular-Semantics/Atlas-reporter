"""Regression tests for orchestration step output schemas.

Pins schema conformance for the four intermediate output files produced
during the workflow: name_resolution, supplementary_findings, all_summaries,
and paper_catalogue. Golden fixtures are derived from the real
fetal_skin_atlas / Iron-recycling_macrophage workflow run.

Pattern: each schema gets a valid golden fixture, then targeted invalid
variants that test the constraints that matter most for anti-hallucination
(required fields, additionalProperties, enum values, minItems).
"""

from __future__ import annotations

import copy

import pytest

jsonschema = pytest.importorskip("jsonschema")

from atlas_chat.schemas import load_schema  # noqa: E402

# ---------------------------------------------------------------------------
# Golden fixtures (from real fetal_skin_atlas run)
# ---------------------------------------------------------------------------

VALID_NAME_RESOLUTION: dict = {
    "label": "Iron-recycling macrophage",
    "resolved_names": ["Iron-recycling macrophage", "iron-recycling macrophage"],
    "scope": "fetal",
    "tissue_context": "prenatal human skin (7-17 post-conception weeks)",
    "confidence": "high",
    "evidence": (
        "Explicitly named in main text of Gopee et al. 2024 as one of four macrophage subsets."
    ),
}

VALID_SUPPLEMENTARY_FINDINGS: dict = {
    "markers": [
        {"gene": "CD5L", "evidence_type": "DE analysis", "source_table": "Supplementary Table 3"},
        {
            "gene": "SLC40A1",
            "evidence_type": "DE analysis / annotation marker",
            "source_table": "Extended Data Fig. 6e",
        },
    ],
    "other_findings": [
        {
            "finding": "Iron-recycling macrophages contribute to spatial microenvironment ME2",
            "category": "location / microenvironment",
            "source_table": "Peer review response Fig. 1d",
        }
    ],
    "evidence_quotes": [
        {
            "quote": "Iron-recycling macrophages: CD5L, APOE, VCAM, TIMD4, SLC40A1",
            "source_file": "Peer Review file - response to Reviewer 2, point 2.2",
            "context": "Marker genes used to annotate iron-recycling macrophage subset",
        }
    ],
}

# Full-text path entry (source_method != snippet_search)
VALID_SUMMARY_FULLTEXT: dict = {
    "paper_doi": "10.1038/s41586-024-08002-x",
    "paper_title": "A prenatal skin atlas reveals immune regulation of human skin morphogenesis",
    "authors": "Gopee NH et al.",
    "year": 2024,
    "journal": "Nature",
    "topic": "Iron-recycling macrophage markers and microenvironment",
    "summary": (
        "Gopee et al. identify iron-recycling macrophages as one of four subsets in prenatal skin."
    ),
    "quotes": ["Iron-recycling macrophages: CD5L, APOE, VCAM, TIMD4, SLC40A1"],
    "source_method": "full_text_europepmc",
}

# ASTA snippet path entry
VALID_SUMMARY_ASTA: dict = {
    "source_corpus_id": "2762329",
    "source_title": "A prenatal skin atlas",
    "section": "Results",
    "snippet_score": 0.57,
    "summary": "Iron-recycling macrophages are found in neurovascular niches.",
    "quotes": ["Iron-recycling macrophages co-locate with endothelial cells"],
    "ref_corpus_ids": ["22612890"],
    "depth": 0,
    "source_method": "snippet_search",
}

VALID_PAPER_CATALOGUE: dict = {
    "10.1038/s41586-024-08002-x": {
        "doi": "10.1038/s41586-024-08002-x",
        "title": "A prenatal skin atlas reveals immune regulation of human skin morphogenesis",
        "authors": "Gopee NH et al.",
        "first_author": "Gopee",
        "year": 2024,
        "journal": "Nature",
        "pmid": "39415002",
        "pmcid": "PMC11578897",
        "role": "primary_atlas",
    },
    "10.1126/science.abo0510": {
        "doi": "10.1126/science.abo0510",
        "title": "Mapping the developing human immune system across organs",
        "authors": "Suo C et al.",
        "first_author": "Suo",
        "year": 2022,
        "journal": "Science",
        "pmid": "35549310",
        "pmcid": None,
        "role": "cited_by_atlas",
    },
}


# ---------------------------------------------------------------------------
# name_resolution
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def name_resolution_validator():
    return jsonschema.Draft202012Validator(load_schema("name_resolution.schema.json"))


@pytest.mark.unit
def test_name_resolution_valid(name_resolution_validator):
    assert list(name_resolution_validator.iter_errors(VALID_NAME_RESOLUTION)) == []


@pytest.mark.unit
def test_name_resolution_missing_required(name_resolution_validator):
    doc = copy.deepcopy(VALID_NAME_RESOLUTION)
    del doc["tissue_context"]
    assert list(name_resolution_validator.iter_errors(doc))


@pytest.mark.unit
def test_name_resolution_extra_field(name_resolution_validator):
    doc = copy.deepcopy(VALID_NAME_RESOLUTION)
    doc["unexpected"] = "nope"
    assert list(name_resolution_validator.iter_errors(doc))


@pytest.mark.unit
def test_name_resolution_bad_confidence_enum(name_resolution_validator):
    doc = copy.deepcopy(VALID_NAME_RESOLUTION)
    doc["confidence"] = "very high"
    assert list(name_resolution_validator.iter_errors(doc))


@pytest.mark.unit
def test_name_resolution_bad_scope_enum(name_resolution_validator):
    doc = copy.deepcopy(VALID_NAME_RESOLUTION)
    doc["scope"] = "embryonic"
    assert list(name_resolution_validator.iter_errors(doc))


@pytest.mark.unit
def test_name_resolution_empty_resolved_names(name_resolution_validator):
    doc = copy.deepcopy(VALID_NAME_RESOLUTION)
    doc["resolved_names"] = []
    assert list(name_resolution_validator.iter_errors(doc))


# ---------------------------------------------------------------------------
# supplementary_findings
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def suppl_findings_validator():
    return jsonschema.Draft202012Validator(load_schema("supplementary_findings.schema.json"))


@pytest.mark.unit
def test_suppl_findings_valid(suppl_findings_validator):
    assert list(suppl_findings_validator.iter_errors(VALID_SUPPLEMENTARY_FINDINGS)) == []


@pytest.mark.unit
def test_suppl_findings_empty_arrays_valid(suppl_findings_validator):
    # Empty markers/other_findings/evidence_quotes are allowed (may find nothing)
    doc = {"markers": [], "other_findings": [], "evidence_quotes": []}
    assert list(suppl_findings_validator.iter_errors(doc)) == []


@pytest.mark.unit
def test_suppl_findings_missing_required(suppl_findings_validator):
    doc = copy.deepcopy(VALID_SUPPLEMENTARY_FINDINGS)
    del doc["markers"]
    assert list(suppl_findings_validator.iter_errors(doc))


@pytest.mark.unit
def test_suppl_findings_extra_field_in_marker(suppl_findings_validator):
    doc = copy.deepcopy(VALID_SUPPLEMENTARY_FINDINGS)
    doc["markers"][0]["p_value"] = 0.01
    assert list(suppl_findings_validator.iter_errors(doc))


@pytest.mark.unit
def test_suppl_findings_extra_top_level_field(suppl_findings_validator):
    doc = copy.deepcopy(VALID_SUPPLEMENTARY_FINDINGS)
    doc["raw_text"] = "..."
    assert list(suppl_findings_validator.iter_errors(doc))


# ---------------------------------------------------------------------------
# all_summaries
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def all_summaries_validator():
    return jsonschema.Draft202012Validator(load_schema("all_summaries.schema.json"))


@pytest.mark.unit
def test_all_summaries_fulltext_valid(all_summaries_validator):
    assert list(all_summaries_validator.iter_errors([VALID_SUMMARY_FULLTEXT])) == []


@pytest.mark.unit
def test_all_summaries_asta_valid(all_summaries_validator):
    assert list(all_summaries_validator.iter_errors([VALID_SUMMARY_ASTA])) == []


@pytest.mark.unit
def test_all_summaries_mixed_valid(all_summaries_validator):
    docs = [VALID_SUMMARY_FULLTEXT, VALID_SUMMARY_ASTA]
    assert list(all_summaries_validator.iter_errors(docs)) == []


@pytest.mark.unit
def test_all_summaries_missing_summary(all_summaries_validator):
    doc = copy.deepcopy(VALID_SUMMARY_FULLTEXT)
    del doc["summary"]
    assert list(all_summaries_validator.iter_errors([doc]))


@pytest.mark.unit
def test_all_summaries_missing_source_method(all_summaries_validator):
    doc = copy.deepcopy(VALID_SUMMARY_FULLTEXT)
    del doc["source_method"]
    assert list(all_summaries_validator.iter_errors([doc]))


@pytest.mark.unit
def test_all_summaries_extra_field_rejected(all_summaries_validator):
    doc = copy.deepcopy(VALID_SUMMARY_FULLTEXT)
    doc["hallucinated_field"] = "value"
    assert list(all_summaries_validator.iter_errors([doc]))


# ---------------------------------------------------------------------------
# paper_catalogue
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def paper_catalogue_validator():
    return jsonschema.Draft202012Validator(load_schema("paper_catalogue.schema.json"))


@pytest.mark.unit
def test_paper_catalogue_valid(paper_catalogue_validator):
    assert list(paper_catalogue_validator.iter_errors(VALID_PAPER_CATALOGUE)) == []


@pytest.mark.unit
def test_paper_catalogue_null_pmcid_valid(paper_catalogue_validator):
    # pmcid: null is allowed when unavailable
    doc = copy.deepcopy(VALID_PAPER_CATALOGUE)
    doc["10.1038/s41586-024-08002-x"]["pmcid"] = None
    assert list(paper_catalogue_validator.iter_errors(doc)) == []


@pytest.mark.unit
def test_paper_catalogue_bad_role(paper_catalogue_validator):
    doc = copy.deepcopy(VALID_PAPER_CATALOGUE)
    doc["10.1038/s41586-024-08002-x"]["role"] = "unknown"
    assert list(paper_catalogue_validator.iter_errors(doc))


@pytest.mark.unit
def test_paper_catalogue_missing_first_author(paper_catalogue_validator):
    doc = copy.deepcopy(VALID_PAPER_CATALOGUE)
    del doc["10.1038/s41586-024-08002-x"]["first_author"]
    assert list(paper_catalogue_validator.iter_errors(doc))


@pytest.mark.unit
def test_paper_catalogue_extra_field_rejected(paper_catalogue_validator):
    doc = copy.deepcopy(VALID_PAPER_CATALOGUE)
    doc["10.1038/s41586-024-08002-x"]["unexpected"] = "value"
    assert list(paper_catalogue_validator.iter_errors(doc))
