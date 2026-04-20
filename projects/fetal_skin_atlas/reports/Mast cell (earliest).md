# Mast cell (earliest)
Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis
Scope: fetal

## CL Mapping

| Field | Value |
|-------|-------|
| CL term | mast cell progenitor |
| CL ID | CL:0000831 |
| CL definition | A mast cell progenitor is a cell that is Kit-positive, FcεR-negative and has the potential to develop into a mature mast cell. |
| Match type | skos:broadMatch |
| Confidence | medium |

**Justification:** The 'Mast cell (earliest)' cluster represents the least differentiated mast cell stage annotated in the fetal skin atlas, corresponding to a cell that has committed to the mast cell lineage but has not yet acquired mature granule content or effector markers. CL:0000831 'mast cell progenitor' is the best available match, being Kit-positive and FcεR-negative — consistent with the pre-granule, early-committed stage. A broad match is used because the atlas annotation likely captures cells spanning the progenitor-to-immature mast cell transition.

## Summary

Mast cell (earliest) is the most immature transcriptional state within the mast cell maturation series identified in fetal human skin (7–17 PCW) by the Gopee et al. (2024) prenatal skin atlas. Mast cells in fetal skin arise from megakaryocyte-erythroid-mast cell progenitors (MEMPs) detected in the dermis from the first trimester:

> "The presence of megakaryocyte-erythrocyte-mast cell progenitors (MEMPs), lymphocyte precursors, B-cell progenitors, ILC precursors and their progeny 41 indicates differentiation of these lineages may be supported within developing dermis."
> — Botting and Haniffa (2020), *Immunology*

Mast cells are among the earliest immune cells detectable in fetal skin, appearing from 8 PCW:

> "Mast cells have been detected in fetal skin as early as 8 PCW, 41 and continue to mature and expand throughout the second trimester."
> — Botting and Haniffa (2020), *Immunology*

The earliest mast cell stage in fetal skin is characterised by immature granule content, with tryptase transcripts detectable before positive staining is observed:

> "Mast cells in first-and second-trimester fetal skin contain immature granules, 39,62 which is reflected in the delayed detection of positive tryptase or toluidine blue staining in the second trimester, 8,39 despite tryptase transcripts being detected from 8 PCW 41 and the presence of a distinct ª 2020 The Authors. Immunology published by John Wiley & Sons Ltd., Immunology, 160, 149-156 population of CD117 + mast cells being detected from 10 to 12 PCW."
> — Botting and Haniffa (2020), *Immunology*

## Markers

The earliest mast cell stage in fetal skin is expected to express:

- **KIT (CD117)** — defining marker of mast cell progenitors; high expression
- **GATA2** — transcription factor essential for mast cell commitment
- **FcεRI** — absent or very low at progenitor stage (per CL:0000831 definition)
- **TPSAB1 / TPSB2 (tryptase)** — transcripts detectable from 8 PCW; protein/granule staining negative
- **CD34** — may be retained from earlier progenitor stages

Specific differentially expressed markers distinguishing this earliest stage from subsequent mast cell states are provided in Supplementary Table 3 of Gopee et al. (2024).

## Location

Mast cell (earliest) cells are located in the dermal immune compartment of fetal skin. They were isolated as CD45+ immune cells by FACS prior to scRNA-seq. CD117+ (Kit+) mast cells are detectable in fetal skin from approximately 10–12 PCW by flow cytometry. Like mature mast cells in adult skin, fetal skin mast cells are commonly located near blood vessels and appendages, though at lower frequency.

## Function

At the earliest stage, fetal skin mast cells have limited effector function due to their immature granule content. Their primary role at this stage is likely to establish the tissue-resident mast cell compartment through in situ maturation. Stem cell factor (SCF/KIT ligand), produced at high levels by embryonic skin, supports mast cell chemotaxis and differentiation in this environment.

The atlas identifies three transcriptionally distinct mast cell states in fetal skin (earliest, medium, most mature), indicating a continuous maturation programme within the tissue rather than a single, uniform population.

## Structure / Morphology

At the earliest stage, fetal skin mast cells have a round-to-oval nucleus and cytoplasm that lacks the electron-dense specific granules characteristic of mature mast cells. Toluidine blue staining (metachromatic granule staining) is negative at this stage. The cells are KIT+ by flow cytometry and immunohistochemistry.

## References

- Gopee, N. et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Botting, R. and Haniffa, M. (2020). "The developing immune network in human prenatal skin." *Immunology*. DOI: [10.1111/imm.13192](https://doi.org/10.1111/imm.13192)
