# Two aims for citation traversal (and a third use for the first)

Written 2026-08-28 after the Stage 3b sufficiency read, which made the distinction obvious:
the same traversal machinery serves two different goals, and they need different gold and
different scoring.

## Aim 1 — verification: does the cited paper support the assertion?

For a sentence in the atlas paper carrying a citation, does the cited paper support,
partially support, contradict, or say nothing about the attributed proposition?

- **Gold**: the atlas paper's own `<xref>` markup gives the target for free; sufficiency has
  to be adjudicated by reading the target (`do_cited_papers_support_the_claims.md`).
- **Measure**: attributability. Can a claim be tied to a source that actually makes it.
- **Status**: 19 claims adjudicated. 12 supported, 5 partial, 1 not supported, 1 contradicted.
  All 19 pass our current `check_quotes` + DOI validation, including the contradicted one.

**Not the primary aim of atlas-reporter**, but worth folding into report generation later:
after a report asserts a property of a cell type on the atlas paper's authority, ask
explicitly whether the atlas paper's own cited sources back that assertion or contradict it.
The Driskell E12.5 case shows the failure is real and silent.

## Aim 2 — enrichment: can we learn more about a cell type than the atlas paper says?

**This is the primary aim.** Given a cell type annotated in the atlas, follow citations in
sentences that mention it and gather information about it that is not in the atlas paper.

- **Gold is different.** Not "does the target support the citing sentence" but "does the
  target contain information about this cell type beyond what the atlas paper states". A
  citation can be perfectly attributable and add nothing, or add a great deal while
  supporting the sentence only loosely.
- **Introduction citations matter as much as results citations.** Stage 3b deliberately kept
  only results/discussion sentences, because Methods citations are tool and dataset pointers.
  For Aim 2 that filter is wrong in the other direction: intro sentences are where the atlas
  paper points at the prior literature defining a cell type, and they are exactly the
  citations worth following. (Note the intro is also where ASTA's copy of Gopee is missing
  text — the genuinely-absent citing sentences were all in the opening section.)
- **Measure**: yield and non-redundancy — how much cell-type-relevant content the followed
  papers add over the atlas paper alone — plus attributability of each retrieved statement.

## Consequence for the test set

The Stage 3b span set scores Aim 1. It is reusable for Aim 2 only as a retrieval probe
(can ASTA find a passage we know exists in a paper we know is cited). A proper Aim 2 gold
needs cell-type-anchored items, drawn from intro as well as results sentences, scored on
what the followed paper adds rather than on whether it agrees.
