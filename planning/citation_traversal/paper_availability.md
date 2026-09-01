# How much of the atlas paper's citation corpus can we actually read?

**August 2026, branch `test/retrieval-matrix`.** All 109 references in Gopee et al. 2024,
tested against both access routes. Script
`experiments/citation_traversal/survey_paper_availability.py`; data
`experiments/citation_traversal/data/paper_availability.json`; every response cached under
`data/availability_cache/`.

Both routes were tested **by actually retrieving the text**, not by reading availability
flags. That distinction is most of the finding.

---

## Headline

| | of 109 references |
|---|---|
| found in EuropePMC | 100 (92%) |
| has a PMCID | 70 (64%) |
| **labelled open access** | 42 (39%) |
| **JATS full text actually retrieved** | **38 (35%)** |
| identifier resolves to an ASTA record | 97 (89%) |
| **ASTA holds body text** (full or partial) | **56 (51%)** |
| **readable by at least one route** | **57 (52%)** |

**Flags overstate access.** 70 references have a PMCID and 42 are labelled open access, but
only 38 yielded a parseable JATS body — 32 of the 70 returned HTTP errors. Anything that
plans a fetch from `isOpenAccess` or `inEPMC` will over-promise by roughly a third.

**ASTA is the broader route, and PMC is almost a subset of it.**

| | n | % |
|---|---|---|
| both routes | 37 | 34% |
| PMC full text only | **1** | 1% |
| ASTA body only | 19 | 17% |
| **neither** | **52** | **48%** |

Of the 38 papers whose JATS we can fetch, 37 are also in ASTA. PMC adds exactly **one** paper
that ASTA lacks. On coverage alone the ordering is not close: ASTA 56, PMC 38.

---

## What this means for a waterfall

**Coverage does not decide the order; text quality does.** ASTA reaches more papers, but the
retrieval work on this branch established what its copy is missing, repeatedly and across
independent papers:

- **introductions are frequently absent** — and introduction citations are the ones most worth
  following, because that is where a paper points at the literature defining a cell type;
- **figure captions are absent**, and evidence does live in legends;
- **it serves a different rendering** of the same sentences (split subscripts, de-hyphenated
  line breaks, dropped characters), which breaks exact-substring quote validation;
- one paper in fifteen was held as **title and abstract only**.

PMC JATS has none of those problems: it is the complete article including captions and tables,
in the rendering our quote checks assume.

So the sensible order is **PMC first for the 38 where it works, ASTA for the 19 it adds, and a
third route for the remaining 52** — accepting that the first rung is narrow. The cost of
getting this backwards is not missing papers, it is silently degraded evidence on papers we
could have read properly.

**A third rung is needed for nearly half the corpus.** Of the 52 unreachable: 24 have no PMCID
at all, 16 have a PMCID but the fetch fails, 14 are abstract-only in ASTA, and 24 are unindexed
by ASTA. **14 carry a PDF flag in EuropePMC**, which is the obvious next thing to test and has
never been measured here.

**Which identifier you resolve does not matter.** Resolving a reference through ASTA's own
citation annotation versus through the reference-list DOI picks the **same record 85/88 (97%)**
of the time, and the refMention route rescues nothing the DOI route misses. No need to
complicate the design with record selection.

**Coverage does not track prominence.** cell2location — a heavily cited methods paper — is
unindexed by ASTA under both resolution routes, as is the Cell Stem Cell mouse skin atlas.
Absence cannot be predicted from how well known a paper is; it has to be probed.

---

## Confidence in these numbers

The ASTA half of this survey was **wrong on first run and is corrected here.**
`get_paper_batch` silently drops identifiers it cannot resolve and returns a shorter list with
no placeholder (verified: 3 ids in, 2 rows out). The original code paired requests to responses
by position, so from the first unresolvable identifier onward every reference was assigned
another reference's paper, and the wrong papers were probed. A second attempt over-corrected by
lowercasing `DOI:` to `doi:` in the matching key, resolving 2 of 109.

Both call sites now match responses to requests by identifier, and the request/response counts
are printed so a silent drop cannot recur unnoticed.

The corrected mapping was validated against an independent measurement: 15 of these papers had
their ASTA indexing band determined separately during the retrieval experiment, and the survey
**agrees with all 15**.

The same latent defect existed in the reference-resolution scorer. It was re-run with the fix
and a cleared cache and produced identical numbers, because its inputs were CorpusIds emitted
by ASTA itself, which all resolve. Nothing else on this branch is affected.

Worth recording: this is the first scoring defect on this branch that did **not** fail
conservatively. The others all made retrieval look worse than it was. This one misassigned
results in an arbitrary direction, which is much harder to spot — it surfaced only because two
verdicts looked implausible for papers I happened to recognise.

## Caveats

- One atlas paper's reference list. A different field or a different journal will differ.
- The PDF route (14 candidates) is unmeasured.
- "ASTA holds body text" counts FULL and PARTIAL together; the retrieval work shows even FULL
  copies are missing introductions and captions, so this is an upper bound on usable text.
