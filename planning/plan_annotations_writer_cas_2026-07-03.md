# Plan: annotations_writer → CAS (big-bang step 2, detailed)

**Date:** 2026-07-03
**Depends on:** `cas_annotation.schema.json` (landed, tested),
`mockup_cas_cxg_annotations_2026-06-24.md` (composition Variant B),
`plan_cas_migration_bigbang_and_prog_agentic_split_2026-06-24.md`.

**Low risk:** `annotations_writer` is imported only by its own test — no live
pipeline consumes it yet. Rewriting it breaks nothing downstream.

---

## 1. Role in the boundary

`annotations_writer` is **purely programmatic** — a deterministic
`intermediate dict → CAS docs` transform + schema validation + file write. It
consumes the classifier's *judgment* (already baked into the intermediate) but
makes none of its own. No LLM, no I/O beyond the final write. This is the
canonical "programmatic side" unit and should be exhaustively unit-tested.

The **assembler** that builds the intermediate (cross-tabs from run.py + roles
from classify-obs-fields) is a separate programmatic step (§6). The writer stays
a pure transform so it's trivially golden-testable.

---

## 2. New input contract — the intermediate dict (v2)

The seam with the rest of the load path. Role-annotated so the writer never
guesses:

```jsonc
{
  "source_meta": { "doi": "...", "title": "...", "subatlas_papers": [...],
                   "data_provenance": {...} },          // as today
  "matrix_file_id": "https://.../hdca_v2.zarr",          // NEW

  "labelsets": [                                         // NEW (from classifier)
    { "name": "refined_celltype", "role": "author_cell_type",
      "rank": 0, "annotation_method": "manual" },
    { "name": "broad_celltype", "role": "author_cell_type",
      "rank": 1, "annotation_method": "manual" }
  ],

  "cell_sets": [                                         // replaces flat "labels"
    {
      "labelset": "refined_celltype",
      "cell_label": "AMACRINE_CELL",
      "n_cells": 78,
      "parent_label": "AUDIOVISUAL_NEURONAL",            // in the next coarser labelset, or null
      "composition": {                                   // keyed by cxg_field / open key
        "tissue": { "author_field_name": "organ",
          "values": [ { "author_value": "Retina", "cell_count": 78, "cell_ratio": 1.0 } ] },
        "development_stage": { "author_field_name": "development_stage",
          "values": [ { "author_value": "unknown", "cell_ratio": 0.808 },
                      { "author_value": "HsapDv:0000048", "cell_ratio": 0.103 } ] }
      },
      "transferred": [                                   // from transferred_labelset x dataset_reference
        { "transferred_cell_label": "AC", "source_label": "Sridhar_et_al_2020_CellPress",
          "cell_count": 77, "cell_ratio": 0.987 }
      ],
      "author_annotation_fields": { "scope": "fetal" }   // unmapped only (assembler guarantees)
    }
  ]
}
```

Non-integrated atlas: `labelsets` has one entry, `cell_sets` carry no
`transferred`, `parent_label` is null. (Matches the fetal_skin golden.)

---

## 3. The transform, field by field

Top level → `{title, source, matrix_file_id, labelsets, annotations}`:

| Output | From | Notes |
|---|---|---|
| `title` | `source_meta.title` | fallback to matrix_file_id basename |
| `source` | `_build_source(source_meta)` | **REUSED as-is** |
| `matrix_file_id` | `intermediate.matrix_file_id` | passthrough |
| `labelsets` | `intermediate.labelsets` | passthrough, sorted by `rank` |
| `annotations[]` | one per `cell_sets[]` entry | §4 |

Per `cell_sets[]` entry → one `Annotation`:

| Annotation field | From | Notes |
|---|---|---|
| `labelset`, `cell_label`, `n_cells` | direct | |
| `cell_set_accession` | generated | `f"{ns}:{labelset}:{cell_label}"` (ns = §7 open) |
| `parent_cell_set_accession` | `parent_label` + parent labelset | null-safe; parent labelset = next-coarser rank |
| `composition` | `composition` | CURIE-enrich each value (§5) |
| `transferred_annotations` | `transferred` | resolve `source_label`→`source_taxonomy` PURL via `source_meta.subatlas_papers`; add `comment` = "Integration provenance (not algorithmic transfer)." |
| `author_annotation_fields` | direct | assembler guarantees unmapped-only; writer asserts (§4) |
| `cell_fullname`, `cell_ontology_term_id`, `cell_ontology_term`, `rationale`, `rationale_dois`, `marker_gene_evidence` | **absent at load** | filled later by name_resolver / ontology-term-lookup / report steps. The CAS doc is *progressively enriched*. |

Key point: at **project-init** the writer emits labelsets + annotation
*skeletons* (label, counts, composition, transfer, hierarchy). The **biological**
fields are populated by the downstream report workflow, in place, on the same
CAS doc.

---

## 4. Hard cases, handled explicitly

- **Multiple labelsets.** One annotation per `(labelset, cell_label)`. `refined`
  and `broad` both appear in `annotations[]`; hierarchy links them.
- **Hierarchy / parent.** `parent_label` comes from the assembler's
  fine×coarse cross-tab (each fine set falls ~entirely in one coarse set). The
  writer only maps it to `parent_cell_set_accession`. The *subsumption check*
  is `validation/hierarchy_checker.py` (step 3), run before write; the writer
  fails the doc if a `parent_label` has no matching coarse annotation.
- **transferred_annotations = integration provenance.** `source_label` →
  `source_taxonomy` by lookup in `source_meta.subatlas_papers` (label→doi →
  `DOI:...`). Unresolved → omit `source_taxonomy`, keep label in `comment`. This
  is where `subatlas_resolver` output feeds in.
- **author_annotation_fields de-dup (invariant).** Writer asserts no key in
  `author_annotation_fields` equals a labelset name or a `composition` category
  key. Violation raises (guards the assembler).
- **label_provenance.json is SUBSUMED** — `studies`→composition (a `study`
  category) + `transferred_annotations.source_taxonomy`; `top_author_labels`→
  `transferred_annotations`. Writer stops emitting the separate file.

---

## 5. CURIE enrichment (adapt existing logic)

Current `_normalize_covariate_value` turns a covariate `{value: "HsapDv:0000048"}`
into `{value, curie, ontology}`. Re-target to composition:
`{author_value: "HsapDv:0000048"}` → add `ontology_term_id: "HsapDv:0000048"`.
`_CURIE_RE` reused verbatim. **Only self-population of already-CURIE author
values** — free-text mapping (organ "Retina" → UBERON) is a later *explicit*
ontology step, never the writer (no-enum / map-later, [[schema-first-no-enums-on-freetext]]).

---

## 6. Reuse / rewrite / delete

| Symbol | Fate |
|---|---|
| `_build_source`, `_SOURCE_PASSTHROUGH` | **reuse** |
| `_CURIE_RE`, `_normalize_covariate_value` | **adapt** → composition (`ontology_term_id`) |
| `validate_annotations` | **repoint** `_SCHEMA_NAME` → `cas_annotation.schema.json` |
| `write_project` | **keep**; drop `label_provenance.json` write |
| `_build_annotation`, `build_documents` | **rewrite** for CAS shape |
| `_RESERVED_KEYS`, `_PROVENANCE_KEYS`, `_normalize_covariate`, `AnnotationsBundle.label_provenance` | **delete** (roles now explicit; provenance subsumed) |

Assembler (`intermediate` builder) — new programmatic function, likely
`build_intermediate(cross_tabs, field_classification)`; reuses run.py's
`cross_tabulate`. Can live in the same module or a sibling; keep the writer a
pure transform either way.

---

## 7. TDD (against the landed golden fixtures)

Red→green, offline:

1. **Golden round-trip.** Hand-author the v2 intermediate for HDCA AMACRINE_CELL
   (+ broad parent) → `build_documents` → assert output validates AND deep-equals
   the `VALID_HDCA_INTEGRATED` fixture in `test_cas_annotation_schema.py` (share
   the fixture).
2. **Non-integrated.** fetal_skin intermediate → validates, `annotations[0]` has
   no `transferred_annotations`, `labelsets` length 1 (over-fit guard mirrors
   the schema test).
3. **CURIE enrichment.** `author_value:"HsapDv:0000048"` → `ontology_term_id` set;
   existing `ontology_term_id` never overwritten; free-text left bare.
4. **Hierarchy.** `parent_label` → correct `parent_cell_set_accession`; dangling
   parent (no coarse annotation) raises.
5. **transferred source_taxonomy** resolved from `subatlas_papers`; unresolved →
   omitted + comment retains label.
6. **aaf de-dup invariant** raises when a labelset/composition key leaks in.
7. **Schema-invalid output raises** in `write_project` (repoint check).
8. Keep the existing writer tests only for symbols that survive; delete tests for
   deleted behaviour in the same commit.

---

## 8. Open questions

1. **`cell_set_accession` namespace** (blocks accession generation): project
   slug? source DOI hash? `{PROJECT}:{labelset}:{label}`? Needs a scheme stable
   across re-runs (migration-plan open decision #5).
2. **Assembler location** — same module vs sibling service. (Lean sibling:
   `services/annotation_assembler.py`, so the writer file stays a pure transform.)
3. **`n_cells` vs cell_count naming** across composition/transferred/annotation —
   confirm consistent (annotation `n_cells`; per-value `cell_count`).
4. **Delete label_provenance.json** — confirmed consumers:
   `services/subatlas_resolver.py` (reads study labels to resolve DOIs) and
   `.claude/skills/local-paper-index/SKILL.md`. Big-bang must re-point
   `subatlas_resolver` to read study labels from the CAS doc
   (`transferred_annotations` + `composition.study`) instead. Not optional — it's
   a live dependency, so this couples step 2 (writer) to the subatlas path.
