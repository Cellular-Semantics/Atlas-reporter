# DL3_NEURON

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (Webb et al., 2026; DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220))
Scope: fetal/embryonic (Carnegie stage 13–14, ~32–33 dpc)
Tissue context: spinal cord (alar plate, dorsal neural tube) — provisional, see §Hypothesised correspondence

Cell Ontology: [neuron of the dorsal spinal cord](http://purl.obolibrary.org/obo/CL_0002611) (CL:0002611, narrow match — dI3-specific term not in CL; NTR candidate)

## Summary

`DL3_NEURON` is one of six "DL"-prefixed clusters (DL1, DL2, DL3, DL5, DL6) in the HDCA v2 integrated atlas, annotated under `broad_celltype = CNS_SPINAL_NEURON` (Webb et al., 2026, Supplementary Table 9). The cluster captures 9,242 cells from HDCA's de novo whole-embryo scRNA-seq at Carnegie stages 13–14. The HDCA-curated top-gene signature for this cluster is dominated by **pan-neuronal differentiation markers** (DCX, STMN2, ELAVL3/4, NEFL/M, TUBB4A, INA, NHLH1/2) rather than dorsal-interneuron-subtype-specific transcription factors; the cluster's correspondence to the canonical dI3 (Class A commissural excitatory) interneuron class is therefore a **hypothesis informed by the HDCA cluster name and by classical dorsal-spinal-cord taxonomy**, not a marker-confirmed identification. We outline below the evidence available, what it does and does not support, and questions to raise with the HDCA annotators.

## Markers

### HDCA top gene signature for `DL3_NEURON`

> "DCX,STMN2,INA,ELAVL4,RGMB,ELAVL3,NEFL,KIF5C,TUBB4A,CNTN2,CRABP1,NEFM,ATP1A3,NHLH2,DPYSL4,ADGRG1,NHLH1,MAP6,STMN4,SCG3"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

**What this signature does support.** Every gene in this signature is a well-established marker of post-mitotic / immature neuron identity: DCX (doublecortin) and STMN2/4 (stathmins) mark migrating immature neurons; ELAVL3/4 (HuC/HuD) are pan-neuronal RNA-binding proteins; NEFL/NEFM and INA encode neurofilament subunits expressed in differentiating neurons; TUBB4A, MAP6, KIF5C are neuronal cytoskeletal genes; NHLH1/2 are early-neuron bHLH transcription factors; CNTN2 is an axon-guidance contactin. Collectively this signature identifies `DL3_NEURON` as a differentiating CNS neuron cluster — consistent with HDCA's broad classification of these cells as spinal-cord neurons.

**What this signature does *not* support.** None of the canonical dI3-specifying transcription factors are present in this 20-gene signature. The classical dI3 molecular code involves the homeodomain factor ISL1 acting downstream of a TLX1/TLX3 excitatory-fate code (Lai et al., 2016; Sagner & Briscoe, 2019; Gupta et al., 2018), and these genes are not enriched in the HDCA top signature. Top HDCA DEGs for this cluster (TUBB3, TAGLN3, DCX, CRABP1, CD24, MAP1B, GPC2, STMN2, TUBB2B, TUBA1A, CRMP1, INA, DPYSL4, ELAVL4, TMEFF1; HDCA Supplementary Table 16) are likewise pan-neuronal differentiation markers, with CRABP1 (retinoic acid binding protein 1) being the most subtype-suggestive single gene — CRABP1 is broadly expressed in differentiating dorsal spinal cord neurons and is not specific to dI3.

### Canonical dI3 literature markers (for reference; not directly verified in HDCA data)

The transcription factor code that distinguishes dI3 from other dorsal interneuron classes in mouse and chick is summarised in Juárez-Morales et al. (2016) and Gupta et al. (2018):

> "Tlx1 and Tlx3, that are required for the specification of excitatory (glutamatergic) fates and these are only expressed in dorsal dI3, dI5 and DIL B cells"
>
> — Juárez-Morales et al. (2016)

> "the dP1 and dP3-5 domains express Atoh1 (arrowheads, B) and Ascl1 (arrowheads, C), respectively, in the E11.5 mouse embryo. The dP1 cells give rise to Lhx2 + dI1s while Isl1 + dI3s emerge from the dP3-5 population."
>
> — Gupta et al. (2018)

The general dorsal-progenitor → dorsal-interneuron framework into which the HDCA "DL" labels are presumed to map is summarised by Wang et al. (2021):

> "The dorsal part contains six dorsal progenitor (dP) domains (dP1-dP6) and then differentiate into the dorsal interneuron (dI) populations (dI1-dI6)."
>
> — Wang et al. (2021)

A verification of dI3 identity in the HDCA `DL3_NEURON` cluster would require checking that TLX1, TLX3, ISL1, LBX1 are co-expressed at the single-cell level — this evidence is not provided in the HDCA supplementary tables and is a question to raise with the HDCA authors.

## Location

`DL3_NEURON` cells are presumed to derive from the dorsal alar plate of the developing spinal cord, in the dI3 progenitor (dP3) domain (Wang et al., 2021; Gupta et al., 2018). All 9,242 cells were captured at Carnegie stages 13–14 from HDCA's whole-embryo scRNA-seq samples, which spans the period of peak dorsal interneuron neurogenesis in humans (Rayon et al., 2021). The HDCA atlas annotations assign organ = whole_embryo for this cluster (i.e. spatial assignment within the embryo was not refined further than "whole embryo" at this stage), so anatomical location within the spinal cord cannot be confirmed from the integrated atlas obs alone.

## Function (hypothesised, from canonical dI3 literature)

If the HDCA `DL3_NEURON` cluster corresponds to canonical dI3 interneurons, the expected function is excitatory (glutamatergic) commissural / local interneuron activity in cutaneous mechanosensory and limb-grip circuits (Lai et al., 2016; Sagner & Briscoe, 2019). The fate-decision logic involves TLX1/TLX3 specifying excitatory neurotransmitter identity (Juárez-Morales et al., 2016) and ISL1 driving dI3 differentiation (Gupta et al., 2018). Commissural axon guidance at this developmental stage involves Lhx1/Lhx9 control of rostral-versus-caudal turning (Avraham et al., 2009) and netrin/DCC-mediated midline crossing (Castellani, 2013). Sibling dorsal-interneuron classes use distinct neurotransmitter codes — e.g. dI4/dI6 are GABAergic and Lbx1-dependent (Gray de Cristoforis et al., 2020; Lu et al., 2015) — so a definitive functional assignment of `DL3_NEURON` would require neurotransmitter-gene (VGLUT2 / GAD1 / SLC32A1) profiling at the single-cell level in the HDCA data.

## Data provenance

Per-cell cross-tabulation of `refined_celltype × original_author_annotation × study` extracted from the HDCA zarr store (`hdca_v2_20260311_f2.zarr`; see `provenance_evidence.md` and `label_provenance.json`):

> "DL3_NEURON (n=9,242 cells): 100% from study=whole_embryo (HDCA de novo data, CS13-14); 1 single cell from Braun et al. 2022 bioRxiv (noise <0.01%). Original author label composition: 86.4% ...DL3 neuron..., 7.6% ...sensory neuron..., 4.0% ...pA3-4 neural progenitor..., 2.0% ...pA2 neural progenitor..."
>
> — Webb et al. (2026), source data + provenance_evidence.md

This is reported as neutral data-provenance context: the cluster is sourced entirely from HDCA's own whole-embryo scRNA-seq, the cells were originally labelled by HDCA's whole-embryo annotation pipeline, and the most common pre-clustering author label ("DL3 neuron", 86.4%) was carried over to the integrated `refined_celltype`. The remaining ~14% of cells were originally labelled "sensory neuron", "pA3-4 neural progenitor" or "pA2 neural progenitor" — consistent with the cluster sitting transcriptionally near both peripheral sensory neuron and dorsal-alar-plate progenitor pools at CS13–14.

Note that this cluster does **not** inherit annotations from Braun et al. (2023), despite HDCA Methods stating:

> "Central nervous system cells retained the original fine-grained annotations from Braun et al., as these annotations were informed by spatial context"
>
> — Webb et al. (2026), Methods

The DL/PA nomenclature is HDCA-internal, as documented in supplementary_findings.json:

> "The HDCA publication does not contain narrative discussion of the DL1-DL6 / PA1-PA4 clusters specifically; these labels appear only in Supplementary Tables 9 (markers + CL) and 16 (DEGs). The DL/PA nomenclature is HDCA-internal terminology not inherited from Braun et al. 2023, which uses Class/Subclass/Region taxonomy (Neuron/Radial glia/Neuroblast/Glioblast/Neuronal IPC) with no DL or PA labels."
>
> — Webb et al. (2026), source data + provenance_evidence.md

## Hypothesised correspondence to canonical dI3 — questions for HDCA authors

The HDCA paper does not contain narrative discussion of DL3_NEURON or any DL/PA cluster (supplementary_findings.json). The dI3 correspondence proposed in this report's name resolution rests on the cluster name ("DL3") and on the broad alignment of the cluster's pan-neuronal differentiation profile with the classical dorsal-spinal-cord interneuron taxonomy (Lai et al., 2016; Sagner & Briscoe, 2019; Wang et al., 2021; Gupta et al., 2018). It is **a hypothesis to discuss with HDCA**, not a marker-confirmed assignment. Specific questions:

1. Is the "DL" nomenclature intended to map 1:1 onto classical dI1–dI6 (i.e. DL3 ↔ dI3)? If so, which transcription factor codes were used to make the assignment during HDCA annotation?
2. Are TLX1, TLX3, ISL1, LBX1 expressed in `DL3_NEURON` cells at single-cell level? (These are not in the curated Supp. Table 9 signature.)
3. Why does the curated signature omit subtype-specifying TFs in favour of pan-neuronal differentiation markers — is this a consequence of the signature being chosen for cluster *discriminability* within the integrated atlas (where pan-neuronal markers may be the most cluster-specific within the CNS-spinal-neuron subspace), or for some other reason?
4. The original-author-label composition (86.4% "DL3 neuron", 7.6% "sensory neuron", 4.0% "pA3-4 neural progenitor", 2.0% "pA2 neural progenitor") suggests this cluster lies on a transcriptional manifold between dorsal interneurons, PNS sensory neurons, and dorsal-alar-plate progenitors — is this an expected feature of CS13–14 dorsal neurogenesis, or a clustering-resolution choice?

## Atlas annotation context

- **HDCA refined_celltype label:** `DL3_NEURON`
- **HDCA broad_celltype:** `CNS_SPINAL_NEURON`
- **HDCA systems / germlayer:** `NERVOUS_SYSTEM` / `ECTODERM`
- **HDCA Cell Ontology mapping (Supp. Table 9):** `CL:0000540` (neuron)
- **Co-annotation siblings:** DL1_NEURON, DL2_NEURON, DL5_NEURON, DL6_NEURON; PA1/PA2/PA3-4 neural progenitors
- **Cell composition:** 9,242 cells from HDCA whole-embryo scRNA-seq (CS13–14); see §Data provenance
- **Cell Ontology mapping (this report):** CL:0002611 (neuron of the dorsal spinal cord) — narrow match; a dI3-specific CL term does not exist and is flagged as an NTR candidate. This mapping is **contingent** on the dI3 correspondence hypothesis above being correct; if the cluster is in fact a broader differentiating dorsal-spinal-neuron pool, CL:0002611 remains the closest available term.

## References

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development". *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Braun E, Danan-Gotthold M, Borm LE, et al. (2023). "Comprehensive cell atlas of the first-trimester developing human brain". *Science 382*. DOI: [10.1126/science.adf1226](https://doi.org/10.1126/science.adf1226)
- Lai HC, Seal RP, Johnson JE (2016). "Making sense out of spinal cord somatosensory development". *Development 143:3434-3448*. DOI: [10.1242/dev.139592](https://doi.org/10.1242/dev.139592)
- Sagner A, Briscoe J (2019). "Establishing neuronal diversity in the spinal cord: a time and a place". *Development 146:dev182154*. DOI: [10.1242/dev.182154](https://doi.org/10.1242/dev.182154)
- Wang Y-F, Liu C, Xu P-F (2021). "Deciphering and reconstitution of positional information in the human brain development". *Cell Regen 10:29*. DOI: [10.1186/s13619-021-00091-7](https://doi.org/10.1186/s13619-021-00091-7)
- Gupta S, Sivalingam D, Hain S, et al. (2018). "Deriving Dorsal Spinal Sensory Interneurons from Human Pluripotent Stem Cells". *Stem Cell Rep 10:390-405*. DOI: [10.1016/j.stemcr.2018.02.013](https://doi.org/10.1016/j.stemcr.2018.02.013)
- Juárez-Morales JL, Schulte CJ, Pezoa SA, et al. (2016). "Evx1 and Evx2 specify excitatory neurotransmitter fates and suppress inhibitory fates through a Pax2-independent mechanism". *Neural Dev 11:5*. DOI: [10.1186/s12915-016-0227-8](https://doi.org/10.1186/s12915-016-0227-8)
- Gray de Cristoforis A, Ferrari F, Clotman F, Vogel T (2020). "Differentiation and localization of interneurons in the developing spinal cord depends on DOT1L expression". *Mol Brain 13:85*. DOI: [10.1186/s13041-020-00623-3](https://doi.org/10.1186/s13041-020-00623-3)
- Lu DC, Niu T, Alaynick WA (2015). "Molecular and cellular development of spinal cord locomotor circuitry". *Front Mol Neurosci 8:25*. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Castellani V (2013). "Building Spinal and Brain Commissures: Axon Guidance at the Midline". *ISRN Cell Biol 2013:315387*. DOI: [10.1155/2013/315387](https://doi.org/10.1155/2013/315387)
- Avraham O, Hadas Y, Vald L, et al. (2009). "Transcriptional control of axonal guidance and sorting in dorsal interneurons by the Lim-HD proteins Lhx9 and Lhx1". *Neural Dev 4:21*. DOI: [10.1186/1749-8104-4-13](https://doi.org/10.1186/1749-8104-4-13)
- Rayon T, Maizels RJ, Barrington C, Briscoe J (2021). "Single-cell transcriptome profiling of the human developing spinal cord reveals a conserved genetic programme with human-specific features". *Development 148:dev199711*. DOI: [10.1242/dev.198309](https://doi.org/10.1242/dev.198309)
