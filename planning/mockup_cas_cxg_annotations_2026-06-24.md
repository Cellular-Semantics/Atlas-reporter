# Mockups: CAS / CxG annotation shapes (for discussion — nothing locked)

Real HDCA_neurons data, two contrasting cells. Goal: react to concrete shapes
before deciding anything. Companion to
`plan_obs_field_classifier_and_cas_alignment_2026-06-24.md`.

---

## 0. What we have today (current bespoke shape)

```jsonc
// cell_type_annotations.json — annotations[]
{
  "label": "AMACRINE_CELL", "scope": "fetal", "granularity": "fine", "n_cells": 78,
  "broad_celltype": "AUDIOVISUAL_NEURONAL", "germlayer": "ECTODERM",
  "systems": "AUDIOVISUAL_SYSTEM", "organ": "Retina",
  "development_stage": [
    {"value": "unknown", "share": 0.808},
    {"value": "HsapDv:0000048", "share": 0.103, "curie": "HsapDv:0000048", "ontology": "HsapDv"},
    {"value": "HsapDv:0000054", "share": 0.09,  "curie": "HsapDv:0000054", "ontology": "HsapDv"}
  ]
}
// label_provenance.json — keyed by label, separate file
"AMACRINE_CELL": {
  "n_cells": 78,
  "studies": [["Sridhar_et_al_2020_CellPress", 78, 1.0]],
  "top_author_labels": [["AC", 77, 0.987], ["imGlia", 1, 0.013]]
}
```

Issues: cell-type col chosen by name allowlist; `studies`/`top_author_labels`
routed by literal-key allowlist; descriptor fields un-typed (no link to CxG);
no record of *which obs column* each co-annotation came from.

---

## 1. classify-obs-fields output (the new agentic step)

What the classifier returns after seeing each categorical obs column's name +
first-20 values. This is the new artifact; everything downstream reads it.

```jsonc
{
  "source_zarr": "hdca_v2_20260311_f2.zarr",
  "fields": [
    {
      "obs_column": "refined_celltype",
      "sample_values": ["AMACRINE_CELL", "BIPOLARS", "DL1_NEURON", "..."],
      "n_categories": 119,
      "functional_role": "author_labelset",   // -> CAS labelset, drives cell_label
      "cxg_field": "cell_type", "target_ontology": "CL",
      "confidence": "high",
      "evidence": "values are biological cell-type names; primary refined annotation"
    },
    {
      "obs_column": "original_author_annotation",
      "sample_values": ["AC", "Bipolars", "RGC", "DORSAL ROOT GANGLIA", "..."],
      "n_categories": 300,
      "functional_role": "transferred_labelset",  // -> CAS transferred_annotations
      "cxg_field": "cell_type", "target_ontology": "CL",
      "paired_reference_field": "study",
      "confidence": "high",
      "evidence": "per-cell author labels inherited from contributing studies"
    },
    {
      "obs_column": "study",
      "sample_values": ["Sridhar_et_al_2020_CellPress", "whole_embryo", "Suo_2022", "..."],
      "n_categories": 14,
      "functional_role": "dataset_reference",   // -> source_taxonomy PURLs
      "cxg_field": null, "target_ontology": null,
      "confidence": "high",
      "evidence": "values are study/dataset identifiers, resolvable to DOIs"
    },
    {
      "obs_column": "development_stage",
      "sample_values": ["HsapDv:0000048", "HsapDv:0000054", "unknown"],
      "n_categories": 12,
      "functional_role": "descriptor",
      "cxg_field": "development_stage", "target_ontology": "HsapDv",
      "confidence": "high",
      "evidence": "values are HsapDv CURIEs"
    },
    {
      "obs_column": "organ",
      "sample_values": ["Retina", "whole_embryo", "Gut ", "Limb", "Heart"],
      "n_categories": 20,
      "functional_role": "descriptor",
      "cxg_field": "tissue", "target_ontology": "UBERON",
      "confidence": "medium",
      "evidence": "anatomical structures; free-text, not yet CURIEs"
    },
    {
      "obs_column": "germlayer",
      "sample_values": ["ECTODERM", "MESODERM", "ENDODERM"],
      "n_categories": 3,
      "functional_role": "descriptor",
      "cxg_field": null, "target_ontology": "UBERON",   // germ layer is UBERON but no CxG slot
      "semantic_category": "germ_layer",                 // open free-text category
      "confidence": "high",
      "evidence": "the three germ layers"
    },
    {
      "obs_column": "leiden",
      "sample_values": ["0", "1", "2", "3", "..."],
      "n_categories": 64,
      "functional_role": "cluster_labelset",   // NOT author cell types (the old trap)
      "cxg_field": null, "target_ontology": null,
      "confidence": "high",
      "evidence": "integer cluster IDs, unannotated clustering output"
    },
    {
      "obs_column": "library_id",
      "sample_values": ["L001", "L002", "..."],
      "n_categories": 4679000,
      "functional_role": "ignore",
      "evidence": "n_categories ~= n_cells, per-cell-unique"
    }
  ]
}
```

---

## 2. CAS document mockup (general + BICAN extension)

```jsonc
{
  "title": "HDCA v2 — neurons",
  "description": "...",
  "matrix_file_id": "CellXGene_dataset:...",     // if available
  "cellannotation_schema_version": "0.1.0",

  "labelsets": [
    {"name": "refined_celltype", "description": "HDCA v2 refined author annotation",
     "annotation_method": "manual", "rank": 0},
    {"name": "broad_celltype", "annotation_method": "manual", "rank": 1},
    {"name": "leiden", "annotation_method": "algorithmic", "rank": 0,
     "automated_annotation": {"algorithm_name": "leiden", "algorithm_version": "...",
                              "algorithm_repo_url": "..."}}
  ],

  "annotations": [
    {
      "labelset": "refined_celltype",
      "cell_label": "AMACRINE_CELL",
      "cell_fullname": "amacrine cell",                 // <- name_resolver
      "cell_ontology_term_id": "CL:0000561",            // <- ontology-term-lookup
      "cell_ontology_term": "amacrine cell",
      "rationale": "Retinal interneuron... (Sridhar et al., 2020).",  // <- report
      "rationale_dois": ["10.1016/j.celrep.2020.108023"],
      "marker_gene_evidence": ["TFAP2A", "GAD1", "SLC6A9"],

      // subatlas / integrated reference  -> NATIVE CAS-BICAN slot
      "transferred_annotations": [
        {"transferred_cell_label": "AC",      "source_taxonomy": "DOI:10.1016/j.celrep.2020.108023", "comment": "share=0.987, n=77"},
        {"transferred_cell_label": "imGlia",  "source_taxonomy": "DOI:10.1016/j.celrep.2020.108023", "comment": "share=0.013, n=1"}
      ],

      // arbitrary original obs kept verbatim  -> NATIVE CAS slot
      "author_annotation_fields": {
        "scope": "fetal", "granularity": "fine",
        "broad_celltype": "AUDIOVISUAL_NEURONAL", "germlayer": "ECTODERM",
        "systems": "AUDIOVISUAL_SYSTEM"
      },

      // *** THE GAP: cross-tab composition ratios. Not in CAS. Two variants below. ***
      "composition": { /* see §3 */ }
    }
  ]
}
```

---

## 3. The one real extension — composition ratios. Two variants to choose between.

### Variant A — structured extension keyed by CxG field (typed)

```jsonc
"composition": {
  "n_cells": 78,
  "by_field": [
    {"obs_column": "organ", "cxg_field": "tissue", "ontology": "UBERON",
     "distribution": [{"value": "Retina", "n": 78, "share": 1.0, "curie": null}]},
    {"obs_column": "development_stage", "cxg_field": "development_stage", "ontology": "HsapDv",
     "distribution": [
       {"value": "unknown", "share": 0.808},
       {"value": "HsapDv:0000048", "share": 0.103, "curie": "HsapDv:0000048"},
       {"value": "HsapDv:0000054", "share": 0.09,  "curie": "HsapDv:0000054"}
     ]},
    {"obs_column": "study", "cxg_field": null, "ontology": null,
     "distribution": [{"value": "Sridhar_et_al_2020_CellPress", "n": 78, "share": 1.0}]}
  ]
}
```
- Pro: every distribution carries its source column + CxG mapping + ontology; the
  classifier output and the data live together; easy to query "stage breakdown".
- Con: a new local extension schema to define and validate.

### Variant B — minimal, nested under author_annotation_fields (CAS-legal today)

```jsonc
"author_annotation_fields": {
  "scope": "fetal", "granularity": "fine",
  "broad_celltype": "AUDIOVISUAL_NEURONAL",
  "_composition": {
    "organ": [{"value": "Retina", "share": 1.0}],
    "development_stage": [{"value": "unknown", "share": 0.808}, {"value": "HsapDv:0000048", "share": 0.103}]
  }
}
```
- Pro: zero schema extension; valid CAS now; ships immediately.
- Con: unstructured (string-keyed blob); loses the obs→CxG mapping unless
  duplicated; "share" semantics not validated; downstream must know the convention.

---

## 4. Contrasting cell — AUTONOMIC_NCCS_SCPS (expert-pooled across studies)

Shows transferred_annotations + multi-study composition working together.

```jsonc
{
  "labelset": "refined_celltype",
  "cell_label": "AUTONOMIC_NCCS_SCPS",
  "cell_fullname": "autonomic neural crest cell / Schwann cell precursor",
  "transferred_annotations": [
    {"transferred_cell_label": "NCC-SCP early autonomic", "source_taxonomy": "DOI:..Suo_2022..",     "comment": "expert-pooled"},
    {"transferred_cell_label": "Schwann cell precursors", "source_taxonomy": "DOI:..Kanemaru_2023..","comment": "expert-pooled"}
  ],
  "composition": {
    "n_cells": 15860,
    "by_field": [
      {"obs_column": "organ", "cxg_field": "tissue", "ontology": "UBERON",
       "distribution": [{"value": "whole_embryo", "share": 0.673}, {"value": "Gut ", "share": 0.075}, {"value": "Limb", "share": 0.05}]},
      {"obs_column": "study", "cxg_field": null,
       "distribution": [{"value": "whole_embryo", "share": 0.67}, {"value": "Suo_2022", "share": 0.08},
                        {"value": "Zhang", "share": 0.05}, {"value": "Kanemaru", "share": 0.05}, {"value": "Lawrence", "share": 0.05}]}
    ]
  }
}
```
Note `organ` value `"Gut "` has a trailing space — verbatim preservation matters;
mapping to UBERON happens on a separate `curie` slot, never by mutating `value`.

---

---

# v2 — incorporating DOS feedback (2026-06-24)

## Schema openness (verified against build/BICAN_schema.json)

- top-level: **open** · `Labelset`: **open** · `Annotation_transfer`: **open**
- **`Annotation`: CLOSED (`additionalProperties: false`)** · `Cell`, `Review`: closed

So composition can't be a free first-class field on an annotation under strict
CAS. We add it via a **local extension schema** (as CAP/BICAN do) that adds
`composition` to `Annotation`. Points 2 (transfer cell_count/ratio) and 5
(labelset hierarchy fields) need no fork — those objects are open.

## Point 1 — matrix_file_id = the actual data target

```jsonc
"matrix_file_id": "https://.../hdca_v2_20260311_f2.zarr"   // URL or filename of h5ad/zarr
```

## Point 5 — labelsets carry hierarchy + rank (rank 0 = most granular)

```jsonc
"labelsets": [
  {"name": "refined_celltype", "annotation_method": "manual", "rank": 0},
  {"name": "broad_celltype",   "annotation_method": "manual", "rank": 1}
]
```
Hierarchy itself is encoded per-annotation via `cell_set_accession` /
`parent_cell_set_accession`, and **verified programmatically** from the obs
cross-tab (refined × broad): every refined label's cells must fall ~entirely
(share ≈ 1.0) within one broad label, else flag. New check, sibling to
report_checker.

## Points 2–4 — one annotation, fully worked (AMACRINE_CELL)

```jsonc
{
  "labelset": "refined_celltype",
  "cell_label": "AMACRINE_CELL",
  "cell_fullname": "amacrine cell",
  "cell_ontology_term_id": "CL:0000561",
  "cell_set_accession": "HDCA:refined:AMACRINE_CELL",
  "parent_cell_set_accession": "HDCA:broad:AUDIOVISUAL_NEURONAL",   // point 5
  "rationale": "Retinal interneuron ... (Sridhar et al., 2020).",
  "rationale_dois": ["10.1016/j.celrep.2020.108023"],
  "marker_gene_evidence": ["TFAP2A", "GAD1"],

  // POINT 2: transfer reused for integration provenance, made explicit + counts
  "transferred_annotations": [
    {"transferred_cell_label": "AC", "source_taxonomy": "DOI:10.1016/j.celrep.2020.108023",
     "cell_count": 77, "cell_ratio": 0.987,              // <- added fields (object is open)
     "comment": "Integration provenance (not algorithmic transfer): author label from contributing study, cross-tabbed from obs."},
    {"transferred_cell_label": "imGlia", "source_taxonomy": "DOI:10.1016/j.celrep.2020.108023",
     "cell_count": 1, "cell_ratio": 0.013,
     "comment": "Integration provenance."}
  ],

  // POINT 4: ONLY genuinely unmapped obs columns — nothing already a labelset
  // (broad_celltype) or mapped to composition (organ/dev_stage/germlayer/systems)
  "author_annotation_fields": {
    "scope": "fetal"
  },

  // POINT 3: composition — TWO VARIANTS, pick one
  "composition": { /* §3-v2 */ }
}
```

## Point 3 — composition — DECIDED: Variant B (keyed objects with distributions)

### Variant A — CxG-flat (closest to CxG, one block per category)

```jsonc
"composition": {
  "tissue": "retina",
  "tissue_ontology_term_id": "UBERON:0000966",
  "author_tissue_field_name": "organ",
  "author_tissue_field_value": "Retina",
  "tissue_cell_count": 78,
  "tissue_cell_ratio": 1.0,

  "development_stage": "unknown",                 // dominant only
  "development_stage_ontology_term_id": null,
  "author_development_stage_field_name": "development_stage",
  "author_development_stage_field_value": "unknown",
  "development_stage_cell_count": 63,
  "development_stage_cell_ratio": 0.808
}
```
- Pro: field names == CxG (`tissue`, `tissue_ontology_term_id`); flat; familiar.
- **Con: only expresses the dominant value.** AMACRINE's minority HsapDv stages
  (0.103, 0.09) have nowhere to go — distributions don't fit a flat block
  without `_2`/`_3` suffixes or arrays, which breaks the CxG-flat look.

### Variant B — keyed objects holding distributions (cell-set-level form of CxG)

**Not a CxG deviation — a level shift.** CxG is a *cell-level* schema: one
`tissue_ontology_term_id` per cell. CAS annotations describe *cell sets*, so the
same field becomes a *distribution over the cells in the set*. The inner value
object mirrors CxG's per-field pair (`value` + `ontology_term_id`) exactly,
wrapped with `cell_count`/`cell_ratio`. A homogeneous set (share 1.0) collapses
to the CxG scalar, so cell-level CxG conformance is recoverable by projection.

```jsonc
"composition": {
  "tissue": {
    "author_field_name": "organ",
    "values": [
      {"author_value": "Retina", "value": "retina",
       "ontology_term_id": "UBERON:0000966", "cell_count": 78, "cell_ratio": 1.0}
    ]
  },
  "development_stage": {
    "author_field_name": "development_stage",
    "values": [
      {"author_value": "unknown",        "cell_count": 63, "cell_ratio": 0.808},
      {"author_value": "HsapDv:0000048", "ontology_term_id": "HsapDv:0000048", "cell_count": 8, "cell_ratio": 0.103},
      {"author_value": "HsapDv:0000054", "ontology_term_id": "HsapDv:0000054", "cell_count": 7, "cell_ratio": 0.09}
    ]
  },
  "germ_layer": {                          // no CxG slot -> open semantic key (point 4 escape hatch)
    "author_field_name": "germlayer",
    "values": [{"author_value": "ECTODERM", "cell_count": 78, "cell_ratio": 1.0}]
  }
}
```
- Full distributions; one consistent inner shape
  (`author_value`/`value`/`ontology_term_id`/`cell_count`/`cell_ratio`); CxG
  field *names* preserved as keys; open keys (`germ_layer`) for non-CxG descriptors.

**DECIDED: Variant B.** It is the cell-set-level analogue of CxG's cell-level
fields — not a compromise. Variant A discards everything but the mode, which is
only correct when the set is homogeneous; B degenerates to A automatically in
that case. A CxG-flat (cell-level) export is the dominant-value projection of B.

## Multi-valued sanity check — AUTONOMIC_NCCS_SCPS in Variant B

```jsonc
"composition": {
  "tissue": {"author_field_name": "organ", "values": [
    {"author_value": "whole_embryo", "cell_ratio": 0.673},
    {"author_value": "Gut ", "value": "intestine", "ontology_term_id": "UBERON:0000160", "cell_ratio": 0.075},  // verbatim "Gut " (trailing space) preserved
    {"author_value": "Limb", "ontology_term_id": "UBERON:0002101", "cell_ratio": 0.05}
  ]}
},
"transferred_annotations": [
  {"transferred_cell_label": "NCC-SCP early autonomic", "source_taxonomy": "DOI:..Suo_2022..",      "cell_ratio": 0.08, "comment": "Integration provenance; expert-pooled"},
  {"transferred_cell_label": "Schwann cell precursors", "source_taxonomy": "DOI:..Kanemaru_2023..", "cell_ratio": 0.05, "comment": "Integration provenance; expert-pooled"}
]
```

---

## Discussion points

1. **Composition slot: Variant A (typed extension) vs B (nested blob)?** A is the
   "proper" CAS extension; B ships today. (Leaning A — the obs→CxG mapping is the
   whole point of the classifier and shouldn't be lost.)
2. **`study` appears twice** — as `dataset_reference` → `transferred_annotations.source_taxonomy`
   AND as a composition distribution. Intentional (reference link + ratio), or
   collapse to one?
3. **Migrate `cell_type_annotations.schema.json` to CAS, or keep current shape +
   add a CAS exporter?** Downstream (report synthesizer, validators,
   report_checker) all read the current shape.
4. **`is X a labelset` vs `descriptor` confidence** — `broad_celltype` is both a
   coarser cell-type labelset (rank 1) AND used as a co-annotation. Can one obs
   column be both a labelset and a descriptor of finer labels? (CAS says yes via
   rank; our composition currently also lists it.)
5. **germ layer / systems** have no CxG slot but are real UBERON-ish descriptors.
   Open `semantic_category` handles them — confirm that's the escape hatch.
