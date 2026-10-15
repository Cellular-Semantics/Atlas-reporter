# Fibroblast routing run

**Request:** "Reports on all the fibroblasts in test_projects/hca_reproductive."
Routing only — no reports were generated in this run.

## What the request resolved to

37 cell sets, 1,117,965 cells (`selection.json`).

Three L2 populations are fibroblasts, and the selection is the leaves of their
subtrees:

- Stromal-interstitial fibroblasts (1,029,469)
- Adventitial fibroblasts (55,206)
- Ligament fibroblast (33,290)

## Judgements made in selecting

- **Excluded** the other mesenchymal L2 populations: Pericytes, Perivascular,
  Smooth muscles, Vascular smooth muscles, Smooth muscle cell, Theca. Theca is
  the arguable one — thecal cells are ovarian-stromal in origin, but this atlas
  files them separately.
- **Included on subtree rather than on text**: `Mesen_OvarianFibs_Medulla_SMCsLike`
  ("Ovarian stroma of the medulla SMCs-like", 13,705) sits under Ovarian stroma
  despite naming smooth muscle. A text match would have dropped it.
- **Leaves only** — parent nodes are not separately reported.
- **States collapsed** (user's decision): the eleven menstrual-phase and cycling
  states of Endometrial functionalis stroma — proliferative, early/mid/late
  secretory, menstrual eutopic, menstrual effluent, postmenopause, the three
  nEMC sets, and the two `_Cyc` sets — are replaced by their L3 parent
  `Endometrial functionalis stroma` (508,382). Treated as states of one cell
  type, not as twelve cell types. Without this collapse the selection is 47.
- **Fetal included**: 19 of the 37 are fetal cell sets. Not separately
  confirmed by the user; drop them if adult-only was meant.

## Files

- `FINDINGS.md` — comparison of the opus plan, a sonnet plan and a
  read-everything baseline, with the open questions to check once the
  subatlas reader lands. **Start here.**
- `compare_plans.py` — re-runnable structural diff of two plans
- `routing_plan.sonnet.json` — a sonnet-model plan, kept for comparison only
  (the agent is pinned to opus; this was an override)
- `selection.json` — the 37 cell sets with accessions and cell counts
- `routing_table.json` — counted provenance, from `cli_route` (74 questions
  across 8 papers; 10 cell sets atlas-paper-only). Counting only, no judgement.
- `routing_plan.json` — the routing judgement, from the `route-subatlas-papers`
  subagent: which contributing papers to read, in what order, which of their
  labels to ask about.

## Not committed

`routing_table.json` and `selection.json` are gitignored as generated output
(`.gitignore`: test projects commit setup only). Both regenerate from
`cas.json` — the accessions below are the only input not otherwise recorded,
so the rebuild works from this file alone.

<details><summary>The 37 accessions</summary>

```
  HCArepro:L3:0033     L3  Mesen_OvarianInclFibs                     96
  HCArepro:L3:0044     L3  Mesen_GonadalFibs_Undiff               26055
  HCArepro:L3:0105     L3  Endometrial functionalis stroma       508382
  HCArepro:L3:0162     L3  Mesen_UGSLig                            2661
  HCArepro:L3:0185     L3  Mesen_OvarianFibs_AdvLike                507
  HCArepro:L3:0192     L3  Mesen_UterotubalJunctionFibs             150
  HCArepro:L3:0288     L3  Mesen_EndoGlandBas                       535
  HCArepro:L3:m003     L3  Mesen_AdvFibs                             19
  HCArepro:L4:0007     L4  Mesen_VaginaFibs_Upper_Fetal            7925
  HCArepro:L4:0016     L4  Mesen_CorpusSpongiosumFib_Fetal        10169
  HCArepro:L4:0020     L4  Mesen_OvarianFibs_Medulla_SMCsLike     13705
  HCArepro:L4:0057     L4  Mesen_GlansFib_Fetal                    5416
  HCArepro:L4:0060     L4  Mesen_AdvFibs_PI16low                  18360
  HCArepro:L4:0071     L4  Mesen_OvarianFibs_InncorMedulla       125985
  HCArepro:L4:0085     L4  Mesen_LabiaFib_Fetal                    1794
  HCArepro:L4:0116     L4  Mesen_EpoophronFib_Fetal               13877
  HCArepro:L4:0120     L4  Mesen_CorpusCavernosumFib_Fetal         9472
  HCArepro:L4:0139     L4  Mesen_OvarianFibs_Outcor               21434
  HCArepro:L4:0153     L4  Mesen_MesonephricFibs_Fetal            28521
  HCArepro:L4:0157     L4  Mesen_UGSFib_Lower                      6277
  HCArepro:L4:0183     L4  Mesen_FallopianLig_Fetal               18265
  HCArepro:L4:0209     L4  Mesen_UterusLig_Fetal                  12364
  HCArepro:L4:0210     L4  Mesen_UGSFib_Upper                     11402
  HCArepro:L4:0215     L4  Mesen_FallopianFib_Fetal               41092
  HCArepro:L4:0217     L4  Mesen_CervixFib_Fetal                  11916
  HCArepro:L4:0220     L4  Mesen_AdvFibs_PI16hi                    3032
  HCArepro:L4:0223     L4  Mesen_MullerianFib                      2471
  HCArepro:L4:0240     L4  Mesen_OvarianFibs_Fetal                32133
  HCArepro:L4:0286     L4  Mesen_OvarianFibs_Perifol              44411
  HCArepro:L4:0287     L4  Mesen_VaginaFib_Lower_Fetal              645
  HCArepro:L4:0291     L4  Mesen_Prepuce_Fetal                     2243
  HCArepro:L4:0294     L4  Mesen_UterusFibs_Fetal                 29462
  HCArepro:L4:0296     L4  Mesen_LabioScrotalSwelling_Fetal        6830
  HCArepro:L4:0298     L4  Mesen_AdvFibsIntr                      33795
  HCArepro:L4:m000     L4  Mesen_VaginaFibs                        1463
  HCArepro:L4:m010     L4  Mesen_FallopianFibs                    64649
  HCArepro:L4:m011     L4  Mesen_CervixFibs                         452
```
</details>

## Rebuild

From the accession list above (or from `selection.json` if you still have it):

```bash
uv run python -m atlas_chat.cli_route \
  --cas projects/test_projects/hca_reproductive/cas.json \
  --accession HCArepro:L4:0217 --accession HCArepro:L4:m011 ... \
  --out projects/test_projects/hca_reproductive/routing/fibroblasts/routing_table.json
```

`cli_route` takes `--accession` repeatably; pass all 37. Note that shell
expansion of a long generated argument list is unreliable here — build the
argv in Python (`subprocess.run`) rather than via `xargs`.
