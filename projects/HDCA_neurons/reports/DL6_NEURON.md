# DL6_NEURON — dI6 (Class B Lbx1+/Pax2+ GABAergic commissural inhibitory interneuron)

Cell Ontology: [neuron of the dorsal spinal cord](http://purl.obolibrary.org/obo/CL_0002611) (CL:0002611, narrow match — refined from HDCA Table 9's broader CL:0000540/CL:4042021). A more specific CL term for this subtype does not currently exist; see §Caveats for new-term-request candidates.

## Summary

DL6 neurons in HDCA express PAX2 and the GABAergic differentiation gene GAD2 alongside pan-neuronal markers (TUBB3, DCX, INA), together with caudal HOX (HOXB2, HOXD3). This profile is the canonical signature of **dI6 dorsal interneurons** — the ventral-most class of Class B (Lbx1+) dorsal interneurons and the only PAX2-positive Class B subtype. dI6 neurons are commissural GABAergic (and sometimes glycinergic) interneurons that migrate into lamina VIII and contribute to left–right alternation in locomotor circuits.

> "DCX,PAX2,INA,STMN2,NEFL,TUBB4A,DNER,KIF5C,ELAVL4,ATP1A3,RAB3A,L1CAM,ENO2,HOXB2,SLIT1,GAD2,NEFM,RTN1,GNG3,HOXD3"
>
> — Webb et al. (2026), HDCA Supplementary Table 9 (top gene signature)

The Human Developmental Cell Atlas (Webb et al., 2026) is a pan-organ integrated single-cell + spatial transcriptomic reference of human prenatal development (4-22 PCW). For central-nervous-system cells, HDCA states:

> "Central nervous system cells retained the original fine-grained annotations from Braun et al., as these annotations were informed by spatial context"
>
> — Webb et al. (2026), Methods

The DL6_NEURON cluster in HDCA's whole-embryo data (CNS_SPINAL_NEURON, NERVOUS_SYSTEM) thus represents a cell state aligned to the standard developmental spinal-cord taxonomy summarised by Wang et al. (2021):

> "The dorsal part contains six dorsal progenitor (dP) domains (dP1-dP6) and then differentiate into the dorsal interneuron (dI) populations (dI1-dI6)."
>
> — Wang et al. (2021)

## Markers

### Top HDCA differentially-expressed genes
- **LAMP5** — score 37.1, log2FC 6.89, p_adj 9.6e-297
- **INA** — score 36.5, log2FC 5.59, p_adj 9.8e-288
- **TUBB3** — score 35.6, log2FC 5.47, p_adj 2.0e-274
- **NSG1** — score 35.2, log2FC 4.33, p_adj 8.8e-268
- **GPC2** — score 34.5, log2FC 4.11, p_adj 2.1e-257
- **TUBB4A** — score 34.4, log2FC 4.90, p_adj 1.4e-255
- **CRMP1** — score 34.1, log2FC 3.91, p_adj 6.1e-252
- **MAP1B** — score 33.9, log2FC 3.89, p_adj 1.1e-248
- **DCX** — score 33.9, log2FC 4.21, p_adj 7.2e-248
- **HOXB2** — score 33.6, log2FC 4.72, p_adj 1.9e-244
- **NSG2** — score 33.5, log2FC 4.90, p_adj 2.4e-242
- **APLP1** — score 33.4, log2FC 3.97, p_adj 4.6e-242
- **STMN2** — score 33.3, log2FC 5.24, p_adj 9.7e-240
- **DNER** — score 33.1, log2FC 4.32, p_adj 1.5e-236
- **TUBB2B** — score 33.0, log2FC 4.03, p_adj 8.5e-236

### Curated HDCA gene signature
> "DCX,PAX2,INA,STMN2,NEFL,TUBB4A,DNER,KIF5C,ELAVL4,ATP1A3,RAB3A,L1CAM,ENO2,HOXB2,SLIT1,GAD2,NEFM,RTN1,GNG3,HOXD3"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Canonical literature markers for dI6

> "The roof-plate independent Class B dI6 commissural inhibitory interneurons express Lbx1, Lhx1, Lhx5, and are Pax2 positive, indicating a GABAergic fate"
>
> — Lu, Niu & Alaynick (2015)

> "Dmrt3, a novel marker in dl6 interneuron was traced to play a key role in locomotor circuitry and in development of commissural interneurons"
>
> — Lu, Niu & Alaynick (2015)

HDCA DL6's signature includes **PAX2** and **GAD2** (glutamate decarboxylase 2), the canonical Pax2+ GABAergic class B dorsal-interneuron fingerprint that distinguishes dI6 from the glutamatergic dI5 and excitatory class A dI3.


## Location

Ventral-most class B dorsal interneuron domain (Pax2+/Lbx1+). 1522 HDCA cells from whole-embryo samples at CS13-14.

## Function

GABAergic / glycinergic commissural inhibitory interneurons of lamina VIII. dI6 are required for the rhythmic alternating output of the central pattern generator; Dmrt3 (a canonical dI6 marker in mouse) modulates gait.

## Atlas annotation context

- **HDCA refined_celltype label:** `DL6_NEURON`
- **HDCA broad_celltype:** `CNS_SPINAL_NEURON`
- **HDCA systems / germlayer:** `NERVOUS_SYSTEM` / `ECTODERM`
- **HDCA Cell Ontology mapping (Supp Table 9):** `CL:0000540`
- **Inferred canonical correspondence:** dI6 (Class B Lbx1+/Pax2+ GABAergic commissural inhibitory interneuron)
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
