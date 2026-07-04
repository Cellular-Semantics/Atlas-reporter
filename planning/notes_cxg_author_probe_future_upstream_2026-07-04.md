# Notes: future upstream work on cxg-author-probe

**Date:** 2026-07-04 · **Status:** speculative notes, NOT committed work.
Context: we import `cxg-author-probe` (Cellular-Semantics, DOS-owned). These are
ideas for pushing functionality UPSTREAM over time, and how the module's output
shape might evolve. Companion to
`plan_adopt_cxg_author_probe_PROVISIONAL_2026-07-04.md`.

---

## REPOSITIONING: CAS(+) schema goes upstream; this repo = map + report (DOS 2026-07-04b)

DOS: push the **CAS(+) / CAP+ schema and its assembly upstream too**, so
cxg-author-probe's job = "dataset → CAS(+) annotation collection" and
atlas-reporter focuses on **mapping and reporting on cell type annotations**.

**Clean split — CAS annotation fields divide into three passes:**
- **Structural (UPSTREAM, cxg-author-probe):** `labelset`, `cell_label`,
  `n_cells`, `cell_set_accession`, `parent_cell_set_accession`, `composition`
  (author values), `transferred_annotations` (labels), `author_annotation_fields`.
- **Map (atlas-reporter):** `cell_ontology_term_id`/`cell_ontology_term`,
  `composition[].ontology_term_id`, `transferred[].source_taxonomy`.
- **Report (atlas-reporter):** `cell_fullname`, `rationale`, `rationale_dois`,
  `marker_gene_evidence`, `synonyms`.

One CAS doc flows: module produces verbatim structure → atlas-reporter fills the
ontology slots (map) + evidence slots (report). "Map + report" literally = the
two enrichment passes.

**The CAP+ doc IS atlas-reporter's INPUT contract (DOS).** atlas-reporter no
longer *assembles* CAS — it *reads* a CAP+ collection produced by the module and
uses it as the input to its own steps (map, report). So `cas_annotation.schema.json`
flips role here: from "our output schema" to "the typed input we validate on the
way in." Every atlas-reporter step (resolve-name, ontology-term-lookup,
synthesize-report, ...) takes a CAP+ annotation (or the collection) as input and
returns an enriched CAP+ annotation. The workflow contract becomes: CAP+ in →
CAP+ (mapped + reported) out.

**REVERSES the earlier "composition stays downstream" call.** CAS is inherently
cell-set-level (a labelset groups cells), so once the module owns CAS it owns
cell-set structure INCLUDING composition cross-tabs (it already classifies
descriptors under Fork A and can `pull_full` them). atlas-reporter only MAPS
composition author values → CURIEs. (Supersedes the cell-level/cell-set-level
paragraphs below and in the trajectory section.)

**Migrates upstream:** `cas_annotation.schema.json` (as a `cas`/`cap+` output
schema — our landed schema + golden tests are the SEED SPEC, not wasted),
`annotations_writer` (intermediate→CAS assembly), composition cross-tabs,
labelset hierarchy/rank.

**Stays here (map + report):** `ontology-term-lookup`, `cl-term-request`,
`resolve-name`, `scan-supplements`, `citation-traverse`, `synthesize-report`,
`report_checker`, CL-mapping-into-header, the literature/ontology service stack.

**Open boundary Q:** subatlas DOI resolution (`subatlas_resolver`: study label →
DOI → `transferred[].source_taxonomy`) — mapping (stay) vs CAS production (up)?
Lean STAY (it's reference mapping, same family as CL lookup).

---

## Format flexibility: reader selection + agentic fallback (DOS 2026-07-04)

Requirement: the workflow must work for atlases **generally / any format**.
Pre-written readers are the fast path when they match; the system must be able
to **improvise** a reader for a format it has never seen — WITHOUT losing
modularity. Reconciliation = the **`ObsHandle` Protocol is the contract**:
improvisation is "implement these 7 methods for this container," not "write
arbitrary file-reading code."

Reader layer (in cxg-author-probe) becomes:

```
url/file → detect format
  ├─ registered reader matches (h5ad, zarr, tiledb)  → pre-written fast path  [deterministic]
  └─ no match → agent inspects container structure    → writes ObsHandle impl  [agentic]
                → VERIFY vs contract + invariants → use + cache
                → CAPTURE code → candidate to PROMOTE to a permanent reader
```

- **Verification gate (mandatory).** An improvised reader is trusted only if it
  passes contract invariants: every column length == `n_cells`; `head_sample`
  decodes to sane primitives (not raw bytes); `pull_full` length == `n_cells`;
  `describe` kinds are coherent. Fail → reject/retry. Turns fuzzy improvisation
  into a testable step.
- **Capture-and-promote loop.** Every improvised reader is saved as code so runs
  are reproducible AND today's improvisation becomes tomorrow's pre-written
  reader (→ PR to the module). Prevents re-improvising the same format forever.
- **Sandbox** improvised readers: obs-only, no stray network beyond the store.
- **Enabling first step: entry-point reader discovery** in cxg-author-probe —
  small, and it (a) fixes "the CLI/plugin can't see externally-registered
  readers" (our zarr reader is in-process only today) and (b) is the hook that
  improvised/contributed readers plug into. Promote our just-built zarr reader
  upstream as the first pre-written contribution.

**Keep two judgements separate:** reader/format selection (improvise here) vs
field classification (Fork A — runs on `probe-v1`, already format-agnostic). Our
CAS / composition / report layer is downstream of the probe and unaffected by
how the probe was produced.

**General pattern worth reusing:** known-fast-path → agentic-fallback →
capture-as-new-fast-path. Flexibility at the edges, stable typed contract in the
middle — the same modularity thesis, applied to the unknown-format edge.

---

## The trajectory

The module's output today is deliberately **narrow**:
`picks-v1` = "which obs columns are author cell-type fields." As we push more
judgment upstream (Fork A and beyond), its natural output shape drifts toward
**CAS** (labelsets + annotations). Rough arc:

1. **Now** — `picks-v1` (cell-type column names only).
2. **Fork A** — full field classification: every obs column →
   `{cell_type | tissue | development_stage | assay | disease | sex |
   self_reported_ethnicity | organism | cluster | id | none}` + ontology target.
   `picks-v1` → a richer `classification-v1`.
3. **+ hierarchy** — detect labelset **hierarchy/rank** (fine cell-type column
   subsumed by a coarser one) from the cross-tab of the two columns. The module
   already identifies the cell-type columns and pulls columns, so it has what it
   needs. This is currently in OUR plan (`validation/hierarchy_checker.py`,
   step 3) but is field-relationship judgment → a candidate to move upstream.
4. **Eventually** — module emits a **CAS-shaped output** (CAP/BICAN extension
   flavour) directly: `labelsets[]` (name, rank, role) + `annotations[]`
   skeletons, instead of the flat picks/pulled wire format. At that point our
   downstream shrinks to composition + evidence enrichment only.

## Candidate features to push upstream (in likely order)

- **Full obs field classification → CxG** (Fork A). Generalises the picker.
- **Integration / transferred detection** — "is this column a source-dataset
  reference or an inherited author label?" Field-identification judgment, so it
  fits upstream; the CAS `transferred_annotations` *wiring* stays downstream.
- **Labelset hierarchy / rank finding** — cross-tab-based subsumption between
  cell-type columns.
- **CAS-shaped output option** — a `--format cas` (or a `cas-v1` schema) that
  emits labelsets + annotation skeletons, converging the module's wire format
  on CAS/CAP+.

## The trade-off to weigh before doing this

- **Wire-format minimalism (current)** — probe/picks/pulled are tiny, stable,
  and keep the cluster (pure) vs LLM (pick) split crisp. Easy to validate, easy
  to defer the LLM step to another machine.
- **CAS-shaped output (future)** — richer, less for downstream to assemble, but
  it pulls *structure* upstream and risks blurring the clean per-stage split.
  Only worth it once the module reliably does full classification + hierarchy.

**Keep the cell-level / cell-set-level boundary honest.** Even if structure
moves upstream, **composition cross-tabs are cell-set-level aggregation and
should stay downstream** in atlas-reporter (the module is cell-level:
probe/pull/augment all operate per observation). Pushing *classification* and
*hierarchy* up is natural; pushing *aggregation* up is not.

## Alignment contract to preserve throughout

One shared **CxG-field vocabulary** (tissue→UBERON, development_stage→HsapDv,
assay→EFO, disease→MONDO, sex→PATO, self_reported_ethnicity→HANCESTRO,
organism→NCBITaxon, cell_type→CL). The module's classification output categories
and our CAS `composition` keys + ontology targets MUST reference the same list.
If the module later emits CAS-shaped output, align its labelset/annotation field
names with our local CAS extension (`cas_annotation.schema.json`).

## What stays in atlas-reporter regardless

- Composition cross-tabs (cell-set-level aggregation of pulled columns).
- CAS assembly into our local extension + the `annotations_writer` transform.
- Biological / evidence enrichment: `cell_ontology_term_id`, `cell_fullname`,
  `rationale`/`rationale_dois`, `marker_gene_evidence` — the report workflow.
