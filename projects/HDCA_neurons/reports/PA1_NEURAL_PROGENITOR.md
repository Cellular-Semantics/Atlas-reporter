# PA1_NEURAL_PROGENITOR — dp1 (roof-plate-adjacent MSX1+/MSX2+/ZIC1+ class A dorsal progenitor)

Cell Ontology: [neural progenitor cell](http://purl.obolibrary.org/obo/CL_0011020) (CL:0011020, broad match — refined from HDCA Table 9's broader CL:0000540/CL:4042021). A more specific CL term for this subtype does not currently exist; see §Caveats for new-term-request candidates.

## Summary

PA1 progenitors in HDCA are SOX2+ proliferating neural progenitors marked by MSX1, MSX2, ZIC1, ZIC2 and DRAXIN. This is the canonical signature of **dp1 dorsal progenitors** — the roof-plate-adjacent neural-tube domain that generates dI1 commissural relay neurons. MSX1 and MSX2 are BMP-responsive transcription factors restricted to the dorsal-most ventricular zone, while DRAXIN is the chemorepellent guiding commissural-axon trajectories. The signature thus pairs naturally with HDCA DL1 (dI1) downstream of the same alar plate.

> "SOX2,ZIC1,DCX,MSX2,MSX1,DCC,BSCL2,ELAVL3,POU3F2,MAP6,ADGRG1,STMN4,SSTR2,DPYSL4,RCOR2,DLL1,LRRN1,ZIC2,RND2,DRAXIN"
>
> — Webb et al. (2026), HDCA Supplementary Table 9 (top gene signature)

The Human Developmental Cell Atlas (Webb et al., 2026) is a pan-organ integrated single-cell + spatial transcriptomic reference of human prenatal development (4-22 PCW). For central-nervous-system cells, HDCA states:

> "Central nervous system cells retained the original fine-grained annotations from Braun et al., as these annotations were informed by spatial context"
>
> — Webb et al. (2026), Methods

The PA1_NEURAL_PROGENITOR cluster in HDCA's whole-embryo data (CNS_SPINAL_PROGENITOR, NERVOUS_SYSTEM) thus represents a cell state aligned to the standard developmental spinal-cord taxonomy summarised by Wang et al. (2021):

> "The dorsal part contains six dorsal progenitor (dP) domains (dP1-dP6) and then differentiate into the dorsal interneuron (dI) populations (dI1-dI6)."
>
> — Wang et al. (2021)

## Markers

### Top HDCA differentially-expressed genes
- **VAT1** — score 34.1, log2FC 3.89, p_adj 5.1e-251
- **RND2** — score 29.8, log2FC 4.67, p_adj 5.7e-191
- **HES6** — score 29.7, log2FC 4.44, p_adj 1.1e-190
- **TUBB** — score 29.7, log2FC 2.23, p_adj 1.1e-190
- **TAGLN3** — score 29.5, log2FC 3.70, p_adj 2.8e-188
- **TUBB3** — score 29.3, log2FC 4.18, p_adj 1.1e-185
- **MAP1B** — score 29.2, log2FC 3.33, p_adj 8.1e-184
- **TUBA1A** — score 29.2, log2FC 3.29, p_adj 1.2e-183
- **TUBB2B** — score 29.1, log2FC 3.58, p_adj 4.2e-183
- **CD24** — score 28.9, log2FC 2.99, p_adj 9.1e-180
- **CKB** — score 28.7, log2FC 3.20, p_adj 1.8e-177
- **PFN2** — score 27.5, log2FC 2.64, p_adj 1.9e-163
- **GDI1** — score 26.8, log2FC 2.56, p_adj 8.8e-155
- **ACTG1** — score 26.8, log2FC 1.58, p_adj 1.5e-154
- **NGRN** — score 26.7, log2FC 2.52, p_adj 6.9e-154

### Curated HDCA gene signature
> "SOX2,ZIC1,DCX,MSX2,MSX1,DCC,BSCL2,ELAVL3,POU3F2,MAP6,ADGRG1,STMN4,SSTR2,DPYSL4,RCOR2,DLL1,LRRN1,ZIC2,RND2,DRAXIN"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Canonical literature markers for dp1

> "the dP1 and dP3-5 domains express Atoh1 (arrowheads, B) and Ascl1 (arrowheads, C), respectively, in the E11.5 mouse embryo. The dP1 cells give rise to Lhx2 + dI1s while Isl1 + dI3s emerge from the dP3-5 population."
>
> — Gupta et al. (2018)

HDCA PA1 progenitors uniquely express **MSX1, MSX2, ZIC1 and ZIC2** at high rank, with **DRAXIN** — the chemorepulsive ligand secreted by roof-plate-adjacent cells that guides commissural axons. This places PA1 as the dp1 / roof-plate-adjacent dorsal progenitor domain, the source of dI1 (HDCA DL1) commissural relay neurons.


## Location

Roof-plate-adjacent dorsal-most ventricular zone of the embryonic spinal neural tube. 16,815 HDCA cells from whole-embryo samples at CS13-14.

## Function

Proliferating progenitor zone giving rise to dI1 (DL1) commissural relay neurons. MSX1/2 maintain progenitor identity under BMP induction from the roof plate; DLL1/DLL3 mediate Notch lateral inhibition during neurogenic divisions.

## Atlas annotation context

- **HDCA refined_celltype label:** `PA1_NEURAL_PROGENITOR`
- **HDCA broad_celltype:** `CNS_SPINAL_PROGENITOR`
- **HDCA systems / germlayer:** `NERVOUS_SYSTEM` / `ECTODERM`
- **HDCA Cell Ontology mapping (Supp Table 9):** `CL:4042021`
- **Inferred canonical correspondence:** dp1 (roof-plate-adjacent MSX1+/MSX2+/ZIC1+ class A dorsal progenitor)
- **Source of label:** HDCA whole-embryo scRNA-seq, annotation framework transferred from Braun et al. (2023). All cells in this cluster originate from `study = whole_embryo` (i.e. HDCA-generated data, not back-mapped from constituent atlases).

## Caveats

1. The names **DL1-DL6** and **pA1-pA3-4** are HDCA-internal labels. Neither the HDCA paper text nor Braun et al. (2023) define these labels explicitly in their narrative. The canonical correspondences above are inferred from the HDCA marker signatures (Supp. Table 9) matched against the published transcription factor codes for dI1-dI6 / dp1-dp4 in mouse and chick.
2. The CL term CL:4042021 assigned in HDCA Supp. Table 9 is broad. More specific CL terms may exist for individual dI subtypes (e.g. CL:0008035 dorsal horn interneuron, CL:4023089 spinal cord glutamatergic interneuron) — see ontology mapping step output for the proposed best CL match.
3. All cells were captured at Carnegie stages 13-14 (~32-33 dpc / ~5 PCW), which is at or just before the peak of dorsal interneuron neurogenesis in humans (Rayon et al., 2021). Some 'neuron' clusters may include cells still completing terminal differentiation.

## References

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development" *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Braun E, Danan-Gotthold M, Borm LE, et al. (2023). "Comprehensive cell atlas of the first-trimester developing human brain" *Science 382*. DOI: [10.1126/science.adf1226](https://doi.org/10.1126/science.adf1226)
- Lu DC, Niu T, Alaynick WA (2015). "Molecular and cellular development of spinal cord locomotor circuitry" *Front Mol Neurosci 8:25*. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Gray de Cristoforis A, Ferrari F, Clotman F, Vogel T (2020). "Differentiation and localization of interneurons in the developing spinal cord depends on DOT1L expression" *Mol Brain 13:85*. DOI: [10.1186/s13041-020-00623-3](https://doi.org/10.1186/s13041-020-00623-3)
- Castellani V (2013). "Building Spinal and Brain Commissures: Axon Guidance at the Midline" *ISRN Cell Biol 2013:315387*. DOI: [10.1155/2013/315387](https://doi.org/10.1155/2013/315387)
- Wang Y-F, Liu C, Xu P-F (2021). "Deciphering and reconstitution of positional information in the human brain development" *Cell Regen 10:29*. DOI: [10.1186/s13619-021-00091-7](https://doi.org/10.1186/s13619-021-00091-7)
- Gupta S, Sivalingam D, Hain S, et al. (2018). "Deriving Dorsal Spinal Sensory Interneurons from Human Pluripotent Stem Cells" *Stem Cell Rep 10:390-405*. DOI: [10.1016/j.stemcr.2018.02.013](https://doi.org/10.1016/j.stemcr.2018.02.013)
- Rayon T, Maizels RJ, Barrington C, Briscoe J (2021). "Single-cell transcriptome profiling of the human developing spinal cord reveals a conserved genetic programme with human-specific features" *Development 148:dev199711*. DOI: [10.1242/dev.198309](https://doi.org/10.1242/dev.198309)
