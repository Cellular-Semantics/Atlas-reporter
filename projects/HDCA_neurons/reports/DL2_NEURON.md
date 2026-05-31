# DL2 Neuron (DL2_NEURON)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human embryonic spinal cord at Carnegie stages 13–14 (HsapDv:0000023 / HsapDv:0000024, ~4–5 post-conception weeks); whole-embryo dissociation, CNS spinal neuron compartment, n=5,044 cells
Cell Ontology: [dorsal horn interneuron](http://purl.obolibrary.org/obo/CL_0011000) (CL:0011000, broad match — no exact CL term)

## Provenance and naming caveat

`DL2_NEURON` is an HDCA-internal annotation. Three points must be made explicit before any classical cross-walk:

1. **Source.** 100% of the 5,044 cells in this cluster come from HDCA's de novo whole-embryo scRNA-seq (donors F137, F147, F158 at CS13–14). The cluster is **not** inherited from Braun et al. (2023) or any other subatlas (Webb et al., 2026, HDCA Supp. Table 9; HDCA `label_provenance.json`). Cluster purity with respect to the original author annotation is 100% — every cell is labelled literally "DL2 neuron" in `obs.original_author_annotation`.
2. **The `DL` prefix is HDCA-internal nomenclature.** Per HDCA's `provenance_evidence.md`, `DL` stands for "dorsal late" interneuron. This is *not* an established term in the published spinal interneuron literature.
3. **HDCA uses parallel `DA` (dorsal alar), `DB` (dorsal basal) and `DL` (dorsal late) axes.** The presence of separate `DA` and `DB` clusters elsewhere in the HDCA atlas (Webb et al., 2026) shows that the authors distinguish multiple dorsal axes rather than a single dI1–dI6 series. **DL2 therefore cannot be asserted to equal dI2.** The most defensible reading is that DL2 *probably* corresponds to the classical dI2 dorsal interneuron of the Helms & Johnson (2003) / Lai et al. (2016) / Sagner & Briscoe (2019) taxonomy, on the basis of (a) the explicit author statement that the DL series follows classical dorsal-interneuron taxonomy (HDCA `provenance_evidence.md`) and (b) consistency of the HDCA top-marker signature with the dI2 transcriptional profile (see below). This mapping is **inferred**, not asserted by the authors.

## Summary

In HDCA v2, `DL2_NEURON` is a CNS spinal-cord interneuron class captured at Carnegie stages 13–14 from whole-embryo scRNA-seq (Webb et al., 2026). The cluster is dominated by pan-neuronal cytoskeletal and growth-cone genes (`TUBB3`, `STMN2`, `INA`, `DCX`, `MAP1B`, `CRMP1`, `TAGLN3`, `TUBB2B`, `TUBA1A`, `GPC2`, `KIF5C`, `DPYSL4`, `ELAVL3`), consistent with newly postmitotic, axon-elaborating neurons at this very early developmental window. The signature also contains anterior `HOX` genes (`HOXB2`, `HOXA3`, `HOXD3`), placing DL2 cells at a cervical/anterior rostrocaudal level (Lawrence et al., 2024), and one striking distinguishing marker — `CRABP1` (logFC ≈ 6.0) — pointing to retinoid signalling in the cluster (Lin et al., 2020). Notably, the curated HDCA signature contains `CNTN2` (TAG-1), a canonical commissural-axon adhesion molecule, and `POU2F2`, both compatible with a `DL2 ~ dI2` mapping: dI2 are commissural relay neurons defined postmitotically by the combinatorial code `FOXD3 / LHX1 / POU4F1` (Lu et al., 2015; Haimson et al., 2020). However, the classical dI2-defining transcription factors `FOXD3`, `LHX1`, and `POU4F1 (BRN3A)` are **not** in the top 30 DL2 DEGs and are absent from the curated 20-gene signature, so the mapping remains transcriptionally suggestive rather than diagnostic at CS13–14.

## Markers

### HDCA-derived signature

HDCA Supplementary Table 9 lists a curated 20-gene signature for DL2_NEURON: `DCX, NGFR, INA, CNTN2, STMN2, ELAVL3, HOXD3, HOXB2, HOXA3, POU2F2, SNCG, CRABP1, MAP6, TUBB4A, KIF5C, DPYSL4, INSM1, NHLH1, SHD, STMN4` (Webb et al., 2026, HDCA Supp. Table 9). The statistical DEG ranking in Supplementary Table 16 places `TUBB3` first (logFC ≈ 5.68, padj ≈ 3×10⁻²⁸³), followed by `MAP1B`, `CRMP1`, `TAGLN3`, `TUBB2B`, `TUBA1A`, `GPC2`, `STMN2`, `DCX`, `INA`, and — distinctively — `CRABP1` (logFC ≈ 5.99) (Webb et al., 2026, HDCA Supp. Table 16).

### What is *not* in the signature — and why this matters for the dI2 mapping

The diagnostic dI2 markers from the mouse/chick literature — `FOXD3`, `LHX1`, `POU4F1` (BRN3A) — are not in the HDCA DL2 top-30 DEGs nor in the curated 20-gene signature. In the canonical Class-A cardinal-marker scheme, dI2 identity is established postmitotically by this combinatorial code:

> "Class A progenitors give rise to interneuron population 1-3 (dI1-dI3) and class B progenitors give rise to interneuron populations 4-6 (dI4-dI6). In class A progenitors, AtOH1 and Olig3 expression gives way to Pou4f1 expression. Further specification can be seen in expression of Lhx9 by dI1s, FoxD3 by dI2s, and Tlx3 by dI3s."
>
> — Roman et al. (2024)

The combinatorial dI2 code has been confirmed independently:

> "The post mitotic dI2 are defined by a combinatorial expression of Foxd3 + /Lhx1 + /Pou4f1 + TFs (Alaynick et al., 2011, Morikawa et al., 2009, Francius et al., 2013)."
>
> — Haimson et al. (2020)

The absence of `FOXD3 / LHX1 / POU4F1` from the DL2 top-30 has two plausible (non-exclusive) explanations: (i) at CS13–14 these LIM-HD / forkhead transcription factors are expressed but at levels below the rank-genes cutoff dominated by neurofilament and tubulin transcripts; or (ii) DL2 corresponds to a dorsal interneuron population partially distinct from the classical FOXD3+ dI2 — consistent with HDCA's parallel use of `DL` alongside `DA`/`DB`. The signature does, however, contain at least one feature compatible with dI2: `POU2F2` (Oct2), which is dynamically expressed in dI2 cells:

> "To discriminate dI2 INs located in ventral regions from V1 cells, which also produce Foxd3, dI2 were additionally labeled for Brn3a... In control embryos, a majority of dI2 cells distributed in a medial stream of cells migrating from the dI2 progenitor domain towards the ventral region of the spinal cord and covering 60% of the ventro-dorsal axis."
>
> — Masgutova et al. (2019)

### Cytoskeleton, axon-guidance, growth-cone and positional markers

The bulk of the DL2 signature reflects general postmitotic-neuron biology, not dI2-specific identity. The class III β-tubulin `TUBB3` (top DEG), tubulin isotypes (`TUBA1A`, `TUBB2A/B`, `TUBB4A`), microtubule-associated proteins (`MAP1B`, `MAP6`), the doublecortin family (`DCX`), CRMP/collapsin-response-mediator family (`CRMP1`, `DPYSL4` = CRMP4), neurofilament `INA` (α-internexin), `STMN2`/`STMN4` (SCG10 / stathmins), `KIF5C` (neuron-specific kinesin) and `TAGLN3` are growth-cone / axogenesis genes characteristic of newly postmitotic neurons at CS13–14. `CNTN2` (TAG-1) is particularly notable because it is the classical adhesion molecule decorating early commissural axons; together with `GPC2` (glypican-2, an axon-guidance HSPG) and `SNCG` (γ-synuclein, axonal projection marker), it is at least transcriptionally compatible with the commissural projection phenotype of dI2 (Avraham et al., 2009; Lu et al., 2015).

### CRABP1: a distinguishing DL2 marker

`CRABP1` (logFC ≈ 6.0, padj ≈ 4×10⁻²⁰⁹) is a striking, highly enriched DL2 marker that is not prominent in the HDCA signatures of neighbouring spinal interneuron clusters. CRABP1 binds retinoic acid intracellularly and mediates non-canonical retinoid signalling; in motor neurons it is induced by Shh–Gli1 signalling:

> "Cellular retinoic acid-binding protein 1 (CRABP1) is highly expressed in motor neurons... Retinoic acid (RA)/sonic hedgehog (Shh)-induced embryonic stem cells differentiation into motor neurons are employed to study up-regulation of Crabp1 by Shh."
>
> — Lin et al. (2020)

The enrichment of `CRABP1` in DL2 at CS13–14 hints that retinoid signalling shapes the differentiation of this dorsal interneuron pool, although its function in dI2 specifically has not (to our knowledge) been characterised.

### Rostrocaudal positional code

Three HOX genes (`HOXB2`, `HOXA3`, `HOXD3`) co-occur in the curated 20-gene signature, placing DL2 cells at a cervical / upper-cervical rostrocaudal level of the spine (Webb et al., 2026, HDCA Supp. Table 9). Lawrence et al. (2024) showed in the developing human spine:

> "In the axial plane of the spinal cord, we find distinct patterns in the ventral and dorsal domains, providing insights into motor pool organisation and loss of collinearity in HOXB genes."
>
> — Lawrence et al. (2024)

This is consistent with the CS13–14 spinal cord being preferentially sampled at anterior axial levels in HDCA's whole-embryo dissociation protocol.

## Location

### Origin in the alar plate, dorsal-to-ventral order dp2 → dI2

If the DL2 ~ dI2 mapping holds, the cells originate from the `dp2` progenitor domain in the dorsal alar plate. The classical class-A/class-B partition of the dorsal neural tube places dI2 alongside dI1 and dI3 as Class A (roof-plate-dependent) neurons:

> "Neurons of the dorsal horn integrate and relay sensory information and arise during development in the dorsal spinal cord, the alar plate. Class A and B neurons emerge in the dorsal and ventral alar plate, differ in their dependence on roof plate signals for specification, and settle in the deep and superficial dorsal horn, respectively."
>
> — Müller et al. (2005)

The six dorsal cardinal interneuron classes are generated in a stereotyped order:

> "In the early developing neural tube during embryonic days 10-11.5 (E10-11.5), six distinct classes of deep dorsal interneurons (dI1-6) arise from six different progenitor domains (dP1-6), followed by the generation of two lateborn neuronal subtypes of superficial laminae, dIL A and dIL B , from a common dorsal progenitor domain during E11-13"
>
> — Hori & Hoshino (2012)

In this scheme, dI2 sits immediately ventral to dI1 (`DA1` in HDCA) and dorsal to dI3:

> "dI2 neurons originate in the dorsal spinal cord. The progenitor pdI2 cells, topographically positioned between the adjacent dorsally located dI1 and ventrally located dI3 neurons, express Ngn1, Ngn2, Olig3, and Pax3 transcription factors (TFs)."
>
> — Haimson et al. (2021)

### Migration and final settling position

After exiting the cell cycle, dI2 neurons undergo a stereotyped ventral migration:

> "At E5, early post mitotic dI2 neurons migrate ventrally from the dorso-lateral to the mid-lateral spinal cord (Fig. 1A). As they migrate ventrally, at E6, dI2 neurons assume a mid-lateral position along the dorso-ventral axis (Fig. 1B). Subsequently, dI2 neurons migrate medially, and at E17, comparable to pos-gestation day 4 (P4) of mouse, they occupy lamina VII (Fig. 1C). At all rostro-caudal levels and embryonic stages, dI2 axons cross the floor plate (Fig. 1A-D)."
>
> — Haimson et al. (2020)

The combined dynamics of position and transcription factor expression are recapitulated in Gray de Cristoforis et al. (2020):

> "Similarly to dI1, the dI2 subclass initially expresses OLIG3 and migrates to ventral positions. We performed a staining for FOXD3, marking both dI2 and V1 domains at E11.5 and E12.5. At E12.5, we co-stained for FOXD3 and BRN3A to detect the entire dI2 population, since migrating dI2 interneurons temporarily lose BRN3A and maintain FOXD3 expression, but they re-express BRN3A when reaching their target medial area."
>
> — Gray de Cristoforis et al. (2020)

At HDCA's sampled stages (CS13–14, equivalent in mouse to ~E9.5–E10.5), DL2 cells would still be in the earliest postmitotic / early-ventral-migration phase — exactly where neurofilament-triplet / growth-cone genes dominate the transcriptome.

### Rostrocaudal level in HDCA

The HOXB2/HOXA3/HOXD3 expression signature places DL2 cells at an anterior (cervical) rostrocaudal level (Webb et al., 2026, HDCA Supp. Table 9; Lawrence et al., 2024).

## Function (prospective)

At CS13–14, DL2 cells are too early in differentiation to express their full mature functional repertoire. The mature dI2 functional role is inferred from chick and mouse work:

> "dI2 interneurons are ascending, contralaterally projecting, relay interneurons that migrate to the intermediate spinal cord and ventral horn (Gowan et al., 2001;Gross et al., 2002). These interneurons have been suggested to convey sensory information via the spinothalamic tract to the thalamus, based on their location (Figure 4E; Brown, 1981;Tracey, 1985;Gross et al., 2002)."
>
> — Lu et al. (2015)

Their commissural projection identity has been independently confirmed:

> "The Lim-HD proteins Lhx2/9 and Lhx1/5 are expressed in the dorsal spinal interneuron populations dI1 and dI2, respectively... dI1 neurons project axons rostrally, either ipsi- or contra-laterally, while dI2 are mostly commissural neurons that project their axons rostrally and caudally. The longitudinal axonal tracks of each neuronal population self-fasciculate to form dI1- and dI2-specific bundles."
>
> — Avraham et al. (2009)

A summary of the post-injury / circuit-level role is concordant:

> "The dI2 interneurons are located in the intermediate spinal cord and the ventral horn, which are speculated to project contralaterally to transmit sensory input to the thalamus via the spinothalamic tract (Figures 1A,B; Gross et al., 2002)."
>
> — Zavvarian et al. (2020)

In chick, mature dI2 interneurons additionally contribute to gait stabilisation via ascending input to the cerebellum:

> "Peripheral and intraspinal feedback is required to shape and update the output of spinal networks that execute motor behavior. We report that lumbar dI2 spinal interneurons in chicks receive synaptic input from afferents and premotor neurons. These interneurons innervate contralateral premotor networks in the lumbar and brachial spinal cord, and their ascending projections innervate the cerebellum. These findings suggest that dI2 neurons function as interneurons in local lumbar circuits, are involved in lumbo-brachial coupling, and that part of them deliver peripheral and intraspinal feedback to the cerebellum."
>
> — Haimson et al. (2021)

A minor fraction of dI2 cells appears to acquire an inhibitory phenotype:

> "The early post mitotic dI2::GFP at E5 are a homogenous population defined by Foxd3 + /Lhx1 + /Pou4f1 + /Pax2 -(Fig. 1E, S2A,B). The dI2 neurons that undergo ventral migration at E5, as well as at E6 and E14, express variable combinations of Lhx1, Pou4f1 and FoxP1/2/4 (Fig. 1E, S2C,D). Interestingly, about 12% of ventrally migrating dI2 neurons (from E5 to E14) express Pax2 (Fig. 1E, S2D). Pax2 is associated with an inhibitory phenotype (Cheng et al., 2004), suggesting that a subpopulation of dI2 are inhibitory neurons."
>
> — Haimson et al. (2020)

### Stage-appropriate caveat

DL2's mature contralateral, ascending sensory-relay function should be read as a *prospective* fate, not as a direct readout of the CS13–14 transcriptome. The transcriptional state at CS13–14 is dominated by axogenesis and migration machinery (`TUBB3`, `MAP1B`, `CRMP1`, `STMN2`, `DCX`, `INA`, `GPC2`, `CNTN2`, `KIF5C`), not by the markers of mature spinothalamic/cerebellar relay neurons.

## Developmental specification

### Dorsal patterning by roof-plate BMP and Wnt

Dorsal interneurons including the dI1–dI3 (Class A) group depend on Wnt and BMP signals from the roof plate. The Wnt branch:

> "In the developing spinal cord, signals from the roof plate are required for the development of three classes of dorsal interneuron: D1, D2, and D3, listed from dorsal to ventral. Here, we demonstrate that absence of Wnt1 and Wnt3a, normally expressed in the roof plate, leads to diminished development of D1 and D2 neurons and a compensatory increase in D3 neuron populations."
>
> — Muroyama et al. (2002)

The compensatory dorsal expansion of D3 in Wnt1/Wnt3a double knockouts is also documented at the marker level:

> "In Wnt1 −/− ;Wnt3a −/− embryos, only trace cell populations expressing LH2 or Is-let1 remained at the dorsal margin of the neural tube. This indicated that D1 and D2 neurons were largely absent... On the other hand, there was a twofold increase in the population of cells marked by expression of Pax2 and Lim1/2 in the dorsal half of Wnt1 −/− ;Wnt3a −/− spinal cord... Thus the number of D3 neurons was increased in the dorsal spinal cord, compensating for the absence of D1 and D2 neurons."
>
> — Muroyama et al. (2002)

The BMP branch is required, more specifically, for the Class-A dI1-related D1A commissural population:

> "We have examined the function of GDF7, a BMP family member expressed selectively by roof plate cells, in the generation of neuronal cell types in the dorsal spinal cord. We find that GDF7 can promote the differentiation in vitro of two dorsal sensory interneuron classes, D1A and D1B neurons. In Gdf7-null mutant embryos, the generation of D1A neurons is eliminated but D1B neurons and other identified dorsal interneurons are unaffected."
>
> — Lee et al. (1998)

The general dorsal patterning logic is summarised by Sagner & Briscoe (2019):

> "Sonic hedgehog (Shh), emanating first from the notochord and later from the floor plate, induces distinct ventral identities (Marti et al., 1995;Roelink et al., 1995), whereas ligands of the bone morphogenetic protein (BMP) and Wnt families, secreted from the roof plate,"
>
> — Sagner & Briscoe (2019)

Direct evidence for the roof-plate requirement for dI1–dI3 (the Class A group, of which dI2 is a member) comes from roof-plate ablation:

> "Direct evidence showing the requirement for roof plate cells in specification of dorsal neuroepithelial cells comes from genetic ablation of roof plate cells with Gdf7-DTA. Progenitors of dorsal interneurons are subclassified as dI1 to dI6, in dorsal-to-ventral order in developing spinal cord. This ablation causes loss of progenitors of dorsal interneurons dI1-3 and compensatory occupation of a dorsal position by dI4-6."
>
> — Shinozuka & Takada (2021)

### Progenitor identity and the bHLH cascade

dI2 progenitors lie in the `dp2` domain and require Olig3, alongside Ngn1/Ngn2. In `Olig3` mutants, dI2 and dI3 are mis-specified as Class B neurons:

> "We show here that the basic helix-loop-helix (bHLH) gene Olig3 is expressed in progenitor cells that generate class A (dI1-dI3) neurons and that Olig3 is an important factor in the development of these neuronal cell types. In Olig3 mutant mice, the development of class A neurons is impaired; dI1 neurons are generated in reduced numbers, whereas dI2 and dI3 neurons are misspecified and assume the identity of class B neurons."
>
> — Müller et al. (2005)

The postmitotic combinatorial code (`FOXD3 / LHX1 / BRN3A`) is laid down immediately after these cells exit the cell cycle:

> "Newly-born dI2 cells express Lhx1 and Olig3 (Helms and Johnson, 2003;Müller et al., 2005)... At later stages, dI2 interneurons are identified as Foxd3 and Brn3a-positive cells (Helms and Johnson, 2003) in dorsal and medial spinal cord."
>
> — Kabayiza et al. (2017)

Roman et al. (2024) provide the concise progenitor-to-postmitotic mapping that anchors the DL2 ~ dI2 correspondence at the marker level:

> "Class A progenitors give rise to interneuron population 1-3 (dI1-dI3) and class B progenitors give rise to interneuron populations 4-6 (dI4-dI6). In class A progenitors, AtOH1 and Olig3 expression gives way to Pou4f1 expression. Further specification can be seen in expression of Lhx9 by dI1s, FoxD3 by dI2s, and Tlx3 by dI3s."
>
> — Roman et al. (2024)

The same marker scheme survives in recent single-cell ontogeny work:

> "Group 1 was composed of the cardinal spinal cord neuron types clearly identified by classical marker genes including dI1 (Barhl2), dI2 (Foxd3+Slc17a6), dI3 (Isl1+Otp), dI4 (inhibitory Lbx1+ without Dmrt3), dI5 (Phox2a), dI6 (Dmrt3)"
>
> — Roome et al. (2024)

The presence of `Slc17a6` (vGluT2) in the canonical dI2 marker set indicates that the mature dI2 population is overwhelmingly glutamatergic excitatory.

### Developmental timing in HDCA

The DL2 cluster is sampled at CS13 (`HsapDv:0000023`, 57.1%) and CS14 (`HsapDv:0000024`, 42.9%), i.e. ~28–32 days post-conception. This corresponds approximately to mouse E9.5–E10.5, i.e. the onset of dorsal-interneuron neurogenesis (Hori & Hoshino, 2012; Müller et al., 2005). The strong axogenesis/growth-cone signature (`TUBB3`, `STMN2`, `DCX`, `MAP1B`, `CRMP1`) confirms that these are recently-born, axon-elaborating neurons; the diversification of dI2 into precerebellar versus propriospinal sub-populations described in chick (Haimson et al., 2021) is not expected to be resolvable at this stage.

## References

- Webb S, Rose A, Xu C, et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Lawrence JEG, Roberts K, Tuck E, et al. (2024). HOX gene expression in the developing human spine. Nature Communications. DOI: [10.1038/s41467-024-54187-0](https://doi.org/10.1038/s41467-024-54187-0)
- Roman A, Huntemer-Silveira A, Waldron MA, et al. (2024). Cell Transplantation for Repair of the Spinal Cord and Prospects for Generating Region-Specific Exogenic Neuronal Cells. Cells. DOI: [10.3390/cells13050492](https://doi.org/10.3390/cells13050492)
- Lu DC, Niu T, Alaynick WA (2015). Molecular and cellular development of spinal cord locomotor circuitry. Frontiers in Molecular Neuroscience. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Haimson B, Hadas Y, Kania A, Daley M, Cinnamon Y, Lev-Tov A, Klar A (2020). Spinal dI2 interneurons regulate the stability of bipedal stepping. bioRxiv. DOI: [10.1101/2020.01.07.898072](https://doi.org/10.1101/2020.01.07.898072)
- Haimson B, Hadas Y, Bernat N, Kania A, Daley M, Cinnamon Y, Lev-Tov A, Klar A (2021). Spinal lumbar dI2 interneurons contribute to stability of bipedal stepping. eLife. DOI: [10.7554/eLife.68677](https://doi.org/10.7554/eLife.68677)
- Kabayiza KU, Masgutova G, Harris A, Rucchin V, Jacob B, Clotman F (2017). The Onecut Transcription Factors Regulate Differentiation and Distribution of Dorsal Interneurons during Spinal Cord Development. Frontiers in Cellular Neuroscience. DOI: [10.3389/fncel.2017.00157](https://doi.org/10.3389/fncel.2017.00157)
- Gray de Cristoforis A, Ferrari F, Clotman F, Vogel T (2020). Differentiation and localization of interneurons in the developing spinal cord depends on DOT1L expression. Molecular Brain. DOI: [10.1186/s13041-020-00623-3](https://doi.org/10.1186/s13041-020-00623-3)
- Müller T, Anlag K, Wildner H, Britsch S, Treier M, Birchmeier C (2005). The bHLH factor Olig3 coordinates the specification of dorsal neurons in the spinal cord. Genes & Development. DOI: [10.1101/gad.326105](https://doi.org/10.1101/gad.326105)
- Hori K, Hoshino M (2012). GABAergic Neuron Specification in the Spinal Cord, the Cerebellum, and the Cochlear Nucleus. Neural Plasticity. DOI: [10.1155/2012/921732](https://doi.org/10.1155/2012/921732)
- Sagner A, Briscoe J (2019). Establishing neuronal diversity in the spinal cord: a time and a place. Development. DOI: [10.1242/dev.182154](https://doi.org/10.1242/dev.182154)
- Muroyama Y, Fujihara M, Ikeya M, Kondoh H, Takada S (2002). Wnt signaling plays an essential role in neuronal specification of the dorsal spinal cord. Genes & Development. DOI: [10.1101/gad.937102](https://doi.org/10.1101/gad.937102)
- Lee KJ, Mendelsohn M, Jessell TM (1998). Neuronal patterning by BMPs: a requirement for GDF7 in the generation of a discrete class of commissural interneurons in the mouse spinal cord. Genes & Development. DOI: [10.1101/gad.12.21.3394](https://doi.org/10.1101/gad.12.21.3394)
- Zavvarian MM, Hong J, Fehlings MG (2020). The Functional Role of Spinal Interneurons Following Traumatic Spinal Cord Injury. Frontiers in Cellular Neuroscience. DOI: [10.3389/fncel.2020.00127](https://doi.org/10.3389/fncel.2020.00127)
- Avraham O, Hadas Y, Vald L, Zisman S, Schejter A, Visel A, Klar A (2009). Transcriptional control of axonal guidance and sorting in dorsal interneurons by the Lim-HD proteins Lhx9 and Lhx1. BMC Developmental Biology. DOI: [10.1186/1471-213X-9-9](https://doi.org/10.1186/1471-213X-9-9)
- Masgutova G, Harris A, Jacob B, Corcoran L, Clotman F (2019). Pou2f2 Regulates the Distribution of Dorsal Interneurons in the Mouse Developing Spinal Cord. Frontiers in Cellular Neuroscience. DOI: [10.3389/fncel.2019.00263](https://doi.org/10.3389/fncel.2019.00263)
- Roome RB, Yadav A, Flores L, et al. (2024). Ontogeny of the spinal cord dorsal horn. bioRxiv. DOI: [10.1101/2024.04.27.591127](https://doi.org/10.1101/2024.04.27.591127)
- Shinozuka T, Takada S (2021). Morphological and Functional Changes of Roof Plate Cells in Spinal Cord Development. IJMS. DOI: [10.3390/ijms22158203](https://doi.org/10.3390/ijms22158203)
- Lin YL, Lin YW, Nhieu J, Zhang X, Wei LN (2020). Sonic Hedgehog-Gli1 Signaling and Cellular Retinoic Acid Binding Protein 1 Gene Regulation in Motor Neuron Differentiation and Diseases. IJMS. DOI: [10.3390/ijms21124329](https://doi.org/10.3390/ijms21124329)
- Lai HC, Seal RP, Johnson JE (2016). Making sense out of spinal cord somatosensory development. Development. DOI: [10.1242/dev.139592](https://doi.org/10.1242/dev.139592)
- Helms AW, Johnson JE (2003). Specification of dorsal spinal cord interneurons. Current Opinion in Neurobiology. PMID: 12593984. DOI: 10.1016/s0959-4388%2803%2900010-2
