# Stage 3b: do the cited papers actually support the claims? (19 claims, frontier read)

**Run 2026-08-28, branch `test/retrieval-matrix`.** A frontier model (this session, Opus 5)
read all 15 cited papers in full and adjudicated each claim against them. Deliberately
small — the point is a span-grounded gold set, not a statistic.

Artefacts under `experiments/citation_traversal/data/`: `claims.json` (19 items), `queries.json` (written
before any target paper was opened), `cited_papers_text/*.md` (15 papers, permissive
extraction), `adjudications.json` (verdicts + verbatim spans),
`verify_gold_spans.py` (asserts every span is an exact substring).

## Why this had to come before any retrieval arm

The reference-resolution work established only that traversal arrives at the paper the author cited. Running ASTA
next would have measured a conjunction — query formulation × ASTA retrieval × ASTA index
coverage — with no way to separate "ASTA missed it" from "it was never there". Reading the
targets first gives the ceiling and, more importantly, a **verbatim supporting span** per
claim, which turns the eventual retrieval comparison into `norm_loc` substring matching:
no judge, same machinery as Stage 1/2.

**Order mattered.** All 19 queries (claim-verbatim and decomposed forms, plus an explicit
`attributed_proposition`) were written and committed to disk *before* any target paper was
opened, so no query is tuned to an answer.

## Results

| verdict | n |
|---|---|
| supported | 12 |
| partially supported | 5 |
| not supported | 1 |
| **contradicted** | **1** |

By citation kind: both dataset citations supported; the one method citation partial;
of 16 biological claims, 10 supported, 4 partial, 1 not supported, 1 contradicted.

46 spans, all verified as exact substrings.

## The individual findings that matter

**One outright miscitation.** Gopee (`HF mesenchymal differentiation`) states that dermal
fibroblast differentiation into papillary and reticular subsets "has been reported to occur
early in mice (about embryonic day 12.5)". The cited paper (Driskell et al., *Nature* 2013)
says the dermis **is homogeneous at E12.5**, puts fate restriction at E16.5, and
papillary/reticular distinguishability at E18.5. E12.5 is that paper's earliest *labelling*
timepoint (Tamoxifen when all fibroblasts are Dlk1+), which is the likely source of the
conflation. This is the case that justifies the whole exercise: traversal would have
retrieved the right paper, and quote validation would have passed, because nothing in our
pipeline compares the claim to what the target says.

**One claim whose target contains none of its content.** Gopee cites a dermal endothelial
atlas for VWF being a GATA2/NFATC1 target involved in endothelial differentiation. VWF,
GATA2 and NFATC1 occur **zero** times in that paper.

**Four of five partials are compound or co-cited claims where the target carries some of
the load and the rest is unaccounted for:**

- APOE, IGFBP7, ITM2A attributed to refs 43+52 — ref 43 supports APOE only; IGFBP7 and ITM2A occur 0 times.
- "promote cell migration and invasion" (EFNB1) — migration is the target's central finding (34 mentions); invasion/invasive occur 0 times.
- "downregulation of inflammation and IL-6 confers anti-fibrogenic properties" — antifibrotic is the target's thesis; IL-6/IL6/interleukin-6 occur 0 times (its cytokine is IL-10).
- AGR2: loss promoting migration is well supported; "functions in assembly of cysteine-rich receptors enriched in HFs" is absent — cysteine, hair follicle and skin all occur 0 times in what is a lung/colorectal cancer cell-line study.

**Frequent, unflagged context transfer.** Supported claims are routinely supported *in a
different system*: GAS6/AXL immunosuppression from human liver regeneration; AGR2 migration
from A549 lung cancer cells; antifibrotic IL-6 framing from mouse xenografts. The claims are
defensible; the transfer is invisible in the citation.

**The best match in the set** is Gopee's TREM2+ yolk-sac macrophage sentence: all three genes
(P2RY12, CX3CR1, OLFML3) and all three organs (brain, skin, gonads) appear in the target,
attached to exactly that population.

## Two things this says about the pipeline, not the experiment

1. **Support is not attributability, and neither is quote validity.** Our `check_quotes` +
   DOI checks would pass every one of the 19 — including the contradicted one. Nothing in the
   pipeline asks whether the retrieved paper says what the citing sentence claims.
2. **2 of 46 gold spans sit in figure captions** (`[FIG]`), which `corpus.py` and
   `local_snippet_index` drop. Extraction here was deliberately permissive so this would
   surface as a measurement rather than being defined away. Any retrieval arm scored against
   these spans is capped below 46/46 by the chunker alone.

## Coverage and what it cost

Of the 175 rows whose sentence was found and whose citation resolved correctly, 83 sit in a results/discussion section (the rest are Methods tool and
dataset citations, which are not claims a paper can support or refute). Those 83 cover 56
distinct claims against 54 target papers; **19 of 54 targets failed to fetch** — `inEPMC=Y`
but access-restricted — leaving 19 rows / 18 distinct claims / 15 papers. The OA subset is
therefore what was read, and that is a selection effect on the gold, not a sample.

## Next

The span set is now usable as gold. The retrieval comparison that follows is mechanical:
issue each `claim_query` / `decomposed_query` against ASTA (and the local index), and check
by `norm_loc` whether the retrieved snippets contain the gold span. Two caveats to carry:
the 2 caption spans are unreachable by the current chunker, and 4 of 5 partials mean a
"retrieved the right paper" success can still be a claim the paper only half supports.

Unrun and worth more than a larger N here: the same treatment on the **synthesis** step.
Stage 2 ruled out the reading step as the source of unsourced prose; the fetal-skin audit
found 60% of reports had unsourced sections; this run shows miscitation survives every check
we currently apply.
