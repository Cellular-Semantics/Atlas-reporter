# Stage 3, checkpoints 1–3: does ASTA traversal get back to the paper the author cited?

**Run 2026-08-27, branch `test/retrieval-matrix`.** Scored mechanically — no judge, no
model reads anything. The answer key is Gopee's own `<xref>` markup and `ref-list`, so
no retrieval method had a hand in choosing the items or their targets.

Scripts: `experiments/citation_traversal/build_gold_from_citations.py`, `experiments/citation_traversal/score_reference_resolution.py`.
Data: `experiments/citation_traversal/data/{claim_reference_pairs,asta_copy_of_atlas_paper,reference_resolution_scores,refmention_audit,corpus_id_dois}.json`.

## The test set

`services._jats_parser.parse_jats_citations` over `experiments/papers/gopee2024.xml`
yields **134 cited sentences and 187 (sentence, reference) pairs** from 109 references,
**175 of them with a target resolvable to a DOI or PMID** across 97 distinct papers.
The 12 unscorable rows are book chapters and web resources with no identifier.

This is free gold: it costs one local parse, and it is method-independent by
construction, which is what Stage 2's rule 7 asks for.

## Results

ASTA's whole indexed copy of Gopee is 72 chunks — 1 title, 1 abstract, 70 body — one
`snippet_search` call with an over-large `limit`.

| checkpoint | conditional | overall |
|---|---|---|
| sentence is an exact substring of ASTA's copy | — | **154/175 (88%)** |
| sentence is present in *some* rendering | — | **162/175 (93%)** |
| ASTA marks a citation inside it and resolves it | 142/154 (92%) | 142/175 (81%) |
| that resolution names the work the ref-list names | 138/142 (97%) | 138/175 (79%) |
| …with an identical DOI/PMID | 133/138 (96%) | 133/175 (76%) |

Independent per-refMention audit, which does not depend on sentence matching at all
(ASTA renders citation markers as bare digits, so the marker *is* the reference number):

| verdict | count |
|---|---|
| agree with Gopee's ref-list | 150/174 (86%) |
| agree, but a different record of the same work | 5/174 (3%) |
| ASTA could not resolve the marker | 18/174 (10%) |
| marker not parseable to one number | 1/174 (1%) |
| **disagree** | **0** |

## What this says

**ASTA's reference resolution is not the weak link.** Zero disagreements in 174
refMentions. Where ASTA resolves a citation, it resolves it correctly. Its failure mode
is silence (10% unresolved), not error — the same shape as the reading result in Stage 2,
where absence was reported reliably and fabrication was near-absent.

**Following a CorpusId can land on a different record of the same work.** Five
refMentions resolve to the bioRxiv preprint (e.g. `10.1101/750042`) where Gopee's
ref-list prints the journal version (`10.1016/j.stem.2020.01.012`); one pair is two
records of *The Human Transcription Factors*. Traversal reaches the right paper and
reports a DOI the citing paper never printed. This is a catalogue/dedup problem, and it
is a live pipeline bug, not a test artefact: the report's References section takes DOIs
from the paper catalogue.

**Every annotation and resolution failure is under-annotation, never mis-annotation.** All 12 unannotated-sentence cases
failures are single-citation sentences: 6 where ASTA marked the citation but could not
resolve it, 6 where it placed no refMention at all. All 4 outright resolution misses are
multi-citation sentences where ASTA annotated some siblings and skipped the target
(CR8 in a 4-citation sentence, CR32 in a 3-citation sentence). So a targeted traversal
asked to follow a *specific* citation will sometimes find nothing to follow — it will
not be sent somewhere wrong.

**The exact/approximate gap is a quote-validation ceiling, not a reach ceiling.** Of
the 21 exact-match failures: 8 are rendering differences, 8 are genuine rewordings, 5 are
genuinely absent. The rendering cases are PDF-extraction artefacts in ASTA's copy —
`Treg` → `T reg` (split subscript), `cancer-related` → `cancerrelated` (de-hyphenated
line break), and one dropped character (`was` → `as`). The content is there and
retrievable; it cannot be quoted, because `check_quotes` does exact substring matching.
**This is direct evidence for the handoff's "record which rendering a quote came from"
fix** — 8 of 21 apparent absences are a rendering mismatch between two copies of the
same sentence.

**The rewordings mean ASTA serves a different version of Gopee, not only a lossy one.**
`Datasets of adult HF[11], adult healthy skin[10] and hair-bearing SkO[1] were
integrated…` appears in ASTA as `and published single cell datasets of adult skin and of
a hair bearing SkO model derived…`. Different sentence, same claim. Stage 1 recorded
this for Suo; it holds for Gopee too.

**The 5 genuine absences are all in the introduction.** Four in `Main`, one in
`Scarless healing`. One of them is `However, immune cells such as macrophages seed the
skin as early as 6 PCW…` — **the exact sentence behind the Stage 2 A3 substitution**,
where a reader given an 8k ASTA window produced a sourced, quote-backed wrong answer
because the paragraph holding 6 PCW is not in ASTA's copy. The two findings are now
tied together mechanically.

## Harness bias found and corrected

Four defects, all in the same direction — making ASTA look worse — consistent with the
handoff's warning that the harness fails closed. Recorded so the next scorer is checked
the same way.

1. **Per-chunk matching.** ASTA's 72 chunks tile a 99,140-char body with 36 overlaps and
   33 gaps, each carrying an exact document offset. A sentence straddling a boundary
   scored as absent. Fixed by reconstructing the document at ASTA's own coordinates
   (zero overlap conflicts, so the reconstruction is sound) and lifting refMention and
   sentence spans into that space. Gaps are filled with a sentinel that cannot match.
2. **Citation markers sit outside the claim span.** ASTA renders superscripts as bare
   digits before the full stop (`adult HFs 11 .`), so a span ending at the claim's last
   letter excludes its own citations. A guessed `+3`-character tolerance cost the annotation step six
   points; extending to the end of ASTA's own sentence span is correct and principled.
3. **DOI equality as the definition of "same paper."** Called all five
   preprint-vs-journal cases resolution errors. Now three-way (`exact_id` /
   `same_work` / `different`), which is what turned "5 disagreements" into "0".
4. **A fuzzy threshold tuned by eye.** The first 0.95 rendering cut misfiled two
   rendering artefacts as rewordings. 0.90 and 0.60 both sit in gaps in the observed
   ratio distribution (renderings ≥0.94, rewordings 0.61–0.83, absences ≤0.55), so the
   distribution does the classifying, not the thresholds — and every failure's ratio is
   written out so the call stays auditable.

## Incidental

`CLAUDE.md` tool rule 3 says CorpusId is not available from `get_paper` fields. It is —
`fields=externalIds` returns `CorpusId` alongside `DOI` and `PubMed`, which is how the resolution check
resolves 89 CorpusIds to DOIs here. Worth correcting on `dev`.

## What checkpoints 1–3 do not answer

Whether the cited paper actually supports the claim. That is a relevance judgement, so
it needs a judge, and it is close enough to the traversal task itself that using it as a
checkpoint would be circular. It belongs with the sufficiency/recall question the
frontier corpus sweep was proposed for.
