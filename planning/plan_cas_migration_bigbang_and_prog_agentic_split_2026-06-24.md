# Plan: big-bang CAS migration + clean programmatic/agentic split + anti-brittleness testing

**Date:** 2026-06-24
**Status:** plan for review — not started
**Depends on:** `plan_obs_field_classifier_and_cas_alignment_2026-06-24.md`,
`mockup_cas_cxg_annotations_2026-06-24.md` (composition = Variant B, decided).

DOS framing: do this as a **big bang** (these workflows resist modular
migration); **testing is mandatory** to stop brittleness; and we need a **clean
programmatic vs agentic division — agentic only where judgment is needed.**

**Decisions locked (2026-07-02):** local CAS extension (not BICAN wholesale);
orchestrator sequences describe → classify → write (skill does not call the
agent internally); per-agent input schemas remain for now.

---

## 0. Motivating case (state it before building — avoids fitting to HDCA)

We skipped this and it matters. Driving use case:

> A curator points at a **published dataset they did not create** (any source,
> any obs convention) and gets a **CAS-conformant annotation set** —
> labelsets + per-cell-set composition + integration provenance + CL mappings —
> ready to drive the existing evidence-grounded report workflow.

The hard part is *not knowing the obs conventions in advance*: column names,
value encodings, which column is the author's cell type, whether it's
integrated, what's a descriptor. That uncertainty is precisely why
`classify-obs-fields` is agentic — and precisely why over-fitting to the two
atlases we happen to have is the central risk (see §6).

## 0b. Scope split — loaders are a SEPARATE effort

This plan (Effort 1) owns: the CAS output shape, `classify-obs-fields`, the
P/A boundary refactor, and testing. **Input is the existing zarr path only.**

**Effort 2 (separate plan): multi-source loaders** — h5ad, CELLxGENE, CAP,
spreadsheet (the `DataProvenance.source_type` enum already anticipates these).
The seam between the efforts is a **source-agnostic column profile**
(`{name, n_categories, sample_values}`) plus the existing intermediate dict
(annotations_writer docstring). Any loader that can emit that profile plugs into
`classify-obs-fields` and the CAS writer unchanged. Keeping loaders out of the
big bang shrinks its blast radius and forces the classifier to be source-agnostic
by construction. **Do Effort 2 after Effort 1 stabilises** (DOS: implement
separately).

---

## 1. The boundary principle (the core of this plan)

> **A step is agentic only if a competent human curator, given the same
> inputs, would have to exercise interpretive judgment that cannot be reduced
> to a deterministic rule or lookup.** Everything else is programmatic:
> fetching, sequencing API calls, cross-tabulation, ratio/share computation,
> schema validation, substring/DOI checks, hierarchy verification, file
> writing, format conversion, PURL formatting.

**Contract that makes the boundary enforceable and testable:**

- An agent **emits one small typed judgment object**, validated against a JSON
  Schema at the tool boundary (existing `StructuredOutput` + PostToolUse hook
  pattern).
- An agent **never** computes numbers, fetches data, writes files, or decides
  schema conformance. Programmatic code gathers the agent's inputs, consumes its
  judgment, computes all derived data, and writes/validates outputs.
- Therefore: **programmatic units are unit/golden-testable; agentic units are
  pinned by output-schema + recorded-fixture contract tests.** Brittleness lives
  at the boundary, so we test the boundary hardest.

### Current anti-pattern this fixes

Today several subagents **mix** the two: e.g. `resolve-name` /
`scan-supplements` / `citation-traverse` each do their own MCP searching AND
their judgment in one unit. That couples deterministic I/O (testable) to LLM
judgment (not), and is a prime brittleness source. The refactor pulls the
deterministic half into `services/` and leaves the subagent a **thin judgment
layer over pre-fetched evidence**.

---

## 2. Step-by-step division (target state)

| Workflow step | Side | The isolated judgment (if agentic) | Programmatic component |
|---|---|---|---|
| Pull `obs/` from zarr | **P** | — | `anndata-zarr-summary/run.py` |
| `--describe-columns` (name + first-20 values) | **P** | — | run.py (new mode) |
| **Classify obs fields** (role + CxG mapping) | **A** | "is this field a cell-type labelset / transfer / descriptor; which CxG field" | feeds writer |
| Compute composition cross-tabs + ratios | **P** | — | run.py / writer |
| Labelset hierarchy subsumption check | **P** | — | new `validation/hierarchy_checker.py` |
| Build + validate CAS docs | **P** | — | `annotations_writer` (rewritten) |
| Fetch supplementary material (MCP sequence) | **P** | — | `services/europepmc.py`, `atlas_paper.py` |
| Resolve cell-type name | **A** | "which author name maps to this label" | search done in service; agent judges over results |
| Scan supplements for markers/findings | **A** | "what counts as a marker / finding here" | text pre-fetched by service |
| Citation traverse | **Hybrid** | "is this snippet relevant; one-line summary" | traversal/fetch in `citation_traverser.py` |
| Synthesize report | **A** | narrative writing grounded in evidence | inputs assembled programmatically |
| Validate report (quotes/DOIs) | **P** | — | `report_checker.py` |
| Correction loop | **P** control flow | (re-runs synthesize) | orchestrator/graph |
| Map to CL | **Hybrid** | "exact/broad/narrow match quality" | OLS search in service |
| Insert CL line into header | **P** | — | small writer util |
| Draft CL term request | **A** | definition/axiom drafting | template/format programmatic |
| Resolve subatlas papers | **Hybrid** | "which S2 candidate matches this study label" | S2 search in `subatlas_resolver.py` |
| Post NTR to GitHub | **P** (+human gate) | — | `gh` call |

**Net new agentic unit:** `classify-obs-fields` (one judgment object).
**Net new programmatic units:** `describe-columns` mode, composition computer,
`hierarchy_checker`, CAS writer rewrite, CAS local extension schema.
**Refactors:** thin out `resolve-name`/`scan-supplements`/`citation-traverse`/
`ontology-term-lookup`/`subatlas_resolver` so search/fetch is in services and
the subagent only judges.

---

## 3. Target schema (big-bang replacement of `cell_type_annotation.schema.json`)

A **local CAS extension** (general + BICAN base, plus our additions):

- adds `composition` to `Annotation` (CAS `Annotation` is closed —
  `additionalProperties:false` — so this is a deliberate fork, the CAP/BICAN
  pattern); shape = Variant B keyed-by-CxG-category distributions.
- adds `cell_count` / `cell_ratio` to `Annotation_transfer` (object is open).
- labelsets carry `rank`; annotations carry `cell_set_accession` /
  `parent_cell_set_accession`.
- `matrix_file_id` = zarr/h5ad URL or filename.
- `author_annotation_fields` = unmapped obs only.

Composition = the **cell-set-level** form of CxG's **cell-level** fields (a
homogeneous set collapses to the CxG scalar — not a deviation). Verbatim author
values preserved; ontology CURIEs additive.

Schema-first commandment holds: this JSON Schema is the single source of truth;
Pydantic generated from it; one validation entry point.

---

## 4. Big-bang sequencing (a big bang still needs an internal order)

All landed behind tests before any single merge to `main`; order = dependency order.

1. **Schema + fixtures.** Write the CAS-extension schema. Author good/bad golden
   fixtures (HDCA integrated + fetal_skin non-integrated). Schema regression
   tests green. *(no behaviour yet)*
2. **Writer rewrite.** `annotations_writer`: intermediate → CAS docs (labelsets,
   annotations, composition, transferred_annotations, hierarchy slots). Unit +
   golden tests green.
3. **Programmatic derivations.** Composition cross-tab/ratio computer;
   `hierarchy_checker`; `--describe-columns`. Unit tests + a describe-columns
   snapshot test.
4. **classify-obs-fields agent.** Subagent + input/output schemas + PostToolUse
   validator hook + recorded-fixture contract tests.
5. **Thin the existing subagents.** Move search/fetch into services; subagents
   become judgment-only. Contract tests per agent.
6. **Migrate downstream readers.** report_synthesizer prompt, `report_checker`,
   CL header insertion, `CLAUDE.md` workflow text — all read the CAS shape.
7. **Delete deprecated `graphs/`** and the old bespoke shape; update every
   fixture/validator in the same commit.
8. **Full integration run** on both golden projects; compare to frozen expected.

No compatibility shim (big bang): correctness is gated by the golden-project
diff, not by dual-shape support.

---

## 5. Testing strategy (the anti-brittleness backbone)

Layered, mirroring the boundary:

**(a) Schema regression** — good/bad golden fixtures per output schema; assert
accept/reject + cross-field rules (extend the existing
`test_cl_mapping_schema.py` pattern to the CAS schema, composition rules,
hierarchy invariants).

**(b) Programmatic golden tests** — deterministic in→out for the writer,
composition computer, hierarchy_checker, report_checker, describe-columns. These
are the bulk of CI and the main brittleness defence.

**(c) Agent contract tests (new — the current gap)** — for every subagent:
record a real LLM output as a fixture; assert it validates against the output
schema AND satisfies invariants (e.g. classify-obs-fields tags ≥1 author_labelset
or explicitly flags ambiguity; never tags `leiden` as author). Pins agent
behaviour without a live call in CI.

**(d) Golden-project regression** — freeze expected CAS output for
`HDCA_neurons` (integrated) and `fetal_skin_atlas` (non-integrated); diff on
every change. The non-integrated project guards against HDCA over-fit (no
`transferred_annotations` should appear).

**(e) Integration tests** — real MCP/LLM, fail-hard on missing creds (per
CLAUDE_dev), run locally; end-to-end on both golden projects.

**(f) Over-fit defence (dedicated — the classifier's main risk)** — because
`classify-obs-fields` must generalize to unseen obs conventions:

- **Diverse external corpus, some held out.** Assemble 4–6 published atlases
  with *deliberately different* conventions: a mouse atlas (MmusDv, different
  organs), a CxG-standardized set (values already `*_ontology_term_id`), an
  adult/disease atlas (MONDO, no developmental stage), a Seurat-origin set
  (`seurat_clusters`/`leiden` only, no author annotation), and a
  spreadsheet/CAP source. **Develop against a subset; evaluate blind on the
  rest.** Only fetal_skin + HDCA as goldens = insufficient.
- **Prompt hygiene, tested.** The classifier prompt reasons from *generic
  morphology* (name form + value form), and MUST NOT enumerate HDCA-specific
  column names. Enforce with a **perturbation test**: rename
  `refined_celltype`→arbitrary, shuffle columns, swap value casing — role
  assignments must be stable. If they aren't, the prompt has memorised.
- **Adversarial synthetic profiles.** Hand-built obs profiles designed to fool
  it: a column literally named `cell_type` whose values are integer cluster IDs;
  a descriptor column named like a cell type; an integrated atlas whose study
  column is named `donor_dataset` not `study`. Assert correct roles.

CI = (a)+(b)+(c)+(d) unit-marked; integration + (f) blind-eval local. Ratchet
`fail_under` upward; update fixtures in the same commit as any contract/validator
change.

---

## 6. Risks

- **Downstream ripple** (report synthesizer/report_checker read inline
  covariates → now `composition`). Mitigated by golden-project diff gating, not
  by a shim.
- **Agent output drift** → schema + recorded fixtures (layer c).
- **Over-fit to our two atlases (SERIOUS — DOS-flagged twice).** Both current
  projects are in-house developmental human atlases; fitting the classifier or
  fixtures to them is the central threat. Mitigation is its own layer — see §5(f).
  fetal_skin alone is NOT sufficient (same lab/ecosystem as HDCA).
- **Hidden coupling in deprecated graph** → it's reference-only; deletion in
  step 7 must not be imported by live code (grep-gate before delete).

---

## 7. Decisions

**Resolved (2026-07-02):**
1. ✅ **CAS base:** local extension of the *general* schema (not BICAN wholesale).
2. ✅ **Data-load orchestration:** orchestrator sequences describe → classify →
   write; the skill does NOT call the agent internally (keeps the P/A boundary
   visible, each unit single-purpose).
3. ✅ **Per-agent input schemas:** keep the current granular set for now.
4. ✅ **Loaders (h5ad/CxG/CAP/spreadsheet):** separate effort (Effort 2, §0b),
   after Effort 1 stabilises.

**Still open:**
5. **`cell_set_accession` scheme** — namespacing (`HDCA:refined:LABEL`?) and
   stability across re-runs.
6. **Scope of the bang** — include deprecated `graphs/` removal (recommend yes),
   or separate follow-up?
7. **Over-fit corpus** — which 4–6 external atlases (§5f), and which are held
   out for blind eval.
