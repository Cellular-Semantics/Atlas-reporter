# PA3_4_NEURAL_PROGENITOR — dp3–dp4 (PAX3+/ASCL1+ class A–B boundary dorsal progenitor)

Cell Ontology: [neural progenitor cell](http://purl.obolibrary.org/obo/CL_0011020) (CL:0011020, broad match — refined from HDCA Table 9's broader CL:0000540/CL:4042021). A more specific CL term for this subtype does not currently exist; see §Caveats for new-term-request candidates.

## Summary

PA3_4 progenitors form a large (8475 cells) PAX3+ASCL1+ proliferative population expressing canonical neural-progenitor markers SOX2, NES, HES5, CCND1, and IRX2. The PAX3/ASCL1 co-expression signature is the textbook marker combination for **canonical dp3 and dp4 dorsal progenitor domains** — the dorsal-most class B (ASCL1-dependent) progenitors that generate dI3, dI4 and dI5 neurons. The HDCA decision to merge dp3 and dp4 into a single annotation ("pA3-4") reflects the difficulty of resolving these two transcriptionally similar domains in dissociated scRNA-seq at this stage.

> "SOX2,PAX3,ASCL1,CXCR4,HES5,SOX9,MSX2,ZIC1,PDPN,EDNRB,IRX2,TTYH1,FZD10,POU3F2,HOXB2,HOXD4,NPPC,JAG1,LRRN1,DLL1"
>
> — Webb et al. (2026), HDCA Supplementary Table 9 (top gene signature)

The Human Developmental Cell Atlas (Webb et al., 2026) is a pan-organ integrated single-cell + spatial transcriptomic reference of human prenatal development (4-22 PCW). For central-nervous-system cells, HDCA states:

> "Central nervous system cells retained the original fine-grained annotations from Braun et al., as these annotations were informed by spatial context"
>
> — Webb et al. (2026), Methods

The PA3_4_NEURAL_PROGENITOR cluster in HDCA's whole-embryo data (CNS_SPINAL_PROGENITOR, NERVOUS_SYSTEM) thus represents a cell state aligned to the standard developmental spinal-cord taxonomy summarised by Wang et al. (2021):

> "The dorsal part contains six dorsal progenitor (dP) domains (dP1-dP6) and then differentiate into the dorsal interneuron (dI) populations (dI1-dI6)."
>
> — Wang et al. (2021)

## Markers

### Top HDCA differentially-expressed genes
- **NES** — score 34.6, log2FC 4.40, p_adj 9.2e-258
- **SOX2** — score 34.5, log2FC 5.69, p_adj 7.4e-257
- **CKB** — score 34.4, log2FC 4.00, p_adj 1.8e-255
- **PAX3** — score 34.2, log2FC 5.68, p_adj 5.6e-252
- **TTYH1** — score 29.9, log2FC 3.99, p_adj 3.7e-193
- **ASCL1** — score 29.6, log2FC 4.43, p_adj 1.1e-188
- **CCND1** — score 29.3, log2FC 3.19, p_adj 6.5e-185
- **RND2** — score 29.2, log2FC 3.99, p_adj 4.7e-184
- **HMGA1** — score 28.4, log2FC 2.68, p_adj 3.9e-174
- **VIM** — score 27.8, log2FC 3.08, p_adj 9.0e-167
- **TUBB** — score 26.3, log2FC 1.99, p_adj 8.1e-149
- **HOXB2** — score 26.3, log2FC 3.33, p_adj 8.4e-149
- **ARL4A** — score 26.1, log2FC 2.77, p_adj 1.8e-147
- **IRX2** — score 25.9, log2FC 3.42, p_adj 7.1e-145
- **FDFT1** — score 25.8, log2FC 2.14, p_adj 2.0e-143

### Curated HDCA gene signature
> "SOX2,PAX3,ASCL1,CXCR4,HES5,SOX9,MSX2,ZIC1,PDPN,EDNRB,IRX2,TTYH1,FZD10,POU3F2,HOXB2,HOXD4,NPPC,JAG1,LRRN1,DLL1"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Canonical literature markers for dp3–dp4

> "the dP1 and dP3-5 domains express Atoh1 (arrowheads, B) and Ascl1 (arrowheads, C), respectively, in the E11.5 mouse embryo. The dP1 cells give rise to Lhx2 + dI1s while Isl1 + dI3s emerge from the dP3-5 population."
>
> — Gupta et al. (2018)

HDCA PA3_4 progenitors carry the textbook **SOX2+/PAX3+/ASCL1+** dorsal class B progenitor signature, alongside the Notch effector **HES5** and the canonical cycling-progenitor markers NES, VIM, CCND1. The merged "pA3-4" annotation reflects the difficulty of separating dp3 and dp4 transcriptionally — both are Pax3+/Ascl1+ and they generate the closely related dI3 and dI4 lineages respectively.


## Location

Dorsal alar plate, intermediate between PA1 (dp1, dorsal-most) and the post-mitotic class B Lbx1+ domain. 8475 HDCA cells at CS13-14 from whole-embryo samples.

## Function

Cycling class B dorsal progenitor pool generating excitatory dI3/dI5 and inhibitory dI4 dorsal interneurons. ASCL1 drives neurogenic competence; HES5/Notch maintains the progenitor pool.

## Atlas annotation context

- **HDCA refined_celltype label:** `PA3_4_NEURAL_PROGENITOR`
- **HDCA broad_celltype:** `CNS_SPINAL_PROGENITOR`
- **HDCA systems / germlayer:** `NERVOUS_SYSTEM` / `ECTODERM`
- **HDCA Cell Ontology mapping (Supp Table 9):** `CL:4042021`
- **Inferred canonical correspondence:** dp3–dp4 (PAX3+/ASCL1+ class A–B boundary dorsal progenitor)
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
