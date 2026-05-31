# Dorsal Late 3 (DL3) Spinal Interneuron

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human fetal CNS spinal cord (CNS_SPINAL_NEURON, dorsal alar plate; whole-embryo dissociation at Carnegie stages 13-14, samples F137/F147/F158; HsapDv:0000023 55% + HsapDv:0000024 45%)
Cell Ontology: [neuron of the dorsal spinal cord](http://purl.obolibrary.org/obo/CL_0002611) (CL:0002611, narrow match — no dI3-specific CL term; cluster 86% pure, so a more specific NTR is not justified)

## Provenance and cluster purity (read first)

`DL3_NEURON` is a 100% HDCA whole-embryo de novo scRNA-seq cluster (n=9,242 cells from samples F137/F147/F158 at CS13-14; ArrayExpress E-MTAB-11504/11520/11911). It is **not** inherited from Braun et al. 2023 or any other subatlas — a single Braun cell present in the cluster is sub-0.01% noise (Webb et al., 2026; HDCA `label_provenance.json`).

**This cluster is impure.** Only 86.4% of cells carry the author label `DL3 neuron`; the remainder is 7.6% `sensory neuron`, 4.0% `pA3-4 neural progenitor`, and 2.0% `pA2 neural progenitor`:

> DL3_NEURON (n=9,242 cells): 100% from study=whole_embryo (HDCA de novo data, CS13-14); 1 single cell from Braun et al. 2022 bioRxiv (noise <0.01%). Original author label composition: 86.4% "DL3 neuron", 7.6% "sensory neuron", 4.0% "pA3-4 neural progenitor", 2.0% "pA2 neural progenitor".
>
> — Webb et al. (2026), HDCA v2 zarr obs cross-tab (`provenance_evidence.md`)

Two consequences follow. First, the 4% `pA3-4 neural progenitor` admixture indicates that **DL3 may not be fully separable from its progenitor pool** in the HDCA v2 integration: `pA3-4` is the HDCA-internal label for the candidate dorsal-alar progenitor (pallial/alar plate progenitor 3-4) of DL3, and the conjunction of DL3 with a small pA3-4 tail is consistent with a developmental continuum at CS13-14 rather than two cleanly separated states. Second, the 7.6% `sensory neuron` contamination reflects a well-documented molecular overlap between dI3/dI5 interneurons and second-order nociceptive / primary sensory afferents through shared TLX3 and PRRXL1 expression (Avraham et al., 2010; Section *Lineage relationship to sensory neurons* below).

The DL/PA naming is HDCA-internal: per `provenance_evidence.md`, DL = "dorsal late" interneuron and PA = dorsal-alar progenitor (pA1-pA4). The HDCA main text contains no narrative description of the DL/PA clusters:

> "The HDCA publication does not contain narrative discussion of the DL1-DL6 / PA1-PA4 clusters specifically; these labels appear only in Supplementary Tables 9 (markers + CL) and 16 (DEGs). The DL/PA nomenclature is HDCA-internal terminology not inherited from Braun et al. 2023, which uses Class/Subclass/Region taxonomy (Neuron/Radial glia/Neuroblast/Glioblast/Neuronal IPC) with no DL or PA labels."
>
> — Webb et al. (2026); HDCA `provenance_evidence.md`

Within the classical Helms & Johnson (2003) / Lai et al. (2016) / Sagner & Briscoe (2019) taxonomy, the most parsimonious correspondence for DL3 is the late-born wave of the **dI3 / dILA-3-like** Class A excitatory lineage (ISL1+/TLX3+/BRN3A+) — see below — though some sensory and progenitor cells co-cluster.

## Summary

`DL3_NEURON` is the third "dorsal late" interneuron cluster of the HDCA v2 spinal cord and most likely corresponds to the late-born / dILA-3-like wave of the canonical **dI3 Class A excitatory interneuron** lineage (Lu et al., 2015; Bui et al., 2015). The HDCA top signature for DL3 (Supp. Table 9) — `DCX,STMN2,INA,ELAVL4,RGMB,ELAVL3,NEFL,KIF5C,TUBB4A,CNTN2,CRABP1,NEFM,ATP1A3,NHLH2,DPYSL4,ADGRG1,NHLH1,MAP6,STMN4,SCG3` — is dominated by pan-postmitotic axonogenesis, neurofilament and tubulin machinery typical of newly born projection interneurons at CS13-14, but contains no dI3-specific selector (Webb et al., 2026). Classical assignment to dI3 rests on the broader literature consensus that this cohort is specified by `ISL1`+`TLX3`+`BRN3A/B (POU4F1/2)` and is glutamatergic with ipsilateral projections (Lu et al., 2015; Bui et al., 2015; Avraham et al., 2010; Gray de Cristoforis et al., 2020). Because the cluster is 86% pure, with 7.6% sensory contamination and 4% pA3-4 progenitor admixture, all dI3-specific properties below describe the dominant 86.4% subpopulation, not the cluster as a whole.

## Markers

### HDCA curated signature and DEGs

HDCA assigns refined_celltype `DL3_NEURON` to ontology term CL:0000540 (neuron) and a 20-gene top signature (Webb et al., 2026):

> "DCX,STMN2,INA,ELAVL4,RGMB,ELAVL3,NEFL,KIF5C,TUBB4A,CNTN2,CRABP1,NEFM,ATP1A3,NHLH2,DPYSL4,ADGRG1,NHLH1,MAP6,STMN4,SCG3"
>
> — Webb et al. (2026), HDCA Supp. Table 9

This signature reflects three postmitotic programmes typical of newly born projection interneurons at CS13-14 — axon outgrowth (`DCX`, `STMN2`, `CRABP1`, `STMN4`, `MAP6`), neuronal cytoskeleton (`NEFL`, `NEFM`, `INA`/α-internexin, `TUBB4A`), and general neuronal machinery (`ATP1A3`, `ELAVL3/4`, `SCG3`, `NHLH1/2`). The top-30 DEGs from Supp. Table 16 confirm this with very large effect sizes (`TUBB3` logFC 5.46, `CRABP1` 6.35, `STMN2` 4.78, `INA` 4.27, `NEFM` 4.49, `DCX` 4.07, `TAGLN3` 4.41) but are pan-neuronal and provide no dI3-versus-other-dorsal-interneuron-specific selector at this stage (Webb et al., 2026).

### Canonical dI3 transcription-factor fingerprint (used for the dI3 assignment)

The classical literature consensus for dI3 identity is the postmitotic combinatorial code `ISL1`+`TLX3`+`BRN3A/B`:

> "the dI3 IN population is well characterized by the expression of Brn3a/b, Tlx3, Gsh1/2, and Ascl1, amongst other transcription factors in progenitor and/or postmitotic cells derived from this population"
>
> — Bui et al. (2015)

> "they are characterized further by the expression of Isl1, a LIM homeodomain transcription factor that is also expressed in motoneurons but uniquely found in dI3 INs amongst neurons of the dorsal spinal cord"
>
> — Bui et al. (2015)

> "the dI1 interneurons express Lhx2/9, while dI2 and dI3 interneurons express Lhx1/5 and Isl1, respectively"
>
> — Zavvarian et al. (2020)

> "The dI3 pool also expresses Tlx3 (T-cell leukemia homeobox 3) and LIM-HD transcription factor Isl1-expressing cells"
>
> — Lu et al. (2015)

In the contemporaneous Roome et al. (2026) mouse dorsal-horn ontogeny atlas, dI3 is again identified by the same minimal `ISL1+OTP+` cassette:

> "Group 1 was composed of the cardinal spinal cord neuron types clearly identified by classical marker genes including dI1 (Barhl2), dI2 (Foxd3+Slc17a6), dI3 (Isl1+Otp), dI4 (inhibitory Lbx1+ without Dmrt3), dI5 (Phox2a), dI6 (Dmrt3)"
>
> — Roome et al. (2026)

`TLX3` is the Class A excitatory neurotransmitter selector shared by dI3 and dI5:

> "Both dI3 and dI5 excitatory interneurons express TLX3 as fate determinant."
>
> — Gray de Cristoforis et al. (2020)

> "Tlx3 functions cell-autonomously to specify a glutamatergic neurotransmitter phenotype"
>
> — Lu et al. (2015)

At CS13-14 the dominant HDCA DL3 programme is general postmitotic neurogenesis machinery rather than the late-onset peptidergic and circuit-specialised genes that arise in postnatal dI3; `ISL1` itself does not appear in the top-30 DEGs of DL3 at this stage, and the dI3-versus-sibling distinction therefore rests on classical-literature assignment rather than HDCA DEGs alone.

## Location

### CNS dorsal alar spinal cord, deep dorsal horn / intermediate laminae

HDCA assigns `DL3_NEURON` to broad_celltype `CNS_SPINAL_NEURON`, germlayer `ECTODERM`, system `NERVOUS_SYSTEM` and organ `whole_embryo` (Webb et al., 2026):

> "broad_celltype=CNS_SPINAL_NEURON, germlayer=ECTODERM, systems=NERVOUS_SYSTEM, organ=whole_embryo, scope=fetal, n_cells=9242"
>
> — Webb et al. (2026), HDCA co-annotation

The cluster is absent from HDCA Supp. Table 17 (the PNS subset), confirming CNS identity rather than a peripheral DRG identity — important because the 7.6% sensory admixture noted above could otherwise be misread as a peripheral assignment.

In mouse, the mature dI3 lineage migrates ventrally from the pdA3/pd3 progenitor domain to laminae V-VII of the deep dorsal horn and intermediate spinal cord:

> "The dI3 neurons are excitatory interneurons in the deep dorsal horn and intermediate spinal cord"
>
> — Lu et al. (2015)

> "Conditional expression of yellow fluorescent protein by Isl1 has been used to determine that dI3 INs are primarily located in laminae V-VII at similar densities in cervical and lumbar spinal segments"
>
> — Bui et al. (2015)

> "At e11.5, the number of control dI3 interneurons had increased and cells were distributed as a lateral stream extending from the pdI3 position to intermediate dorsoventral levels of the spinal cord"
>
> — Kabayiza et al. (2017)

> "dI3 and dI5 interneurons use different migratory paths, where dI3 migrates ventrally, while dI5 settles in the dorsal horn"
>
> — Gray de Cristoforis et al. (2020)

Because HDCA DL3 is sampled at CS13-14 (before columnar / laminar consolidation), these laminar coordinates apply to the mature dI3 endpoint; the HDCA cells correspond molecularly to the freshly postmitotic / late-wave dI3 cohort that is beginning the lateral/ventral migratory stream described by Kabayiza et al. (2017).

### Rostro-caudal spatial context in the developing human spine

The human-specific axial context is provided by Lawrence et al. (2024) — one of the HDCA subatlases:

> "In the axial plane of the spinal cord, we find distinct patterns in the ventral and dorsal domains, providing insights into motor pool organisation and loss of collinearity in HOXB genes."
>
> — Lawrence et al. (2024)

## Function

### Excitatory, ipsilateral, sensorimotor-integrating interneuron

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

### Axon trajectory

> "dI3 axons are projected ipsilaterally along two longitudinal fascicules at the ventral lateral funiculus (VLF) and the dorsal funiculus (DF)."
>
> — Avraham et al. (2010)

> "They have axons that project rostrally, ipsilaterally, and longitudinally in two fascicles."
>
> — Lu et al. (2015)

### Role in motor recovery (mature stage; not directly captured by HDCA CS13-14)

Postnatal mouse work has established a specialised role for the mature dI3 lineage in motor-system plasticity after spinal cord injury:

> "We demonstrate that while dI3 interneurons are not necessary for normal locomotor activity, locomotor circuits rhythmically inhibit them and dI3 interneurons can activate these circuits."
>
> — Bui et al. (2016)

> "Removing dI3 interneurons from spinal microcircuits by eliminating their synaptic transmission left locomotion more or less unchanged, but abolished functional recovery, indicating that dI3 interneurons are a necessary cellular substrate for motor system plasticity following transection."
>
> — Bui et al. (2016)

These postnatal mouse properties are not directly observed in HDCA CS13-14 transcriptomes, where the dominant programme is axonogenesis and cytoskeletal assembly.

## Developmental specification

### Origin in the pdA3 / pd3 progenitor domain (Class A, roof-plate-dependent)

dI3 is one of six early-born dorsal interneuron classes, generated from the third Class A progenitor domain:

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

The HDCA-internal name "pA3-4" denotes the dorsal-alar progenitor domain immediately upstream of DL3 (and DL4); the 4% `pA3-4 neural progenitor` admixture inside the DL3 cluster is consistent with this progenitor-to-postmitotic-neuron developmental continuity. Human-iPSC differentiation work has confirmed the equivalent specification logic:

> "the dP1 and dP3-5 domains express Atoh1 (arrowheads, B) and Ascl1 (arrowheads, C), respectively, in the E11.5 mouse embryo. The dP1 cells give rise to Lhx2 + dI1s while Isl1 + dI3s emerge from the dP3-5 population."
>
> — Gupta et al. (2018)

### Migration and Onecut-factor regulation

The ventrally directed dI3 migratory stream is modulated by Onecut transcription factors:

> "we detected OC factors in multiple dIN subsets including excitatory (dI2, dI3 and dI5) or inhibitory (dI4 and dI6) populations"
>
> — Kabayiza et al. (2017)

> "the dI3 population in the central intermediate region of the spinal cord, with a few dI3 cells migrating towards the floor plate"
>
> — Kabayiza et al. (2017)

### Postmitotic LIM-homeodomain code: ISL1 imposes the ipsilateral axon-turning behaviour

> "Loss and gain of function of the Lim-HD protein Isl1 demonstrate that Isl1 is not required for dI3 cell fate. However, Isl1 is sufficient to impose ipsilateral turning along the motor axons when expressed ectopically in the commissural dI1"
>
> — Avraham et al. (2010)

### Lineage relationship to sensory neurons — explains the 7.6% sensory admixture

A diagnostic complication of dI3 is its molecular overlap with second-order nociceptive neurons and with primary sensory afferents of the DRG, mediated by shared expression of `TLX3` and `PRRXL1`:

> "dI3 and dI5 neurons are considered to be nociceptive secondorder sensory neurons"
>
> — Avraham et al. (2010)

> "both populations express transcription factors that are shared by the primary afferent and second-order nociceptive neurons, Tlx3 and PrrxL1"
>
> — Avraham et al. (2010)

This shared cassette is the most parsimonious explanation for the 7.6% `sensory neuron` admixture documented in the DL3 author-label composition (`provenance_evidence.md`) and motivates the HDCA decision to conservatively pre-assign DL3 to the parent term CL:0000540 (neuron) rather than to a more specific peripheral identity. The cluster is anchored as CNS by its `CNS_SPINAL_NEURON` broad_celltype assignment and its absence from the PNS supplementary subset.

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
- Lawrence JEG et al. (2024). "HOX gene expression in the developing human spine". *Nature Communications*. DOI: [10.1038/s41467-024-54187-0](https://doi.org/10.1038/s41467-024-54187-0)
- Gupta S, Sivalingam D, Hain S, et al. (2018). "Deriving Dorsal Spinal Sensory Interneurons from Human Pluripotent Stem Cells". *Stem Cell Reports* 10:390-405. DOI: [10.1016/j.stemcr.2018.02.013](https://doi.org/10.1016/j.stemcr.2018.02.013)
- Lai HC, Seal RP, Johnson JE (2016). "Making sense out of spinal cord somatosensory development". *Development* 143:3434-3448. DOI: [10.1242/dev.139592](https://doi.org/10.1242/dev.139592)
- Sagner A, Briscoe J (2019). "Establishing neuronal diversity in the spinal cord: a time and a place". *Development* 146:dev182154. DOI: [10.1242/dev.182154](https://doi.org/10.1242/dev.182154)
