# Roadmap (draft, Aug 2026)

Written against [`docs/functional_spec.md`](docs/functional_spec.md). It records what
the pipeline can already do, what the spec asks for that we don't have, and the order
we intend to close the gap. The previous roadmap (structured around the deprecated
programmatic graph and the pre-CAS+ config) is archived at
`planning/ROADMAP_pre_2026-08_superseded.md`; the parts still worth keeping are folded
in below.

Open tracker issues are referenced as `#n` throughout
(github.com/Cellular-Semantics/Atlas-reporter).

---

## 1. Release and branch policy

- `dev` is the integration branch. Feature work forks from `dev` and merges back via PR.
- `dev` is allowed to be mid-refactor. `main` is not.
- We release `dev` → `main` only at a point where new functionality (or a refactor) is
  complete *and* nothing that worked before has got worse. "Nothing got worse" means the
  regression suite in §9 passes and a reference project still generates reports of the
  quality bar set by the April 2026 fetal-skin corpus.
- Content branches (per-atlas projects, e.g. `fetal_skin_atlas`, `HDCA_Neurons`) are not
  part of this cycle; they carry reports, not code.
- Practical consequence: don't merge half a theme to `main` just because the PR is green.
  Batch a theme's PRs on `dev`, run the release check, then promote.

---

## 2. Where we are

Working today on `dev`:

| Capability | Where |
|---|---|
| CAS+ as the single project config | `schemas/cas_annotation.schema.json`, `generate-cas` skill (#18) |
| Annotation ingest from labels / CSV / h5ad / zarr / CxG | `generate-cas`, `anndata-zarr-summary` skills |
| Subatlas paper discovery + ingest waterfall (ASTA → JATS → needs PDF) | `services/subatlas_resolver.py`, `local-paper-index` skill |
| Local snippet index for papers ASTA can't serve (JATS + PDF) | `services/local_snippet_index.py`, `_jats_parser.py`, `_pdf_parser.py` |
| Sentence-gated citation traversal with reference splicing | `citation-traverse` agent + `cli_annotate` (#14, #16) |
| Evidence provenance: `source_paper.role` + `retrieval_method` | `schemas/evidence_summary.schema.json` (#12, #15) |
| Report synthesis with quote + DOI validation and a retry loop | `synthesize-report`, `validation/report_checker.py` |
| CL mapping and draft NTR, optional posting to the CL tracker | `ontology-term-lookup`, `cl-term-request` agents |
| Output-schema hooks on every orchestration | `.claude/hooks/check_*.py` |

In flight:

- **`query-decomposer` branch** — PR #20 open against `dev` (Layer A: query-driven
  selection of cell types over CAS+). Layer B (per-cell-type aspect decomposition, the
  `query-decomposer` agent + schema + hybrid traversal strategy) is committed on the same
  branch but not yet in a PR; PR #19 was closed because it targeted `main`. Also adds
  `name_resolution.schema.json` and `projects/test_projects/` run tracking.
- **`generate-cas` branch** — merged to `dev` (#18); worktree can be retired.
- **`cxg-entrypoint-reader-discovery` branch** — obs-field classifier that would remove
  the "ask the user which column is the label" step in `generate-cas`. Not merged.

---

## 3. Gaps against the functional spec

Spec section by section, what's missing:

**Setup / init.** There is no `init` orchestration. Today project creation is manual:
make the directory, run `generate-cas`, run `setup_local_index.py discover-subatlas` /
`init-corpus` by hand. The spec asks for one entry point that takes an atlas name, sets
up the branch and directory structure (from `main`), takes the primary paper + subatlas
papers + annotations, and then reports back on what is actually retrievable.

**Paper availability triage.** We probe ASTA, but the probe can't fail — `_probe_asta()`
returns true whenever the paper has a CorpusId, including for papers with zero body text
in the snippet index (#22, with calibrated thresholds already measured). So the
`asta → jats → needs_pdf` waterfall short-circuits and we silently build reports on
abstract-only evidence. The spec's "initial report on papers — what is reliably
available and what needs manual assist" doesn't exist as an artifact.

**Supplementary material.** Fetched mid-run through MCP into agent context, per cell
type. The spec (and #21) wants it fetched once per paper to disk at setup, with a
manifest of content pointers ("DEG table for cell type X is in media-4.xlsx, sheet B")
plus a negative cache so failures don't retry forever.

**Initial report on annotations.** Not produced. `generate-cas` asks the user about field
roles but emits no summary of what was found: hierarchy, marker availability, whether
subatlas annotations are present, or clashes between multiple annotation sources.

**Asserted vs derived markers.** `marker_gene_evidence` in CAS+ is a flat list of gene
symbols — no provenance, no distinction between an author assertion and a DEG/NS-Forest
result, no DEG context (what was compared against, how many genes were reported). The
spec wants literature and asserted markers checked against derived markers, with the
limitations of the DEG evidence stated when they disagree.

**Subatlas consistency.** `transferred_annotations` carries the integration provenance
(with `cell_ratio`), and `resolve-name` uses it to pick the source paper — but no step
reports on agreement or disagreement between an atlas annotation and the subatlas labels
it was built from, and there's no long-tail cutoff.

**Location from data.** Spatial evidence in the atlas/subatlas (e.g. spatial
transcriptomics) is not treated differently from literature evidence; there's no way to
say "this location comes from the data, and here is the method".

**ID validation.** `report_checker` validates quotes and DOIs against the catalogue only.
Gene symbols and ontology IDs are unvalidated, and DOIs are not checked against an
external source (the fabricated-catalogue failure mode).

**Query entry point.** The spec's "for each annotation, generate a report" is per-label.
PR #20's free-text query selection is the right shape for this and should land.

---

## 4. Theme A — project setup and corpus triage

1. **`init-project` skill** (#9, #21). One entry point: atlas name → branch off `main` +
   project skeleton → collect primary paper, subatlas papers, annotation source (file
   dropped in `input/`, or a link) → run `generate-cas` → run corpus ingest → emit the
   two setup reports below. Wraps existing pieces; no new retrieval logic.
2. **Fix the ASTA depth probe** (#22). Replace the CorpusId check with the calibrated
   snippet-count/char-count signals; record an indexing band per paper
   (`indexed` / `abstract_only` / `absent`) in the CAS+ `SubatlasPaper.status`.
3. **`fetch-supplements` setup skill** (#21) — **prerequisite for the retrieval
   evaluation** (§5 B1), so it comes before the rest of Theme A. Direct API to disk via
   `services/europepmc.py` / `fetch_preprint.py`, per-paper manifest with content
   pointers, negative cache. Traversal and `scan-supplements` consult the store instead
   of fetching inline. Consider folding it into the `local-paper-index` per-paper
   materials manifest rather than a second store.
4. **Setup report: papers.** Per corpus paper — indexing band, full text route (ASTA /
   JATS / PDF / none), supplements retrieved, and an explicit list of what the user must
   fetch by hand.
5. **Setup report: annotations.** Labelsets and hierarchy, cell counts, marker
   availability and kind, presence of `transferred_annotations`, and any clash between
   multiple annotation sources — with questions for the user where a clash can't be
   resolved automatically.

---

## 5. Theme B — literature search and retrieval

This is the biggest lever on report quality and the place we are genuinely stuck. The
honest position: we do not yet know which retrieval strategy is best, and the testing so
far was two examples deep, which is not enough to conclude anything. Everything else in
this theme is downstream of settling that, so it goes first.

### What we know

- An ASTA snippet search scoped to a single paper at `limit 20` returns nearly as much
  text as the paper itself. Paper-scoped snippet search is therefore not buying much
  reduction — its value may be entirely in *cross-paper discovery* (which paper has the
  answer) rather than *within-paper localisation* (where in this paper is the answer).
  That is a testable claim and it changes the architecture if true.
- We found no way to tune on the ASTA relevance score — it did not separate useful from
  useless snippets well enough to threshold on.
- Both observations push back toward working from full text. But that immediately raises
  the questions we have not answered: which model reads it, what is it asked, and does it
  read in the main context or in a subagent.
- The local index's dense ranking is currently measuring a bug, not a strategy (#23).

### What we don't know

- How strong the ASTA encoding actually is for the questions we need to ask. "Find markers
  for cell type X (synonyms Y, Z)" is the canonical case. Is dense retrieval better than
  a plain string search for the cell-type names plus terms like *marker*, *DEG*,
  *enriched*, handed to a frontier model that can judge from context? We assume the
  embedding earns its place; we have not shown it.
- Whether decomposing into per-aspect queries helps, hurts, or is noise. That is the whole
  premise of the `query-decomposer` work and it is untested.
- Whether alias expansion and steering away from confusable sibling cell types improves
  precision enough to matter.
- What the cheapest model is that can gate passages reliably, and whether gating in a
  subagent (context stays clean) beats gating in the main context (no dispatch overhead,
  better continuity).

### B0. Retrieval strategy evaluation (blocking)

Build a broader test set and run a matrix of strategies against it. Not a benchmark for
its own sake — the outcome decides what we build in B2 and how the workflow is shaped.

**Test set.** Ten to twenty cell types spanning at least four atlases, deliberately mixed:
opaque cluster labels (c1/c2-style, where the name is only resolvable from another paper)
and descriptive names; well-studied cell types and novel ones; open-access JATS papers and
PDF-only ones; papers ASTA indexes fully and papers it barely indexes. Two examples from
one atlas is how we got over-confident last time.

**Gold passages, cheaply.** Every quote in a validated report is a passage we already know
is both relevant and locatable — the April 2026 reports give us gold for free. Supplement
that with hand-marked passages for the cases those reports got wrong or missed (the
cluster-mapping tables, the marker tables), and record for each cell type the handful of
claims a good report must support.

**Strategy axes.** Cross these rather than testing one path:

| Axis | Options |
|---|---|
| Retrieval | ASTA snippets (vary limit); local dense index; lexical search over full text; lexical + dense; no retrieval — whole paper to the model |
| Query | one combined query; per-aspect decomposed queries; aliases on/off; sibling-steering on/off; lexical name+term patterns |
| Reader/gating model | Haiku, Sonnet, Opus |
| Context | subagent vs main context |
| Unit of work | per cell type vs one pass per paper covering all its cell types |

**Sources per aspect.** Score each aspect against the source that actually carries it.
Markers and cluster-to-name mappings usually live in supplementary tables, not in the body
text; function and location usually live in prose. If supplements are absent when the
matrix runs, marker recall will look like a retrieval failure when it is a missing source
— this is the trap we have already fallen into. Record, per gold passage, whether it came
from body text or a supplement, and never average the two into one recall number.

**Measures.**
- Recall of the gold passages, per aspect (markers, location, function, structure) and per
  source (body text vs supplement).
- Precision — what fraction of returned text is worth reading. This is the number that
  matters when snippet search returns most of a paper.
- Is the ASTA score usable at all? Score the retrieved passages against the relevance
  labels; if it doesn't separate them, we stop trying to threshold on it and gate with a
  model instead.
- Tokens read, calls made, wall clock, cost — per cell type and per paper.
- Whether the claims a good report needs actually survive into the report.

**Specific comparisons to settle:**
1. ASTA paper-scoped snippets vs lexical search vs whole full text, holding the reader
   model fixed. Does the embedding beat grep?
2. Per-aspect queries vs one combined query, same retrieval method.
3. Cheap model over more text vs expensive model over less. The batched per-paper pass
   (one read covering every cell type from that paper) is the interesting cell here — it
   changes the cost picture more than any per-query tuning.
4. ASTA for discovery only (which paper), full text for extraction (where in it) — the
   hypothesis implied by the limit-20 observation.

The harness stays as a permanent artifact, not a one-off: strategies get re-measured when
retrieval changes (§9).

### B1. Prerequisites — get the sources right before measuring them

Three things have to be in place first. The two bugs would benchmark themselves rather
than the strategy; the missing supplement store would misattribute its absence to whatever
retrieval arm happened to be running.

- **Chunk/embed mismatch in the local index** (#23). MiniLM truncates at 256 word pieces
  while chunks are ~500–700, so roughly half of every chunk is invisible to ranking. Fix
  the chunk size (or the model), and get the chunking parameters into `_manifest_hash()`
  or bump `MANIFEST_VERSION` so existing corpora rebuild rather than silently serving
  stale vectors.
- **ASTA depth probe** (#22). The probe cannot fail, so papers with no body text in the
  snippet index look identical to fully indexed ones. Any per-paper comparison needs to
  know which band a paper is in, or the ASTA arm loses for the wrong reason.
- **Supplement store** (#21, Theme A). Supplementary material carries content that is
  critical to a report and often available nowhere else — DEG tables, cluster annotation
  tables, the marker lists that name resolution depends on. Any end-to-end arm of the
  matrix without it is measuring an incomplete corpus. Needed at least to the point where
  supplements for the test-set papers are on disk with a manifest of content pointers;
  the polish (negative cache, folding into the `local-paper-index` manifest) can follow.

### B2. Held behind the evaluation

- **`query-decomposer` Layer B** — the agent, its schema, and the hybrid traversal
  strategy (combined query, assess per-aspect coverage, targeted queries for thin aspects,
  scope-targeted free search as a last resort). It is written and committed on the
  `query-decomposer` branch. Whether we merge it as-is depends on comparison 2 above.
- **Layer A (PR #20)** is *not* held — selecting which cell types to report on from a
  free-text query is orthogonal to how evidence is retrieved, and it replaces the
  per-label entry point the spec has outgrown. Merge it.

### B3. Scope-aware evidence

The spec allows out-of-context evidence (different species, stage, tissue) when nothing
better exists, provided the context is made clear. That needs to be explicit rather than
implicit: tag each evidence item with the context of its source paper, prefer in-scope
evidence during selection, and have the synthesizer state the mismatch in the report when
it uses off-scope evidence. Whether scope terms belong *in the query* or are applied as a
filter *after* retrieval is one of the things B0 should tell us.

### B4. Efficiency

The design in `planning/efficient_workflow_design.md` still stands, and B0's "unit of
work" axis is the same question asked empirically. Three phases: name resolution (full
text permitted, once per source paper, covers all cells), evidence gathering (batched per
paper), synthesis (no tool calls). The April 2026 bulk run cost ~$597 for ~119 cell types
because every subagent independently loaded full text.

Two wins already available regardless of the outcome: the supplement store (Theme A) keeps
large files out of context, and `cli_annotate` already keeps raw snippet JSON out of the
agent's context. And the probe fix should stop wasting hop-1 dispatches on papers with no
retrievable text — 5 of 14 in the 2026-08-19 run.

### B5. PDF citation edges (#13)

PDF-sourced papers contribute no outbound edges, so a PDF-only atlas can't seed a citation
walk. Per-paper extraction waterfall: link annotations → in-text GOTO anchors →
plain-text DOIs → title resolution via Crossref/S2. Independent of B0 — needed for the
reproductive atlas whichever strategy wins.

---

## 6. Theme C — report content

1. **Marker provenance in CAS+.** Extend `marker_gene_evidence` from a bare string list
   to objects carrying kind (`asserted` / `derived`), method (DE, NS-Forest, …), the
   comparison context, and a rank or cutoff where known. Schema change plus a
   `generate-cas` change to populate it, plus migration of existing `cas.json` files.
2. **Marker cross-check.** For each marker claimed by the literature or asserted by the
   authors, compare against derived markers; where they disagree, state the limitations
   of the DEG evidence (top-N truncation, over-broad comparison group) rather than
   silently dropping the marker.
3. **Subatlas consistency section.** Compare the atlas annotation against its
   `transferred_annotations`, apply a `cell_ratio` cutoff to drop long-tail noise, and
   where labels disagree, try to explain it from markers.
4. **Location from data.** Where the atlas or a subatlas provides spatial evidence,
   report it as data with its method named, distinct from literature claims.
5. **Report shape.** Reports read as a short paper — scientific prose about the biology,
   not about the process of generating the report. Every literature assertion carries a
   supporting quote; the report ends with a standard reference section. Largely true
   today; keep it in the acceptance checks.

---

## 7. Theme D — validation and anti-hallucination

- **External DOI check.** Validate every DOI against Europe PMC, not just against
  `paper_catalogue.json` — the catalogue itself can be fabricated (the Szabó et al. 2025
  incident).
- **Gene symbol validation.** Check symbols against an authority (HGNC/MGI as
  appropriate) and flag unrecognised ones.
- **Ontology ID validation.** Check every CL/UBERON/HsapDv ID in a report or CAS+ file
  resolves in OLS and that the label matches.
- **Blockquote attribution.** Every `> "..."` must be followed by an attribution line;
  currently only quote content is checked. The April 2026 Neuroendocrine report is the
  reference failure — 15 verifiable quotes, no attribution.
- **Evidence-source transparency.** Add a `Sources:` header line counting
  citation-traversed vs free-search papers, and mark free-search citations inline. A
  report built entirely from free search is a signal that name resolution failed; the
  validator should warn, not fail.
- **Generic-background heuristic.** Count atlas-specific claims against background
  paragraphs with no quote; flag reports padded with generic cell biology.

---

## 8. Theme E — user-facing documentation

Currently the README describes a per-cell-type run against a config file that no longer
exists (#10), and the ingest paths that do exist are undocumented (#9). Everything else
lives in `CLAUDE.md` / `CLAUDE_dev.md`, which are instructions for agents, not for users.

Target set:

1. **README** — what the tool does, what a report looks like, what is and isn't
   guaranteed, install, and a five-minute path to a first report. Replace the stale
   ingest instructions (#10).
2. **Getting started / new atlas project** — the `init` flow end to end: papers,
   annotations, what the setup reports tell you, and what to do when a paper needs a
   manual PDF.
3. **Annotation ingest guide** (#9) — every supported source (label list, spreadsheet,
   h5ad, zarr, CxG, supplementary table), what CAS+ fields each populates, and what the
   tool will ask you.
4. **Reading a report** — how to read the evidence: quotes, provenance tags, in-scope vs
   off-scope evidence, what validation does and does not guarantee.
5. **CL mapping and new term requests** — how mappings are classified and what happens
   when a request is posted to the CL tracker.
6. **Worked example** — one project (the knee chondrocyte pilot, #11 / #2) followed from
   init to reports to NTRs, with the real artifacts.
7. Keep the developer material where it is; add a short contributor page pointing at
   `CLAUDE_dev.md` and the branch policy in §1.

Docs are built with Sphinx + MyST (`scripts/check-docs.py`); the user-facing guides
belong in `docs/` and should be part of that build.

**The docs build is broken today and has to be fixed before any of the above can
land.** `scripts/check-docs.py` fails immediately with "Sphinx is unable to load the
master document": `docs/conf.py` sets no `root_doc`, so Sphinx looks for
`docs/index.rst`, which does not exist. Everything in `docs/` is a loose markdown
file that no toctree references. Three things to settle while fixing it:

- Add a root `index.md` (MyST is already loaded) with a toctree over the existing
  pages, so `sphinx-build -W` gets past the first step.
- `CLAUDE_dev.md` claims API docs come from "Sphinx + AutoAPI", but `conf.py` loads
  only `autodoc`, `napoleon` and `myst_parser` — there is no AutoAPI and no
  `automodule` directive anywhere. Either wire up API generation or correct the dev
  guide; right now no module docstring is ever rendered or checked, so RST errors in
  them are invisible.
- `conf.py` puts `src/` on `sys.path`, but the package lives at
  `src/atlas_chat/atlas_chat/`, so `import atlas_chat` would not resolve from there
  even once autodoc has something to do. (Phase 1 of the archived roadmap wanted this
  nesting flattened; whichever happens first, the path needs to match.)

Until the build is green, `check-docs.py` cannot join pre-commit or the release check
in §9, and docstring quality is unenforced.

---

## 9. Theme F — testing and the release check

The release gate in §1 needs something concrete to run.

- **Schema regression** — good/bad fixtures per output schema. Exists for CAS+, evidence
  provenance, traversal, and (on the query-decomposer branch) name resolution and query
  decomposition. Extend to `cl_term_request` and any new contract.
- **Report validation regression** — `check_quotes`, `check_references`,
  `check_source_tags` pinned on known inputs; three reference reports must keep passing.
- **Reference corpus** — the April 2026 fetal-skin reports are the quality bar
  (`projects/fetal_skin_atlas/reports/`). Named tests from the archived roadmap worth
  keeping: the c1/c2 name-resolution case (needs full text from two papers, snippet
  search alone fails), and the c2 evidence-chain case (three papers each contributing
  distinct evidence).
- **Retrieval evaluation** (§5 B0) re-run and reported per release, not pass/fail —
  it is how we notice a retrieval change made things worse.
- **Cost/turn accounting** per run so efficiency changes are visible.
- **Coverage floor** is currently `fail_under = 0`. Raise it as tests arrive; don't set an
  aspirational floor that forces `--no-verify`.

---

## 10. Suggested order

The order is set by one thing: we cannot design the retrieval layer until we know how
well the pieces we already have actually retrieve. Everything with a dependency on that
answer waits; everything without one proceeds in parallel.

**First — unblock the retrieval question.**

1. Fix the two bugs that would corrupt any measurement: chunk/embed mismatch (#23) and
   the ASTA depth probe (#22).
2. Supplement store (#21) — enough of it that supplements for the test-set papers are on
   disk with content pointers. Supplements carry the marker and cluster-annotation tables
   a report cannot be written without, so an end-to-end matrix run without them measures
   the wrong thing. Rebuild the local indexes for the test-set papers at the same time,
   after #23, so every number comes from one index generation.
3. Build the test set and the evaluation harness (§5 B0). Broader than last time —
   10-20 cell types over at least four atlases, gold passages seeded from the quotes in
   validated reports and tagged by source (body text vs supplement).
4. Run the strategy matrix. Report recall, precision, and cost per strategy; settle
   whether the ASTA score is usable, whether the embedding beats lexical search, whether
   per-aspect decomposition earns its keep, and whether a per-paper batched read beats
   per-cell-type retrieval.
5. Decide the retrieval architecture from the results, then either merge
   `query-decomposer` Layer B as-is, rework it, or drop it.

**In parallel — work with no dependency on the outcome.**

- Merge PR #20 (Layer A cell-type selection).
- `init-project` (Theme A) wrapped around the supplement store once that exists, plus the
  two setup reports. This also makes the evaluation easier to run across several atlases.
- Marker provenance in CAS+ and the marker cross-check (Theme C 1-2).
- Validation additions: external DOI check, gene symbols, ontology IDs, blockquote
  attribution (Theme D).
- PDF citation edges (#13).

**After the architecture is settled.**

- Rebuild the evidence-gathering phase on whatever won, and re-run the reference corpus
  to confirm no regression before promoting `dev` to `main`.
- Documentation rewrite (Theme E) — the getting-started guide should describe the flow we
  actually settled on, not the one we are mid-way through replacing.
- Subatlas consistency and location-from-data (Theme C 3-4).

Pilot projects (#11, #2) run alongside throughout, and double as test-set material — the
knee chondrocyte set is small, open access, and has clean marker tables, which makes it a
good second atlas for the matrix as well as a good first end-to-end run.
