---
name: subatlas-consistency
description: Judge whether an atlas cell-type label agrees with what the contributing studies called the same cells, explain any disagreement from markers, and decide which paper defines the cell type (and so where evidence retrieval should start).
model: sonnet
input:
  schema: src/atlas_chat/atlas_chat/schemas/subatlas_consistency_input.schema.json
output:
  schema: src/atlas_chat/atlas_chat/schemas/subatlas_consistency.schema.json
---

# Subagent: Subatlas Consistency

An integrated atlas's cell sets are usually built from cells that other studies
already annotated. Those studies' labels are recorded in CAS+
`transferred_annotations`, and `subatlas_contributors.json` has already reduced them
to the papers that contributed enough cells to be worth reading.

Your job is the judgement the counts cannot make: **does the atlas's label mean the
same thing the contributing paper's label meant?** And where it doesn't, **why** —
preferably from markers.

You also make one call the rest of the workflow depends on: **which paper actually
defines this cell type**. Where a label was inherited essentially unchanged from one
study, that study is where the biology was characterised, and traversal should start
there. Getting this wrong is measurable — inherited annotations have historically
drawn less than half the evidence per report of the atlas's own, because traversal
always seeded on the atlas paper.

## Input

Per `subatlas_consistency_input.schema.json`. The paths are given to you; do not
derive them from a project name.

## Procedure

### 1. Fix what the atlas means, before reading any contributor

Read the CAS+ annotation (`cas_path`) for this `cell_label`: its `cell_fullname`,
`synonyms`, `marker_gene_evidence`, `composition` (stage / tissue / assay), and its
place in the hierarchy (`parent_cell_set_accession`, and the labelset's `rank` — a
rank-0 label is a fine subtype and should be *expected* to be narrower than a coarse
upstream call). If `name_resolution_path` is given, fold in its `resolved_names`.

Write that up as `working_definition` **first**. Judging one contributor at a time
without a fixed reading drifts toward whichever upstream definition you read last.

Note the atlas's `synonyms` particularly. If a synonym is identical to one of the
upstream labels, that is a strong signal about where the name came from — and it may
not be the *dominant* upstream label. On the reference cell set the atlas's synonym
`aPCV` is its contributor's 11% minority call, not its 59% majority one.

### 2. For each contributor over the cutoff

Work through `contributors` in `subatlas_contributors.json` in order. Every one gets
a verdict — including the awkward ones. A contributor listed there and missing from
your output is an omission, and the hook will say so.

Read its numbers before deciding what to retrieve:

- `contribution` — how much of the atlas cell set came from this paper.
- `purity` — of the cells it contributed, the fraction under its dominant label.
  **High purity is not the same as agreement.** A paper that called all its cells
  "endothelial cell" is pure and uninformative; that's a broad match, not an exact
  one.
- `within_source_share` per label — how this paper split its contribution. This is
  where a disagreement becomes visible.
- `reverse_share` — of everything the upstream paper gave that label anywhere in the
  atlas, the fraction that landed in this cell set. **A high `within_source_share`
  with a low `reverse_share` means the atlas split that upstream cell type across
  several of its own cell sets** — set `split_upstream_type`. That is a genuine
  re-partition, not a rename, and the counts inside this one cell set cannot show it.
- `tier` — `primary` warrants retrieving the paper's text. `secondary` is named,
  counted and judged from what you already know; do not spend retrieval on it unless
  the atlas synonym points at it or its purity is low enough to matter.
- `status` / `asta_band` — whether the text is reachable at all, before you try.

**Choose which upstream label to compare.** Usually `dominant_label`. But if the
atlas label or one of its synonyms corresponds to a different listed label, compare
against *that* and say so in `compared_label`. Comparing against the majority call
when the atlas plainly adopted a minority one gets the relationship backwards.

**Retrieve the contributing paper's own account of that label.** Scoped to that
paper only:

```bash
# Papers with a local index (status: local) — JATS or PDF
python -m atlas_chat.cli_annotate fetch \
  --query "<upstream label>: definition, markers, cluster identity" \
  --local --project-dir <project_dir> --papers <contributor DOI> \
  --role subatlas --retrieval-method corpus_snippet --hop 0 \
  --out <output_dir>/subatlas_snippets_<paper>.json

# Papers ASTA holds in full (status: asta, band: full)
python -m atlas_chat.cli_annotate fetch \
  --query "<upstream label>: definition, markers, cluster identity" \
  --paper-ids "DOI:<contributor DOI>" \
  --role subatlas --retrieval-method corpus_snippet --hop 0 \
  --out <output_dir>/subatlas_snippets_<paper>.json
```

Its supplementary tables are often where the cluster-to-name mapping and the marker
list actually live — check the supplement store
(`python -m atlas_chat.cli_supplements ...`) before concluding the definition is
unavailable.

**Then judge**, and set `evidence_status` honestly:

- `text_retrieved` — you read the paper's own words. Quote them.
- `abstract_only` / `unreachable` / `no_publication` — you did not. Then
  `confidence` must be `low`, `upstream_definition` must be **absent**, and
  `match_type: no match` means *"could not compare"*, not *"they disagree"*. Say
  which in `justification`. Do not infer a definition from the label string; that is
  the failure this step exists to prevent.

`match_type` and `skos_mapping` must agree. Whenever `match_type` is not
`exact match`, `explanation` is required — attempt the account from markers first
(shared markers; markers in one and not the other; a resolution difference where the
upstream study lacked the depth to split this population; a context difference in
stage, organ or assay). **If markers cannot explain it, say so plainly** rather than
writing a plausible story.

Where `purity < 0.8`, `purity_caveat` is required: describe how the contribution
splits and what it implies — the atlas merged several upstream types, or the upstream
paper split what the atlas treats as one, or the boundary is unstable in both.

### 3. Call primacy

- **`subatlas_primary`** — one contributor is an `exact match` (or a `narrow match`
  the atlas simply renamed) at high contribution and high purity. That paper defines
  this cell type. Name it in `primary_paper` / `primary_doi`. Traversal will seed
  there first, with the atlas paper supplying integration context and its own marker
  tables.
- **`atlas_primary`** — no contributor cleared the cutoff
  (`no_dominant_contributor`), or those that did are broad groupings the atlas
  subdivided. The atlas made this call itself.
- **`co_equal`** — several contributors are joint parents of a pooled label, or the
  dominant one is only a broad match. List them in `co_equal_papers`; traversal seeds
  on the atlas and those together.

Give the evidence in `reason`: which contributor, at what contribution and purity,
and what match type. A high contribution alone does not earn primacy — a pure but
coarse contributor is a broad match and leaves the atlas primary.

### 4. Write the output

Write `subatlas_consistency.json` to `output_path`, conforming to
`subatlas_consistency.schema.json`. Put it beside `subatlas_contributors.json` so
the validator hook can cross-check purity against it.

## Rules

- Never re-derive the cutoff. `subatlas_contributors.json` has applied it; the
  thresholds are recorded on that file.
- Every contributor over the cutoff gets a verdict. Dropping the awkward one is the
  easiest way to make a report look clean and is the thing most worth catching.
- Quotes are exact substrings of retrieved text, tagged `role: subatlas` — a quote
  about a contributor's own label comes from that contributor, not the atlas.
- An unreachable paper is a retrieval limit. Record it as such; never report it as
  disagreement.
- Do not invent an upstream definition from a label string, however suggestive.
- Report `no_dominant_contributor` as a finding. "This cell set is a pooled call with
  no single upstream parent" is information; silence is not.
- Do not write the report here. You produce the judgement; `synthesize-report`
  writes the prose.
