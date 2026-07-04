"""Shared writer: intermediate loader output -> schema-valid project files.

Every project-initialisation loader (local h5ad/zarr, CELLxGENE, spreadsheet,
DOI/paper-only, ...) converges here. Loaders stay simple and produce a single
in-process **intermediate** dict; this module is the *only* thing that writes
the canonical ``cell_type_annotations.json``, guaranteeing schema conformance in
one place.

Design rules (see project memory):
  * **Schema-first.** The JSON Schema is the single source of truth. This module
    does NOT re-declare allowed values; the sole enforcement point is
    :func:`validate_annotations`, driven by ``cell_type_annotation.schema.json``.
  * **No enums on free text.** ``scope``/``granularity`` and every co-annotation
    value are preserved verbatim from upstream; controlled vocabulary is added
    later by an explicit ontology-mapping step, never by constraining raw text.
  * **Co-annotations are inline.** Diverse covariates (``broad_celltype``,
    ``germlayer``, ``organ``, ``development_stage``, ...) are written as sibling
    keys on each annotation object, matching the working HDCA config.

Intermediate shape (in-process, not persisted)::

    {
      "labels": [
        {
          "label": "AUTONOMIC_NCCS_SCPS",     # required, verbatim
          "n_cells": 15860,                    # optional
          "scope": "fetal",                    # optional, verbatim (no enum)
          "granularity": "fine",               # optional, verbatim (no enum)
          "covariates": {                      # optional; merged inline, one shape each
              "germlayer": "ECTODERM",                     # scalar
              "organ": [{"value": "whole_embryo", "share": 0.673}, ...],   # distribution
              "development_stage": [{"value": "HsapDv:0000023", "share": 0.47}, ...]
          },
          # optional provenance, preserved verbatim into label_provenance.json:
          "studies": [["whole_embryo", 10670, 0.673], ...],
          "top_author_labels": [["AC", 77, 0.987], ...]
        },
        ...
      ],
      "source_meta": {
        "doi": "10.1038/...",                  # required (schema needs it)
        "title": "...",                        # optional passthrough
        "pmcid": "...", "pmid": "...", "abstract": "...", "authors": [...],
        "local_text_path": "...",              # optional
        "subatlas_papers": [...],              # optional (subatlas_resolver shape)
        "data_provenance": {"source_type": "spreadsheet", ...}  # optional
      }
    }

Outputs written under ``project_dir``:
  - ``cell_type_annotations.json``  — canonical, schema-validated (co-annotations inline)
  - ``label_provenance.json``       — only when labels carry provenance fields
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from atlas_chat.schemas import load_schema

_SCHEMA_NAME = "cell_type_annotation.schema.json"

# Reserved annotation keys; everything else on the object is a co-annotation.
_RESERVED_KEYS = ("label", "scope", "granularity", "n_cells")

# Top-level source fields copied straight through from source_meta when present.
_SOURCE_PASSTHROUGH = (
    "doi",
    "title",
    "pmcid",
    "pmid",
    "abstract",
    "authors",
    "local_text_path",
    "subatlas_papers",
    "data_provenance",
)

# Provenance fields preserved verbatim, per label, into label_provenance.json.
_PROVENANCE_KEYS = ("n_cells", "studies", "top_author_labels")

# OBO-style CURIE (prefix:digits), used to recognise covariate values that are
# already ontology terms (e.g. "HsapDv:0000048") so we can self-populate `curie`.
_CURIE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*:[0-9]+$")


@dataclass
class AnnotationsBundle:
    """Derived documents ready to serialise."""

    annotations: dict[str, Any]
    label_provenance: dict[str, Any] | None = None


def _normalize_covariate_value(item: Any) -> Any:
    """Self-populate ontology slots when a distribution value is already a CURIE.

    Additive only — never rewrites the verbatim ``value``. Leaves free-text
    values (and any item that already carries a ``curie``) untouched, ready for a
    later explicit mapping step.
    """
    if not isinstance(item, dict) or "value" not in item or "curie" in item:
        return item
    value = item["value"]
    if isinstance(value, str) and _CURIE_RE.match(value):
        return {**item, "curie": value, "ontology": value.split(":", 1)[0]}
    return item


def _normalize_covariate(value: Any) -> Any:
    """Normalise a covariate: pass scalars through, CURIE-enrich distributions."""
    if isinstance(value, list):
        return [_normalize_covariate_value(it) for it in value]
    return value


def _build_annotation(label_entry: dict[str, Any]) -> dict[str, Any]:
    """Map one intermediate label to a ``CellTypeAnnotation`` with inline covariates.

    No vocabulary validation happens here — scope/granularity/covariate values
    are preserved verbatim and enforced (for shape) by :func:`validate_annotations`.
    """
    label = label_entry.get("label")
    if not label or not str(label).strip():
        raise ValueError(f"label entry missing a non-empty 'label': {label_entry!r}")

    # Start from covariates so reserved keys (set below) always win on collision.
    annotation: dict[str, Any] = {}
    for key, value in (label_entry.get("covariates") or {}).items():
        if key in _RESERVED_KEYS:
            continue
        annotation[key] = _normalize_covariate(value)

    annotation["label"] = label
    for key in ("scope", "granularity"):
        if label_entry.get(key) is not None:
            annotation[key] = label_entry[key]
    if label_entry.get("n_cells") is not None:
        annotation["n_cells"] = int(label_entry["n_cells"])

    return annotation


def _build_source(source_meta: dict[str, Any]) -> dict[str, Any]:
    """Assemble the ``source`` block from passthrough source_meta fields."""
    doi = (source_meta.get("doi") or "").strip()
    if not doi:
        raise ValueError(
            "source_meta is missing 'doi'. Every project needs a DOI for the report "
            "workflow; prompt the user for one before writing the project."
        )
    source: dict[str, Any] = {}
    for key in _SOURCE_PASSTHROUGH:
        value = source_meta.get(key)
        if value is not None:
            source[key] = value
    source["doi"] = doi
    return source


def build_documents(intermediate: dict[str, Any]) -> AnnotationsBundle:
    """Pure transform: intermediate -> the derived documents.

    Performs no I/O and no schema validation (call :func:`validate_annotations`
    or use :func:`write_project`, which validates before writing).
    """
    labels = intermediate.get("labels") or []
    if not labels:
        raise ValueError("intermediate has no 'labels' — nothing to write.")
    source_meta = intermediate.get("source_meta") or {}

    source = _build_source(source_meta)
    annotations = [_build_annotation(entry) for entry in labels]
    annotations_doc = {"source": source, "annotations": annotations}

    provenance: dict[str, Any] = {}
    for entry in labels:
        prov_entry = {k: entry[k] for k in _PROVENANCE_KEYS if entry.get(k) is not None}
        # Only emit when there is actual source/author breakdown, not just a count.
        if prov_entry.keys() & {"studies", "top_author_labels"}:
            provenance[entry["label"]] = prov_entry

    return AnnotationsBundle(
        annotations=annotations_doc,
        label_provenance=provenance or None,
    )


def validate_annotations(doc: dict[str, Any]) -> list[str]:
    """Validate a ``cell_type_annotations.json`` doc against the JSON Schema.

    This is the single enforcement point — constraints come from the schema, not
    from this module. Returns a list of human-readable error strings (empty when
    valid).
    """
    import jsonschema

    schema = load_schema(_SCHEMA_NAME)
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
    return [f"{'/'.join(str(p) for p in e.path) or '<root>'}: {e.message}" for e in errors]


def write_project(
    project_dir: str | Path,
    intermediate: dict[str, Any],
    *,
    validate: bool = True,
) -> dict[str, Path]:
    """Write project files from an intermediate dict; validate first by default.

    Returns a mapping of artifact name -> written path. Raises ``ValueError`` if
    the produced ``cell_type_annotations.json`` fails schema validation.
    """
    project_dir = Path(project_dir)
    bundle = build_documents(intermediate)

    if validate:
        errors = validate_annotations(bundle.annotations)
        if errors:
            joined = "\n  - ".join(errors)
            raise ValueError(
                f"Generated cell_type_annotations.json is not schema-valid:\n  - {joined}"
            )

    project_dir.mkdir(parents=True, exist_ok=True)
    written: dict[str, Path] = {}

    ann_path = project_dir / "cell_type_annotations.json"
    ann_path.write_text(json.dumps(bundle.annotations, indent=2) + "\n", encoding="utf-8")
    written["cell_type_annotations"] = ann_path

    if bundle.label_provenance is not None:
        prov_path = project_dir / "label_provenance.json"
        prov_path.write_text(json.dumps(bundle.label_provenance, indent=2) + "\n", encoding="utf-8")
        written["label_provenance"] = prov_path

    return written
