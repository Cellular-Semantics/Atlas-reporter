# DL1 Neuron (DL1_NEURON)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human embryonic spinal cord at Carnegie stages 16–17 per sample provenance (whole-embryo dissociations F137/F147 CS16 and F158 CS17, ArrayExpress E-MTAB-11504/11520/11911; HDCA metadata codes the development stage as HsapDv:0000023 / HsapDv:0000024); CNS spinal neuron compartment, n=2454 cells, cluster purity 100%
Cell Ontology: [dorsal horn interneuron](http://purl.obolibrary.org/obo/CL_0011000) (CL:0011000, broad match — no exact CL term)

## Summary

`DL1_NEURON` is a CNS-spinal-cord interneuron cluster of n=2454 cells from the HDCA v2 prenatal atlas (Webb et al., 2026). Data provenance is unambiguous: **100% of these cells come from HDCA's own de novo whole-embryo scRNA-seq (samples F137/F147 CS16, F158 CS17; ArrayExpress E-MTAB-11504/11520/11911), not from Braun 2023 or any other constituent subatlas**, and HDCA's `obs.original_author_annotation` column labels every cell literally as `"DL1 neuron"` (100% purity). Per the HDCA project's own `provenance_evidence.md`, **the DL prefix is HDCA-internal nomenclature for "dorsal late" interneuron**, used alongside the parallel HDCA-internal axes `DA` (dorsal alar) and `DB` (dorsal basal). DL1 is therefore **not** equivalent to DA1: both express LHX9, but they are separate clusters in HDCA's parcellation, and the "dorsal late" label encodes intended correspondence to the late-born **dILA / dILB** classes of the classical Helms–Johnson dorsal-interneuron taxonomy (Helms & Johnson 2003; Lai et al. 2016; Sagner & Briscoe 2019; Hori & Hoshino, 2012; Buckley et al., 2020) rather than to the early-born **dI1** class. The marker signature is partly contradictory with a strict "dorsal late" interpretation: the top postmitotic LIM-HD marker is **LHX9** (logFC 5.85, padj ≈ 10⁻²⁵⁰), the canonical identifier of the early-born dI1 lineage (Gray de Cristoforis et al., 2020; Castellani, 2013; Lu et al., 2015), and the Supp Table 9 signature also includes the commissural-axon machinery genes `DCC` (netrin-1 receptor) and `CNTN2` (TAG-1) — features of dI1 commissural neurons (Hadas et al., 2013; Tran et al., 2013). The remainder of the signature is dominated by pan-neuronal cytoskeletal/growth-cone genes (`TUBB3`, `STMN2`, `DCX`, `INA`, `MAP1B`, `CRMP1`, `NCAM1`, `DPYSL4`, `APP`, `APLP1`), the early-postmitotic bHLH `NHLH1`, the neurotrophin receptor `NGFR` (p75NTR), the retinoic-acid signalsome component `CRABP1` (the single top DEG, logFC 8.11), and an anterior/cervical HOX signature (`HOXA3`, `HOXB2`, `HOXD3` all logFC > 4.5; Lawrence et al., 2024). Taken together, DL1 is best read at this resolution as **a recently postmitotic LHX9⁺ dorsal spinal interneuron population at cervical/upper-rostral level**, with HDCA's "dorsal late" label encoding the authors' intended placement within the late-born dorsal cohort, but with a marker profile consistent with the dI1 lineage broadly. **The mapping to a single classical class (dI1 vs dILA-1 vs an HDCA-specific intermediate) is not definitive at this resolution and is reported here as approximate, per the prompt and `provenance_evidence.md`.**

## Markers

### HDCA-derived signature

HDCA Supplementary Table 9 lists the curated top-20 signature for DL1_NEURON as:

`NGFR, DCX, CNTN2, ELAVL3, INA, STMN2, HOXD3, HOXA3, DCC, HOXB2, LHX9, BSCL2, NHLH1, DNER, CRABP1, DPYSL4, SNCG, ADGRG1, SHD, RGMB` (Webb et al., 2026, HDCA Supp. Table 9). The statistical DEG ranking in Supp Table 16 places `CRABP1` first (logFC ≈ 8.11, padj ≈ 5×10⁻³⁰⁶), followed by `TUBB3` (5.67), `CRMP1` (3.94), `GPC2` (4.11), `MAP1B` (3.92), `HOXB2` (4.62), `TUBB2B` (4.18), `LHX9` (5.85), `TAGLN3` (4.23), `TUBA1A` (3.89), `NGFR` (4.80), `HOXA3` (4.66), `HOXD3` (4.60), `STMN2` (4.84), `DCX` (3.61), `INA` (4.46) and `DNER` (3.96) — confirming a cohesive postmitotic-neuron + LHX9⁺ + anterior-HOX⁺ + CRABP1-high signature (Webb et al., 2026, HDCA Supp. Table 16).

### LHX9 — postmitotic LIM-HD marker of the dI1 lineage

LHX9 is the most informative cardinal-class marker present in the DL1 signature. Gray de Cristoforis et al. (2020) state directly:

> "The dorsal-most interneuron class, dI1, is characterized by expression of Lhx2 and Lhx9."
>
> — Gray de Cristoforis et al. (2020)

> "From a shared pool of progenitors, two subpopulations emerge based on the proportion of Lhx2 and Lhx9 transcripts: ventromedially located interneurons express highly LHX2 and to a lesser extend LHX9, whereas a ventrolateral counterpart expresses highly LHX9 but not"
>
> — Gray de Cristoforis et al. (2020)

Castellani (2013) makes the same assignment textbook-explicit:

> "Dl1 neurons are generated from a pool of progenitor cells expressing Math1, and can be identified by two LIM transcription factors, Lhx2 and Lhx9"
>
> — Castellani (2013)

LHX9 expression is biphasic in dI1 development. Wheaton et al. (2022) note that LHX9 is expressed in two waves: in recently born dI1 neurons during early neurogenesis, and again in dI1 neurons that have settled in the deep dorsal horn:

> "Lhx9c mRNA is expressed in the first wave of dI1 neurons born at E10.5/HH26 and E11.5/HH26 mouse/chicken embryos."
>
> — Wheaton et al. (2022)

Onishi & Zou (2018) refine the relative-level interpretation in the post-migration period:

> "Lhx2 is expressed in dI1 neurons derived from Atoh1-positive pdI1 progenitors."
>
> — Onishi & Zou (2018)

> "The dI1 neurons, which express high levels of Lhx2 (Lhx2 high ) at E11.5, project axons contralaterally (dI1c), whereas the Lhx2 low (and Lhx9 high ) dI1 neurons, which are located ventral to the Lhx2 high neurons at E11.5, project axons ipsilaterally (dI1i)"
>
> — Onishi & Zou (2018)

That LHX9 features in DL1's top signature (and that LHX2 does not appear) supports a LHX9⁺ dI1-lineage identity, although at HDCA's resolution we cannot resolve a strict dI1c/dI1i partition.

### Commissural axon machinery: DCC and CNTN2

Two members of HDCA's Supp Table 9 DL1 signature are specifically associated with commissural midline-crossing axons of dI1 neurons. Hadas et al. (2013) describe TAG1 (CNTN2) regulation in dI1:

> "bHLH and Lim-HD proteins are expressed in motor and dI1 neurons: Olig2, Ngn2, NeuroD and Ascl1 in motor neurons and Atoh1 in dI1 neurons; Isl1,Isl2 and Lhx3 in motor neurons and Lhx2 and Lhx9 in dI1 neurons."
>
> — Hadas et al. (2013)

> "All these interneurons express bHLH and Lim-HD proteins: Atoh1+Lhx2/9 in dI1, Ngn1/2+Lhx1/5 in dI2,dI4 and dI6."
>
> — Hadas et al. (2013)

Tran et al. (2013) directly link Atoh1-derived dI1 commissural neurons to the cognate guidance machinery:

> "we show that the dI1, not the dI4, population of commissural neurons derived from Atoh1 progenitors, and a subset of the GABAergic ventral commissural neurons express the Npn2 receptor on all segments of their axons"
>
> — Tran et al. (2013)

The presence of `DCC` (netrin-1 receptor) and `CNTN2` (TAG-1) in the DL1 Supp Table 9 signature is consistent with a postmitotic neuron actively extending a commissural axon — a feature shared by the dI1 class and also by dI2, dI4 and dI6 (Hadas et al., 2013; Zavvarian et al., 2020).

### CRABP1 — striking top DEG

The single top DEG of the DL1 cluster (logFC 8.11) is `CRABP1`, the cytosolic retinoic-acid-binding protein. Lin et al. (2020) note that:

> "Cellular retinoic acid-binding protein 1 (CRABP1) is highly expressed in motor neurons."
>
> — Lin et al. (2020)

> "Up-regulation of Crabp1 by Shh is mediated by glioma-associated oncogene homolog 1 (Gli1) that binds the Gli target sequence in Crabp1′s neuron-specific regulatory region upstream of minimal promoter."
>
> — Lin et al. (2020)

CRABP1 is therefore a marker of retinoic-acid-responsive, Shh-experienced postmitotic neurons. Its very high expression in DL1 is biologically plausible for a recently-postmitotic spinal-cord neuron but, unlike LHX9, is not class-diagnostic. It is one of the strongest molecular distinctions between DL1 and the otherwise marker-overlapping DA1 cluster (Webb et al., 2026, HDCA Supp. Table 16).

### Positional identity — anterior/cervical HOX code

`HOXA3` (logFC 4.66), `HOXB2` (4.62) and `HOXD3` (4.60) place DL1 cells at anterior/cervical-to-upper-rostral spinal level. Lawrence et al. (2024) provide the human-specific framework:

> "In the axial plane of the spinal cord, we find distinct patterns in the ventral and dorsal domains, providing insights into motor pool organisation and loss of collinearity in HOXB genes."
>
> — Lawrence et al. (2024)

## Location

### Origin in the alar plate of the dorsal neural tube

Whether DL1 represents the early-born dI1 class or the late-born dILA/dILB cohort intended by HDCA's "dorsal late" naming, it arises from the dorsal alar plate. Müller et al. (2005) define the alar-plate origin:

> "Neurons of the dorsal horn integrate and relay sensory information and arise during development in the dorsal spinal cord, the alar plate."
>
> — Müller et al. (2005)

> "Class A and B neurons emerge in the dorsal and ventral alar plate, differ in their dependence on roof plate signals for specification, and settle in the deep and superficial dorsal horn, respectively."
>
> — Müller et al. (2005)

Hori & Hoshino (2012) place the early-born dI1-dI6 and the late-born dILA/dILB classes in their canonical taxonomy:

> "In the early developing neural tube during embryonic days 10-11.5 (E10-11.5), six distinct classes of deep dorsal interneurons (dI1-6) arise from six different progenitor domains (dP1-6), followed by the generation of two lateborn neuronal subtypes of superficial laminae, dIL A and dIL B , from a common dorsal progenitor domain during E11-13"
>
> — Hori & Hoshino (2012)

Buckley et al. (2020) summarise the migration destinations:

> "For dorsal neural progenitors, the early-born proliferative cells (E10-E11.5) give rise to dI4 and dI5 interneurons, while the later-born class (E12-E14.5) generates dILA and dILB interneurons"
>
> — Buckley et al. (2020)

Meziane et al. (2013) summarise the migration patterns of the cardinal classes:

> "The dorsal interneuron subtypes dI1-3 migrate ventrally, whereas a subset of dI4 and dI5 cells migrate laterally to populate the deep dorsal horn (laminae IV-V). The dILA/B subclasses migrate to the superficial dorsal laminae (I-III), and mediate pain and temperature sensitive circuits"
>
> — Meziane et al. (2013)

### Final settling position

For the dI1 lineage (with which DL1's LHX9 signature is consistent), Lu et al. (2015) note that:

> "The dI1 interneurons migrate to the deep dorsal horn and intermediate gray where they receive proprioceptive input from the periphery and form commissural projections of dorsal and ventral SCTs"
>
> — Lu et al. (2015)

Bui et al. (2015) provide a complementary statement:

> "Defined by expression of Atoh1 (formerly Math1), dI1 INs are also a population of dorsally derived neurons that migrate ventrally to be positioned in the deep dorsal horn of the spinal cord"
>
> — Bui et al. (2015)

Cross-species single-cell work (Ignatyev et al., 2025) confirms the conservation of this dorsoventral architecture between mouse and other tetrapods:

> "The ventral spinal cord displayed a characteristic dorsoventral layering of V0-V3, dI1-2, and dI6 interneurons, mirroring previous distributions in the mouse spinal cord"
>
> — Ignatyev et al. (2025)

### Caveat on the late-born interpretation

If DL1 instead represents the HDCA-intended late-born **dILA-1** family (consistent with the literal "dorsal late" label), the destination would be the superficial dorsal laminae (I-III) rather than the deep dorsal horn (Meziane et al., 2013; Hori & Hoshino, 2012). Roome et al. (2025), in the only available transcriptional ontogeny of mouse dILA/dILB families, name the first-born members of each late-born family **dILA1** and **dILB1**:

> "Among dILA families, we found that the families were born in overlapping waves of neurogenesis with dILA1 born at E10.5-E11.0, dILA2 born at E11.0, dILA3 and dILA4 born at E11.5, dILA5 born at E11.5-E12.0, and dILA6 born last at E12.0"
>
> — Roome et al. (2025)

This makes the **HDCA name "DL1" most parsimoniously a parallel of "dILA1" / "dILB1"** (the first-born sub-family of the late-born dIL cohort) under the authors' "dorsal late" naming convention. The LHX9 signature is the principal evidence that complicates this assignment — LHX9 is not a classical dILA/dILB marker (the late-born classes are defined by Lbx1/Pax2/Lhx1-5 or Lbx1/Tlx3/Lmx1b; Hori & Hoshino, 2012; Buckley et al., 2020). We therefore flag DL1 as **approximate dI1 / dILA-1**, per the user prompt.

## Function

At CS16-17 (~5.5-6 pcw), DL1 cells are recently postmitotic — dominated by `TUBB3`, `STMN2`, `DCX`, `MAP1B`, `CRMP1`, `INA`, `NCAM1`, `GAP43`-class growth-cone machinery and the early-postmitotic bHLH `NHLH1` — and so are best interpreted as a transcriptionally early dorsal spinal interneuron class, not a circuit-integrated mature population. The mature functional role is inferred from the dI1 lineage (if DL1 ≈ dI1) or the dILA/dILB lineage (if DL1 ≈ dILA-1).

### Prospective mature dI1 function (proprioceptive spinocerebellar relay)

Zavvarian et al. (2020) summarise the canonical dI1 role:

> "The dI1 interneurons are located in the dorsal horn and integrate proprioceptive signals from the peripheral organs and project rostrally to the spinocerebellar tract"
>
> — Zavvarian et al. (2020)

> "These neurons can be further subdivided into contralaterallyprojecting dI1c and ipsilaterally-projecting dI1i interneurons"
>
> — Zavvarian et al. (2020)

Bui et al. (2015) elaborate:

> "These neurons form three distinct spinocerebellar tracts (SCTs), by which sensory feedback is relayed to the cerebellum."
>
> — Bui et al. (2015)

Castellani (2013) confirms the relay's anatomy:

> "The proprioceptive dl1 class settles at the most dorsal position of the spinal cord, close to the roof plate, and transmits information to the cerebellum via the spinocerebellar and the cuneocerebellar tracts."
>
> — Castellani (2013)

> "It is composed of two types of neurons, those establishing ipsilateral projections (dl1i) and those establishing commissural projections (dl1c)"
>
> — Castellani (2013)

### Prospective mature dILA/dILB function (somatosensory dorsal-horn circuitry)

If DL1 represents dILA-1, its mature role is part of the somatosensory dorsal-horn circuit that mediates pain and temperature processing (Meziane et al., 2013): inhibitory GABAergic dILA neurons (Pax2/Lhx1-5+) integrate with excitatory glutamatergic dILB neurons (Tlx3/Lmx1b+) to form the substantia gelatinosa and laminae III-IV (Buckley et al., 2020).

### Developmental-stage caveat

The DL1 transcriptional state is dominated by neurofilament, growth-cone and microtubule-trafficking genes — features of recently-postmitotic neurons actively engaged in axonogenesis. The mature dI1 (proprioceptive spinocerebellar) or dILA-1 (somatosensory) functional roles described above should be read as **prospective fates**, not as evidence that CS16-17 DL1 neurons already participate in those mature circuits.

## Developmental Specification

### Dorsal-plate origin and roof-plate signalling

The dorsal-most progenitors of the alar plate are specified by roof-plate-derived BMP/Wnt signals (the Class A program; Müller et al., 2005). Müller et al. (2005) note:

> "the basic helix-loop-helix (bHLH) gene Olig3 is expressed in progenitor cells that generate class A (dI1-dI3) neurons"
>
> — Müller et al. (2005)

Lu et al. (2015) describe the Atoh1+ progenitor → LHX9+ postmitotic mapping that defines dI1:

> "The roof-plate-dependent Class A dp1 progenitors of the dI1 class express the bHLH transcription factors Olig3 and Math1"
>
> — Lu et al. (2015)

> "The dI1 neurons in mouse are born between E10 and E12.5 and express Lhx2/9, Barhl1 (bar homeobox like 1) and Brn3a (Pou4f1, a class IV POU domaincontaining transcription factor; Helms and Johnson, 1998)."
>
> — Lu et al. (2015)

BMP signalling is required for the broader Class A cohort:

> "Loss of function experiments with BMP7 in chick and Bmp7 mutant mice results in loss of dI1, dI3, and dI5"
>
> — Lu et al. (2015)

### Late-born dIL lineage as an alternative HDCA-intended program

If HDCA's "DL = dorsal late" label is to be taken literally, the developmental program is that of the late-born dIL cohort: Lbx1+ pdIL progenitors generating Ptf1a+ inhibitory dILA (Lhx1/5+, Pax2+) and Ascl1-driven excitatory dILB (Tlx3+, Lmx1b+) neurons (Buckley et al., 2020; Hori & Hoshino, 2012):

> "resulting in the generation of a common pool of late-born dIL progenitors and subsequently dILA (Lbx1 + , Ptf1a + , Pax2 + ) inhibitory GABAergic and dILB (Lbx1 + , Ptf1a − , Tlx1/3 + ) excitatory glutamatergic interneurons. Most of the superficial dorsal horn, substantia gelatinosa (lamina II), and lamina propria (laminae III-IV), is comprised of dIL-derived neurons"
>
> — Buckley et al. (2020)

> "GABAergic neurons in the dorsal spinal cord are composed of early-born dI4 and dI6 and late-born dIL A neurons. These three classes of postmitotic interneurons express the HD transcription factor Lbx1, Pax2 and Lhx1/5"
>
> — Hori & Hoshino (2012)

DL1's marker signature does **not** include Lbx1, Pax2, Lhx1/5, Tlx1/3 or Lmx1b at top-DEG level; it does include LHX9 prominently. This favours the dI1-lineage interpretation over the dILA-1 interpretation in molecular terms — while the HDCA naming convention favours the latter. The HDCA authors' rationale for assigning the "DL" prefix to this LHX9⁺ cluster is not made explicit in their Supp Table 9 note and may reflect an HDCA-internal clustering decision rather than a strict mapping to the classical taxonomy.

### Developmental timing in HDCA

Per HDCA's metadata, the DL1 cluster is captured at HsapDv:0000023 (54%) and HsapDv:0000024 (46%); per provenance these correspond to embryo samples F137/F147 at Carnegie stage 16 and F158 at Carnegie stage 17 (~5.5-6 pcw). This is later than the peak dI1 generation window in mouse (E10-E12.5; Lu et al., 2015) but consistent with both the dI1 second-wave LHX9 expression (Wheaton et al., 2022) and the late-born dIL generation window (E11-E14.5; Buckley et al., 2020; Hori & Hoshino, 2012). The HDCA developmental window therefore does not by itself discriminate between the dI1 and dILA/dILB interpretations.

### Cardinal-class architecture across vertebrates

Roome et al. (2025) provide the framework that motivates parsing the late-born cohort into numbered dILA-1 ... dILA-6 and dILB-1 ... dILB-6 sub-families:

> "Groups 2 and 3 represented the putative dILA neurons (Group 2) and dILB neurons (Group 3), based on the expression of general embryonic dorsal markers (shared with putative dI4 and dI5 classes), modest residual expression of early post-mitotic markers (suggesting recent neurogenesis), later-born temporal transcription factors, as well as the expression of known markers of mature dorsal neurons, the region where dILA/B neurons reside"
>
> — Roome et al. (2025)

HDCA's `DL1`–`DL6` cluster set is most plausibly a human/CS16-17 parallel of this dILA-1/B-1 ... dILA-6/B-6 sub-family decomposition, with DL1 corresponding to the first/most-dorsal late-born family. The LHX9 signature complicates the assignment but does not by itself overturn the HDCA authors' intended late-born interpretation.

## References

- Webb S, Rose A, Xu C, et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: 10.64898/2026.03.30.714220
- Lawrence JEG, Roberts K, Tuck E, et al. (2024). HOX gene expression in the developing human spine. Nature Communications. DOI: 10.1038/s41467-024-54187-0
- Gray de Cristoforis A, Ferrari F, Clotman F, Vogel T (2020). Differentiation and localization of interneurons in the developing spinal cord depends on DOT1L expression. Molecular Brain. DOI: 10.1186/s13041-020-00623-3
- Lu DC, Niu T, Alaynick WA (2015). Molecular and cellular development of spinal cord locomotor circuitry. Frontiers in Molecular Neuroscience. DOI: 10.3389/fnmol.2015.00025
- Castellani V (2013). Building Spinal and Brain Commissures: Axon Guidance at the Midline. International Scholarly Research Notices. DOI: 10.1155/2013/315387
- Wheaton BJ, Häggström S, Muppavarapu M, González-Castrillón LM, Wilson SI (2022). Alternative LIM homeodomain splice variants are dynamically regulated at key developmental steps in vertebrates. Developmental Dynamics. DOI: 10.1002/dvdy.466
- Hori K, Hoshino M (2012). GABAergic Neuron Specification in the Spinal Cord, the Cerebellum, and the Cochlear Nucleus. Neural Plasticity. DOI: 10.1155/2012/921732
- Zavvarian MM, Hong J, Fehlings MG (2020). The Functional Role of Spinal Interneurons Following Traumatic Spinal Cord Injury. Frontiers in Systems Neuroscience. DOI: 10.3389/fnsys.2020.00127
- Hadas Y, Nitzan N, Furley A, Kozlov S, Klar A (2013). Distinct Cis Regulatory Elements Govern the Expression of TAG1 in Embryonic Sensory Ganglia and Spinal Cord. PLOS ONE. DOI: 10.1371/journal.pone.0057960
- Bui TV, Stifani N, Panek I, Farah C (2015). Genetically identified spinal interneurons integrating tactile afferents for motor control. Journal of Neurophysiology. DOI: 10.1152/jn.00522.2015
- Ignatyev Y, Papadopoulos S, Soretić M, et al. (2025). Innovations in spinal cord cell type heterogeneity across vertebrate evolution. bioRxiv. DOI: 10.1101/2025.10.09.680955
- Roome RB, Yadav A, Flores L, et al. (2025). Ontogeny of the spinal cord dorsal horn. bioRxiv. DOI: 10.1101/2025.03.14.643370
- Onishi K, Zou Y (2018). Sonic Hedgehog switches on Wnt/planar cell polarity signaling in commissural axon growth cones by reducing levels of Shisa2. eLife. DOI: 10.7554/eLife.31097
- Tran TS, Carlin E, Lin R, Martinez E, Johnson JE, Kaprielian Z (2013). Neuropilin2 regulates the guidance of post-crossing spinal commissural axons in a subtype-specific manner. Neural Development. DOI: 10.1186/1749-8104-8-12
- Buckley DM, Burroughs-Garcia J, Kriks S, Lewandoski M, Waters ST (2020). Gbx1 and Gbx2 Are Essential for Normal Patterning and Development of Interneurons and Motor Neurons in the Embryonic Spinal Cord. Journal of Developmental Biology. DOI: 10.3390/jdb8030017
- Meziane H, Fraulob V, Riet F, et al. (2013). The homeodomain factor Gbx1 is required for locomotion and cell specification in the dorsal spinal cord. PeerJ. DOI: 10.7717/peerj.142
- Müller T, Anlag K, Wildner H, Britsch S, Treier M, Birchmeier C (2005). The bHLH factor Olig3 coordinates the specification of dorsal neurons in the spinal cord. Genes & Development. DOI: 10.1101/gad.326105
- Lin YL, Lin YW, Nhieu J, Zhang X, Wei LN (2020). Sonic Hedgehog-Gli1 Signaling and Cellular Retinoic Acid Binding Protein 1 Gene Regulation in Motor Neuron Differentiation and Diseases. Cells. DOI: 10.3390/cells9061477
