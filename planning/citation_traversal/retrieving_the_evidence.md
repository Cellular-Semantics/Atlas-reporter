# Stage 3c: ASTA citation traversal, scored against the Stage 3b gold spans

**Run 2026-08-28/29, branch `test/retrieval-matrix`.** Scripts
`experiments/citation_traversal/asta_retrieval.py` and `experiments/citation_traversal/asta_reference_list_search.py`; data
`experiments/citation_traversal/data/asta_{ceiling,scoped,corpus,shotgun}.json`, raw responses cached under
`experiments/citation_traversal/data/asta_responses/`. 19 claims, 15 target papers, 46 gold spans. Scored by
`norm_loc` substring against verified spans — no judge, no model call.

Four arms, ordered so a miss can be attributed rather than guessed at:

| arm | question |
|---|---|
| `ceiling` | is the gold span in ASTA's indexed copy of the target *at all*? |
| `scoped` | with `paper_ids` set to the target, does a query return it? |
| `corpus` | with **no paper filter at all** (the whole ASTA index), does the target come back? |
| `shotgun` | restricted to the **87 papers Gopee cites**, does the target come back, and does the span? |

The `shotgun` arm is `experiments/citation_traversal/asta_reference_list_search.py`, added after the first three: the
`corpus` arm searches all of ASTA, which is not the condition originally proposed. The
shotgun proper takes the atlas paper's reference list as the search space. The restricted set
is the 89 CorpusIds ASTA resolved from Gopee's refMentions (87 distinct DOIs); all 15 target
papers are inside it, so a miss there is retrieval, not set definition.

## Headline

**Within a paper, coverage is the binding constraint and ranking is not.** (The shotgun arm
below adds a second, separate constraint: snippet budget spread across papers.)

| | strict | lenient |
|---|---|---|
| gold spans present in ASTA's copy (ceiling) | 24/46 (52%) | 32/46 (70%) |
| returned by a scoped `claim_query` | 23/46 | 31/46 |
| returned by a scoped `decomposed_query` | 22/46 | 30/46 |
| **scoped recall among spans ASTA actually holds** | — | **31/32 (97%) / 30/32 (94%)** |

Per claim, every one of the 16 claims with any reachable span had one returned, by both
query forms. Excluding the 2 papers small enough that a 20-snippet window returns the whole
copy, recall is 28/29 and 27/29 — so the result is not an artefact of the window.

**Free search over all of ASTA fails. Restricting to the reference list nearly always works.**

| search space | query form | target paper in top-20 | at rank 1 |
|---|---|---|---|
| whole ASTA index | claim-verbatim | 1/19 | — |
| whole ASTA index | decomposed | 6/19 | — |
| Gopee's 87 cited papers | claim-verbatim | 18/19 | 11/19 |
| Gopee's 87 cited papers | decomposed | **19/19** | **15/19** |

Papers matched by CorpusId→DOI, not by title (the titles in `claims.json` are EuropePMC
strings truncated at 60 characters, so title substring matching was unsound in both
directions; the numbers are identical under both, but only the identifier version is
defensible).

But the shotgun's *span* recall is much worse than the paper-scoped arm's, because a
20-snippet budget spread over ~5 papers leaves ~4 snippets each:

| | spans returned, of the 32 ASTA holds |
|---|---|
| shotgun, claim-verbatim | 17/32 |
| shotgun, decomposed | 23/32 |
| paper-scoped, claim-verbatim | 31/32 |
| paper-scoped, decomposed | 30/32 |

## What this means for traversal

**The natural design is two hops, and both are cheap.** Restricting search to the atlas
paper's reference list identifies the right cited paper essentially always (19/19, rank 1 for
15 of them). Then a paper-scoped search inside it returns the supporting passage 97% of the
time it exists. Neither hop alone is sufficient: free corpus search cannot find the paper
(1–6/19), and the shotgun alone finds the paper but returns the specific evidence only
17–23/32 of the time. Chaining them — decomposed shotgun to pick the paper (19/19), then a
paper-scoped search inside it (31/32) — should recover essentially all of the ~70% of
supporting evidence ASTA holds. That chain is not itself measured here; it is the composition
of two arms that were.

Note what this does *not* need: the citation link is not required to *locate* the answer —
the reference list as a search space is enough to identify which cited paper is relevant. The
citation link's value is in defining that search space (and, for Aim 1, in saying which paper
the author actually credited).

**Decomposed queries win whenever the space is bigger than one paper.** 6/19 vs 1/19 over all
of ASTA; 19/19 vs 18/19 and rank-1 15 vs 11 over the reference list; 23 vs 17 spans in the
shotgun. Paper-scoped they are marginally worse (27/29 vs 28/29). Clean result for
`query-decomposer`: decompose for any multi-paper hop, don't bother once scoped to one paper.

## Where the missing 30% goes — and why it collides with Aim 2

Of 14 unreachable spans:

- **4 are in a paper ASTA holds as title+abstract only** — the yolk sac atlas
  (`10.1126/science.add7564`, *Science* 2023, 4 chunks). That paper carries the single
  best-matched claim in the whole Stage 3b set: all three genes Gopee names (P2RY12, CX3CR1,
  OLFML3) and all three organs (brain, skin, gonads). Via ASTA it is entirely unreachable.
- **10 are in papers ASTA indexes in full.** By location: **5 Introduction prose**, 2 figure
  captions, 1 Abstract, 2 Results. Ratios are mostly 0.09–0.56, i.e. genuinely absent, not a
  rendering difference.

**The introduction pattern generalises.** Earlier work found ASTA's copy of Gopee
missing its opening paragraphs (all 5 genuinely-absent citing sentences were in the opening section). It now recurs
across multiple independent papers. This closes the handoff's open question — it is not a
Gopee quirk.

That matters directly for **Aim 2** (`aims.md`): introduction
citations are the ones most worth following, because that is where an atlas paper points at
the literature defining a cell type. It is also where ASTA's coverage is weakest, at both
ends — the citing paper's intro and the cited paper's intro.

**Figure captions are lost twice over.** Both caption spans are absent from ASTA, and our own
`corpus.py` / `local_snippet_index` drop captions too. Evidence in a legend is currently
unreachable by either route.

## Rendering, again

8 spans are present only under lenient matching (ratios 0.90–0.97). ASTA serves a different
rendering of the same sentence, so a quote lifted from PMC JATS fails exact validation
against ASTA text and vice versa. This is the third independent measurement of the same
thing and it keeps mattering: `check_quotes` is exact-substring, so the route a quote came
from has to be recorded. (Handoff §5, still unimplemented.)

## Caveats

- 15 papers, 46 spans. Small, and the papers are the OA subset that could be fetched — the 19
  access-restricted targets are absent from the gold, and there is no reason to think their
  ASTA coverage matches.
- The scoped arm assumes traversal already arrived at the correct paper. Two separate
  measurements say that assumption is cheap: the reference-resolution measurement found ASTA makes
  0 disagreements in 174, and the shotgun arm reaches the right paper 19/19 from the
  reference list alone.
- The shotgun's search space is ASTA's resolution of Gopee's refMentions (87 of 109
  references). The ~20 references ASTA could not resolve are silently outside it — for these
  claims it did not matter, since all 15 targets were inside, but a production shotgun would
  inherit that gap.
- Gold spans mark passages that *support* a claim (Aim 1). Aim 2 — whether a followed paper
  adds cell-type information the atlas paper lacks — is not measured here and needs its own
  item set.
