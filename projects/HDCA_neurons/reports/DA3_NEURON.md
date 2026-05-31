# Dorsal Alar 3 (DA3) Spinal Interneuron

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human fetal spinal cord (CNS_SPINAL_NEURON, dorsal alar plate; whole-embryo dissociation at Carnegie stages 13-14, samples F137/F147/F158; HsapDv:0000023 65% + HsapDv:0000024 35%)
Cell Ontology: [neuron of the dorsal spinal cord](http://purl.obolibrary.org/obo/CL_0002611) (CL:0002611, narrow match — no dI3-specific CL term; NTR drafted)

## Summary

In the HDCA v2 integrated reference, the cell-type label `DA3_NEURON` is the third dorsal-alar interneuron class (`DA3`) of the developing CNS spinal cord and resolves to the canonical **dI3 / Class A excitatory ipsilateral interneuron** of classical spinal-cord patterning (Helms & Johnson, 2003; Lai et al., 2016; Sagner & Briscoe, 2019). The HDCA notes for this dataset state that the DA1-3 / DB1 / V0-V3 naming follows that classical taxonomy:

> "HDCA whole-embryo de novo scRNA-seq (samples F137/F147/F158 at CS13-14); naming follows classical spinal cord interneuron taxonomy (Helms & Johnson 2003; Lai et al. 2016; Sagner & Briscoe 2019). DA = dorsal alar, DB = dorsal basal, V0-V3 = ventral interneuron classes V0-V3 (V0 commissural, V1 Engrailed-1+ ipsilateral, V2 Chx10+/Gata3+, V3 Sim1+ commissural)."
>
> — Webb et al. (2026), HDCA notes

DA3 is captured at n=9,211 cells almost entirely from HDCA whole-embryo CS13-14 samples and is assigned to broad_celltype `CNS_SPINAL_NEURON`, germlayer `ECTODERM`, organ `whole_embryo` (Webb et al., 2026). Its curated marker signature (Supp. Table 9) includes the LIM-homeodomain selector `ISL1`-pathway gene context together with the **dI3/dI5 Class-A excitatory determinant `TLX3`** and pan-neuronal axonogenesis genes (`GAP43`, `DCX`, `STMN2`, `NEFL`, `NEFM`, `INA`, `TUBB4A`) — a profile that matches the postmitotic ISL1+/TLX3+ dI3 fingerprint documented across mouse and chick (Lu et al., 2015; Gray de Cristoforis, 2020; Bui et al., 2015; Avraham et al., 2010). Because DA3 is sampled at the earliest, deeply embryonic stages (CS13-14, ~32-33 dpc), this report restricts conclusions to early developmental identity (specification, migration, axon outgrowth) and avoids over-extrapolation to mature deep-dorsal-horn microcircuit behaviour, which is described in postnatal mouse studies.

## Markers

### HDCA curated signature (Supplementary Table 9)

HDCA assigns the refined_celltype `DA3_NEURON` to ontology term CL:0000540 (neuron) and lists a curated 20-gene top signature (Webb et al., 2026):

> "GAP43,DCX,INA,NEFL,STMN2,TH,TFAP2A,TUBB4A,TLX3,BSCL2,NEFM,RAB3A,KIF5C,ATP1A3,ENO2,RTN1,ELAVL4,GNG3,CRABP1,SRRM4"
>
> — Webb et al. (2026), HDCA Supp. Table 9

The diagnostic feature in this list is **`TLX3`**, the Class-A excitatory fate determinant shared by dI3 and dI5 dorsal interneurons:

> "Both dI3 and dI5 excitatory interneurons express TLX3 as fate determinant."
>
> — Gray de Cristoforis et al. (2020)

> "Tlx3 functions cell-autonomously to specify a glutamatergic neurotransmitter phenotype"
>
> — Lu et al. (2015)

The remainder of the signature reflects three postmitotic programmes typical of newly born projection interneurons at CS13-14: (i) axon outgrowth and growth-cone biology (`GAP43`, `DCX`, `STMN2`, `CRABP1`), (ii) neuronal cytoskeleton (the type-IV intermediate filaments `NEFL`, `NEFM`, `INA`/α-internexin, and tubulins `TUBB4A`, `TUBA1A`, `TUBB2B`), and (iii) general neuronal/secretory machinery (`RAB3A`, `ATP1A3`, `ENO2`, `GNG3`). Together with `TLX3`, these are precisely the features expected from a Class-A excitatory dorsal interneuron undergoing initial axonogenesis.

### Statistical DEGs (Supplementary Table 16)

The top differentially expressed genes from the integrated atlas confirm the curated signature with very large effect sizes — `TUBB3` (logFC 5.51), `NEFM` (logFC 5.99), `TAGLN3` (logFC 4.53), `INA` (logFC 4.91), `NEFL` (logFC 5.67), `STMN2` (logFC 5.39), `CRABP1` (logFC 6.55), `DCX` (logFC 3.96), `TFAP2A` (logFC 5.43), `TUBB4A` (logFC 4.41), `GAP43` (logFC 4.47) — a pan-neuronal axon-outgrowth signature with no DEGs uniquely diagnostic for dI3 versus other early-born dorsal interneuron classes (Webb et al., 2026, Supp. Table 16). The selector that distinguishes DA3 from its DA1/DA2/DL siblings is the curated marker `TLX3`, not any of the DEGs.

### Canonical dI3 transcription-factor fingerprint

The literature canon for dI3 identity is the combinatorial postmitotic code `ISL1` + `TLX3` + `BRN3A/BRN3B (POU4F1/2)` + `LBX1`-negative:

> "the dI3 IN population is well characterized by the expression of Brn3a/b, Tlx3, Gsh1/2, and Ascl1, amongst other transcription factors in progenitor and/or postmitotic cells derived from this population"
>
> — Bui et al. (2015)

> "they are characterized further by the expression of Isl1, a LIM homeodomain transcription factor that is also expressed in motoneurons but uniquely found in dI3 INs amongst neurons of the dorsal spinal cord"
>
> — Bui et al. (2015)

> "the dI1 interneurons express Lhx2/9, while dI2 and dI3 interneurons express Lhx1/5 and Isl1, respectively"
>
> — Zavvarian et al. (2020)

In the contemporaneous Roome et al. (2026) mouse dorsal-horn ontogeny atlas, dI3 is again identified by the same minimal cassette:

> "Group 1 was composed of the cardinal spinal cord neuron types clearly identified by classical marker genes including dI1 (Barhl2), dI2 (Foxd3+Slc17a6), dI3 (Isl1+Otp), dI4 (inhibitory Lbx1+ without Dmrt3), dI5 (Phox2a), dI6 (Dmrt3)"
>
> — Roome et al. (2026)

At CS13-14, the HDCA DA3 transcriptional state is dominated by general postmitotic neurogenesis machinery rather than the late-onset peptidergic and circuit-specialised genes that arise in postnatal dI3; consequently the discriminating signal in the HDCA data is the curated `TLX3` (and accompanying class-A context), with `ISL1` itself not appearing in the top-30 DEGs at this stage.

## Location

### CNS dorsal alar spinal cord, deep dorsal horn / intermediate laminae

HDCA assigns `DA3_NEURON` to broad_celltype `CNS_SPINAL_NEURON`, germlayer `ECTODERM`, system `NERVOUS_SYSTEM` and organ `whole_embryo` (Webb et al., 2026):

> "broad_celltype=CNS_SPINAL_NEURON, germlayer=ECTODERM, systems=NERVOUS_SYSTEM, organ=whole_embryo, scope=fetal, n_cells=9211"
>
> — Webb et al. (2026), HDCA co-annotation

The cells are absent from HDCA Supplementary Table 17 (the PNS subset), confirming a CNS spinal-cord identity rather than a peripheral DRG identity — important because dI3 neurons share their `ISL1+/TLX3+` fingerprint with primary sensory neurons of the DRG, and incomplete cluster separation in earlier HDCA versions could have created a sensory-neuron admixture. (Indeed, the sibling cluster `DL3_NEURON`, which captures the late-born / more mature wave of dI3, carries a 7.6% sensory-neuron admixture in its `original_author_annotation` composition; the early-born DA3 wave does not.)

In mouse, the dI3 lineage migrates ventrally from the pdA3/pd3 progenitor domain during E10.5-E12.5 to settle in laminae V-VII of the deep dorsal horn and intermediate spinal cord:

> "The dI3 neurons are excitatory interneurons in the deep dorsal horn and intermediate spinal cord"
>
> — Lu et al. (2015)

> "Conditional expression of yellow fluorescent protein by Isl1 has been used to determine that dI3 INs are primarily located in laminae V-VII at similar densities in cervical and lumbar spinal segments"
>
> — Bui et al. (2015)

> "At e11.5, the number of control dI3 interneurons had increased and cells were distributed as a lateral stream extending from the pdI3 position to intermediate dorsoventral levels of the spinal cord"
>
> — Kabayiza et al. (2017)

> "consistent with their final location in the deep dorsal horn and in the intermediate laminae"
>
> — Kabayiza et al. (2017)

> "dI3 and dI5 interneurons use different migratory paths, where dI3 migrates ventrally, while dI5 settles in the dorsal horn"
>
> — Gray de Cristoforis et al. (2020)

Because the HDCA DA3 cells are sampled at CS13-14 (well before columnar / laminar consolidation), these laminar coordinates apply to the *mature* dI3 endpoint rather than the developmental snapshot in HDCA; the HDCA cells correspond molecularly to the freshly postmitotic dI3 cohort that is just beginning the lateral/ventral migratory stream described by Kabayiza et al. (2017).

### Rostro-caudal coverage in the developing human spine

The human-specific spatial context for the DA3 cluster is provided by Lawrence et al. (2024) — one of the HDCA subatlases — which mapped HOX-coded segmental identity along the developing human spine using spatial transcriptomics and in-situ sequencing:

> "In the axial plane of the spinal cord, we find distinct patterns in the ventral and dorsal domains, providing insights into motor pool organisation and loss of collinearity in HOXB genes."
>
> — Lawrence et al. (2024)

## Function

### Excitatory, ipsilateral, sensorimotor-integrating interneuron class

The mature dI3 lineage is glutamatergic, ipsilaterally projecting, and forms direct sensorimotor connections in the deep dorsal horn / intermediate cord:

> "dI3 INs are predominantly glutamatergic with ipsilateral projections"
>
> — Bui et al. (2015)

> "Retrograde tracing of synaptic inputs to motoneurons using modified rabies virus demonstrated that dI3 INs directly contact motoneurons in the spinal cord"
>
> — Bui et al. (2015)

> "These cells target motor neurons monosynaptically, as revealed by recent rabies tracing experiments"
>
> — Lu et al. (2015)

> "In mice model, dl3 appears to convey input from low threshold cutaneous afferents to the motor neurons that is critical in hand/forelimb grip"
>
> — Lu et al. (2015)

### Axon trajectory: two ipsilateral fascicles in DF and VLF

The axonal trajectory of dI3 cells has been mapped in chick by Avraham and colleagues. Although DA3 in HDCA is sampled at a stage where axons are only beginning to extend, the trajectory is established as a defining property of the lineage:

> "dI3 axons are projected ipsilaterally along two longitudinal fascicules at the ventral lateral funiculus (VLF) and the dorsal funiculus (DF)."
>
> — Avraham et al. (2010)

> "They have axons that project rostrally, ipsilaterally, and longitudinally in two fascicles."
>
> — Lu et al. (2015)

### Role in motor recovery (mature stage; not directly captured by HDCA CS13-14)

For completeness, postnatal mouse work has established a specialised role for the mature dI3 lineage in motor-system plasticity after spinal cord injury (Bui et al., 2016):

> "We demonstrate that while dI3 interneurons are not necessary for normal locomotor activity, locomotor circuits rhythmically inhibit them and dI3 interneurons can activate these circuits."
>
> — Bui et al. (2016)

> "Removing dI3 interneurons from spinal microcircuits by eliminating their synaptic transmission left locomotion more or less unchanged, but abolished functional recovery, indicating that dI3 interneurons are a necessary cellular substrate for motor system plasticity following transection."
>
> — Bui et al. (2016)

> "We suggest that dI3 interneurons compare inputs from locomotor circuits with sensory afferent inputs to compute sensory prediction errors that then modify locomotor circuits to effect motor recovery."
>
> — Bui et al. (2016)

These properties pertain to the fully mature postnatal mouse dI3 and are not directly observed in HDCA CS13-14 transcriptomes, where the dominant programme is axonogenesis and cytoskeletal assembly rather than circuit-specific connectivity.

## Developmental specification

### Origin in the pdA3 / pd3 progenitor domain (Class A, roof-plate-dependent)

dI3 is one of six early-born dorsal interneuron classes (dI1-dI6) generated between E10 and E11.5 in mouse from six progenitor domains (pdA1/2/3 = pd1/2/3 = Class A "alar", roof-plate-dependent; pdB1/2/3 = pd4/5/6 = Class B "basal", roof-plate-independent):

> "dI3 INs represent one of six identified, early born, dorsally derived populations of INs (dI1-dI6) of the spinal cord"
>
> — Bui et al. (2015)

> "There are eight classes of dorsally-derived interneurons, dI1 to dI6 as well as dILA and dILB, arising from seven progenitor cells"
>
> — Zavvarian et al. (2020)

> "Although these interneurons originate from the dorsal region, some migrate ventrally during development. These cells are generated sequentially in early, mid, and late phases. The early phased interneurons include dI1 to dI3 and are generated from pd1 to pd3 progenitor cells, respectively."
>
> — Zavvarian et al. (2020)

> "The third dorsal class marked by OLIG3 is dI3, a subpopulation that shares excitatory fate with the more ventrally localized dI5 interneurons"
>
> — Gray de Cristoforis et al. (2020)

The HDCA DA1/DA2/DA3 (= dI1/dI2/dI3) labels correspond to the Class A "alar" cohort and the DB1 (= dI6 / dB1) label to the Class B "basal" inhibitory class, with the late-born dILA/dILB superficial-laminae pool likely captured by the sibling DL1-DL6 clusters.

### Postmitotic LIM-homeodomain code: ISL1 and TLX3 specify glutamatergic dI3 fate

Once pdA3 progenitors exit the cell cycle they switch on an ISL1+/TLX3+/BRN3A+ postmitotic code that distinguishes them from the closely related dI5 (which retains TLX3 but lacks ISL1):

> "The dI3 pool also expresses Tlx3 (T-cell leukemia homeobox 3) and LIM-HD transcription factor Isl1-expressing cells"
>
> — Lu et al. (2015)

> "Tlx3 functions cell-autonomously to specify a glutamatergic neurotransmitter phenotype"
>
> — Lu et al. (2015)

ISL1 is doubly important for dI3 — it is shared with motor neurons (and is the only LIM-HD factor expressed in both dorsal interneurons and MNs), and it determines the ipsilateral axon-turning behaviour that defines dI3 anatomy:

> "Loss and gain of function of the Lim-HD protein Isl1 demonstrate that Isl1 is not required for dI3 cell fate. However, Isl1 is sufficient to impose ipsilateral turning along the motor axons when expressed ectopically in the commissural dI1"
>
> — Avraham et al. (2010)

### Migration and Onecut-factor regulation

The migratory behaviour of dI3 — a ventrally directed stream from the pdA3 domain to laminae V-VII — is modulated by Onecut (HNF6/OC-2/OC-3) transcription factors and by DOT1L-mediated H3K79 methylation:

> "we detected OC factors in multiple dIN subsets including excitatory (dI2, dI3 and dI5) or inhibitory (dI4 and dI6) populations"
>
> — Kabayiza et al. (2017)

> "the dI3 population in the central intermediate region of the spinal cord, with a few dI3 cells migrating towards the floor plate"
>
> — Kabayiza et al. (2017)

### Lineage relationship to sensory neurons and overlap caveat

A diagnostic complication of dI3 is its molecular overlap with second-order nociceptive neurons and with primary sensory afferents of the DRG, mediated by shared expression of `TLX3` and `PrrxL1`:

> "dI3 and dI5 neurons are considered to be nociceptive secondorder sensory neurons"
>
> — Avraham et al. (2010)

> "both populations express transcription factors that are shared by the primary afferent and second-order nociceptive neurons, Tlx3 and PrrxL1"
>
> — Avraham et al. (2010)

This shared cassette likely explains the 7.6% "sensory neuron" admixture documented in the sibling `DL3_NEURON` cluster's author-label composition (`provenance_evidence.md`) and motivates the HDCA decision to conservatively pre-assign DA3 to the parent term CL:0000540 (neuron) rather than to a more specific peripheral identity. The HDCA DA3 cluster itself is anchored as CNS by its CNS_SPINAL_NEURON broad_celltype assignment and its absence from the PNS supplementary subset (Webb et al., 2026).

## References

- HDCA consortium / Webb et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development". *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Lu DC, Niu T, Alaynick WA (2015). "Molecular and cellular development of spinal cord locomotor circuitry". *Frontiers in Molecular Neuroscience* 8:25. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Gray de Cristoforis A, Ferrari F, Clotman F, Vogel T (2020). "Differentiation and localization of interneurons in the developing spinal cord depends on DOT1L expression". *Molecular Brain* 13:85. DOI: [10.1186/s13041-020-00623-3](https://doi.org/10.1186/s13041-020-00623-3)
- Bui TV, Stifani N, Panek I, Farah C (2015). "Genetically identified spinal interneurons integrating tactile afferents for motor control". *Journal of Neurophysiology* 114:3050-3063. DOI: [10.1152/jn.00522.2015](https://doi.org/10.1152/jn.00522.2015)
- Avraham O, Hadas Y, Vald L, Hong S, Song M-R, Klar A (2010). "Motor and Dorsal Root Ganglion Axons Serve as Choice Points for the Ipsilateral Turning of dI3 Axons". *Journal of Neuroscience* 30:15546-15557. DOI: [10.1523/JNEUROSCI.2380-10.2010](https://doi.org/10.1523/JNEUROSCI.2380-10.2010)
- Bui TV, Stifani N, Akay T, Brownstone RM (2016). "Spinal microcircuits comprising dI3 interneurons are necessary for motor functional recovery following spinal cord transection". *eLife* 5:e21715. DOI: [10.7554/eLife.21715](https://doi.org/10.7554/eLife.21715)
- Kabayiza KU, Masgutova G, Harris A, Rucchin V, Jacob B, Clotman F (2017). "The Onecut Transcription Factors Regulate Differentiation and Distribution of Dorsal Interneurons during Spinal Cord Development". *Frontiers in Molecular Neuroscience* 10:157. DOI: [10.3389/fnmol.2017.00157](https://doi.org/10.3389/fnmol.2017.00157)
- Zavvarian MM, Hong J, Fehlings MG (2020). "The Functional Role of Spinal Interneurons Following Traumatic Spinal Cord Injury". *Frontiers in Cellular Neuroscience* 14:127. DOI: [10.3389/fncel.2020.00127](https://doi.org/10.3389/fncel.2020.00127)
- Roome RB, Yadav A, Flores L, et al. (2026). "Ontogeny of the spinal cord dorsal horn". *Science* 391:eadx5781. DOI: [10.1126/science.adx5781](https://doi.org/10.1126/science.adx5781)
- Lai HC, Seal RP, Johnson JE (2016). "Making sense out of spinal cord somatosensory development". *Development* 143:3434-3448. DOI: [10.1242/dev.139592](https://doi.org/10.1242/dev.139592)
- Sagner A, Briscoe J (2019). "Establishing neuronal diversity in the spinal cord: a time and a place". *Development* 146:dev182154. DOI: [10.1242/dev.182154](https://doi.org/10.1242/dev.182154)
- Lawrence JEG et al. (2024). "HOX gene expression in the developing human spine". *Nature Communications*. DOI: [10.1038/s41467-024-54187-0](https://doi.org/10.1038/s41467-024-54187-0)
