# Annotation-provenance workflow improvements — draft plan

Status: draft, not implemented. Authored 2026-05-31 after a HDCA_neurons run
where 10 of 11 retinal cell types failed to surface their actual annotation
source (Sridhar et al., 2020) in `paper_catalogue.json`, and the orchestrator
fell back to a hand-authored `provenance_evidence.md` to compensate.

## Problem statement

Cell-type provenance has two axes that the current pipeline collapses into one:

1. **Cells-from-X** — the raw expression matrices behind the integrated label
   were inherited from study X. Mechanically derivable from
   `obs.study × obs.refined_celltype` cross-tabs (this is what
   `label_provenance.json` encodes today).
2. **Annotations-from-X** — the cell-type *label and its biological definition*
   were inherited from study X. This is a textual claim about the taxonomy:
   the atlas may keep, rename, re-cluster, or expert-merge upstream labels.
   Currently inferred only by humans reading `label_provenance.json` plus
   atlas Methods text (e.g. `provenance_evidence.md` in HDCA_neurons).

The two axes can come apart in every combination. Examples from HDCA v2:

| Cells | Annotations | Example | Citation implication |
|---|---|---|---|
| Subatlas | Subatlas (preserved) | retinal labels (AMACRINE_CELL, BIPOLARS …) | Cite subatlas as the *definitional* source |
| Subatlas | HDCA-relabelled | PNS/NCC expert-pooled labels | Cite HDCA for the label; subatlases only as cell-origin |
| HDCA (de novo) | External literature | DL1–DL6, pA1–pA4 (spinal-cord taxonomy) | Cite developmental-biology reviews for nomenclature |
| HDCA | HDCA | RETINAL_NEURAL_PROGENITOR | Cite HDCA only |

The pipeline currently encodes axis 1. Axis 2 leaks into out-of-band notes.

## Observed pipeline gaps

1. **Subatlases are registered but not seeded.** `source.subatlas_papers` lists
   Sridhar 2020 with `status: "asta"`, but the citation traverser builds
   `seed_ids = [atlas_doi]` only ([report_graph.py:275-287](../src/atlas_chat/atlas_chat/graphs/report_graph.py#L275-L287)).
   ASTA fan-out from the atlas paper *may* pull a subatlas in for a given
   cell-type query (it did for AMACRINE_CELL); it has no obligation to. For
   the other 10 retinal labels Sridhar never entered the catalogue, so any
   report citing her DOI would fail validation.

2. **Snippet-only retrieval misses annotation-provenance evidence.** The
   textual claims that decide axis 2 — "we retained Sridhar's labels", "we
   re-clustered and renamed", "DL = dorsal late, after Helms & Johnson" —
   typically live in Methods, Supplementary Notes, or figure legends. These
   chunks are often deranked by cell-type-biology queries. Nomenclature
   equivalence ("AC" ≡ "AMACRINE_CELL") is not what semantic similarity
   ranks for. Negative-evidence claims ("Braun Table S2 has no DL/pA labels")
   are unreachable via top-k retrieval at all.

3. **`provenance_evidence.md` is a non-standard, per-project, one-off note.**
   It is not produced by any pipeline stage and is not consumed by the
   orchestrator's published contract. Depending on it makes the workflow
   non-reproducible across projects.

## Proposed improvements

### Improvement A — seed-paper injection from `label_provenance.json`

For each cell type, before traversal:

1. Read `label_provenance.json[cell_type].studies` and take the top-N
   contributing studies by share (e.g. N=3, share ≥ 0.05).
2. Map each study to a DOI via `source.subatlas_papers[].label`.
3. Inject those DOIs into `citation_traverser.traverse(seed_ids=[atlas_doi, *subatlas_dois])`.

Effect: any subatlas that contributes meaningful cells to a label is
guaranteed to enter `paper_catalogue.json` for that cell type, regardless of
ASTA fan-out luck. Cheap; preserves the existing ASTA contract.

Open question: should subatlas DOIs also expand the query scope (separate
ASTA query per seed, results merged)? Probably yes for the dominant
contributor (≥ 0.5 share) only — otherwise costs scale poorly for pooled
labels.

### Improvement B — atlas-level annotation-provenance pass

Run once per atlas (not per cell type), output a structured
`annotation_sources.json` consumed by the synthesizer.

**Inputs**
- Atlas paper full text (already locally indexed as JATS or PDF).
- `label_provenance.json` — gives the candidate subatlas list per cell type.
- For each candidate subatlas with cells-share ≥ threshold: a fetched
  copy of the subatlas's Methods / Results / figure-label sections (full
  text via local index if available, otherwise targeted snippet search
  scoped to that paper).

**Procedure** (one LLM call per atlas, or one per atlas+subatlas pair)
1. Extract the atlas's Methods passages that describe how author
   annotations were treated. Standard cues: "retained the original
   annotations", "re-clustered", "expert-curated", "harmonised", "renamed".
2. For each subatlas with a substantial cells-share, compare the atlas's
   refined_celltype names against the subatlas's published cluster names
   (which the subatlas paper lists in its own Results / figures).
3. Classify each (cell_type, subatlas) pair as:
   - `inherited` — name and definition preserved from subatlas;
   - `relabelled` — same cells, atlas-specific new name;
   - `merged` — cells from multiple subatlases pooled under a new label;
   - `de_novo` — cells/labels created by the atlas with no upstream parent;
   - `external_taxonomy` — label borrowed from non-atlas literature (cite
     external reviews instead of a subatlas).
4. Capture the evidence quote and source location for each classification.

**Output** (`projects/{project}/annotation_sources.json`)

```json
{
  "atlas_doi": "10.64898/2026.03.30.714220",
  "generated_at": "2026-05-31T...",
  "cell_types": {
    "AMACRINE_CELL": {
      "classification": "inherited",
      "primary_source_doi": "10.1016/j.celrep.2020.01.007",
      "primary_source_label": "Sridhar et al. 2020",
      "subatlas_label_in_source": "AC",
      "evidence": "...exact atlas-paper quote describing label inheritance...",
      "evidence_source": "atlas Methods §X"
    },
    "DL1_NEURON": {
      "classification": "external_taxonomy",
      "primary_source_doi": null,
      "primary_source_label": "Helms & Johnson 2003; Lai et al. 2016; Sagner & Briscoe 2019",
      "evidence": "...",
      "evidence_source": "atlas Methods + classical literature"
    }
  }
}
```

The synthesizer reads this file as a first-class input alongside
`name_resolution.json`. The Summary template gets an explicit `Annotation
provenance:` line that consumes the classification + evidence.

### Improvement C — fail fast on missing primary source

If `annotation_sources.json` says a cell type's primary source is X but
`paper_catalogue.json` for that cell type does not contain X's DOI, raise a
validation error during synthesis rather than silently producing a report
that omits the most important citation. This is the missing exit condition.

### Improvement D — encourage full atlas-paper read for ambiguous cases

When `annotation_sources.json` classifies a cell type as `inherited` or
`relabelled`, also load the relevant Methods/Supp full-text chunks into the
synthesizer's context (not just snippets). The current snippet-only mode is
fine for the biology sections; provenance reasoning benefits from full
passages.

## Critiques / open questions of my own

- **Threshold sensitivity.** "Cells-share ≥ X" is arbitrary. For pooled
  labels (e.g. AUTONOMIC_NCCS_SCPS at 67% whole_embryo + several minor
  contributors), no single subatlas is the annotation source and every
  rule-based threshold will misclassify some cases. The annotation pass
  needs to allow a `merged` classification with a list of co-equal sources.
- **Atlas Methods text isn't always explicit.** Many atlases describe label
  inheritance in vague language ("we integrated published annotations")
  without saying which labels came from where. The pass should mark
  low-confidence calls and surface them for human review rather than
  guessing.
- **One-pass per atlas vs per cell-type-batch.** Running a single LLM call
  over the full atlas Methods is cheaper but loses cell-type-specific
  detail. Running per cell type duplicates work. Probably best: one pass
  to extract the policy ("how does this atlas handle author annotations?"),
  then per-cell-type lookups against the policy + the cell type's
  contributing-study list.
- **Subatlas full-text access cost.** Some subatlases will be paywalled
  with no PDF dropped in. The pass should degrade gracefully — if a
  subatlas's text is unreachable, classification falls back to "inferred
  from cells-share alone" with an explicit confidence marker.
- **Don't bake `provenance_evidence.md` into the contract.** The file is
  useful as scratch but should not be a pipeline input. Once Improvements
  A–C ship, it should be deletable without breaking any cell-type report.
- **Re-running on new subatlas additions.** If a user drops a new PDF into
  `_pdfs/`, the local index rebuild should be sufficient to re-run
  Improvement B incrementally for just the cell types whose primary
  source changed. Worth designing the output to be diffable.

## Evidence from a worked example (HDCA_neurons retinal labels)

Reading the atlas paper full text (`2026.03.30.714220v2.full.pdf`) directly,
the annotation-provenance claim for retinal labels is textually grounded —
not just an inference from cells-share. Two passages in particular are
exactly the kind of evidence Improvement B should be extracting
automatically:

1. **Atlas-wide policy** (page 33, lines 887–895): *"The annotations for the
   community datasets were informed by the original author-provided labels
   and subsequently harmonised across studies. In contrast, the WE dataset
   lacked pre-existing cell type annotations and extensively manually
   curated through literature informed gene markers and expert input."*
2. **System-specific mechanism for audiovisual / retina** (pages 49–50,
   lines 1347–1355, 1376–1383): cluster-centric kNN harmonisation with k=10
   from community data; *"Clusters that were largely dominated by cells
   from community data, the whole embryo cells of those clusters were
   assigned the kNN-classifier predicted cell types"*; *"previously
   published annotations were retained where they were unambiguous and
   provided higher-resolution labels than those obtained from unbiased
   clustering."*

These two quotes alone classify all retinal-system labels as `inherited`
from the dominant community contributor, except `RETINAL_NEURAL_PROGENITOR`
which is 100% whole-embryo (and therefore `de_novo`). Sridhar 2020's own
Figures 2–3 supply the matching cluster vocabulary
(`Progenitors / T1 / T2 / T3 / RGC / Amacrine / HC / PR / Bipolar /
imGlia / Glia`) and the marker definitions for T1 (ATOH7/HES6/DLL1), T2
(PRDM13), and T3 (FABP7/DLL3) that any retinal report would need to cite.

A modest LLM pass against the atlas Methods chunked at section level would
have surfaced both quotes reliably. Snippet search for the cell-type-biology
query "AMACRINE_CELL location structure function markers" does not.

## Pipeline bugs / gaps surfaced while debugging the HDCA_neurons run

These are independent of the annotation-provenance plan above but were
exposed by the same retinal-report failure and should be tracked:

1. **Agentic `citation-traverse` subagent ignores the local snippet index.**
   The merge of ASTA + local snippets only happens inside the programmatic
   graph ([report_graph.py:296-329](../src/atlas_chat/atlas_chat/graphs/report_graph.py#L296-L329)).
   The subagent doc ([.claude/agents/citation-traverse.md](../.claude/agents/citation-traverse.md))
   describes an ASTA-only flow. As a result, a project that has gone to the
   trouble of building a local index (e.g. for a paywalled subatlas with a
   PDF dropped in `_pdfs/`) gets no benefit from it on the agentic route.
   The two runtimes are not behaviourally equivalent, which contradicts
   the design intent stated in `AGENT.md` / `CLAUDE_dev.md`.

   *Fix*: extend the citation-traverse subagent to (a) call
   `local_snippet_index.search` (or a thin MCP wrapper around it) in
   parallel with ASTA when `corpus.json.use_in_fanout` is true, and (b)
   merge the snippets into `all_summaries.json` and the per-paper
   metadata into `paper_catalogue.json` with the same shape the graph
   uses.

2. **`traverse_local` only catalogues the top-ranked paper.**
   [citation_traverser.py:210-221](../src/atlas_chat/atlas_chat/services/citation_traverser.py#L210-L221)
   reads `raw_snippets[0]` and constructs a one-entry catalogue from it.
   If multiple local papers contribute snippets (which is the whole point
   of the multi-paper local corpus), only one of them — whichever ranked
   first for that query — enters `paper_catalogue.json`. Any quote
   sourced from a lower-ranked paper would then fail DOI validation in
   the report.

   *Fix*: iterate over all distinct papers represented in `raw_snippets`
   and emit one catalogue entry per paper, keyed by each paper's
   `corpus_id`.

3. **The `local_<hash>` corpus IDs don't round-trip through S2 backfill.**
   `_backfill_catalogue` ([report_graph.py:459-512](../src/atlas_chat/atlas_chat/graphs/report_graph.py#L459-L512))
   fetches metadata for corpus IDs in evidence that aren't already in the
   catalogue. Local-index papers carry synthetic IDs of the form
   `CorpusId:local_<hash>` which S2 cannot resolve, so any local paper
   missing from the catalogue (e.g. because of bug 2) cannot be backfilled.
   This makes bug 2 worse, not just inconvenient.

   *Fix*: skip the S2 lookup for `local_*` IDs and instead read metadata
   from the corresponding `local_index/papers/<slug>/manifest.json`.

4. **The orchestrator currently has no atlas-paper full-text channel.**
   Improvements B and D in the section above depend on reading the atlas
   Methods section directly. The local index already chunks the atlas
   paper, but the synthesize-report subagent only sees
   `all_summaries.json` (top-k snippets) — not the underlying chunks.
   Reading a *section* (e.g. all chunks tagged `section: Methods`) needs
   a small helper that doesn't exist yet.

   *Fix*: expose a `local_snippet_index.read_section(project, doi,
   section_name)` API that returns concatenated chunks for a named
   section. Wire it into the orchestrator for the annotation-provenance
   pass (Improvement B).

## Phasing

1. Improvement A (seed injection) is small, low-risk, and unblocks the
   immediate retinal-report problem. Ship first.
2. Improvement B (annotation_sources.json pass) is the substantive change.
   Ship behind a flag; start with HDCA_neurons as the development project.
3. Improvement C (validation) only makes sense once B exists.
4. Improvement D (full-text loading for provenance sections) is a synthesizer
   prompt change — small, do alongside C.
