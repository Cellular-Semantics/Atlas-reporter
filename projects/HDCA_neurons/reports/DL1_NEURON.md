# DL1_NEURON — dI1 (Class A roof-plate-dependent commissural relay interneuron)

Cell Ontology: [neuron of the dorsal spinal cord](http://purl.obolibrary.org/obo/CL_0002611) (CL:0002611, narrow match — refined from HDCA Table 9's broader CL:0000540/CL:4042021). A more specific CL term for this subtype does not currently exist; see §Caveats for new-term-request candidates.

## Summary

DL1 neurons are HDCA-annotated post-mitotic dorsal-lateral spinal cord neurons captured in newly-generated whole-embryo scRNA-seq at Carnegie stages 13–14 (~32–33 dpc). Based on their transcriptional signature — particularly LHX9, contactin-2 (CNTN2), and the netrin receptor DCC — they correspond to **canonical dI1 dorsal interneurons**: the dorsal-most class of spinal interneurons, dependent on roof-plate BMP/Wnt signalling, projecting commissural axons across the floor plate to relay proprioceptive information rostrally.

> "NGFR,DCX,CNTN2,ELAVL3,INA,STMN2,HOXD3,HOXA3,DCC,HOXB2,LHX9,BSCL2,NHLH1,DNER,CRABP1,DPYSL4,SNCG,ADGRG1,SHD,RGMB"
>
> — Webb et al. (2026), HDCA Supplementary Table 9 (top gene signature)

The Human Developmental Cell Atlas (Webb et al., 2026) is a pan-organ integrated single-cell + spatial transcriptomic reference of human prenatal development (4-22 PCW). For central-nervous-system cells, HDCA states:

> "Central nervous system cells retained the original fine-grained annotations from Braun et al., as these annotations were informed by spatial context"
>
> — Webb et al. (2026), Methods

The DL1_NEURON cluster in HDCA's whole-embryo data (CNS_SPINAL_NEURON, NERVOUS_SYSTEM) thus represents a cell state aligned to the standard developmental spinal-cord taxonomy summarised by Wang et al. (2021):

> "The dorsal part contains six dorsal progenitor (dP) domains (dP1-dP6) and then differentiate into the dorsal interneuron (dI) populations (dI1-dI6)."
>
> — Wang et al. (2021)

## Markers

### Top HDCA differentially-expressed genes
- **CRABP1** — score 37.7, log2FC 8.11, p_adj 4.7e-306
- **TUBB3** — score 36.3, log2FC 5.67, p_adj 5.5e-284
- **CRMP1** — score 34.4, log2FC 3.94, p_adj 1.1e-255
- **GPC2** — score 34.2, log2FC 4.11, p_adj 2.6e-253
- **MAP1B** — score 34.2, log2FC 3.92, p_adj 4.8e-252
- **HOXB2** — score 34.1, log2FC 4.62, p_adj 6.3e-252
- **TUBB2B** — score 34.1, log2FC 4.18, p_adj 3.2e-251
- **LHX9** — score 34.0, log2FC 5.85, p_adj 1.1e-250
- **TAGLN3** — score 33.6, log2FC 4.23, p_adj 1.1e-244
- **TUBA1A** — score 33.6, log2FC 3.89, p_adj 2.4e-244
- **NGFR** — score 33.3, log2FC 4.80, p_adj 5.2e-240
- **HOXA3** — score 33.3, log2FC 4.66, p_adj 1.0e-239
- **CD24** — score 33.2, log2FC 3.51, p_adj 6.6e-239
- **TUBB** — score 32.4, log2FC 2.43, p_adj 6.1e-227
- **GDI1** — score 32.4, log2FC 3.11, p_adj 1.1e-226

### Curated HDCA gene signature
> "NGFR,DCX,CNTN2,ELAVL3,INA,STMN2,HOXD3,HOXA3,DCC,HOXB2,LHX9,BSCL2,NHLH1,DNER,CRABP1,DPYSL4,SNCG,ADGRG1,SHD,RGMB"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Canonical literature markers for dI1

> "The dorsal-most interneuron class, dI1, is characterized by expression of Lhx2 and Lhx9."
>
> — Gray de Cristoforis et al. (2020)

> "Dl1 neurons are generated from a pool of progenitor cells expressing Math1, and can be identified by two LIM transcription factors, Lhx2 and Lhx9."
>
> — Castellani (2013)

The HDCA DL1 cluster expresses both **LHX9** (signature rank 11) and **CNTN2** (contactin-2, axon-guidance receptor) and **DCC** (netrin receptor) — the canonical molecular fingerprint of dI1 commissural relay neurons.


## Location

Spinal cord dorsal-most domain (lamina I-equivalent progenitor zone). At CS13-14, the cells are migrating ventrally from the alar plate. All 2454 DL1 cells in HDCA derive from whole-embryo samples.

## Function

Commissural relay of proprioceptive/cutaneous input from the dorsal horn to higher centres. dI1 neurons divide into ipsilateral (dI1i) and contralateral (dI1c) projection populations whose trajectory is controlled by the LHX2/LHX9 LIM-homeodomain switch acting on ROBO3.

## Atlas annotation context

- **HDCA refined_celltype label:** `DL1_NEURON`
- **HDCA broad_celltype:** `CNS_SPINAL_NEURON`
- **HDCA systems / germlayer:** `NERVOUS_SYSTEM` / `ECTODERM`
- **HDCA Cell Ontology mapping (Supp Table 9):** `CL:0000540`
- **Inferred canonical correspondence:** dI1 (Class A roof-plate-dependent commissural relay interneuron)
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
- Gupta S, Sivalingam D, Hain S, et al. (2018). "Deriving Dorsal Spinal Sensory Interneurons from Human Pluripotent Stem Cells" *Stem Cell Rep 10:390-405*. DOI: [10.1016/j.stemcr.2018.02.013](https://doi.org/10.1016/j.stemcr.2018.02.013)
- Avraham O, Hadas Y, Vald L, et al. (2009). "Transcriptional control of axonal guidance and sorting in dorsal interneurons by the Lim-HD proteins Lhx9 and Lhx1" *Neural Dev 4:21*. DOI: [10.1186/1749-8104-4-13](https://doi.org/10.1186/1749-8104-4-13)
