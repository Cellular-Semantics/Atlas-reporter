# Plan: ingest to CAS+

**Date:** 2026-09-06
**Status:** plan for review — not started

**Supersedes** the multi-source loader framework in
`plan_project_initialization_v2_2026-06-23.md`, the ingestion half of
`plan_cas_migration_bigbang_and_prog_agentic_split_2026-06-24.md`, and the
repositioning in `notes_cxg_author_probe_future_upstream_2026-07-04.md`.

---

## The shape of it

Atlases arrive however their authors left them: an h5ad with several obs fields
alongside a spreadsheet and a supplementary table; an R frame; a directory of
mtx and csv files. Agents work these out. A loader framework does not help, and
the multi-source case — several sources for one atlas, needing reconciliation —
is one no such framework was going to handle.

So extraction is improvised per atlas, and the discipline sits elsewhere:

> **The agent writes the script; the numbers come from the library.**

An agent writing `n_cells: 78` into a document is asserting a number it did not
compute. A library function doing a value count is reproducible and checkable.
Which format, which library, how to get the columns out — all incidental, and
all improvisable.

Ingest is also **iterative**. Which papers are subatlases is setup knowledge, not
data, and it is often filled in after the document is first populated. So CAS+ is
enriched across passes rather than produced once, and each pass is a script saved
with its output.

## Where CAS+ lives

**CAS+ is owned here.** `cxg-author-probe` keeps `probe-v1`, `picks-v1` and
`pulled-v1`. It has no opinion about CAS.

Those three wire shapes are small and stable, and they are the whole value of the
coupling. CAS+ is about to grow composition, the subatlas denominators and
atlas-paper provenance, none of which the module can populate. A schema with two
owners is how we ended up with two copies of it: `schemas/cas-v1.schema.json` on
the module's unmerged `cas-annotation-upstream` branch is a near-copy of our
`cas_annotation.schema.json`, already drifting both ways.

---

## The work

### 1. Fill in the CAS+ schema descriptions

The schema is what an agent works from, so its field descriptions are the
specification. **40 of 83 fields have no description at all** — most of
`SubatlasPaper`, most of `AtlasPaper`, several `TransferredAnnotation` and
`Labelset` fields.

Say what each field means and how it would be computed or found from source. This
is cheap and it is the highest-leverage work here. It is self-checking: if a
description is not enough for an agent to populate the field, the description is
wrong.

In the same pass: fold in upstream's `schema_version` and `data_provenance`, keep
`AstaIndexing`, add the two subatlas denominator fields below, and follow upstream
in dropping `title` and `source` from `required`. **Require only what structure
demands.** A document being enriched across passes is legitimately incomplete in
between; completeness is checked where a field is used, not where it is written.

### 2. The ingestion skill

A skill, not a framework. Use an existing skill where one fits, otherwise
improvise, aiming to produce CAS+ from whatever sources are to hand.

It produces two artifacts and a script.

**The cell table** — `pulled-v1` shape: a small JSON with `dataset_id`, `n_cells`
and a `data_path` to a parquet sidecar holding `observation_joinid` plus one
column per field. Cell IDs linked to annotation key/value pairs, whatever the
source was. The expression matrix is never read; `matrix_file_id` records where
it lives.

**The field typing** — `picks-v1` shape, extended: which columns hold author
cell-type annotations, which are covariates, which is the study reference, which
carry transferred labels. Per-column tags with confidence and a one-line reason,
plus `picker` recording who made each call — the benchmarked picker, a free
agent, or the curator.

**The script**, saved into the project, with its inputs pinned — source paths or
accessions, and the library version. A script whose inputs float is a record of
intent, not something that runs.

The skill carries recipes rather than machinery: streaming obs from a remote h5ad
without pulling the matrix; joining multi-file sources **on cell ID, never on row
position** — a wrong-order join of the right length is silent and corrupts every
count downstream.

It must **stop and ask** when representations clash. Several cell-type columns
that disagree, several developmental-stage encodings, sources that contradict
each other: these need the curator, and resolving them is a normal outcome of
ingest rather than a failure of it. Nothing should suggest that construction runs
to completion regardless.

### 3. The library

Composable functions the agent calls as information arrives. Composing them is the
intended use; reimplementing one is not. If a function does not fit a real atlas,
that is a bug report against the library — say so in the skill, because an agent
will otherwise helpfully write its own.

The test for what belongs here: does it have a correctness rule that must be
identical across projects?

In the library:

- **Profile a table** — per column: kind, dtype, exact `n_unique`, `n_categories`,
  a sample. Structural facts only, so it generalises to a format nobody has seen.
  It also decides which columns are worth showing to a judgment step: near-unique
  columns are identifiers, constant columns say nothing. **It must record the
  columns it withheld and why.** A dropped column cannot be picked and nobody
  finds out, which is a failure a wrong pick does not have.
- **Assemble** — the ported `cas.py`, grown: labelsets with rank by cardinality,
  one annotation per cell set with `n_cells` and a deterministic accession,
  parents where subsumption is strict, composition cross-tabs, the subatlas
  denominators. Invariant assertions on what it is handed: columns the same
  length, counts summing to the obs total, no ratio above one.
- **Validate** against the schema.
- **Summarise** — see below.

Anything supplied rather than derived — the atlas DOI, the title, subatlas paper
metadata — is passed as an argument, not typed into the document. `build_cas`
already works this way. The document has exactly one writer.

### 4. The summary, and the conversation after it

A deterministic rendering of the produced CAS+ for the curator: per labelset, how
many cell sets and whether their cells total the obs count; per contributing
study, its contribution; the subsumption result and its exceptions; which columns
the profile withheld; a few annotations shown in full.

This is what makes asking for corrections real. A wrong cell-type column shows up
at once as an implausible cell-set count; a bad labelset ranking shows up as a
failed subsumption; a mis-filtered column shows up in the withheld list.

### 5. Align the module, drop the rest

Small changes upstream so the shapes fit this order of operations:

- `pulled-v1` is documented as a pull *after* picking, its `picks` field being a
  subset of `picks-v1.picks`. Here the order inverts — extract, then profile, then
  type — so either relax that field's meaning or agree a reading where it lists
  everything extracted.
- `picks-v1` needs to carry more than author cell-type columns, and needs a little
  structure beyond per-column tags (below).

Adopt as a dependency: the picker and its prompt, benchmarked at n=73 (Jaccard
0.81 against CL_KG curation) — the evaluation corpus is the asset, and forking it
strands the benchmark. `probe()`, `pull_full_column()` and the readers behind them
are convenient where they fit; nothing is required to route through them.

Do not adopt: `cas-v1.schema.json`, or the CAS assembly on the unmerged branch.
Port `cas.py` and its tests down. Two things on that branch are worth merging
upstream and have nothing to do with CAS — the PostToolUse write-hook that gates
on `schema_version`, and the CLI batch-robustness fix. Expect a small conflict in
`cli.py` when cherry-picking them without the CAS commit.

Upstream is at 0.1.0 with no tags and no PyPI release, so the dependency is a git
pin until they cut one.

---

## Field typing cannot be closed, and should not pretend to be

Some typing depends on knowledge that is not in the data. Judging which dataset a
transferred label came from needs the list of subatlases, which is setup — and is
sometimes filled in after the document is first populated.

So typing is enriched like the document is. A column may be typed as carrying
transferred labels from an unresolved source, and resolved to a named study in a
later pass. The typing schema must permit that rather than requiring completeness
at one moment.

This also settles the picker-versus-agent question, which turns out not to be the
distinction that matters. What matters is that a judgment lands in a **validated
artifact** rather than being implicit in the extraction script. Once it is an
artifact it appears in the summary, it diffs across runs, and a wrong call is
fixed by correcting it and re-running. The picker is one producer of that
artifact; an agent in conversation with the curator is another; `picker` records
which.

And determinism is satisfied either way: **given the same recorded judgments, the
same CAS+ comes out.** Judgment is not deterministic by nature; the build is.

### The one place per-column tags are not enough

Transferred annotations are a relational judgment. The study column and the
original-author-label column are a pair, and whether the atlas is integrated at
all is a fact about the dataset rather than about any column. A flat
`column → category` typing cannot express "this label column came from that study
column", nor two integration sources encoded differently.

So the typing needs a little structure: at minimum a transferred-label column
naming the study column it pairs with.

Look at `feature/subatlas-consistency` before designing this — it already produces
`transferred_annotations` from obs, so it has a working answer to which signals
identify the pair.

---

## Subatlas overlap measures — denominators at ingest

### The four measures

Per (atlas cell set, contributing study, subatlas cell set):

- `purity` = `overlap_cells / subatlas_contribution_cells` — of what this study
  contributed to this atlas cell set, the fraction that is this one subatlas cell
  set. The denominator is the study's whole contribution, whatever it called the
  cells, so purity is blind to how much of the atlas cell set came from elsewhere.
- `fraction_of_subatlas_set` = `overlap_cells / subatlas_set_total_cells` — of
  this subatlas cell set, the fraction that ended up here.
- `fraction_of_atlas_set` = `overlap_cells / n_cells` — recorded, never gated. It
  is confounded by every other study's cells, so a low value describes the atlas
  cell set's mixture rather than the correspondence.
- `f1` = harmonic mean of the first two. High only when both are, which is what a
  one-to-one correspondence requires; neither alone discriminates.

`feature/subatlas-scoring` implements all four over `subatlas_scores.schema.json`.
Merge it, then change where the denominators come from.

### Why they move to ingest

That branch derives `subatlas_set_total_cells` post hoc from CAS+, by summing a
subatlas cell set across a partition of the atlas — the hierarchy leaves, or one
whole labelset. A partition is needed because CAS+ holds cell sets with counts,
not cells. Where none is usable the run is marked `degraded`:
`fraction_of_subatlas_set` and `f1` cannot be computed at all and the cutoff falls
back to `purity_floor`.

At ingest the problem does not arise. The table carries, per cell, the atlas
label, the contributing study and the original author label, so every denominator
is a direct count: cells with (study, source label); cells with (atlas cell set,
study); cells with all three, which is the existing
`TransferredAnnotation.cell_count`. No partition, no inference, nothing to
degrade. The partition machinery, `basis`, `degraded`, `purity_floor` and
`purity_only` all come out.

### Where they live

- **`SubatlasPaper.cell_sets[]`** — `{source_labelset, cell_label, n_cells}`. The
  denominator table for `fraction_of_subatlas_set`. It describes the contributing
  study rather than any one annotation, so it is stated once.
  `SubatlasPaper.total_cells` already holds the study's overall contribution.
- **`TransferredAnnotation.subatlas_contribution_cells`** — the study's
  contribution to this atlas cell set. Repeated across entries of the same study
  within an annotation; a cross-field test should assert the repeated values
  agree. Recording it explicitly rather than summing the transferred entries
  matters: they are exhaustive at ingest, but anything that later prunes them
  would quietly shrink the denominator.

`cell_count` and `cell_ratio` already exist, so `fraction_of_atlas_set` needs
nothing new.

### What it does not fix

The counts stay obs-derived, so they measure cells from the subatlas cell set
*present in the atlas*. Where an integration subsampled its source, that is not
the published cell set's size, and `fraction_of_subatlas_set` is recall against
the atlas's copy rather than against the original study. Computing at ingest
removes an inference failure, not a provenance limit.

Where a source has no per-cell data at all — a supplementary table of cell types
and their sizes — labelsets, annotations and `n_cells` are still produced, but
composition, subsumption and the denominators are not, because the joint
distribution was summed away before we saw it. The summary must say which parts
are absent and why. That limit is a property of the source, not of anything we
build.

---

## The subsumption hierarchy

Where an atlas has more than one author labelset, try to build a single
inheritance hierarchy across them, and report where it cannot be done.

The test is containment, not correlation: for each cell set in the finer labelset,
are all of its cells inside one cell set of the coarser labelset? If some fine
cell set splits across two or more coarser cell sets, the labelsets are not a
hierarchy — either they cut the data differently, or the annotation is
inconsistent.

**`parent_cell_set_accession` is set only where subsumption is strict.** Where it
fails the field is left unset and the exception is reported. This is a change to
the assembler as it stands: `build_cas` assigns a parent by dominant coarser
label, so it always produces an answer, including where no containment exists. A
parent meaning "mostly inside" is a claim the field does not make, and it is
invisible once written.

The check is nearly free — `build_cas` already computes the cross-tab and takes
`idxmax`; strict containment is the same cross-tab with one non-zero column per
fine label, and the failures are the rows with more.

Report exceptions with their numbers — this fine cell set has 312 cells in one
coarse set and 47 in another — so the curator can see whether it is stray cells or
a real disagreement.

Anything treating `parent_cell_set_accession` as a total ordering needs checking
against this. The scoring branch's `hierarchy_leaves` partition defines leaves as
cell sets that are no other cell set's parent, which shifts under a stricter
parent — though that partition is on its way out anyway.

If a non-containment relationship is ever worth recording it is an overlap
measure, not a parent, and it does not belong in CAS. Not proposed here.

Skip it when there is only one author labelset.

---

## What we are not building

- **The multi-source loader framework** — `anndata_loader`, `cellxgene_loader`,
  `spreadsheet_loader`, `cap_loader`, the `data-sources` extra, `/init-project` as
  a router.
- **A reader layer of our own**, or any requirement to route through upstream's.
- **Agentic reader improvisation as machinery.** The useful half is the invariant
  assertions, which live in the assembler.
- **`annotations_writer`'s sidecar files** — `co_annotations.json` and
  `label_provenance.json` were workarounds for a schema that could not hold
  covariates. CAS+ `composition` holds them.
- **A separate hierarchy-checking module** — it is a cross-tab in the assembler.
- **The six-layer testing taxonomy** — keep schema regression, deterministic
  golden tests of the library, and golden-project regression.

The field classifier — widening the picker from author cell-type columns to
annotating what every column contains, in CxG category vocabulary — is not in
scope here. It is a producer of the typing artifact, so it can arrive later
without changing anything downstream. Note it types what a column *contains*;
choosing the authoritative column for a category and resolving values to CURIEs
is ontology work and stays here.

---

## Sequencing

Merge `feature/subatlas-scoring` and `feature/subatlas-consistency` before the
assembler work, or it will rebuild them. Merging the scoring branch is not the end
of it: the measures stay, the post-hoc denominators are replaced by ingest-time
counts, and the partition machinery comes out — best as a follow-up commit on top
of the merge, so the two changes stay legible.

## Open questions

1. **Published subatlas cell-set sizes** — worth recovering from subatlas papers
   later, or is the obs-derived count sufficient permanently?
2. **Denominator scope** — every cell with (study, source label) in the table, or
   only those carrying an atlas annotation? They differ wherever cells were
   filtered out of the annotation.
3. **`cell_set_accession` scheme** — namespacing and stability across re-runs.
   Unresolved since June; `build_cas` currently uses `dataset_id:labelset:label`.
