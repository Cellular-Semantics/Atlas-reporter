# DL5_NEURON — dI5 (Class B Lbx1+/Lmx1b+ glutamatergic interneuron)

Cell Ontology: [neuron of the dorsal spinal cord](http://purl.obolibrary.org/obo/CL_0002611) (CL:0002611, narrow match — refined from HDCA Table 9's broader CL:0000540/CL:4042021). A more specific CL term for this subtype does not currently exist; see §Caveats for new-term-request candidates.

## Summary

DL5 neurons in HDCA stand out from DL1-3 by strong expression of the proneural bHLH factor ASCL1, PAX3, and the AP-2 factors TFAP2A/TFAP2B, together with Notch-pathway DLL3 and INSM1. This signature places them firmly in the **Class B (roof-plate-independent) Lbx1-positive dorsal interneuron lineage**, specifically the **canonical dI5 class** — glutamatergic excitatory interneurons whose fate depends on Lmx1b and which settle in the dorsal horn as Phox2a-positive cells contributing to nociceptive circuits.

> "ASCL1,PAX3,TFAP2A,INSM1,TFAP2B,DLL3,HOXB2,TOX3,MIAT,HOXD3,RCOR2,ADGRG1,SRRM4,HOXA3,ELAVL3,IRX2,GADD45G,NHLH1,DPYSL4,DCX"
>
> — Webb et al. (2026), HDCA Supplementary Table 9 (top gene signature)

The Human Developmental Cell Atlas (Webb et al., 2026) is a pan-organ integrated single-cell + spatial transcriptomic reference of human prenatal development (4-22 PCW). For central-nervous-system cells, HDCA states:

> "Central nervous system cells retained the original fine-grained annotations from Braun et al., as these annotations were informed by spatial context"
>
> — Webb et al. (2026), Methods

The DL5_NEURON cluster in HDCA's whole-embryo data (CNS_SPINAL_NEURON, NERVOUS_SYSTEM) thus represents a cell state aligned to the standard developmental spinal-cord taxonomy summarised by Wang et al. (2021):

> "The dorsal part contains six dorsal progenitor (dP) domains (dP1-dP6) and then differentiate into the dorsal interneuron (dI) populations (dI1-dI6)."
>
> — Wang et al. (2021)

## Markers

### Top HDCA differentially-expressed genes
- **TUBB3** — score 33.2, log2FC 4.96, p_adj 9.3e-238
- **TAGLN3** — score 31.7, log2FC 4.25, p_adj 1.7e-216
- **CD24** — score 29.1, log2FC 3.05, p_adj 9.7e-182
- **HOXB2** — score 28.4, log2FC 4.09, p_adj 9.0e-174
- **CKB** — score 28.2, log2FC 3.35, p_adj 7.5e-171
- **TUBB2B** — score 28.0, log2FC 3.42, p_adj 5.5e-169
- **PCBP4** — score 27.9, log2FC 3.28, p_adj 1.5e-167
- **MAP1B** — score 27.8, log2FC 3.12, p_adj 5.4e-167
- **GDI1** — score 27.8, log2FC 2.72, p_adj 8.8e-167
- **GPC2** — score 27.3, log2FC 3.24, p_adj 1.0e-160
- **CRMP1** — score 27.0, log2FC 2.97, p_adj 1.2e-157
- **ACTG1** — score 26.3, log2FC 1.52, p_adj 2.9e-149
- **TUBA1A** — score 26.1, log2FC 2.90, p_adj 9.6e-147
- **NGRN** — score 26.0, log2FC 2.52, p_adj 1.7e-145
- **DLL3** — score 25.7, log2FC 4.22, p_adj 1.5e-142

### Curated HDCA gene signature
> "ASCL1,PAX3,TFAP2A,INSM1,TFAP2B,DLL3,HOXB2,TOX3,MIAT,HOXD3,RCOR2,ADGRG1,SRRM4,HOXA3,ELAVL3,IRX2,GADD45G,NHLH1,DPYSL4,DCX"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Canonical literature markers for dI5

> "Lbx1 is essential for the specification and migration of the Class B neurons dI4-6 in the E12.5 neural tube"
>
> — Gray de Cristoforis et al. (2020)

> "dI4/6 are inhibitory GABAergic neuronal types, utilizing GABA as a neurotransmitter, whilst Lmx1b-expressing dI5 is glutamatergic, utilizing VGLUT2 as a neurotransmitter"
>
> — Gray de Cristoforis et al. (2020)

The HDCA DL5 cluster top-rank ASCL1 expression and strong PAX3/TFAP2A/TFAP2B/DLL3 places it firmly in the class B Lbx1+ proneural lineage destined to become Lmx1b+ glutamatergic dorsal-horn interneurons.


## Location

Dorsal alar plate (Pax3+ class B domain). 3842 HDCA cells from whole-embryo samples at CS13-14.

## Function

Glutamatergic (VGLUT2) excitatory dorsal-horn interneurons. dI5 are 'Lbx1+ without Pax2' (distinguishing from inhibitory dI4 and dI6); the proneural ASCL1 profile observed here is consistent with their origin from class B dp3-dp5 progenitors.

## Atlas annotation context

- **HDCA refined_celltype label:** `DL5_NEURON`
- **HDCA broad_celltype:** `CNS_SPINAL_NEURON`
- **HDCA systems / germlayer:** `NERVOUS_SYSTEM` / `ECTODERM`
- **HDCA Cell Ontology mapping (Supp Table 9):** `CL:0000540`
- **Inferred canonical correspondence:** dI5 (Class B Lbx1+/Lmx1b+ glutamatergic interneuron)
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
- Juárez-Morales JL, Schulte CJ, Pezoa SA, et al. (2016). "Evx1 and Evx2 specify excitatory neurotransmitter fates and suppress inhibitory fates through a Pax2-independent mechanism" *Neural Dev 11:5*. DOI: [10.1186/s12915-016-0227-8](https://doi.org/10.1186/s12915-016-0227-8)
