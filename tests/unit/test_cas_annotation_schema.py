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
