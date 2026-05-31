# DA1 Neuron (DA1_NEURON)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human embryonic spinal cord at Carnegie stages 13–14 (HsapDv:0000023 / HsapDv:0000024, ~4–5 post-conception weeks); whole-embryo dissociation, CNS spinal neuron compartment, n=3047 cells
Cell Ontology: [dorsal horn interneuron](http://purl.obolibrary.org/obo/CL_0011000) (CL:0011000, broad match — no exact CL term)

## Summary

In the HDCA v2 integrated reference, the refined cell type `DA1_NEURON` is a CNS spinal-cord interneuron class captured at Carnegie stages 13–14 from whole-embryo scRNA-seq (Webb et al., 2026). The HDCA authors adopt a `DA` (dorsal alar) / `DB` (dorsal basal) / `V0`–`V3` (ventral) naming scheme that "follows classical spinal cord interneuron taxonomy (Helms & Johnson 2003; Lai et al. 2016; Sagner & Briscoe 2019)" — placing DA1 as the dorsal-most alar class, equivalent to the classical **dI1** dorsal interneuron of the alar plate (Müller et al., 2005; Lu et al., 2015). The DA1 top marker `LHX9` (logFC 6.16; padj ≈ 6×10⁻²⁹²) is the canonical postmitotic identifier of dI1 neurons born from Atoh1+/Olig3+ progenitors of the most dorsal `dp1` progenitor domain (Gray de Cristoforis et al., 2020; Roman et al., 2024). The remaining DA1 signature — pan-neuronal cytoskeletal and growth-cone genes (`INA, NEFL, NEFM, STMN2, TUBB3, GAP43, DCX`) — is consistent with newly postmitotic neurons at this very early developmental stage, before dI1 sub-pool diversity (commissural dI1c vs. ipsilateral dI1i; spinocerebellar tract subtypes) emerges. HOXB2 expression places DA1 cells at an anterior (cervical/rostral) rostrocaudal level of the spinal cord (Lawrence et al., 2024). At this developmental window, DA1_NEURON is best understood as the dorsal-most alar plate (Class A) interneuron class — the population that in subsequent fetal stages will diversify into proprioceptive relay neurons projecting via the spinocerebellar and cuneocerebellar tracts (Castellani, 2013; Bui et al., 2015; Pop et al., 2021).

## Markers

### HDCA-derived signature

HDCA Supplementary Table 9 lists a curated 20-gene signature for DA1_NEURON:

`GAP43, INA, TRH, DCX, NEFL, STMN2, LHX9, NGFR, L1CAM, TUBB4A, RGMB, RAB3A, RTN1, NEFM, ATP1A3, ENO2, SNCG, PRRT2, HOXB2, KIF5C` (Webb et al., 2026, HDCA Supp. Table 9). The statistical DEG ranking in Supplementary Table 16 places `LHX9` first (logFC ≈ 6.16, padj ≈ 6×10⁻²⁹²), followed by `INA` (5.56), `TUBB3` (5.79), `STMN2` (5.90), `NEFM` (5.91) and `NEFL` (5.55), with `HOXB2` (4.40) and `RGMB` (4.53) also in the top 30 (Webb et al., 2026, HDCA Supp. Table 16).

### LHX9 — the diagnostic dI1 marker

LHX9 is the single most informative marker for assigning DA1 to the classical dI1 class. Gray de Cristoforis et al. (2020) state directly:

> "The dorsal-most interneuron class, dI1, is characterized by expression of Lhx2 and Lhx9."
>
> — Gray de Cristoforis et al. (2020)

They further describe how dI1 progenitors give rise to two subpopulations defined by the relative levels of LHX2 vs. LHX9:

> "From a shared pool of progenitors, two subpopulations emerge based on the proportion of Lhx2 and Lhx9 transcripts: ventromedially located interneurons express highly LHX2 and to a lesser extend LHX9, whereas a ventrolateral counterpart expresses highly LHX9 but not"
>
> — Gray de Cristoforis et al. (2020)

LHX9 is robustly expressed throughout dI1 development, as Wheaton et al. (2022) note:

> "pan-Lhx9, which labels all Lhx9 variants, was expressed at all stages of dI1 neuron development analyzed: in neurons as they delaminate from the ventricular zone, in migrating neurons and in maturing neurons as they settle in the deep dorsal horn."
>
> — Wheaton et al. (2022)

A textbook-level mapping of cardinal-class markers also assigns LHX9 specifically to the dI1 class:

> "Class A progenitors give rise to interneuron population 1-3 (dI1-dI3) and class B progenitors give rise to interneuron populations 4-6 (dI4-dI6). In class A progenitors, AtOH1 and Olig3 expression gives way to Pou4f1 expression. Further specification can be seen in expression of Lhx9 by dI1s, FoxD3 by dI2s, and Tlx3 by dI3s."
>
> — Roman et al. (2024)

The full LIM-HD/BAR-class postmitotic identity of dI1 neurons additionally includes BARHL1/2 and Brn3a/POU4F1 (Lu et al., 2015; Wilson & Sweeney, 2023). These are not in the top 30 DEGs of HDCA's DA1 cluster, which is expected for cells captured at CS13–14, when neurofilament and growth-cone genes (`NEFL`, `NEFM`, `INA`, `STMN2`, `GAP43`, `DCX`) dominate the expression profile (Webb et al., 2026):

> "Dl1 neurons are generated from a pool of progenitor cells expressing Math1, and can be identified by two LIM transcription factors, Lhx2 and Lhx9"
>
> — Castellani (2013)

### Other markers: cytoskeleton, growth cone, positional identity

The bulk of the DA1 signature reflects general postmitotic-neuron biology rather than dI1-specific identity. The neurofilament triplet (`NEFL`, `NEFM`, `INA` / α-internexin) and the type-IV tubulin `TUBB4A` are abundant in newly born projection neurons; `GAP43`, `DCX`, `STMN2`, `L1CAM`, `RTN1` and `KIF5C` are growth-cone, axon-guidance and microtubule-trafficking genes that mark axonogenesis at CS13–14. `RGMB` (RGM-b / DRAGON), a BMP co-receptor, is consistent with the BMP signalling environment from the dorsal roof plate that specifies the dI1 class. `HOXB2` provides positional context: in the developing human spine, HOX gene expression encodes anterior–posterior identity, and HOXB2 marks an anterior (upper cervical / hindbrain–spinal junction) level (Lawrence et al., 2024). HDCA pre-assigns the broad Cell Ontology term CL:0000540 (neuron) for this cluster (Webb et al., 2026, HDCA Supp. Table 9), reflecting the absence of a CL term specific to dI1.

## Location

### Origin in the alar plate of the dorsal neural tube

dI1 / DA1 neurons originate from the most dorsal progenitor domain (`dp1`) of the alar plate, directly adjacent to the roof plate. Müller et al. (2005) describe this division:

> "Neurons of the dorsal horn integrate and relay sensory information and arise during development in the dorsal spinal cord, the alar plate."
>
> — Müller et al. (2005)

> "Class A and B neurons emerge in the dorsal and ventral alar plate, differ in their dependence on roof plate signals for specification, and settle in the deep and superficial dorsal horn, respectively."
>
> — Müller et al. (2005)

Hori & Hoshino (2012) place this within the broader dI1–6 framework, with dI1 the dorsal-most:

> "In the early developing neural tube during embryonic days 10-11.5 (E10-11.5), six distinct classes of deep dorsal interneurons (dI1-6) arise from six different progenitor domains (dP1-6), followed by the generation of two lateborn neuronal subtypes of superficial laminae, dIL A and dIL B , from a common dorsal progenitor domain during E11-13"
>
> — Hori & Hoshino (2012)

HDCA's `DA` prefix (dorsal alar) maps onto Class A of this scheme; `DB` (dorsal basal) maps onto Class B; numbering proceeds dorsal-to-ventral, so DA1 corresponds to the dorsal-most member, dI1.

### Migration and final settling position

dI1 neurons are born in the dorsal ventricular zone and migrate to the deep dorsal horn, with later-developing sub-populations also extending ventrally:

> "Defined by expression of Atoh1 (formerly Math1), dI1 INs are also a population of dorsally derived neurons that migrate ventrally to be positioned in the deep dorsal horn of the spinal cord"
>
> — Bui et al. (2015)

> "The proprioceptive dl1 class settles at the most dorsal position of the spinal cord, close to the roof plate, and transmits information to the cerebellum via the spinocerebellar and the cuneocerebellar tracts."
>
> — Castellani (2013)

Cross-species single-cell work confirms that the cardinal class architecture, including dI1, is conserved in tetrapods:

> "The ventral spinal cord displayed a characteristic dorsoventral layering of V0-V3, dI1-2, and dI6 interneurons, mirroring previous distributions in the mouse spinal cord"
>
> — Ignatyev et al. (2025)

### Rostrocaudal position in HDCA

HOXB2 in the DA1 top markers (logFC 4.40) indicates anterior (cervical / upper rostral) positional identity. Lawrence et al. (2024) demonstrate that human fetal spinal cord cell types are organised along the AP axis by HOX-gene combinatorial codes:

> "In the axial plane of the spinal cord, we find distinct patterns in the ventral and dorsal domains, providing insights into motor pool organisation and loss of collinearity in HOXB genes."
>
> — Lawrence et al. (2024)

## Function

At CS13–14 the DA1 cluster is best interpreted as a transcriptionally early, postmitotic Class A alar interneuron population — actively undergoing axonogenesis and migration. Its mature functional role is inferred from the well-characterised dI1 lineage in mouse and chick.

### Proprioceptive sensorimotor relay (mature dI1 role)

Once they mature, dI1 neurons relay proprioceptive and tactile information from the periphery to the cerebellum:

> "It is composed of two types of neurons, those establishing ipsilateral projections (dl1i) and those establishing commissural projections (dl1c)"
>
> — Castellani (2013)

> "These neurons form three distinct spinocerebellar tracts (SCTs), by which sensory feedback is relayed to the cerebellum."
>
> — Bui et al. (2015)

The two subdivisions of dI1 are functionally distinguished by axonal projection: dI1c neurons cross the midline to project contralaterally, whereas dI1i project ipsilaterally. Both are glutamatergic and identified by BARHL1/2:

> "The dI1 population in mice is composed of an ipsilateral (dI1-ipsi) and a contralateral LHX2expressing (dI1-contra) population, both of which express the transcription factors BARHL1/2 and are glutamatergic"
>
> — Wilson & Sweeney (2023)

Distinct rostrocaudal levels of dI1 contribute to different spinocerebellar circuits in adult animals:

> "we find that two of the indirect pathways, the spino-lateral reticular nucleus and spino-olivary pathways, are in part, derived from cervical Atoh1-lineage neurons, whereas thoracolumbar Atoh1-lineage neurons project mostly locally within the spinal cord."
>
> — Pop et al. (2021)

### Caveat — developmental-stage appropriateness

HDCA's DA1 cluster captures dI1 cells very early in their differentiation (CS13–14, ~4–5 pcw), before commissural-vs-ipsilateral sub-fates and spinocerebellar projection subtypes are resolved. The transcriptional state at this stage is dominated by neurofilament-triplet expression, axon-growth machinery (GAP43, DCX, STMN2, L1CAM) and the postmitotic LIM-HD selector LHX9. The mature proprioceptive-relay function should therefore be read as a prospective fate of the DA1 class, not as evidence that CS13–14 DA1 neurons already project via the spinocerebellar tracts.

## Developmental Specification

### Dorsal patterning by roof-plate BMP and Wnt

The dorsal-to-ventral pattern of the spinal cord is set by opposing morphogen gradients. Sagner & Briscoe (2019) summarise:

> "Sonic hedgehog (Shh), emanating first from the notochord and later from the floor plate, induces distinct ventral identities"
>
> — Sagner & Briscoe (2019)

> "ligands of the bone morphogenetic protein (BMP) and Wnt families, secreted from the roof plate,"
>
> — Sagner & Briscoe (2019)

Both branches of the dorsal signal are individually required for dI1 specification. The Wnt branch:

> "In the developing spinal cord, signals from the roof plate are required for the development of three classes of dorsal interneuron: D1, D2, and D3, listed from dorsal to ventral."
>
> — Muroyama et al. (2002)

> "Here, we demonstrate that absence of Wnt1 and Wnt3a, normally expressed in the roof plate, leads to diminished development of D1 and D2 neurons and a compensatory increase in D3 neuron populations."
>
> — Muroyama et al. (2002)

The BMP-family branch, specifically GDF7 from the roof plate, is required for the commissural dI1A (dI1c) sub-class:

> "We find that GDF7 can promote the differentiation in vitro of two dorsal sensory interneuron classes, D1A and D1B neurons."
>
> — Lee et al. (1998)

> "In Gdf7-null mutant embryos, the generation of D1A neurons is eliminated but D1B neurons and other identified dorsal interneurons are unaffected."
>
> — Lee et al. (1998)

Additional BMP family members are required for the broader dI1 lineage:

> "Loss of function experiments with BMP7 in chick and Bmp7 mutant mice results in loss of dI1, dI3, and dI5"
>
> — Lu et al. (2015)

### Progenitor identity and the bHLH cascade

dI1 neurons arise from the dorsal-most `dp1` progenitor domain, defined by combinatorial bHLH expression. Lu et al. (2015) describe the postmitotic identity:

> "The roof-plate-dependent Class A dp1 progenitors of the dI1 class express the bHLH transcription factors Olig3 and Math1"
>
> — Lu et al. (2015)

> "The dI1 neurons in mouse are born between E10 and E12.5 and express Lhx2/9, Barhl1 (bar homeobox like 1) and Brn3a (Pou4f1, a class IV POU domaincontaining transcription factor; Helms and Johnson, 1998)."
>
> — Lu et al. (2015)

Olig3 is specifically required to coordinate Class A specification:

> "the basic helix-loop-helix (bHLH) gene Olig3 is expressed in progenitor cells that generate class A (dI1-dI3) neurons"
>
> — Müller et al. (2005)

Roman et al. (2024) provide the concise progenitor-to-cell-type mapping that links the molecular fate determinants to HDCA's DA1 signature:

> "Class A dorsal progenitors, which are dependent on roof plate signaling for appropriate specification, predominantly express AtOH1 and Olig3."
>
> — Roman et al. (2024)

### Developmental timing in HDCA

The DA1 cluster is captured at CS13 (HsapDv:0000023, 62.4% of cells) and CS14 (HsapDv:0000024, 37.6%), i.e. ~28–32 days post-conception. This corresponds to the very onset of dI1 generation — in mouse, the homologous dp1 progenitors generate dI1 between E10 and E12.5 (Lu et al., 2015), and the strong expression of growth-associated genes (`GAP43`, `DCX`, `STMN2`) in the HDCA cluster confirms these are recently born, actively elaborating neurons. Sub-pool diversification of dI1 into commissural (dI1c) vs. ipsilateral (dI1i), and into rostral / dorsal / ventral spinocerebellar tract neurons, occurs later in development and is therefore not expected to be resolvable in DA1 at this stage.

## References

- Webb S, Rose A, Xu C, et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: 10.64898/2026.03.30.714220
- Lawrence JEG, Roberts K, Tuck E, et al. (2024). HOX gene expression in the developing human spine. Nature Communications. DOI: 10.1038/s41467-024-54187-0
- Sagner A, Briscoe J (2019). Establishing neuronal diversity in the spinal cord: a time and a place. Development. DOI: 10.1242/dev.182154
- Lu DC, Niu T, Alaynick WA (2015). Molecular and cellular development of spinal cord locomotor circuitry. Frontiers in Molecular Neuroscience. DOI: 10.3389/fnmol.2015.00025
- Müller T, Anlag K, Wildner H, Britsch S, Treier M, Birchmeier C (2005). The bHLH factor Olig3 coordinates the specification of dorsal neurons in the spinal cord. Genes & Development. DOI: 10.1101/gad.326105
- Hori K, Hoshino M (2012). GABAergic Neuron Specification in the Spinal Cord, the Cerebellum, and the Cochlear Nucleus. Neural Plasticity. DOI: 10.1155/2012/921732
- Gray de Cristoforis A, Ferrari F, Clotman F, Vogel T (2020). Differentiation and localization of interneurons in the developing spinal cord depends on DOT1L expression. Molecular Brain. DOI: 10.1186/s13041-020-00623-3
- Wilson A, Sweeney LB (2023). Spinal cords: Symphonies of interneurons across species. Frontiers in Neural Circuits. DOI: 10.3389/fncir.2023.1146449
- Ignatyev Y, Papadopoulos S, Soretić M, et al. (2025). Innovations in spinal cord cell type heterogeneity across vertebrate evolution. bioRxiv. DOI: 10.1101/2025.10.09.680955
- Wheaton BJ, Häggström S, Muppavarapu M, González-Castrillón LM, Wilson SI (2022). Alternative LIM homeodomain splice variants are dynamically regulated at key developmental steps in vertebrates. Developmental Dynamics. DOI: 10.1002/dvdy.466
- Pop IV, Espinosa F, Blevins CJ, et al. (2021). Structure of Long-Range Direct and Indirect Spinocerebellar Pathways as Well as Local Spinal Circuits Mediating Proprioception. Journal of Neuroscience. DOI: 10.1523/jneurosci.2157-20.2021
- Bui TV, Stifani N, Panek I, Farah C (2015). Genetically identified spinal interneurons integrating tactile afferents for motor control. Journal of Neurophysiology. DOI: 10.1152/jn.00522.2015
- Castellani V (2013). Building Spinal and Brain Commissures: Axon Guidance at the Midline. International Scholarly Research Notices. DOI: 10.1155/2013/315387
- Muroyama Y, Fujihara M, Ikeya M, Kondoh H, Takada S (2002). Wnt signaling plays an essential role in neuronal specification of the dorsal spinal cord. Genes & Development. DOI: 10.1101/gad.937102
- Lee KJ, Mendelsohn M, Jessell TM (1998). Neuronal patterning by BMPs: a requirement for GDF7 in the generation of a discrete class of commissural interneurons in the mouse spinal cord. Genes & Development. DOI: 10.1101/gad.12.21.3394
- Roman A, Huntemer-Silveira A, Waldron MA, et al. (2024). Cell Transplantation for Repair of the Spinal Cord and Prospects for Generating Region-Specific Exogenic Neuronal Cells. Cells. DOI: 10.3390/cells13050492
- Braun E, Danan-Gotthold M, Borm LE, et al. (2023). Comprehensive cell atlas of the first-trimester developing human brain. Science. DOI: 10.1126/science.adf1226
