# DB1_NEURON — Dorsal (likely GABAergic, class-B / dI4-like) Spinal Interneuron

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human fetal spinal cord (neural-tube-derived CNS spinal neuron; whole-embryo dissociation at Carnegie stages CS13–CS14, samples F137/F147/F158)
Cell Ontology: [neuron of the dorsal spinal cord](http://purl.obolibrary.org/obo/CL_0002611) (CL:0002611, broad match — no exact CL term for an immature PAX2+/TFAP2+/GAD2+ dorsal spinal interneuron at this stage)

## Summary

In the HDCA v2 integrated reference, the refined cell-type label `DB1_NEURON` is one of HDCA's internal dorsal spinal interneuron classes (`DA = dorsal alar`, `DB = dorsal basal`, alongside ventral classes V0–V3 and the motor-neuron class) within the `CNS_SPINAL_NEURON` broad class, captured from de novo whole-embryo scRNA-seq of three Carnegie-stage 13–14 embryos (F137, F147, F158; n=6862 cells) (Webb et al., 2026). HDCA Supplementary Table 9 maps `DB1_NEURON` to the non-informative parent term `CL:0000540` (neuron) and lists a curated 20-gene top signature dominated by `PAX2`, `TFAP2A`, `TFAP2B`, `GAD2`, plus pan-neuronal microtubule / neurofilament / growth-cone genes (`DCX`, `INA`, `STMN2`, `NEFL`, `NEFM`, `TUBB4A`, `STMN4`, `KIF5C`, `DPYSL4`, `ELAVL3/4`, `SRRM4`, `BSCL2`) and the BMP-coreceptor / axon-guidance gene `RGMB`, `NGFR` and the rostral axial selector `HOXB2`. Statistical DEGs in Table 16 confirm this signature, with `PAX2` (logFC 6.7), `TFAP2B` (logFC 5.7), `HOXB2` (logFC 4.6) and `LAMP5` (logFC 6.9) among the strongest discriminators (Webb et al., 2026). The co-expression of `PAX2` + `TFAP2A` + `TFAP2B` + `GAD2` is the canonical molecular signature of inhibitory (GABAergic) dorsal-spinal interneurons of the class-B (PTF1A-dependent) lineage that generates dI4, dI6 and late-born dILA neurons (Helms & Johnson, 2003; Hori & Hoshino, 2012; Lu et al., 2015; Batista & Lewis, 2008; Zainolabidin et al., 2017). DB1 is absent from HDCA Supplementary Table 17 (PNS subset), confirming a CNS spinal-cord identity, and `HOXB2` enrichment places these cells at a rostral cervical / hindbrain–spinal-cord axial level. At CS13–14 the dorsal horn laminae have not yet formed and the cardinal dorsal classes dI1–dI6 / dILA–dILB are not transcriptionally resolved in HDCA, so DB1 is most accurately interpreted as an immature, postmitotic, dorsal-spinal GABAergic interneuron population rather than mapped one-to-one onto a single classical dI sub-class.

## Markers

### HDCA curated signature (Supplementary Table 9)

HDCA assigns refined_celltype `DB1_NEURON` to ontology term CL:0000540 and lists a curated 20-gene top signature for this population (Webb et al., 2026):

> "top_gene_signatures": "DCX,PAX2,INA,TFAP2A,STMN2,TFAP2B,NEFL,ELAVL3,RGMB,HOXB2,NGFR,TUBB4A,NEFM,GAD2,DPYSL4,ELAVL4,BSCL2,SRRM4,STMN4,KIF5C"
>
> — Webb et al. (2026), HDCA Supp. Table 9

This signature decomposes into four programmes. (i) **Inhibitory-neurotransmitter / dorsal-class-B selectors**: `PAX2`, `TFAP2A`, `TFAP2B` and the GABA-synthesising enzyme `GAD2` (glutamate decarboxylase 2, GAD65). PAX2 (with redundant PAX8) is the canonical specifier of GABAergic and glycinergic fates in multiple spinal inhibitory interneurons, and TFAP2A/TFAP2B act in parallel to direct PAX2+ interneuron differentiation (see Function and Specification sections below). (ii) **Immature-neuron microtubule / neurofilament / growth-cone genes**: `DCX` (doublecortin), `INA` (alpha-internexin), `STMN2` and `STMN4` (axonal microtubule dynamics), `NEFL`, `NEFM`, `TUBB4A`, `DPYSL4` (CRMP-4), `KIF5C` and `BSCL2` (seipin) — consistent with a recently postmitotic neuron with extending axons. (iii) **Pan-neuronal RNA-binding / splicing**: `ELAVL3` and `ELAVL4` (Hu-C/D) and the neural-specific splicing factor `SRRM4` (nSR100). (iv) **Patterning / signalling cues**: `RGMB` (a repulsive guidance molecule and BMP coreceptor implicated in dorsal patterning), `NGFR` (p75 neurotrophin receptor — expressed in early dorsally-derived class-B / dILA progenitors per Helms & Johnson, 2003) and `HOXB2` (a rostral axial selector).

### Statistical DEGs (Supplementary Table 16)

The top differentially-expressed genes from the integrated atlas confirm the curated signature with very large effect sizes. The canonical inhibitory-dorsal-interneuron marker `PAX2` is among the strongest DEGs:

> "gene": "PAX2", "score": 29.95546, "logfc": 6.7047534, "pval_adj": 2.85292348914248e-194
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "TFAP2B", "score": 29.100292, "logfc": 5.7421865, "pval_adj": 2.2654834797237e-183
>
> — Webb et al. (2026), HDCA Supp. Table 16

Other notable DEGs include `LAMP5` (a GABAergic interneuron marker; logFC 6.9, score 35.5), `HOXB2` (logFC 4.6, score 33.5), `DCX`, `INA`, `STMN2`, `NEFL`, `NEFM`, `TUBB3`, `TUBB4A`, `TAGLN3`, `CD24`, `GPC2`, `CRMP1`, `MAP1B`, `DPYSL4`, `NSG1`, `NREP`, `MLLT11`, `NGRN`, `GNG3` and `GDAP1L1`. The combination of strong `PAX2`, `TFAP2B`, `GAD2` and `LAMP5` against a pan-neuronal microtubule / neurofilament background is diagnostic of an inhibitory dorsal-spinal interneuron in its early postmitotic state.

> "gene": "HOXB2", "score": 33.547104, "logfc": 4.6282077, "pval_adj": 2.36832141721506e-243
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "LAMP5", "score": 35.50574, "logfc": 6.902095, "pval_adj": 2.55131381419273e-272
>
> — Webb et al. (2026), HDCA Supp. Table 16

### Classical correspondence: dorsal class-B (PAX2+/LBX1+/LHX1/5+) inhibitory lineage

The PAX2+/TFAP2+/GAD2+ molecular profile of DB1 maps directly onto the inhibitory dorsal-spinal interneuron lineage defined in mouse:

> "GABAergic neurons in the dorsal spinal cord are composed of early-born dI4 and dI6 and late-born dIL A neurons. These three classes of postmitotic interneurons express the HD transcription factor Lbx1, Pax2 and Lhx1/5"
>
> — Hori & Hoshino (2012)

> "The early born (E10.5-E11) dI4 interneurons become Pax2 + , Lhx1 + , and Lhx5 + GABAergic ipsilaterally projecting somatosensory associative neurons that migrate laterally to the deep dorsal horn"
>
> — Lu et al. (2015)

At CS13–14 the canonical sub-class markers that distinguish dI4 from dI6 (e.g. `DMRT3` for dI6; absence in dI4) and from late-born dILA (temporal markers) are not strongly expressed in DB1, so the cluster is best interpreted as a generic inhibitory class-B dorsal interneuron rather than as a single dI sub-class. The recent mouse dorsal-horn ontogeny atlas defines the cardinal classes by classical markers:

> "Group 1 was composed of the cardinal spinal cord neuron types clearly identified by classical marker genes including dI1 (Barhl2), dI2 (Foxd3+Slc17a6), dI3 (Isl1+Otp), dI4 (inhibitory Lbx1+ without Dmrt3), dI5 (Phox2a), dI6 (Dmrt3)"
>
> — Roome et al. (2026)

## Location

### CNS spinal cord (dorsal compartment), CS13–14, rostral bias

HDCA Supplementary Table 9 assigns DB1 to broad_celltype `CNS_SPINAL_NEURON`, germlayer `ECTODERM` and system `NERVOUS_SYSTEM` (Webb et al., 2026). DB1 is absent from Table 17 (the PNS subset), corroborating its CNS spinal-cord identity rather than a peripheral ganglion identity. The HDCA atlas paper itself draws the boundary explicitly:

> "Although somatic motor neurons contribute to peripheral nerve circuitry, they are neural tube–derived and therefore developmentally CNS in origin"
>
> — Webb et al. (2026)

Within the CNS_SPINAL_NEURON class, DB1's HDCA-internal name (`DB = dorsal basal`) and its PAX2+/TFAP2+/GAD2+ signature place it in the dorsal half of the spinal cord. Classical dorsoventral patterning establishes six dorsal progenitor domains (dP1–dP6) and produces the cardinal dorsal interneurons:

> "six early-born (in the mouse, by embryonic day E10-12.5) dorsal neuron populations called dI1-dI6 and two late-born (E11-E13) populations called dILA and dILB"
>
> — Helms & Johnson (2003)

The dorsal inhibitory dI4/dI6 + dILA classes migrate to specific destinations in the mature cord — dI4/dI5 to the deep dorsal horn (laminae IV–V) and dILA/dILB to the superficial laminae (I–III) — although at CS13–14 these migrations are not yet complete and laminar architecture has not yet formed. Onecut-factor work in mouse summarises the migratory destinations of the dorsal interneuron classes:

> "OC factors in multiple dIN subsets including excitatory (dI2, dI3 and dI5) or inhibitory (dI4 and dI6) populations, generated at various levels along DV axis of the neural tube (from dI2 to dI6), involved in modulating motor control (dI3, dI4, dI5 and dI6) or processing sensory information (dI2), and migrating to ventral (dI3, dI5 and dI6) or deep dorsal (dI2 to dI5) locations in the mature spinal cord"
>
> — Kabayiza et al. (2017)

### Rostral axial position (HOXB2)

The strong DEG `HOXB2` (logFC 4.6) and its inclusion in the curated Table 9 signature place DB1 at a rostral cervical / hindbrain–spinal junction axial level, consistent with the rostral bias of HDCA's whole-embryo CS13–14 samples. Lawrence et al. (2024), the principal HDCA subatlas of the human spine, directly maps dorsal HOX patterns to spinal axial position:

> "In the axial plane of the spinal cord, we find distinct patterns in the ventral and dorsal domains, providing insights into motor pool organisation and loss of collinearity in HOXB genes."
>
> — Lawrence et al. (2024)

### Developmental staging and complementary human references

DB1's 6862 cells were captured at CS13–14 (HsapDv:0000023 share 0.586; HsapDv:0000024 share 0.413) — substantially earlier than the human spinal-cord scRNA-seq references that mostly target later first-trimester or midgestation. Sagner & Briscoe (2019) describe the canonical patterning logic that gives rise to dorsal classes:

> "different types of neurons differentiate from transcriptionally distinct neural progenitors that are arrayed in discrete domains along the dorsal-ventral and anterior-posterior axes of the embryonic spinal cord"
>
> — Sagner & Briscoe (2019)

Rayon et al. (2021) provide the human first-trimester spinal-cord scRNA-seq reference and Delile et al. (2019) the conserved mouse temporal cascade. The Braun et al. (2023) first-trimester human brain atlas covers the rostral neural tube (hindbrain through forebrain) and provides the brain-side reference for HDCA neuronal annotations:

> "The adult human brain is divided into hundreds of spatial domains, each comprising tens or hundreds of distinct neuronal, glial, and other cell types. This complex arrangement of cells is initially established during the first trimester of development"
>
> — Braun et al. (2023)

## Function

### Inhibitory (GABAergic) neurotransmitter phenotype

The strongest functional inference for DB1_NEURON is its inhibitory neurotransmitter phenotype. The curated Table 9 signature includes `GAD2` (GAD65, one of the two enzymes synthesising GABA), and the inhibitory-interneuron marker `LAMP5` is a top Table 16 DEG (logFC 6.9). Together with PAX2/TFAP2A/TFAP2B, this defines a GABAergic identity. Direct functional evidence for PAX2's role in establishing this phenotype comes from Batista & Lewis (2008):

> "in zebrafish most glycinergic and many GABAergic spinal interneurons express Pax2a, Pax2b and Pax8 and that these transcription factors are redundantly required for the neurotransmitter fates of many of these cells"
>
> — Batista & Lewis (2008)

> "In mouse, Pax2 is required for correct specification of GABAergic interneurons in the dorsal horn"
>
> — Batista & Lewis (2008)

In the mouse and human dorsal cord, GABAergic dI4/dI6/dILA interneurons mediate presynaptic inhibition of primary sensory afferents and shape circuits for somatosensory processing and proprioceptive gating (Hori & Hoshino, 2012; Lu et al., 2015), although the precise circuit role of DB1 at CS13–14 is necessarily speculative because dorsal-horn circuits have not yet assembled.

### Axon outgrowth and immature neuronal cytoskeleton at CS13–14

The dominance of microtubule (`DCX`, `STMN2`, `STMN4`, `TUBB3`, `TUBB4A`, `MAP1B`, `DPYSL4`, `CRMP1`), neurofilament (`NEFL`, `NEFM`, `INA`) and growth-cone-adjacent (`GAP43`-class, axon-guidance `GPC2`) genes among DB1's curated signature and DEGs is consistent with a developmental window in which dorsal interneurons are actively extending axons towards their commissural / ipsilateral targets. `RGMB` (repulsive guidance molecule B) in the curated signature and `LAMP5` as a top DEG additionally implicate BMP coreceptor signalling and inhibitory-interneuron identity respectively (Webb et al., 2026).

## Developmental specification and structure

### Dorsoventral patterning and the class-B (PTF1A-dependent) progenitor lineage

Dorsal spinal interneurons originate from six progenitor domains (dP1–dP6) of the dorsal neural tube, patterned by graded BMP and Wnt signalling from the roof plate and class-defining bHLH selectors (ATOH1, NEUROG1/2, ASCL1, PTF1A) (Sagner & Briscoe, 2019; Helms & Johnson, 2003). The classical distinction between class-A and class-B dorsal interneurons separates roof-plate-dependent dI1–dI3 (glutamatergic, BARHL1/2, ISL1+) from PTF1A-dependent dI4/dI6 + dILA (GABAergic, PAX2+/LBX1+/LHX1/5+):

> "six early-born (in the mouse, by embryonic day E10-12.5) dorsal neuron populations called dI1-dI6 and two late-born (E11-E13) populations called dILA and dILB"
>
> — Helms & Johnson (2003)

> "A bHLH transcription factor Ptf1a plays a central role in the specification of these GABAergic inhibitory dorsal interneurons while suppressing the generation of excitatory glutamatergic interneurons"
>
> — Hori & Hoshino (2012)

DB1's molecular profile (PAX2+/TFAP2A+/TFAP2B+/GAD2+, in absence of strong BARHL/ATOH1/ISL1 or PHOX2A/LMX1B markers) places it firmly within this PTF1A-dependent class-B inhibitory lineage rather than the class-A excitatory lineage that gives rise to DA1–DA3 in HDCA's own naming.

### Postmitotic specification: PAX2 directs neurotransmitter fate, TFAP2A/B refine interneuron identity

Once PTF1A-dependent progenitors exit the cell cycle, PAX2 (with redundant PAX8) acts as the master switch for inhibitory neurotransmitter identity, while TFAP2A and TFAP2B refine GABAergic interneuron specification:

> "Pax2 is required for the maintained expression of Lhx1, Lhx5, Pax5, and Pax8"
>
> — Lu et al. (2015)

> "Tfap2A is expressed by all GABAergic neurons, whereas Tfap2B is selectively expressed by interneurons"
>
> — Zainolabidin et al. (2017)

> "we found a two-fold increase in the number of Pax2 + interneurons in Tfap2A-misexpressed cells relative to control"
>
> — Zainolabidin et al. (2017)

> "Tfap2B is necessary for the specification of cerebellar GABAergic interneurons"
>
> — Zainolabidin et al. (2017)

Although the Zainolabidin et al. work was carried out in the cerebellum, the same TFAP2A/TFAP2B → PAX2 logic acts in the dorsal-spinal class-B lineage, where TFAP2A and TFAP2B are co-expressed with PAX2 in the inhibitory progeny (Hori & Hoshino, 2012). DB1's curated co-expression of TFAP2A + TFAP2B + PAX2 + GAD2 thus provides a mechanistically coherent identity for a postmitotic inhibitory dorsal interneuron.

### Rostro-caudal HOX patterning and developmental timing

Rostro-caudal identity along the dorsoventral progenitor framework is imposed by a HOX code. HOXB2 enrichment in DB1 places these cells at a rostral cervical / hindbrain–spinal junction level — consistent with the rostral bias of HDCA's CS13–14 whole-embryo samples and with the Lawrence et al. (2024) finding of distinct dorsal HOXB patterns in the developing human spine (Lawrence et al., 2024). At CS13–14, dorsal neurogenesis is in its early postmitotic phase; the dorsal horn laminae have not yet formed and the late-born dILA/dILB classes (E11–E13 in mouse, equivalent later in human) have not yet been generated. This temporal context explains why DB1 expresses the inhibitory cassette (PAX2/TFAP2A/TFAP2B/GAD2) without yet expressing the sub-class-distinguishing markers (DMRT3 for dI6, PHOX2A for dI5, etc.) that would resolve it into a single classical dI sub-class.

### Cell-type vs circuit-module framing

Osseward & Pfaff (2019) and Gupta & Butler (2021) frame the value of cardinal dorsal interneuron classes for understanding circuit assembly and emphasise that single-cell transcriptional atlases reveal extensive sub-type heterogeneity within each cardinal class — heterogeneity that emerges over developmental time. DB1, at CS13–14, sits early on this trajectory: a transcriptionally coherent immature inhibitory dorsal-spinal interneuron pool that will later diversify into the inhibitory subtypes that mediate presynaptic inhibition and somatosensory gating in the mature dorsal horn (Gupta & Butler, 2021; Osseward & Pfaff, 2019).

## References

- HDCA consortium / Webb et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper)". *preprint (HDCA)*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Braun et al. (2023). "Comprehensive cell atlas of the first-trimester developing human brain". *Science*. DOI: [10.1126/science.adf1226](https://doi.org/10.1126/science.adf1226)
- Lawrence et al. (2024). "HOX gene expression in the developing human spine". *Nature Communications*. DOI: [10.1038/s41467-024-54257-3](https://doi.org/10.1038/s41467-024-54257-3)
- Sagner & Briscoe (2019). "Establishing neuronal diversity in the spinal cord: a time and a place". *Development*. DOI: [10.1242/dev.182154](https://doi.org/10.1242/dev.182154)
- Helms & Johnson (2003). "Specification of dorsal spinal cord interneurons". *Current Opinion in Neurobiology* 13(1):42-49.
- Lu, Niu & Alaynick (2015). "Molecular and cellular development of spinal cord locomotor circuitry". *Frontiers in Molecular Neuroscience*. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Hori & Hoshino (2012). "GABAergic Neuron Specification in the Spinal Cord, the Cerebellum, and the Cochlear Nucleus". *Neural Plasticity*. DOI: [10.1155/2012/921732](https://doi.org/10.1155/2012/921732)
- Zainolabidin et al. (2017). "Distinct Activities of Tfap2A and Tfap2B in the Specification of GABAergic Interneurons in the Developing Cerebellum". *Frontiers in Molecular Neuroscience*. DOI: [10.3389/fnmol.2017.00281](https://doi.org/10.3389/fnmol.2017.00281)
- Batista & Lewis (2008). "Pax2/8 act redundantly to specify glycinergic and GABAergic fates of multiple spinal interneurons". *Developmental Biology*. DOI: [10.1016/j.ydbio.2008.08.009](https://doi.org/10.1016/j.ydbio.2008.08.009)
- Kabayiza et al. (2017). "The Onecut Transcription Factors Regulate Differentiation and Distribution of Dorsal Interneurons during Spinal Cord Development". *Frontiers in Molecular Neuroscience*. DOI: [10.3389/fnmol.2017.00157](https://doi.org/10.3389/fnmol.2017.00157)
- Roome et al. (2026). "Ontogeny of the spinal cord dorsal horn". *Science*. DOI: [10.1126/science.adx5781](https://doi.org/10.1126/science.adx5781)
- Delile et al. (2019). "Single cell transcriptomics reveals spatial and temporal dynamics of gene expression in the developing mouse spinal cord". *Development*. DOI: [10.1242/dev.173807](https://doi.org/10.1242/dev.173807)
- Rayon et al. (2021). "Single-cell transcriptome profiling of the human developing spinal cord reveals a conserved genetic programme with human-specific features". *Development*. DOI: [10.1242/dev.199711](https://doi.org/10.1242/dev.199711)
- Gupta & Butler (2021). "Getting in touch with your senses: mechanisms specifying sensory interneurons in the dorsal spinal cord". *WIREs Mechanisms of Disease*. DOI: [10.1002/wsbm.1520](https://doi.org/10.1002/wsbm.1520)
- Osseward & Pfaff (2019). "Cell type and circuit modules in the spinal cord". *Current Opinion in Neurobiology*. DOI: [10.1016/j.conb.2019.04.003](https://doi.org/10.1016/j.conb.2019.04.003)
