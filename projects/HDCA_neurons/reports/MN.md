# Motor Neuron (MN)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human fetal spinal cord (neural-tube-derived CNS spinal neuron; whole-embryo dissociation at CS13–CS14, samples F137/F147/F158)
Cell Ontology: [spinal cord motor neuron](http://purl.obolibrary.org/obo/CL_0011001) (CL:0011001, exact match)

## Summary

In the HDCA v2 integrated reference, the cell-type label `MN` resolves to spinal somatic motor neurons (motor neuron, CL:0000100) within the CNS_SPINAL_NEURON broad class, captured from de novo whole-embryo scRNA-seq of three Carnegie-stage 13–14 embryos (F137, F147, F158; n=7984 cells) (Webb et al., 2026). HDCA Supplementary Table 9 lists a curated motor-neuron signature dominated by neurofilaments, growth-cone and axonogenesis genes (`GAP43, INA, DCX, MAPT, L1CAM, NEFL, STMN2, NGFR, SLIT3, RAB3A, ENO2, ATP1A3, SLIT2, RTN1, TUBB4A, NEFM, SNCG, BSCL2, KIF5C, ECEL1`), with statistical DEGs in Table 16 confirming `NEFL`, `NEFM`, `INA`, `STMN2`, `DCX`, `TUBB3` and the classical motor-neuron-enriched gene `ECEL1` as the top discriminators (Webb et al., 2026). These cells are neural-tube-derived CNS neurons of the ventral spinal cord that ultimately become cholinergic, project to skeletal muscle via the neuromuscular junction, and are specified at the pMN progenitor domain by the combinatorial activity of OLIG2, NKX6.1 and PAX6 followed by postmitotic expression of ISL1, LHX3 and MNX1/HB9 (Pfaff et al., 1996; Ericson et al., 1997; Mazzoni et al., 2013). Motor-pool subtype identity along the rostro-caudal axis is then refined by an instructional HOX code overlaid on these LIM-homeodomain selectors (Allan & Thor, 2015; Lawrence et al., 2024).

## Markers

### HDCA curated signature (Supplementary Table 9)

HDCA assigns refined_celltype `MN` to ontology term CL:0000100 and lists a curated 20-gene top signature for this population (Webb et al., 2026):

> "top_gene_signatures": "GAP43,INA,DCX,MAPT,L1CAM,NEFL,STMN2,NGFR,SLIT3,RAB3A,ENO2,ATP1A3,SLIT2,RTN1,TUBB4A,NEFM,SNCG,BSCL2,KIF5C,ECEL1"
>
> — Webb et al. (2026), HDCA Supp. Table 9

Functionally this signature is dominated by three programmes. (i) **Axonogenesis and growth-cone biology**: `GAP43` (the canonical growth-associated protein of extending axons), `DCX` (doublecortin, microtubule binding in migrating/extending neurons), `STMN2` (stathmin-2, axonal microtubule dynamics) and `L1CAM` (axonal adhesion). (ii) **Neuronal cytoskeleton**: the type-IV intermediate filaments `NEFL`, `NEFM` and `INA` (alpha-internexin), and the tubulin `TUBB4A` — neurofilaments are particularly abundant in long-projection motor neurons. (iii) **Motor-neuron–enriched specialised genes**: `ECEL1` (endothelin-converting-enzyme-like-1), a classical motor-neuron-enriched gene required for terminal arborisation at the neuromuscular junction; `NGFR` (p75); the neuronal glycolytic enzyme `ENO2`; and the Na/K-ATPase α3 subunit `ATP1A3`. The HDCA curated signature also includes guidance ligands `SLIT2` and `SLIT3`, consistent with active axon-pathfinding behaviour at CS13–14.

### Statistical DEGs (Supplementary Table 16)

The top differentially-expressed genes from the integrated atlas mirror the curated signature, with very large effect sizes:

> "gene": "NEFL", "score": 38.260754, "logfc": 8.415406, "pval_adj": 0
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "ECEL1", "score": 31.419098, "logfc": 6.6737967, "pval_adj": 7.56915446200444e-214
>
> — Webb et al. (2026), HDCA Supp. Table 16

`NEFL` (logFC 8.4) and `NEFM` (logFC 8.0) lead the DEG ranking, followed by `INA`, `STMN2`, `DCX`, `TUBB3`, `CRMP1`, `TUBB2A`, `GAP43`, `MAP1B`, `TUBB4A`, `APLP1`, `RTN1`, `SLIT3`, `L1CAM`, `ATP1A3`, `ENO2`, `RAB3A` and `ECEL1`. The combination of neurofilament triplet (`NEFL/NEFM/INA`), pan-neuronal tubulins (`TUBB3/TUBA1A/TUBB2A/TUBB4A`), and `ECEL1` is diagnostic of postmitotic somatic motor neurons.

### Canonical motor-neuron transcription factors and cholinergic genes

The HDCA marker list reflects the postmitotic state at CS13–14 (when neurofilament and axon-growth genes dominate) rather than the lineage selectors used in the developmental literature. The canonical fate determinants include the LIM-homeodomain combinatorial code:

> "Lhx3 is expressed in developing V2 interneurons, whereas both Lhx3 and Isl1 are expressed in postmitotic motor neurons."
>
> — Gadd et al. (2011)

> "ISL1 is expressed by both somatic and visceral motor neurons"
>
> — Pfaff et al. (1996)

For human fetal cord at CS19–22 (slightly later than HDCA's CS13–14), Mathis & Wichterle directly catalogue the molecular hallmarks of spinal MNs:

> "Markers of spinal motor neurons (ISL1, ISL2, HB9, RET ) as well as key cholinergic genes (CHAT, CHT1, VACHT, CHRNA3, CHRNA4, CHRNB2) were enriched in GFP-positive cells"
>
> — Mathis et al. (2013)

This grounds the cholinergic identity (CHAT/VACHT/CHT1) and the ISL1/ISL2/MNX1(HB9)/RET selector cassette that, although not the strongest discriminators in the HDCA DEG list, define spinal MN identity across human and rodent.

## Location

### CNS spinal cord (ventral horn)

HDCA Supplementary Table 9 assigns `MN` to broad_celltype `CNS_SPINAL_NEURON`, germlayer `ECTODERM` and system `NERVOUS_SYSTEM` (Webb et al., 2026). The cells are absent from Table 17 (the PNS subset), corroborating their CNS identity rather than a peripheral ganglion identity. Although motor axons project into the periphery, the cell bodies sit in the ventral horn of the spinal cord and are developmentally CNS:

> "Ventral progenitors (p0-p3 and progenitor motor neuron (pMN) domains) broadly give rise to neuronal populations responsible for locomotor coordination."
>
> — Iyer & Ashton (2022)

Within the ventral horn, motor neurons are organised into columnar groups along the rostro-caudal axis, with stereotyped LIM and ETS codes:

> "MMC neurons are located all throughout the spinal cord and are characterized by the co-expression of Hb9, ISL1/2, OCT6, and LHX3/4"
>
> — Roman et al. (2024)

> "LMC neurons are found in the brachial and lumbar levels of the spinal cord, and are characterized by the expression of ISL2, FOXP1, and RALDH2"
>
> — Roman et al. (2024)

> "HMC neurons are located in the thoracic level of the spinal cord, and are known to express Hb9, ISL1, and ER81"
>
> — Roman et al. (2024)

In situ work in human embryonic spinal cord at CS19–22 confirms that these columns are anatomically demarcated and use the conserved HB9/ISL1 combinatorial scheme:

> "Consistent with the pattern of expression in chick and mouse, the MMC expressed both HB9 and ISL1, the LMC l was ISL1 − / HB9 + , and many LMC m neurons were ISL1 + /HB9 −"
>
> — Mathis et al. (2013)

> "human motor neurons are characterized by variable patterns of HB9 and ISL1 expression"
>
> — Mathis et al. (2013)

### Developmental staging in HDCA and complementary human references

In the HDCA reference, the MN population is sampled at Carnegie stages 13–14 from whole-embryo dissociations (samples F137/F147/F158, n=7984 cells), well before columnar consolidation is morphologically complete (Webb et al., 2026). Complementary human references covering later spinal-cord timepoints — Rayon et al. (2021) at first trimester, Andersen et al. (2021) at midgestation, Shi et al. (2024) by image-based seqFISH, and Yadav et al. (2023) in the adult — show how MN heterogeneity sharpens with time:

> "We discovered a surprisingly early diversification of alpha (α) and gamma (γ) motor neurons that control and modulate contraction of muscle fibers, which was suggestive of accelerated developmental timing in human spinal cord compared to rodents."
>
> — Andersen et al. (2021)

> "Our study also illuminated the spatial differences and molecular cues underlying motor neuron (MN) diversification, and the enrichment of Amyotrophic Lateral Sclerosis (ALS) risk genes in MNs and microglia."
>
> — Shi et al. (2024)

> "our work here revealed that dorsal-ventral location is the shared, fundamental axis of spinal neuron transcriptional diversity"
>
> — Yadav et al. (2023)

HOX-coded motor-pool organisation along the rostro-caudal axis has been mapped directly in the developing human spine by Lawrence et al. (2024) — one of the principal HDCA subatlases:

> "In the axial plane of the spinal cord, we find distinct patterns in the ventral and dorsal domains, providing insights into motor pool organisation and loss of collinearity in HOXB genes."
>
> — Lawrence et al. (2024)

The Braun et al. (2023) first-trimester human brain atlas covers the hindbrain and rostral cord and provides the principal brain-side reference for HDCA neuronal annotations:

> "The adult human brain is divided into hundreds of spatial domains, each comprising tens or hundreds of distinct neuronal, glial, and other cell types. This complex arrangement of cells is initially established during the first trimester of development"
>
> — Braun et al. (2023)

## Function

### Cholinergic skeletal-muscle innervation

Spinal somatic motor neurons are the final motor output of the CNS: their axons leave the ventral root, traverse peripheral nerves, and form cholinergic neuromuscular junctions on skeletal muscle fibres. Direct evidence in human-fetal-derived MNs confirms enrichment of acetylcholine biosynthesis and transport machinery (`CHAT`, `CHT1`, `VACHT`) and nicotinic receptor subunits (Mathis et al., 2013, quoted above). Cranial and spinal MNs share the cholinergic state but differ in selector code:

> "Cranial motor neurons share many features with spinal motor neurons: they are cholinergic and express the transcription factor Isl1"
>
> — Mazzoni et al. (2013)

> "unlike ventral spinal motor neurons, they express Tbx20 instead of Hb9, and their specification depends on the pairedlike homeodomain transcription factors Phox2a and Phox2b instead of LIM homeodomain factor Lhx3"
>
> — Mazzoni et al. (2013)

The HDCA `MN` cluster expresses `MNX1` (HB9) signature and uses LHX3/ISL1 logic (curated Table 9 / Mathis 2013 markers), consistent with spinal rather than cranial identity.

### Axon outgrowth and pathfinding at CS13–14

The dominance of growth-cone (`GAP43`), microtubule (`STMN2`, `DCX`, `TUBB3`, `TUBB4A`, `MAP1B`), adhesion (`L1CAM`) and guidance (`SLIT2`, `SLIT3`) genes in the HDCA Table 9 signature is consistent with a developmental window in which motor axons are actively extending into the periphery. `ECEL1` — a particularly motor-neuron-enriched DEG (logFC 6.7) — is essential for distal axon arborisation and neuromuscular junction maturation, and is one of the strongest molecular signposts of motor-neuron identity in the HDCA reference (Webb et al., 2026).

## Developmental specification and structure

### Dorsoventral patterning and the pMN progenitor domain

Spinal motor neurons originate from the pMN (progenitor-motor-neuron) domain of the ventral neural tube, specified by graded Sonic hedgehog (Shh) signalling from the notochord and floor plate. The pMN is delimited dorsally by the p2 domain and ventrally by the p3 domain via cross-repressive transcription-factor pairs:

> "Distinct classes of motor neurons and ventral interneurons are generated by the graded signaling activity of Sonic hedgehog (Shh)."
>
> — Ericson et al. (1997)

> "Pax6 establishes distinct ventral progenitor cell populations and controls the identity of motor neurons and ventral interneurons"
>
> — Ericson et al. (1997)

> "The pMN progenitor domain is characterized by the expression of homeodomain proteins PAX6, NKX6.1, and basic helixloop-helix (bHLH) protein OLIG2"
>
> — Roman et al. (2024)

The bistable OLIG2/NKX2.2 switch resolves the pMN–p3 boundary and toggles MN versus V3 interneuron / oligodendrocyte fate:

> "Repression of Olig2 in non-motor neuron progenitors appears to be partly achieved by temporal adaptation of spinal cells to Sonic hedgehog (Shh) signal."
>
> — Chen & Chen (2019)

> "Clearance of Olig2 from the p3 domain ... depends on induction of the repressor Nkx2.2 in response to sustained Shh signaling"
>
> — Chen & Chen (2019)

> "TLE overexpression causes increased numbers of p3 progenitors and promotes the V3 interneuron fate while suppressing the motor neuron fate."
>
> — Todd et al. (2012)

> "TLE is important to promote the formation of the p3 domain and subsequent generation of V3 interneurons"
>
> — Todd et al. (2012)

After the neurogenic phase, pMN progenitors switch to producing oligodendrocyte precursors, in part via dynamic ventral recruitment of new pMN cells:

> "Addition of new progenitors to the pMN domain requires Hh signaling because blocking Hh eliminated ventral cell movement, reduced the number of pMN cells, and abolished OPC formation."
>
> — Ravanelli & Appel (2015)

A human-specific feature of the pMN, identified by Jang et al. (2024), is that NKX2-2 does not strongly repress OLIG2 in human progenitors, extending the neurogenic window in the human MN lineage:

> "evolutionary extension of neurogenesis in humans arises through changes in the interaction between two genes, NKX2-2 and OLIG2"
>
> — Jang et al. (2024)

> "this difference in turn allows for co-expression of NKX2-2 and NEUROG2 in the human spinal motor neuron lineage"
>
> — Jang et al. (2024)

### Postmitotic specification: the LIM-homeodomain code (ISL1, LHX3, MNX1)

Once pMN progenitors exit the cell cycle they switch on a postmitotic LIM-homeodomain code in which ISL1 is the essential switch for motor-neuron versus V2 interneuron fate:

> "Motor neurons are not generated without ISL1, although many other aspects of cell differentiation in the neural tube occur normally."
>
> — Pfaff et al. (1996)

> "The additional expression of the LIM-homeodomain protein Islet 1 (ISL1) in a neighbouring band of cells triggers a transcriptional switch that directs these cells to become spinal motor neurons"
>
> — Smith et al. (2020)

> "Lhx3 and Lhx4 are expressed in motor neuron precursor cells prior to the onset of Isl1 expression and then coexpressed with Isl1 after the final cell division"
>
> — Jurata et al. (1998)

> "Lhx3 and Lhx4 expression is down-regulated in all but the MMC m neurons, which maintain Isl1 expression and up-regulate Isl2 expression"
>
> — Jurata et al. (1998)

> "In mice and zebrafish, exogenous Isl1 or Isl2 can trigger motor neuron differentiation, but both must be expressed to maintain proper motor neuron cell fate"
>
> — Gadd et al. (2011)

ISL1 has functions beyond initial fate specification — it is also required for soma positioning, columnar organisation and axon growth:

> "Isl1 is required for the survival and specification of spinal cord motor neurons."
>
> — Liang et al. (2011)

> "Isl1 in multiple aspects of motor neuron development, including motor neuron cell body localization, motor column formation and axon growth."
>
> — Liang et al. (2011)

### Motor-pool diversification: HOX code and retinoic acid

Rostro-caudal motor-pool identity (cervical → brachial → thoracic → lumbar) is imposed on the LIM code by an instructional HOX programme that operates in young postmitotic motor neurons, with retinoic acid from paraxial mesoderm as a key extrinsic cue:

> "Motor neuron identity along the rostral end of the neural tube is induced by a combination of high paraxial mesodermal RA expression and low caudal FGF8 and GDF11 expression"
>
> — Roman et al. (2024)

> "an instructional Hox gene coding system that is established and operates in young postmitotic motor neurons"
>
> — Allan & Thor (2015)

> "numerous of these Hox genes are activated in postmitotic motor neurons in ignorance of typical A-P axial expression domains"
>
> — Allan & Thor (2015)

> "Also, specific retinoic acid signaling and Lhx1/Isl1 discrimination requires the activity of Hoxc6 and Hoxc8."
>
> — Allan & Thor (2015)

> "Both HOX genes and neuronal birth date contribute to region-specific neuronal diversification"
>
> — Iyer & Ashton (2022)

In the developing human spine specifically, Lawrence et al. (2024) showed using spatial transcriptomics and in-situ sequencing that ventral motor pools display distinct HOX patterns along the axis with loss of HOXB collinearity, providing the human spatial reference for the HDCA `MN` cluster (Lawrence et al., 2024).

### Synthesis of MN identity in human postmortem single-cell data

Blum & Gitler frame the value of the HDCA-style approach for understanding MN biology:

> "there is ample opportunity to perform descriptive postmortem single-cell transcriptomics and epigenomics during human development"
>
> — Blum & Gitler (2022)

Rayon et al. (2021) provide the first-trimester human spinal cord scRNA-seq reference against which HDCA MNs are most directly comparable:

> "focused on first trimester spinal cord derived from four human embryos, and identified diverse progenitor and neuronal populations, and performed a systematic comparison with the spinal cord cell types of the developing mouse spinal cord"
>
> — Rayon et al. (2021)

The HDCA prenatal atlas extends this work by placing CS13–14 spinal motor neurons in an integrated whole-embryo multi-organ context (Webb et al., 2026), and is complemented by the human embryonic limb atlas (Zhang et al., 2024) and the multi-omic skeletal atlas (To et al., 2024), which characterise the muscle and skeletal targets innervated by motor pools.

## References

- HDCA consortium / Webb et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper)". *preprint (HDCA)*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Braun et al. (2023). "Comprehensive cell atlas of the first-trimester developing human brain". *Science*. DOI: [10.1126/science.adf1226](https://doi.org/10.1126/science.adf1226)
- Lawrence et al. (2024). "HOX gene expression in the developing human spine". *Nature Communications*. DOI: [10.1038/s41467-024-54257-3](https://doi.org/10.1038/s41467-024-54257-3)
- Pfaff et al. (1996). "Requirement for LIM homeobox gene Isl1 in motor neuron generation reveals a motor neuron-dependent step in interneuron differentiation". *Cell*.
- Smith et al. (2020). "Contrasting DNA-binding behaviour by ISL1 and LHX3 underpins differential gene targeting in neuronal cell specification". *Journal of Structural Biology: X*. DOI: [10.1016/j.yjsbx.2020.100043](https://doi.org/10.1016/j.yjsbx.2020.100043)
- Gadd et al. (2011). "Structural Basis for Partial Redundancy in a Class of Transcription Factors, the LIM Homeodomain Proteins, in Neural Cell Type Specification". *Journal of Biological Chemistry*. DOI: [10.1074/jbc.M111.248559](https://doi.org/10.1074/jbc.M111.248559)
- Jurata et al. (1998). "The Nuclear LIM Domain Interactor NLI Mediates Homo- and Heterodimerization of LIM Domain Transcription Factors". *Journal of Biological Chemistry*. DOI: [10.1074/jbc.273.6.3152](https://doi.org/10.1074/jbc.273.6.3152)
- Liang et al. (2011). "Isl1 Is required for multiple aspects of motor neuron development". *Molecular and Cellular Neurosciences*. DOI: [10.1016/j.mcn.2011.04.007](https://doi.org/10.1016/j.mcn.2011.04.007)
- Mathis et al. (2013). "Accelerated high-yield generation of limb-innervating motor neurons from human stem cells". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.0906-12.2013](https://doi.org/10.1523/JNEUROSCI.0906-12.2013)
- Mazzoni et al. (2013). "Synergistic binding of transcription factors to cell-specific enhancers programs motor neuron identity". *Nature Neuroscience*. DOI: [10.1038/nn.3467](https://doi.org/10.1038/nn.3467)
- Roman et al. (2024). "Cell Transplantation for Repair of the Spinal Cord and Prospects for Generating Region-Specific Exogenic Neuronal Cells". *Cell Transplantation*. DOI: [10.1177/09636897241241998](https://doi.org/10.1177/09636897241241998)
- Allan & Thor (2015). "Transcriptional selectors, masters, and combinatorial codes: regulatory principles of neural subtype specification". *Wiley Interdisciplinary Reviews: Developmental Biology*. DOI: [10.1002/wdev.191](https://doi.org/10.1002/wdev.191)
- Ericson et al. (1997). "Pax6 controls progenitor cell identity and neuronal fate in response to graded Shh signaling". *Cell*.
- Chen & Chen (2019). "Multifaceted roles of microRNAs: From motor neuron generation in embryos to degeneration in spinal muscular atrophy". *eLife*. DOI: [10.7554/eLife.50848](https://doi.org/10.7554/eLife.50848)
- Todd et al. (2012). "Establishment of Motor Neuron-V3 Interneuron Progenitor Domain Boundary in Ventral Spinal Cord Requires Groucho-Mediated Transcriptional Corepression". *PLoS ONE*. DOI: [10.1371/journal.pone.0031176](https://doi.org/10.1371/journal.pone.0031176)
- Ravanelli & Appel (2015). "Motor neurons and oligodendrocytes arise from distinct cell lineages by progenitor recruitment". *Genes & Development*. DOI: [10.1101/gad.271312.115](https://doi.org/10.1101/gad.271312.115)
- Jang et al. (2024). "Independent control of neurogenesis and dorsoventral patterning by NKX2-2". *bioRxiv*. DOI: [10.1101/2024.10.10.617692](https://doi.org/10.1101/2024.10.10.617692)
- Iyer & Ashton (2022). "Bioengineering the human spinal cord". *Frontiers in Cell and Developmental Biology*. DOI: [10.3389/fcell.2022.942742](https://doi.org/10.3389/fcell.2022.942742)
- Andersen et al. (2021). "Landscape of human spinal cord cell type diversity at midgestation". *bioRxiv*. DOI: [10.1101/2021.12.29.473693](https://doi.org/10.1101/2021.12.29.473693)
- Shi et al. (2024). "Decoding the spatiotemporal regulation of transcription factors during human spinal cord development". *Cell Research*. DOI: [10.1038/s41422-023-00897-x](https://doi.org/10.1038/s41422-023-00897-x)
- Yadav et al. (2023). "A Cellular Taxonomy of the Adult Human Spinal Cord". *Neuron*. DOI: [10.1016/j.neuron.2022.10.019](https://doi.org/10.1016/j.neuron.2022.10.019)
- Blum & Gitler (2022). "Singling out motor neurons in the age of single-cell transcriptomics". *Trends in Genetics*. DOI: [10.1016/j.tig.2022.03.016](https://doi.org/10.1016/j.tig.2022.03.016)
- Rayon et al. (2021). "Single-cell transcriptome profiling of the human developing spinal cord reveals a conserved genetic programme with human-specific features". *Development*. DOI: [10.1242/dev.199711](https://doi.org/10.1242/dev.199711)
- Zhang et al. (2024). "A human embryonic limb cell atlas resolved in space and time". *Nature*. DOI: [10.1038/s41586-023-06806-x](https://doi.org/10.1038/s41586-023-06806-x)
- To et al. (2024). "A multi-omic atlas of human embryonic skeletal development". *Nature*. DOI: [10.1038/s41586-024-08189-z](https://doi.org/10.1038/s41586-024-08189-z)
