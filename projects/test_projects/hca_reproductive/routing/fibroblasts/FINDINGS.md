# Routing comparison: opus vs sonnet vs read-everything

**Run date:** 2026-09-22. Routing only — no reports were generated, and no
paper was read. Every finding below is a property of the *plans*, not of any
actual reading. Kept so it can be checked against real runs once the subatlas
reader lands.

Selection: the 37 fibroblast cell sets described in `README.md`.
Table: `routing_table.json` (74 questions, 8 readable papers, floor 50 cells).

## The three versions

| | read-everything | opus | sonnet |
|---|---|---|---|
| papers read | 8 | 8 | 8 |
| questions | 74 | 45 | 44 |
| cell sets served | 27 | 27 | 26 |
| `atlas_only` | 10 | 10 | 11 |
| `not_reading` | 1 | 1 | 1 |
| tokens | 0 | 79,826 | 47,806 |
| tool calls | — | 9 | 3 |
| wall clock | — | 5m44s | 5m29s |

Plans: `routing_plan.json` (opus), `routing_plan.sonnet.json` (sonnet).
`routing_table.json` and `selection.json` are gitignored as generated output —
regenerate them per `README.md` before re-running the numbers below.
Re-run the diff with `python3 compare_plans.py routing_plan.json routing_plan.sonnet.json opus sonnet`.

## Finding 1 — the models select no papers

Both plans read all 8 readable papers. Neither skipped one; the single
`not_reading` entry (`celltype_OvarySanger2026`) is there because it has no
DOI, which is a fact from the table, not a judgement.

**So at the paper level the counting already gave the answer.** If the
question is only "which papers must be assessed", `cli_route` answers it and
the subagent adds nothing. This may be specific to this selection — 37 cell
sets spanning the whole atlas will pull in most contributors. A narrower
selection is where paper-level pruning could start to happen, and that is
worth re-testing rather than assuming.

## Finding 2 — question pruning is principled but may not be worth having

Both models cut ~40% of questions, and the cut separates cleanly:

| | kept | pruned |
|---|---|---|
| median contribution share | 0.66 | 0.02 |
| median label share | 0.85 | 0.05 |
| median overlap cells | ~6,000 | ~280 |

Neither pruned either of the 2 synonym-asserted rows — the check that would
have caught careless pruning. They agree on 71 of 74 questions (both keep 43,
both prune 28; 3 disagreements).

**But pruning saves no paper fetch.** Per the agent spec, reading a paper once
about one of its labels answers for every cell set under it — so all 8 papers
are read either way, and dropping a question only narrows what is asked of a
paper already open. The saving is therefore small, while the risk is real:
sonnet's extra cut lost a cell set (below). On this evidence pruning is
justified on focus/quality, not cost, and that justification is untested.

**Open question for the real run:** does a long question list actually degrade
a read, or does the reader handle spillover rows fine? If the latter, the
pruning step is doing harm for no gain and the plan should keep more. Measure
this when the reader lands — compare a read driven by the 45-question plan
against one driven by all 74.

## Finding 3 — the coverage difference is where the models genuinely differ

Opus pruned 29 questions with no coverage loss: 27 cell sets served, same as
reading everything. Sonnet's 30 cuts lost one — `Mesen_UterotubalJunctionFibs`
moves from served to `atlas_only`.

The disputed row: Weigert's generic `stromal cell`, 64 cells, contribution 1.0,
43% of the atlas cell set, but 0.13% of the label. Sonnet judged a generic
label at 64 cells to say nothing; opus kept it. The agent spec leans toward
opus — a coarse label still earns one pass to establish the source did not make
the distinction — but this is genuinely arguable, and sonnet flagged it for
review rather than burying it.

**Check against the real run:** read Weigert for `stromal cell` and see whether
it yields anything about the uterotubal junction. That settles the call
empirically and tells us which model's instinct to trust on this class of row.

## Finding 4 — accuracy and flagging went to sonnet

- Opus misstated the `Fibroblast_basalis` overlap as "~45 cells"; it is **30**.
  The spec tells it not to restate numbers at all, so this is a double miss.
  Low impact, but note the failure mode: a restated number in a `reason` can be
  wrong while the plan itself is correct.
- Opus marked 3 papers `from_background_knowledge`, sonnet 2. The gap is
  Ulrich 2022. Sonnet's non-flagging is arguably the better call — the
  myofibroblast/stromal-cell naming disagreement is visible in the table's own
  label strings, so it is table-derived, not background knowledge. Opus flagged
  it because it ranked on what a contractile phenotype would imply.
- Sonnet wrote fuller reasons (mean 1,004 vs 791 chars) at 60% of the tokens.

## Finding 5 — the ordering call that favours opus

Middle-of-ranking shuffle: Garcia-Alonso 2021 at #3 (opus) vs #5 (sonnet);
HECA #4/#3; Weigert #6/#4; Ulrich 2024 #5/#6. Lorenzi #1, GA2022 #2,
Ulrich 2022 #7, Lardenois #8 in both.

The substantive one is Garcia-Alonso 2021. `Fibroblast C7` → `Mesen_AdvFibsIntr`
is contribution 0.89 **and** label share 0.81 — the one-population-two-names
signature — while Ulrich 2024's `C7-Fibroblast` synonym on the same cell set is
0.37 / 0.74. GA2021 looks like the origin paper, so reading it before the
papers that cite it is the better sequence. Both models saw the paper mattered;
only opus ordered on it.

**Check against the real run:** whether reading GA2021 first actually changes
what the later reads produce. If order turns out not to matter — because each
read is independent — this advantage evaporates and the models are near
equivalent.

## Findings all three versions share

Worth recording because these came out of the table and survived every
version, so they are the robust part:

- `celltype_OvarySanger2026` has no DOI: 179,450 cells across 21 of the 37 cell
  sets, and the sole contributor to six adult ovarian cell sets totalling over
  206,000 cells (incl. `Mesen_OvarianFibs_InncorMedulla`, 125,985). Those
  reports will rest on the atlas paper alone and must say so. **This is the
  largest single limitation on the fibroblast reports and no routing choice
  can work around it.**
- `Mesenchymal_GATA2` (GA2022) reaches 11 cell sets at very high contribution
  to each while no cell set holds much of the label — one coarse category where
  the atlas has eleven regions. Expect a useful negative.
- The adventitial PI16-high/low split and the uterotubal junction are
  atlas-level cuts with no upstream label behind them.
- Ulrich 2022 calls `Mesen_FallopianFibs` cells `myofibroblast cell` where
  Weigert calls them `stromal cell`. A contractile phenotype would change how
  the cell set is described.
- Adult/fetal asymmetry: fetal cervix and upper vagina are well served, while
  adult `Mesen_CervixFibs` and `Mesen_VaginaFibs` have no provenance at all.
- `Mesen_UGSLig` is served only by Lorenzi's `Urogenital Sinus Lig` at ~3% of
  the cell set. Kept by both, marked thin by both.

## Caveats on this comparison

- **n=1.** One selection, one atlas, one table. Nothing here establishes a
  general opus-vs-sonnet result.
- **The agent is pinned to `model: opus`.** The sonnet run was a deliberate
  override, not the configured behaviour.
- **No paper was read.** Every "better" judgement above is about which plan
  looks better reasoned, not which produced better reports. That is exactly
  what the real run will settle.

## Recommendation as of this run

Keep `model: opus` pinned, on Finding 3 (coverage) and Finding 5 (ordering).
The margin is narrow — one cell set and one ordering call — and sonnet was more
accurate on numbers, flagged more honestly, and cost 40% less. If cost becomes
a constraint, sonnet is a reasonable fallback. Revisit once Findings 2, 3 and 5
have been checked against real reads.
