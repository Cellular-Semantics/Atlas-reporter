# PA2_NEURAL_PROGENITOR — dp2 (PAX3+ neurogenic dorsal progenitor / pre-neurogenic transition)

Cell Ontology: [neural progenitor cell](http://purl.obolibrary.org/obo/CL_0011020) (CL:0011020, broad match — refined from HDCA Table 9's broader CL:0000540/CL:4042021). A more specific CL term for this subtype does not currently exist; see §Caveats for new-term-request candidates.

## Summary

PA2 progenitors carry a strongly neurogenic transcriptional profile (NHLH1, NEUROD4, INSM1, DLL3, TFAP2B) on a PAX3 background, indicating they are not naïve cycling progenitors but transitional **dp2-domain intermediate neurogenic progenitors / pre-neurons**. Their PAX3+ identity places them in the class A dorsal progenitor field; coexpression of NGFR, NHLH1 and INSM1 marks them as committed neurogenic cells beginning differentiation into dI2 commissural neurons and possibly contributing to dI3.

> "NGFR,PAX3,DCX,DCC,NHLH1,DLL3,PDPN,INSM1,ELAVL3,HOXD3,HOXB2,RCOR2,SRRM4,NEUROD4,ADGRG1,MAP6,ELAVL4,TFAP2B,GADD45G,HOXA3"
>
> — Webb et al. (2026), HDCA Supplementary Table 9 (top gene signature)

The Human Developmental Cell Atlas (Webb et al., 2026) is a pan-organ integrated single-cell + spatial transcriptomic reference of human prenatal development (4-22 PCW). For central-nervous-system cells, HDCA states:

> "Central nervous system cells retained the original fine-grained annotations from Braun et al., as these annotations were informed by spatial context"
>
> — Webb et al. (2026), Methods

The PA2_NEURAL_PROGENITOR cluster in HDCA's whole-embryo data (CNS_SPINAL_PROGENITOR, NERVOUS_SYSTEM) thus represents a cell state aligned to the standard developmental spinal-cord taxonomy summarised by Wang et al. (2021):

> "The dorsal part contains six dorsal progenitor (dP) domains (dP1-dP6) and then differentiate into the dorsal interneuron (dI) populations (dI1-dI6)."
>
> — Wang et al. (2021)

## Markers

### Top HDCA differentially-expressed genes
- **TAGLN3** — score 36.1, log2FC 4.99, p_adj 8.4e-281
- **NHLH1** — score 35.4, log2FC 6.37, p_adj 3.7e-270
- **TUBB3** — score 34.0, log2FC 5.08, p_adj 1.5e-249
- **ENC1** — score 33.9, log2FC 4.44, p_adj 1.7e-247
- **CDKN1C** — score 33.1, log2FC 4.05, p_adj 1.4e-236
- **DLL3** — score 32.7, log2FC 5.19, p_adj 1.9e-230
- **PCBP4** — score 32.4, log2FC 3.87, p_adj 4.0e-227
- **HOXB2** — score 31.8, log2FC 4.44, p_adj 6.5e-218
- **CD24** — score 31.4, log2FC 3.29, p_adj 1.0e-212
- **HES6** — score 31.4, log2FC 4.72, p_adj 1.8e-212
- **RBP1** — score 31.3, log2FC 3.34, p_adj 1.6e-211
- **GDI1** — score 30.7, log2FC 3.05, p_adj 1.7e-203
- **RCOR2** — score 30.4, log2FC 4.55, p_adj 1.3e-199
- **INSM1** — score 30.0, log2FC 5.25, p_adj 7.3e-195
- **GPC2** — score 29.7, log2FC 3.54, p_adj 4.2e-191

### Curated HDCA gene signature
> "NGFR,PAX3,DCX,DCC,NHLH1,DLL3,PDPN,INSM1,ELAVL3,HOXD3,HOXB2,RCOR2,SRRM4,NEUROD4,ADGRG1,MAP6,ELAVL4,TFAP2B,GADD45G,HOXA3"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Canonical literature markers for dp2

HDCA PA2 progenitors combine residual progenitor markers (SOX2 expression elsewhere in the lineage) with strong neurogenic/pre-neuronal transcription factors **NHLH1, NEUROD4, INSM1, DLL3** — a 'transitioning' progenitor signature consistent with the dp2 domain at the cusp of post-mitotic conversion to dI2 neurons. The HDCA pA2 → DL2 (dI2) lineage relationship parallels the canonical dp2 → dI2 specification:

> "The Lim-HD proteins Lhx9 and Lhx1 serve as a binary switch in controlling the rostral versus caudal longitudinal turning of the caudal commissural axons. Lhx1 determines caudal turning and Lhx9 triggers rostral turning."
>
> — Avraham et al. (2009)


## Location

Dorsal alar plate of the spinal neural tube, intermediate between PA1 (dp1) and PA3_4 (dp3-4). 1064 HDCA cells from whole-embryo samples at CS13-14.

## Function

Late-stage dorsal progenitors transitioning to post-mitotic neurons — likely the immediate precursors of DL2 (dI2) and a fraction of DL3 (dI3).

## Atlas annotation context

- **HDCA refined_celltype label:** `PA2_NEURAL_PROGENITOR`
- **HDCA broad_celltype:** `CNS_SPINAL_PROGENITOR`
- **HDCA systems / germlayer:** `NERVOUS_SYSTEM` / `ECTODERM`
- **HDCA Cell Ontology mapping (Supp Table 9):** `CL:4042021`
- **Inferred canonical correspondence:** dp2 (PAX3+ neurogenic dorsal progenitor / pre-neurogenic transition)
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
