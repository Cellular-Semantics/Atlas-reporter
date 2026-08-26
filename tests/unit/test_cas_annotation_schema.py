"""Schema regression for the CAS+ cell-annotation collection.

Pins cas_annotation.schema.json: well-formedness, the minimal valid document
(the floor for the "simple list + paper" starting point), the local extensions
(nullable parent, transferred-annotation subatlas_paper/source_labelset), and the
additionalProperties teeth on the root / Labelset / DataProvenance objects.
"""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

from atlas_chat.schemas import load_schema

FIXTURES = Path(__file__).parent / "fixtures" / "cas"
SCHEMA = "cas_annotation.schema.json"


def _load(name: str) -> object:
    return json.loads((FIXTURES / name).read_text())


def _errors(data: object) -> list[str]:
    validator = jsonschema.Draft202012Validator(load_schema(SCHEMA))
    return [e.message for e in validator.iter_errors(data)]


@pytest.mark.unit
def test_schema_is_well_formed() -> None:
    jsonschema.Draft202012Validator.check_schema(load_schema(SCHEMA))


@pytest.mark.unit
def test_minimal_document_validates() -> None:
    # The floor for a "simple list of annotations + a paper" starting point.
    assert _errors(_load("cas_annotation.minimal.good.json")) == []


@pytest.mark.unit
def test_rich_document_validates() -> None:
    assert _errors(_load("cas_annotation.good.json")) == []


@pytest.mark.unit
def test_annotation_requires_cell_label() -> None:
    assert _errors(_load("cas_annotation.bad.json"))


@pytest.mark.unit
def test_parent_cell_set_accession_is_nullable() -> None:
    data = _load("cas_annotation.good.json")
    assert data["annotations"][0]["parent_cell_set_accession"] is None
    assert _errors(data) == []


@pytest.mark.unit
def test_transferred_annotation_carries_subatlas_and_source_labelset() -> None:
    data = _load("cas_annotation.good.json")
    ta = data["annotations"][0]["transferred_annotations"][0]
    assert ta["subatlas_paper"] == "Smith2021"
    assert ta["source_labelset"] == "celltype_Smith2021"
    assert _errors(data) == []


@pytest.mark.unit
def test_transferred_annotation_carries_the_atlas_wide_label_total() -> None:
    """``source_label_cell_count`` is what makes the reverse share computable.

    ``cell_count`` / ``cell_ratio`` say how much of *this cell set* an upstream
    label accounted for. The atlas-wide total says how much of that *upstream
    label* this cell set captured — which is how a consumer tells an upstream cell
    type the atlas split from one it merely renamed.
    """
    data = _load("cas_annotation.good.json")
    ta = data["annotations"][0]["transferred_annotations"][0]
    assert ta["cell_count"] / ta["source_label_cell_count"] == 0.25
    assert _errors(data) == []


@pytest.mark.unit
def test_source_label_cell_count_must_be_a_non_negative_integer() -> None:
    data = _load("cas_annotation.good.json")
    data["annotations"][0]["transferred_annotations"][0]["source_label_cell_count"] = -1
    assert _errors(data)


@pytest.mark.unit
def test_root_additional_properties_are_closed() -> None:
    data = _load("cas_annotation.minimal.good.json")
    data["bogus_top_level"] = 1
    assert _errors(data)


@pytest.mark.unit
def test_annotation_additional_properties_are_closed() -> None:
    data = _load("cas_annotation.minimal.good.json")
    data["annotations"][0]["bogus_field"] = 1
    assert _errors(data)


@pytest.mark.unit
def test_labelset_additional_properties_are_closed() -> None:
    data = _load("cas_annotation.minimal.good.json")
    data["labelsets"][0]["bogus_field"] = 1
    assert _errors(data)


# --------------------------------------------------------------------------
# ASTA indexing band (#22)
# --------------------------------------------------------------------------


@pytest.mark.unit
def test_subatlas_papers_carry_the_asta_indexing_band() -> None:
    """Band and ingest route are separate axes and both round-trip."""
    papers = _load("cas_annotation.good.json")["source"]["subatlas_papers"]
    served, built = papers[0], papers[1]

    assert served["status"] == "asta"
    assert served["asta_indexing"]["band"] == "full"

    # The point of keeping the two fields apart: ASTA holds only this paper's
    # abstract, yet its text is available locally because the JATS build worked.
    assert built["status"] == "local"
    assert built["source_type"] == "jats"
    assert built["asta_indexing"]["band"] == "abstract_only"

    assert _errors(_load("cas_annotation.good.json")) == []


@pytest.mark.unit
@pytest.mark.parametrize("band", ["full", "partial", "abstract_only", "unindexed", "not_in_s2"])
def test_every_band_value_is_accepted(band: str) -> None:
    data = _load("cas_annotation.good.json")
    data["source"]["subatlas_papers"][0]["asta_indexing"]["band"] = band
    assert _errors(data) == []


@pytest.mark.unit
def test_unknown_band_is_rejected() -> None:
    data = _load("cas_annotation.good.json")
    data["source"]["subatlas_papers"][0]["asta_indexing"]["band"] = "FULL"
    assert _errors(data)


@pytest.mark.unit
def test_asta_indexing_requires_a_band() -> None:
    data = _load("cas_annotation.good.json")
    data["source"]["subatlas_papers"][0]["asta_indexing"] = {"snippets": 30}
    assert _errors(data)


@pytest.mark.unit
def test_asta_indexing_additional_properties_are_closed() -> None:
    data = _load("cas_annotation.good.json")
    data["source"]["subatlas_papers"][0]["asta_indexing"]["bogus_field"] = 1
    assert _errors(data)


@pytest.mark.unit
def test_asta_indexing_counts_cannot_be_negative() -> None:
    data = _load("cas_annotation.good.json")
    data["source"]["subatlas_papers"][0]["asta_indexing"]["snippets"] = -1
    assert _errors(data)


@pytest.mark.unit
def test_source_type_is_constrained() -> None:
    data = _load("cas_annotation.good.json")
    data["source"]["subatlas_papers"][1]["source_type"] = "docx"
    assert _errors(data)
