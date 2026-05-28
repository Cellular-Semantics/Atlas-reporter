# DL2_NEURON — dI2 (Class A roof-plate-dependent commissural interneuron)

Cell Ontology: [neuron of the dorsal spinal cord](http://purl.obolibrary.org/obo/CL_0002611) (CL:0002611, narrow match — refined from HDCA Table 9's broader CL:0000540/CL:4042021). A more specific CL term for this subtype does not currently exist; see §Caveats for new-term-request candidates.

## Summary

DL2 neurons are HDCA's annotated post-mitotic dorsal-lateral spinal cord neurons at Carnegie stages 13–14, expressing pan-neuronal markers (TUBB3, DCX, STMN2, INA) together with the POU-domain transcription factor POU2F2 and caudal HOX genes. Their transcriptional profile is consistent with **canonical dI2 dorsal interneurons** — Class A roof-plate-dependent commissural relay neurons that, like dI1, project axons across the midline but, unlike dI1, use the LHX1/LHX5 transcriptional code to direct caudal rather than rostral longitudinal turning.

> "DCX,NGFR,INA,CNTN2,STMN2,ELAVL3,HOXD3,HOXB2,HOXA3,POU2F2,SNCG,CRABP1,MAP6,TUBB4A,KIF5C,DPYSL4,INSM1,NHLH1,SHD,STMN4"
>
> — Webb et al. (2026), HDCA Supplementary Table 9 (top gene signature)

The Human Developmental Cell Atlas (Webb et al., 2026) is a pan-organ integrated single-cell + spatial transcriptomic reference of human prenatal development (4-22 PCW). For central-nervous-system cells, HDCA states:

> "Central nervous system cells retained the original fine-grained annotations from Braun et al., as these annotations were informed by spatial context"
>
> — Webb et al. (2026), Methods

The DL2_NEURON cluster in HDCA's whole-embryo data (CNS_SPINAL_NEURON, NERVOUS_SYSTEM) thus represents a cell state aligned to the standard developmental spinal-cord taxonomy summarised by Wang et al. (2021):

> "The dorsal part contains six dorsal progenitor (dP) domains (dP1-dP6) and then differentiate into the dorsal interneuron (dI) populations (dI1-dI6)."
>
> — Wang et al. (2021)

## Markers

### Top HDCA differentially-expressed genes
- **TUBB3** — score 36.2, log2FC 5.68, p_adj 3.1e-283
- **MAP1B** — score 35.1, log2FC 4.15, p_adj 1.2e-266
- **CRMP1** — score 34.4, log2FC 4.02, p_adj 4.4e-256
- **TAGLN3** — score 34.2, log2FC 4.46, p_adj 1.3e-252
- **TUBB2B** — score 33.7, log2FC 4.13, p_adj 7.7e-246
- **TUBA1A** — score 33.5, log2FC 3.89, p_adj 1.9e-242
- **GDI1** — score 32.8, log2FC 3.25, p_adj 1.3e-232
- **GPC2** — score 32.5, log2FC 3.86, p_adj 1.3e-227
- **STMN2** — score 32.3, log2FC 5.17, p_adj 1.6e-225
- **CD24** — score 31.9, log2FC 3.34, p_adj 1.5e-219
- **DCX** — score 31.8, log2FC 3.81, p_adj 4.5e-218
- **VAT1** — score 31.7, log2FC 3.33, p_adj 4.7e-217
- **INA** — score 31.4, log2FC 4.67, p_adj 1.2e-212
- **TUBB** — score 31.2, log2FC 2.35, p_adj 1.2e-210
- **CRABP1** — score 31.1, log2FC 5.99, p_adj 4.3e-209

### Curated HDCA gene signature
> "DCX,NGFR,INA,CNTN2,STMN2,ELAVL3,HOXD3,HOXB2,HOXA3,POU2F2,SNCG,CRABP1,MAP6,TUBB4A,KIF5C,DPYSL4,INSM1,NHLH1,SHD,STMN4"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Canonical literature markers for dI2

> "The Lim-HD proteins Lhx9 and Lhx1 serve as a binary switch in controlling the rostral versus caudal longitudinal turning of the caudal commissural axons. Lhx1 determines caudal turning and Lhx9 triggers rostral turning."
>
> — Avraham et al. (2009)

The HDCA DL2 cluster lacks LHX9 but retains pan-neuronal commissural markers (CNTN2, STMN2, INA) and expresses **POU2F2** at the top of its signature — consistent with the LHX1/LHX5-coded class A dI2 lineage that projects caudally rather than rostrally.


## Location

Spinal cord dorsal alar plate, just ventral to dI1. All 5044 cells in HDCA from whole-embryo samples at CS13-14.

## Function

Predominantly commissural projection; in mouse the LHX1/LHX5 code in dI2 directs caudal turning of commissural axons (the opposite of LHX2/LHX9 in dI1).

## Atlas annotation context

- **HDCA refined_celltype label:** `DL2_NEURON`
- **HDCA broad_celltype:** `CNS_SPINAL_NEURON`
- **HDCA systems / germlayer:** `NERVOUS_SYSTEM` / `ECTODERM`
- **HDCA Cell Ontology mapping (Supp Table 9):** `CL:0000540`
- **Inferred canonical correspondence:** dI2 (Class A roof-plate-dependent commissural interneuron)
- **Source of label:** HDCA whole-embryo scRNA-seq, annotation framework transferred from Braun et al. (2023). All cells in this cluster originate from `study = whole_embryo` (i.e. HDCA-generated data, not back-mapped from constituent atlases).

## Caveats

1. The names **DL1-DL6** and **pA1-pA3-4** are HDCA-internal labels. Neither the HDCA paper text nor Braun et al. (2023) define these labels explicitly in their narrative. The canonical correspondences above are inferred from the HDCA marker signatures (Supp. Table 9) matched against the published transcription factor codes for dI1-dI6 / dp1-dp4 in mouse and chick.
2. The CL term CL:0000540 assigned in HDCA Supp. Table 9 is broad. More specific CL terms may exist for individual dI subtypes (e.g. CL:0008035 dorsal horn interneuron, CL:4023089 spinal cord glutamatergic interneuron) — see ontology mapping step output for the proposed best CL match.
3. All cells were captured at Carnegie stages 13-14 (~32-33 dpc / ~5 PCW), which is at or just before the peak of dorsal interneuron neurogenesis in humans (Rayon et al., 2021). Some 'neuron' clusters may include cells still completing terminal differentiation.

## References

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development" *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Braun E, Danan-Gotthold M, Borm LE, et al. (2023). "Comprehensive cell atlas of the first-trimester developing human brain" *Science 382*. DOI: [10.1126/science.adf1226](https://doi.org/10.1126/science.adf1226)
- Lu DC, Niu T, Alaynick WA (2015). "Molecular and cellular development of spinal cord locomotor circuitry" *Front Mol Neurosci 8:25*. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Gray de Cristoforis A, Ferrari F, Clotman F, Vogel T (2020). "Differentiation and localization of interneurons in the developing spinal cord depends on DOT1L expression" *Mol Brain 13:85*. DOI: [10.1186/s13041-020-00623-3](https://doi.org/10.1186/s13041-020-00623-3)
- Castellani V (2013). "Building Spinal and Brain Commissures: Axon Guidance at the Midline" *ISRN Cell Biol 2013:315387*. DOI: [10.1155/2013/315387](https://doi.org/10.1155/2013/315387)
- Wang Y-F, Liu C, Xu P-F (2021). "Deciphering and reconstitution of positional information in the human brain development" *Cell Regen 10:29*. DOI: [10.1186/s13619-021-00091-7](https://doi.org/10.1186/s13619-021-00091-7)
- Avraham O, Hadas Y, Vald L, et al. (2009). "Transcriptional control of axonal guidance and sorting in dorsal interneurons by the Lim-HD proteins Lhx9 and Lhx1" *Neural Dev 4:21*. DOI: [10.1186/1749-8104-4-13](https://doi.org/10.1186/1749-8104-4-13)
