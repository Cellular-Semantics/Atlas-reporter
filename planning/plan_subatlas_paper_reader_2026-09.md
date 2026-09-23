# Reading the subatlas papers

**Plan, September 2026.** Covers the reader only: taking the papers a routing
plan names, reading each whole, and writing evidence records for the cell sets it
was asked about — including whether the upstream study agrees with what the atlas
did with those cells.

Related: #73 (the routing plan this consumes) and #74 (the overlap measures it
rests on), both merged; #42 (why the read happens at this point in the sequence),
#46 (the record shape), #34 (the original work), #71 (paper retrieval, merged as
the `retrieve-paper` skill), #47 (report prose).

---

## What this is for

An integrated atlas mostly does not characterise its own cell types. The cells
arrive already annotated by the studies that generated them, and where a label
was carried across essentially unchanged, the biology was described in the
upstream paper and nowhere else. `planning/report_coverage_audit_2026-08.md`
measured what that costs: inherited annotations drew 1.4 evidence items per
report against 3.0 for the atlas's own, because retrieval always started at the
atlas paper.

So the contributing papers get read too. Which ones, and what to ask each, is
already decided deterministically at setup.

## What is already in place

**The dispatch.** `routing_plan.json` (#73, merged) gives, per study: its registry
label and DOI, why it is worth reading at all, and a list of questions. A
question is one subatlas cell set — the study's own label — the atlas cell sets
it `serves`, and an `ask`: what to put to this paper about this label, written
knowing how the cells actually divided.

Keyed by subatlas cell set on purpose: one of them commonly spans several atlas
cell sets and is still one question and one read.

**The overlap measures**, recorded in CAS+ at ingest and checked on write (#74),
so both correspondence directions are available without recomputing anything.

**The reading pattern.** `read-atlas-paper` (#63, merged): resolve the project's
paths, assemble the paper with `paper_ingest`, assemble a subject block per
subject, then take subjects one at a time — naming first, because the names found
there are what every later answer is searched with, then location, markers,
structure, function. Every assertion carries a verbatim quote, checked against
the job file before it is recorded, and `found: false` is a correct answer.

**Half the record shape.** `evidence_summary.schema.json` already has
`source_paper.role: subatlas`.

## What has to be built

### 1. One reader, not two

`read-atlas-paper` becomes `read-paper`. The questions a contributing study gets
are the atlas paper's questions; what differs is where the subject block comes
from, one additional question, and the role recorded on each record. Two copies
of the question prose would be two copies of the part most likely to be revised.

The agent takes a project, a paper (registry label or DOI, defaulting to the
atlas), and its subjects.

### 2. Per-paper path resolution

`project_paths.resolve()` knows one paper — the atlas — and resolves its text and
supplement store from `source.doi`. A reader working through nine contributing
studies needs the same answer for any paper in the project's corpus: given a
registry label or DOI from `source.subatlas_papers[]`, where is its text, where
is its supplement store, and what is missing.

Extend the existing service rather than adding a parallel one, and expose it as
`cli_project paper --doi <doi>`. It keeps reporting absences as absences; a
paper not yet fetched is a normal state.

### 3. The subject block: the routing question, plus how the cells divided

`cli_subject_block` builds subjects out of CAS+ `annotations[]`, which are the
*atlas's* cell sets. A contributing study's subject is its own cell set, and most
of it is already in the routing plan: the study's label, the atlas cell sets it
serves, and the `ask`.

What the routing plan does not carry is the arithmetic underneath, and the reader
needs it in both directions to answer anything about concordance:

- **Where this label's cells went** — every atlas cell set it fed, with the
  cells, the share of that atlas cell set, and the share of this subatlas label.
  A label split three ways is the interesting case and is invisible from the
  `serves` list alone.
- **What fed each served atlas cell set** — the other subatlas labels from this
  same study that went into it. An atlas cell set assembled from four of this
  study's labels is a different situation from one taken over wholesale, and only
  this direction shows it.

**Trim it, or it is unusable.** Untrimmed, this is 63k tokens for Lorenzi 2025
alone. Almost all of that is the hierarchy: `Mesen_Prepuce_Fetal` and `Prepuce
Fibroblast` are the same cells at two levels, and every ancestor up to
`Mesenchymal` overlaps as well. Keep the finest claimant where an ancestor and a
descendant are both present — the same collapse the scoring work already does —
and drop rows under 5% in the relevant direction unless the cell set is one this
question serves.

Measured on the fibroblast routing plan, trimmed:

| paper | questions | tokens |
| --- | --- | --- |
| Lorenzi 2025 | 20 | ~5,000 |
| HECA | 9 | ~1,600 |
| García-Alonso 2022 | 3 | ~1,350 |
| the remaining five | 1–5 | 350–1,000 |

About 1k tokens per question. Small enough that the reader gets the **whole
paper's block at once** rather than a question's slice — which is what lets it
see that two of its questions are about labels the atlas merged.

Deterministic transform of the routing plan and CAS+, so: a service with a CLI,
tests, no model. The rule from the atlas subject block applies unchanged and
should be stated in the same words — **it says who you are being asked about, and
it is not evidence.** None of these numbers may be quoted or reported as a
finding. They are the atlas's arithmetic, not something this paper said.

### 4. The extra questions: definition, then concordance

Two, asked once per subatlas cell set.

**What does this study mean by its own label?** In its own words, quoted. Not the
same as the naming question — naming asks what this paper calls a cell type, this
asks what it takes that cell type to be. Aspect: `upstream_definition`. (#42
called the label to compare the `compared_label`; it is simply the one the
question is keyed by.)

**Does that agree with what the atlas did with those cells?** The reader has the
transfer block, so it can see that this study's `Prepuce` went 37% to the atlas's
prepuce fibroblasts, 31% to labio-scrotal swelling and 21% to corpus cavernosum —
and it has just read what the paper means by `Prepuce`. Judging whether those are
the same population is a reading judgement, not an arithmetic one, which is why
it belongs here and not at setup.

Aspect: `concordance`. The answer says which it is and why, resting on the
paper's own words as everything else does. The routing `ask` frequently names the
specific thing to settle, and where it does, that is the question.

**The two outcomes are not symmetric, and the report treats them differently:**

- **Concordant** — the upstream characterisation describes the atlas's cells, so
  its markers, location and function are evidence *about this cell type* and are
  written into the report's own sections alongside the atlas's.
- **Discordant** — the upstream study made a different call about these cells.
  That does not get folded into the description, because doing so would state as
  settled something two papers disagree about. It gets its own section, naming
  the study, what it called these cells, and the evidence it gave — markers and
  location particularly, since those are what a reader needs to judge the
  disagreement.

A disagreement between the studies that made an atlas is a finding about the cell
type, not a defect in the evidence, and the report should read that way. The
prose rules for that section are #47's; what this plan owes it is a record shape
that keeps the two apart, so synthesis is not left inferring which is which from
tone.

### 4a. Everything is labelled by atlas cell type

Stated here because it is the thing most likely to go wrong: a record's identity
is the **atlas** `cell_label`, taken from the routing question's `serves`, and a
question serving three atlas cell sets produces records naming all three. The
study's own label goes in `subatlas_cell_label` and is never the identity.

The reader is reading a paper that uses its own names throughout, for cells the
atlas groups differently, so the pull toward filing an answer under the name on
the page is constant. Every consumer downstream — synthesis, CL mapping,
reconciliation — finds evidence by atlas `cell_label` and finds nothing filed
under anything else.

### 5. The record shape, reassessed

`evidence_summary.schema.json` was left alone last round on the grounds that it
worked. It still mostly does, but one thing has changed: **a record does not say
which cell type it is about.** The directory says. That holds only while every
producer files by cell type, and it stops holding here.

So `cell_label` goes on the record. This is forced by the filing decision, not a
preference — a record that cannot say what it is about cannot be harvested, only
found. Existing files fill it deterministically from their directory name; no
re-read, no model.

Three smaller additions:

- The atlas cell sets a subatlas record bears on, each with its own overlap
  numbers. One atlas cell set may hold 24% of the upstream set at purity 0.8 and
  another 3% of it, and a reader needs to know how much of its cell type this
  paper is actually describing.
- `subatlas_cell_label`, so the atlas's name for a set of cells and the study's
  own name are never taken for each other.
- `retrieval_method: whole_text`, which does not exist. `read-atlas-paper`
  currently writes `corpus_snippet` for a read that involved no snippet search;
  correct it in the same change.

**This is an increment on #46, not a second shape.** #46 asks for one record
written by every producer, and everything above is part of what it asks for.
What it also asks for and this does *not* take — the per-gene marker join,
`cited_sentence`, the identity/characterisation distinction — stays with #46.
The two must not grow competing schemas for the same file, which is the failure
already visible between the two CAS schemas.

### 6. Filing, and one way to read it back

There is more than one producer and they are dispatched on different things. A
paper read takes one paper and answers for many cell types. A cross-paper scan
takes one cell type and works across many papers. Neither key is right for the
other, and forcing either to file under the other's key means copying.

**So a producer files under what it was dispatched on, and names the subject in
the filename.** A paper read writes `traversal_output/papers/<paper>/<cell
type>.json`, beside that paper's job file, which is where the quote check already
looks for sources. A cell-type scan writes under that cell type. Both readers —
atlas and subatlas — behave identically, because they are the same agent given a
different paper.

One file per (dispatch, subject) rather than one per dispatch, so that a failure
part way through a long read leaves the finished subjects on disk. That is
already why `read-atlas-paper` writes as it goes.

**Consumers do not read the layout at all.** A collector is the only sanctioned
way to get a cell type's evidence: given the traversal directory and a
`cell_label`, it returns every record naming that label, wherever it was written
and by whichever producer, with the overlap numbers for that cell set rather than
all of them. Synthesis, CL mapping and anything later call it; none of them knows
where anything is filed.

Three things follow, and they are the reason for doing it this way:

- **Nothing is copied, so nothing can drift.** The alternative — placing a copy
  in each cell type's directory — needs a placement service, a staging area, and
  a check that placement happened at all, since a model that skips a step leaves
  an absence that looks exactly like a paper with nothing to say.
- **New producers cost nothing.** The cross-paper scanner files under its own
  key and is harvestable the day it is written, with no consumer change.
- **The layout stops being a contract.** Where files sit becomes a producer's
  local decision, changeable later without touching a consumer.

The existing per-cell-type `all_summaries.json` files are read by the same
collector once they carry `cell_label` — they are the case where every record in
a file shares one. So nothing has to be re-read, and there is no window where two
conventions are both live contracts.

**No index.** Nine papers and a few hundred small records: walk the directory and
parse. An index is a second thing to keep true, and it earns its place only once
a walk is measurably slow.

The one property the per-cell-type layout had is that the directory *is* the
filter — a consumer cannot accidentally read another cell type's evidence. Keep
it by requiring `cell_label` on every collector call, so nothing can be read
without saying what it is being read for.

### 7. Completeness, which the layout does not decide

Independently of where things are filed: did every question in the read plan get
an answer? A study that was never read and a study that was read and said nothing
are different findings, and #42 is firm that the first has to be written up as a
retrieval limit rather than as silence.

So a reconciliation over the read plan and the records — questions in, answered
and unanswered out. Called before synthesis and again before CL mapping, which is
where it matters most: a mapping made from evidence known to be incomplete
produces a confident `cl_mapping.json` and possibly a public issue on
`obophenotype/cell-ontology`. Better to refuse.

This is not a hook. Hooks here fire on a write, and the failure is a write that
never happened.

## Sequence

Two pull requests, split so that the plumbing is settled and exercised on real
output before anything subatlas-specific is built on it.

**Step 0, in parallel with everything: build the corpus.** Retrieve the eight
reachable studies and index their supplements (below). Nothing in PR 1 waits on
it, and PR 2 cannot be tested without it, so it starts now.

**PR 1 — the new output pattern, and the collector that reads it.** No subatlas
paper, no retrieval: the atlas preprint is on disk and the reader works, so the
new pattern can be produced and consumed for real.

1. `cell_label` on `evidence_summary.schema.json` — a **list**, since one answer
   can genuinely be about several atlas cell sets and duplicating its prose per
   cell set reintroduces the drift the layout decision removed. With
   `check_evidence_summary.py` and its fixtures updated in the same commit, and a
   one-off pass filling it on existing files from their directory name.
2. The reader writes the new pattern: one file per (paper, cell type) under
   `papers/<paper>/`, every record naming the atlas cell sets it is about.
3. **Re-run it on the atlas paper for a few cell types.** This is what the
   collector is then built against — real model output in the new shape, rather
   than a fixture written to match assumptions the reader may not share.
4. The collector, and synthesis and CL mapping pointed at it. It must read both
   the new files and the migrated legacy ones.
5. The reconciliation, called from both consumers.
6. A round-trip test pinning the contract: records in each producer's shape,
   collected by `cell_label`, asserting what comes back *and* what does not.

Everything the reader is likely to churn on afterwards — the transfer block, the
aspect vocabulary, how a concordance answer reads — is invisible to the
collector, which filters on `cell_label` and returns records whole. The list
question above is the one real coupling, which is why it is settled here.

**PR 2 — subatlas reads**, on plumbing already proven.

7. Per-paper path resolution, and the transfer block. Both deterministic, both
   services with CLIs and unit tests, both usable without a Claude Code session.
8. The two extra questions and the role from the caller; the remaining record
   fields — the subatlas context, `upstream_definition`, `concordance`,
   `whole_text` — arrive with them.
9. Reference run on `hca_reproductive`, the only project with real joint
   provenance.

## The corpus, without which none of this can be tested

`hca_reproductive` currently holds the text of **one** paper — the atlas
preprint. Eight of its nine contributing studies have DOIs and none of them has
been retrieved; there is no supplement store for the project at all.

So before any of this can be run end to end:

- **Retrieve the eight**, with the `retrieve-paper` skill (#71), which records how
  each one arrived. Expect a mixed result rather than eight clean JATS files:
  PNAS and Nature Communications should come through Europe PMC, the Nature and
  Developmental Cell papers may only be reachable as PDF or not at all. Whatever
  happens is recorded per paper, which is what the reader needs anyway.
- **Index their supplements**, with `index-supplements`. This matters more for a
  contributing study than for the atlas: what its label means is frequently
  settled in a supplementary cluster table or a methods supplement rather than in
  a body that had four pages for the whole result. A subatlas read against body
  text alone would test the reader on the easy half of its evidence.

The ninth, `celltype_OvarySanger2026`, has no DOI and contributes 179,450 cells
across 21 of the 37 fibroblast cell sets. Nothing reaches it, and reports resting
on those cell sets have a ceiling that should be stated in them rather than
discovered at synthesis.

Retrieval is therefore a prerequisite for *testing*, not for the design: the
reader has to handle an unreadable study regardless, because one of them is
permanently unreadable. Until the corpus is complete, the coverage number the
audit asked for — 1.4 evidence items against 3.0 — cannot be re-measured, and
that is the number that says whether any of this worked.

## Out of scope

- The consistency verdict and the primacy call (#42 §3) — a comparator over
  records that already exist, not part of reading.
- Threshold changes in the read plan (#45 leaves the defaults provisional).
- Report prose rules for provenance (#47).
