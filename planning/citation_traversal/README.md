# Following citations out of an atlas paper: what works, what doesn't, and what it costs

**Branch `test/retrieval-matrix`, August 2026. Experimental — not for merge.**

This is the whole story in one document. It assumes no prior reading. Numbers quoted here
are reproducible from `experiments/citation_traversal/` (see *Reproducing this* at the end).

---

## The question

An atlas paper (here Gopee et al. 2024, the prenatal human skin atlas) annotates cell types
and cites ~110 other papers. Atlas-reporter wants to follow those citations to learn about
those cell types. Does that work?

Two different things were being conflated under "does traversal work", and separating them
was the most useful outcome of this work:

**Enrichment** — can we learn *more* about a cell type than the atlas paper itself says, by
following citations in sentences that mention it? This is atlas-reporter's primary aim.

**Verification** — does a cited paper actually support the assertion the atlas paper attaches
to it? Not the primary aim, but valuable, and cheap to add later: after a report asserts a
cell-type property on the atlas paper's authority, ask whether the atlas paper's own sources
back it.

The work below measures the machinery both share — reaching the cited paper and retrieving
evidence from it — and then measures verification directly. Enrichment needs its own test set
and has not been measured; see *What is still unmeasured*.

---

## Answers, in one page

**Reaching the right paper is a solved problem.** Given a sentence in the atlas paper and its
citation marker, the retrieval service (ASTA) resolves that marker to the correct paper with
**zero errors in 174 citations**. Its failure mode is silence — 10% of markers go unresolved —
never a wrong answer.

**Searching the whole literature to find the cited paper does not work; searching the atlas
paper's reference list does.** Asking the same question of everything ASTA indexes surfaces
the correct paper in the top 20 for 1–6 of 19 claims. Restricting the search space to the ~87
papers the atlas cites finds it **19 out of 19**, ranked first for 15 of them.

**Getting the specific supporting passage needs a second, paper-scoped hop.** Searching inside
one known paper returns the supporting passage **97% of the time it exists**. Searching across
the reference list returns it only 53–72% of the time, because a fixed snippet budget spread
over five papers leaves four snippets each. Neither hop alone suffices; chained, they should
recover essentially everything the service holds.

**Access is the outer limit. Only about half the citation corpus can be read at all** — 38 of
109 references yield full text from PMC, 56 are held by the retrieval service, 57 by either,
and 48% by neither. Availability flags overstate this badly: 70 references have a PMCID and 42
are labelled open access, but only 38 actually fetch. Details in `paper_availability.md`.

**Within the papers we can reach, coverage is still the binding constraint. Only 70% of
supporting passages are in the service at all.**
The misses are not random: they concentrate in **introductions**, in **figure captions**, and
in one paper held as title-and-abstract only.

**Citations are not always sound, and nothing in our pipeline would notice.** Of 19 claims read
against the full text of the papers they cite: 12 supported, 5 partially, 1 not supported, and
**1 flatly contradicted** by the paper cited for it. All 19 would pass our current quote and
reference validation.

---

## How each answer was established

### Reaching the cited paper

The atlas paper's own markup is the answer key. Its JATS XML links each citing sentence to a
numbered reference and each reference to a DOI, giving **187 (sentence, reference) pairs** —
175 with a resolvable target across 97 papers — at the cost of one local parse. No model and
no retrieval method was involved in choosing the items or their targets, so nothing can win by
construction.

Against that key, over ASTA's complete indexed copy of the atlas paper (72 chunks):

| step | result |
|---|---|
| the citing sentence is in ASTA's copy, exactly | 154/175 (88%) |
| …present in *some* rendering | 162/175 (93%) |
| ASTA marks a citation inside it and resolves it | 142/154 (92%) |
| that resolution names the work the paper cited | 138/142 (97%) |

Because ASTA renders citation markers as bare digits inside the sentence, the marker *is* the
reference number, which gives a second check that needs no sentence matching at all: for each
of the 174 citation markers in ASTA's copy, does its resolved paper match what the atlas
paper's reference list says?

| | count |
|---|---|
| agrees with the reference list | 150 (86%) |
| agrees, but names a different record of the same work | 5 (3%) |
| ASTA could not resolve the marker | 18 (10%) |
| marker not parseable | 1 (1%) |
| **disagrees** | **0** |

Two things fall out. Every failure is *under*-annotation, never mis-annotation: traversal asked
to follow a specific citation will sometimes find nothing to follow, but will not be sent
somewhere wrong. And five citations resolve to the **preprint** where the reference list gives
the journal version — traversal reaches the right paper and reports a DOI the citing paper
never printed. That is a live catalogue and dedup bug, since report references take DOIs from
the catalogue.

### Do the cited papers support the claims?

Reference markup says *which* paper was cited, not whether it supports anything. So a frontier
model (this session) read **all 15 cited papers in full** and adjudicated **19 claims**,
recording a **verbatim supporting span** for each — 46 spans, every one machine-verified as an
exact substring of the paper it came from.

Two design points that make the result usable rather than anecdotal:

- **Queries were written and committed to disk before any cited paper was opened**, so no query
  is tuned to an answer it had already seen.
- **The output is spans, not verdicts.** A span turns every later retrieval measurement into
  string matching, with no judge in the loop.

| verdict | n |
|---|---|
| supported | 12 |
| partially supported | 5 |
| not supported | 1 |
| **contradicted** | **1** |

The contradiction is the case that justifies the exercise. The atlas paper states that dermal
fibroblast differentiation into papillary and reticular subsets occurs "early in mice (about
embryonic day 12.5)". The paper cited says the dermis **is homogeneous at E12.5**, and puts the
split at E16.5–E18.5. E12.5 is that paper's earliest cell-*labelling* timepoint, which is the
likely source of the conflation. Traversal reaches the right paper; quote validation passes;
the DOI exists. Nothing we run compares the claim to what the source says.

Four of the five partials share one shape — a compound or co-cited claim where the target
carries part of the load and the rest is unaccounted for. Three genes attributed to two
references, of which the read target supports one and never mentions the other two. "Migration
and invasion", where migration is the target's central finding and "invasion" never appears.
"Inflammation and IL-6", where the antifibrotic effect is the target's thesis and IL-6 never
appears. Supported claims also transfer context silently and routinely: a signalling mechanism
from human liver regeneration, a migration result from a lung cancer cell line, both applied to
prenatal skin without qualification.

### Retrieving the evidence

With verified spans in hand, every retrieval question becomes mechanical. Four conditions, in
an order that lets a miss be attributed rather than guessed at:

| condition | what the searcher gets |
|---|---|
| ceiling | ASTA's entire indexed copy of the cited paper — is the passage there at all? |
| paper-scoped | search restricted to the one correct paper |
| reference-list | search restricted to the ~87 papers the atlas cites |
| whole index | search with no restriction |

**Is the passage there at all?** 24/46 spans exactly, 32/46 (70%) allowing for rendering
differences. This is the denominator; without it, "not returned" and "never indexed" are
indistinguishable.

**Given the right paper, does a query return the passage?**

| | of the 32 passages ASTA holds |
|---|---|
| paper-scoped, claim as query | 31/32 (97%) |
| paper-scoped, keyword query | 30/32 (94%) |
| reference-list, keyword query | 23/32 (72%) |
| reference-list, claim as query | 17/32 (53%) |

The paper-scoped result is not an artefact of the window: only 2 of 15 papers are small enough
that a 20-snippet request returns the whole copy, and excluding them it is 28/29 and 27/29.

**Does the correct paper come back at all?**

| search space | query form | in top 20 | ranked first |
|---|---|---|---|
| whole ASTA index | claim as query | 1/19 | — |
| whole ASTA index | keyword query | 6/19 | — |
| atlas reference list | claim as query | 18/19 | 11/19 |
| atlas reference list | keyword query | **19/19** | **15/19** |

**The design this implies is two hops.** Search the reference list to identify which cited
papers are relevant (19/19), then search inside each to extract the evidence (31/32). Free
search over the whole literature cannot do the first step, and reference-list search alone does
the second step badly.

Worth noting what this does *not* require: the citation link is not needed to *locate* an
answer — the reference list as a search space is enough. What the link buys is defining that
space, and, for verification, saying which paper the authors actually credited.

**Keyword reduction helps whenever the space is bigger than one paper** — 6 vs 1 over the whole
index, 19/19 vs 18/19 and first-ranked 15 vs 11 over the reference list, 23 vs 17 passages —
and is marginally worse once scoped to a single paper (27/29 vs 28/29). That is a clean rule for
query decomposition: decompose for any multi-paper hop, don't bother inside one paper.

---

## The three coverage problems, which are the real constraint

**Introductions are missing.** Of the 10 unretrievable passages in papers ASTA indexes *in
full*, five are introduction prose (plus one abstract), with similarity scores of 0.09–0.56 —
genuinely absent, not reworded. The same pattern was already known for the atlas paper itself,
where every genuinely-absent citing sentence was in the opening section. It now recurs across
several independent papers, so it is not a quirk of one publisher or one paper.

This lands squarely on the enrichment aim: **introduction citations are the ones most worth
following**, because that is where a paper points at the literature defining a cell type — and
introductions are exactly where coverage is weakest, at both ends of the hop.

**One paper in fifteen is held as title and abstract only.** It happens to carry the single
best-matched claim in the set: the atlas paper names three marker genes and three organs, and
all six appear in that paper, attached to precisely the population described. Through this
route it is entirely unreachable.

**Figure captions are lost twice over.** Both caption-sourced passages are absent from ASTA,
and our own text extraction drops captions as well. Evidence in a legend is currently
unreachable by either path. The extraction used for the gold set here was deliberately more
permissive than production so that this surfaced as a measurement instead of being defined
away.

**Renderings differ.** Eight passages match only approximately (0.90–0.97): split subscripts
(`Treg` → `T reg`), de-hyphenated line breaks (`cancer-related` → `cancerrelated`), dropped
characters. A quote taken from one source fails exact validation against the other. Our quote
check is exact-substring, so **which rendering a quote came from has to be recorded** — the
same conclusion three independent measurements have now reached.

---

## Working notes that cost real time

Every scoring defect found in this work biased the same way — making retrieval look worse than
it is. Assume the next scorer does too, and check deliberately rather than waiting to notice.

- **Matching per chunk instead of per document.** Chunks tile the paper with overlaps and gaps;
  a sentence straddling a boundary scores as absent. Reconstruct the document from the chunks'
  own offsets first.
- **Assuming where a citation marker sits.** Markers render as bare digits *inside* the
  sentence, before the full stop. A span ending at the last letter excludes its own citations;
  a guessed character tolerance cost six points until it was replaced by extending to the end
  of the sentence.
- **Treating DOI equality as paper identity.** It turned five correct preprint-vs-journal
  resolutions into "disagreements". Three-way matching (same identifier / same work / different)
  is what turned five disagreements into zero.
- **Matching papers by title.** The titles stored during collection were truncated at 60
  characters, making substring matching unsound in both directions. Match by identifier.
- **A threshold picked by eye.** The first cut misfiled two rendering artefacts as genuine
  rewordings. Thresholds are defensible only when they sit in an observed gap in the
  distribution — and the underlying ratios should be written out so the call stays auditable.

Two habits that paid: **derive the answer key from markup rather than from anything a model or
a search produced**, and **verify every quoted span is an exact substring before using it** —
that check caught a misquote of mine mid-run.

---

## What is still unmeasured

- **Enrichment itself.** Everything here measures whether a passage supporting a *citing
  sentence* can be found. Whether a followed paper adds cell-type information the atlas paper
  lacks is a different question needing cell-type-anchored items, drawn from introductions as
  well as results.
- **Closed-access papers.** 19 of 54 candidate targets could not be fetched, so the read gold is
  the open-access subset. There is no reason to assume their coverage looks like this.
- **Whether the synthesis step is where unsourced prose enters.** Reading has been ruled out as
  the source; an audit found 60% of one project's reports had unsourced sections; and this work
  shows miscitation survives every check we currently apply. Highest-value measurement still
  unrun.
- **Scale.** 19 claims, 15 papers, one atlas paper. Directionally strong, statistically thin.

---

## Reproducing this

```bash
uv run --active python experiments/citation_traversal/build_gold_from_citations.py   # claim -> cited paper pairs
uv run --active python experiments/citation_traversal/score_reference_resolution.py  # does traversal reach the right paper
uv run --active python experiments/citation_traversal/fetch_cited_papers.py          # fetch + extract the cited papers
uv run --active python experiments/citation_traversal/verify_gold_spans.py           # every span is an exact substring
uv run --active python experiments/citation_traversal/asta_retrieval.py              # ceiling / paper-scoped / whole-index
uv run --active python experiments/citation_traversal/asta_reference_list_search.py  # reference-list search
```

All API responses are cached under `experiments/citation_traversal/data/asta_responses/`, so
re-runs cost nothing and reproduce the numbers above exactly. Needs `ASTA_API_KEY` in `.env`
for a cold run.

Companion documents, if you want the detail behind a section:
`aims.md` (the two aims), `reaching_the_cited_paper.md`,
`do_cited_papers_support_the_claims.md`, `retrieving_the_evidence.md`,
`paper_availability.md` (how much of the citation corpus is readable, and by which route).
