# V2 Interneuron (V2_INTERNEURON)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human fetal spinal cord (neural-tube-derived CNS spinal interneuron; whole-embryo dissociation at CS13–CS14, samples F137/F147/F158)
Cell Ontology: [spinal cord interneuron](http://purl.obolibrary.org/obo/CL_0005000) (CL:0005000, broad match — no exact CL term for V2 / V2a / V2b)

## Summary

In the HDCA v2 integrated reference, the cell-type label `V2_INTERNEURON` resolves to the V2 class of ventral spinal cord interneurons (broad CL:0005000, spinal cord interneuron) within the `CNS_SPINAL_NEURON` broad class, captured from de novo whole-embryo scRNA-seq of three Carnegie-stage 13–14 embryos (F137, F147, F158; n=14854 cells) (Webb et al., 2026). V2 interneurons are derived from the p2 progenitor domain of the ventral neural tube, located immediately dorsal to the pMN (motor neuron) progenitor domain, and are specified by graded Sonic hedgehog (Shh) signalling acting on the Nkx6.1/Irx3/Pax6 transcription-factor code (Ericson et al., 1997; Sander et al., 2000). The V2 class is canonically subdivided into excitatory V2a (Chx10/Vsx2+ Lhx3+ glutamatergic, ipsilateral) and inhibitory V2b (Gata2+/Gata3+/Scl/Tal1+) interneurons whose binary fate decision is initiated by Notch–Delta signalling and the Foxn4/Mash1/Scl programme (Hori & Hoshino, 2012; Lu et al., 2015), together with a Sox1+ V2c subset that branches from V2b (Panayi et al., 2010) and additional uncharacterised V2 sub-populations marked by Arid3c, Onecut factors and Vsx1 (Francius et al., 2016; Renaux et al., 2024). V2a interneurons are central components of the spinal locomotor central pattern generator, providing ipsilateral excitatory drive to motor neurons and regulating left–right alternation, rhythm and speed (Crone et al., 2009; Dougherty & Kiehn, 2010; Li et al., 2022). HDCA Supplementary Table 9 lists a 20-gene curated signature for `V2_INTERNEURON` dominated by pan-neuronal axonogenesis and synaptic genes plus the V2-class GATA factors `GATA2` and `GATA3` (Webb et al., 2026), and Table 16 confirms `GATA2` (logFC 4.39) and `GATA3` (logFC 4.50) as top discriminative DEGs. At CS13–14 the canonical V2a marker `VSX2/CHX10` does not appear in the top signature, so the HDCA cluster represents the V2 grouping (with a transcriptional bias toward early-born V2b/V2c) rather than a single resolved subtype.

## Markers

### HDCA curated signature (Supplementary Table 9)

HDCA assigns refined_celltype `V2_INTERNEURON` to ontology term CL:0005000 (spinal cord interneuron) and lists a curated 20-gene top signature for this population (Webb et al., 2026):

> "refined_celltype": "V2_INTERNEURON", "cell_type_ontology_term_id": "CL:0005000", "top_gene_signatures": "DCX,INA,STMN2,GATA3,ELAVL4,TUBB4A,ATP1A3,GATA2,KIF5C,ASIC4,BSCL2,DPYSL4,SRRM4,RAB3A,ENO2,STMN4,SCG3,GNG3,ELAVL3,GAP43"
>
> — Webb et al. (2026), HDCA Supp. Table 9

Functionally this signature is dominated by three programmes. (i) **V2-class transcription factors**: `GATA3` and `GATA2`, the diagnostic V2b/V2c selectors in the canonical V2a–V2b–V2c scheme (Hori & Hoshino, 2012; Panayi et al., 2010). (ii) **Pan-neuronal axonogenesis and growth-cone machinery**: the doublecortin family (`DCX`), neurofilament `INA` (alpha-internexin), stathmins (`STMN2`, `STMN4`), tubulins (`TUBB4A`), and `GAP43`/`DPYSL4` (the canonical growth-cone proteins). (iii) **Postmitotic-neuronal identity and synaptic vesicle/regulated-secretion machinery**: the HuC/HuD RNA-binding proteins `ELAVL3` and `ELAVL4`, the neuron-specific splicing factor `SRRM4` (nSR100), the Na/K-ATPase α3 `ATP1A3`, the neuronal kinesin `KIF5C`, neuron-specific enolase `ENO2`, the synaptic vesicle GTPase `RAB3A`, secretogranin III `SCG3`, the heterotrimeric G-protein gamma subunit `GNG3`, the seipin gene `BSCL2`, and the acid-sensing channel `ASIC4`. Conspicuously, the canonical V2a markers `VSX2/CHX10`, `SOX14` and `SHOX2` (Ericson et al., 1997; Li et al., 2022) are *not* in the top signature — the V2a sub-population is therefore either a minority within the HDCA V2 grouping at CS13–14 or transcriptionally less distinctive at this early stage relative to the GATA2/GATA3-defined V2b/V2c arm.

### Statistical DEGs (Supplementary Table 16)

The top differentially-expressed genes from the integrated atlas confirm the V2-class GATA selectors and the pan-neuronal axonogenesis programme, with very large effect sizes for the GATA factors:

> "gene": "GATA2", "score": 22.714445, "logfc": 4.3891187, "pval_adj": 3.84875800464149e-111
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "GATA3", "score": 21.265566, "logfc": 4.4958243, "pval_adj": 1.61354955453655e-97
>
> — Webb et al. (2026), HDCA Supp. Table 16

Other top DEGs include `CD24`, `NREP`, `NGRN`, `TUBB`, `RBP1`, `ACTG1`, `GPC2`, `MARCKSL1`, `CLIP3`, `STMN1`, `FSCN1` (growth-cone actin-bundling), `GDI1`, `PFN2`, `DPYSL4`, `DBN1`, `NIPSNAP1`, `NNAT`, `PRDX2`, `MLLT11`, `GABARAP`, `ARL6IP1`, `DCX`, `APLP1`, `H2AFY2`, `TMEFF1`, `RNASEK`, `PCBP4`, and `MTRNR2L12`. The combination of pan-neuronal cytoskeletal/growth-cone genes with very high log-fold-change for both GATA2 and GATA3 is consistent with a recently-postmitotic V2 interneuron population in which V2b/V2c identity dominates the transcriptional signature.

### Canonical V2 transcription factors in the broader literature

The HDCA Table 9 signature recovers the V2b/V2c selector pair `GATA2`/`GATA3` but does not foreground the V2a-specific selectors. The canonical transcription-factor code that subdivides the V2 class is well established:

> "V2 interneurons generated from a homogenous p2 progenitor domain are subdivided into two distinct subtype interneurons: excitatory V2a glutamatergic interneurons, marked by the expression of HD factors Lhx3 and Chx10, and inhibitory V2b GABAergic interneurons, which are characterized by the expression of GATA2/3 and a bHLH transcription factor SCL"
>
> — Hori & Hoshino (2012)

> "A second class of interneurons, V2, is defined by coexpression of Chx10, Lim3, and Gsh4"
>
> — Ericson et al. (1997)

The V2c subset, which extends the original V2a/V2b binary, is marked by Sox1 and arises within the V2b lineage:

> "the transcription factor Sox1 is expressed in, and is required for, a third type of p2-derived interneuron, which we named V2c"
>
> — Panayi et al. (2010)

> "These are close relatives of V2b interneurons, and, in the absence of Sox1, they switch to the V2b fate"
>
> — Panayi et al. (2010)

> "The V2 interneuron class has recently been shown to further diverge to a Sox1-expressing Gata3-negative population named V2c interneurons"
>
> — Lu et al. (2015)

More recent work shows the p2 domain is more diverse than a simple V2a/V2b/V2c trichotomy:

> "A single ventral progenitor population named p2 generates at least five V2 interneuron subsets"
>
> — Francius et al. (2016)

> "Arid3c identifies an uncharacterized subset of V2 that partially overlaps with V2c interneurons. These two populations are characterized by the production of Onecut factors and Sox2, suggesting that they could represent a single functional V2 unit"
>
> — Renaux et al. (2024)

This molecular complexity is highly relevant for interpreting the HDCA V2 cluster: at CS13–14 (~32–35 dpc; the earliest end of the human V2 birthdating window), Foxn4+ p2 progenitors have only recently begun to resolve into V2a, V2b, V2c and additional Arid3c+/Onecut+ subsets, and a single integrated cluster is expected to subsume all of them.

## Location

### CNS ventral spinal cord (p2-domain–derived)

HDCA Supplementary Table 9 assigns `V2_INTERNEURON` to broad_celltype `CNS_SPINAL_NEURON`, germlayer `ECTODERM` and system `NERVOUS_SYSTEM` (n=14854 cells; Webb et al., 2026). The cluster is absent from HDCA Supp Table 17 (the PNS subset), corroborating CNS spinal cord rather than peripheral identity. V2 interneurons are developmentally CNS:

> "somatic motor neurons contribute to peripheral nerve circuitry, they are neural tube–derived and therefore developmentally CNS in origin"
>
> — Webb et al. (2026)

> "Ventral progenitors (p0-p3 and progenitor motor neuron (pMN) domains) broadly give rise to neuronal populations responsible for locomotor coordination."
>
> — Webb et al. (2026)

Within the spinal cord, V2 interneurons settle in lamina VII of the ventral grey matter, immediately dorsal to the motor columns, where they are positioned to provide ipsilateral premotor input:

> "Anatomical studies have placed Chx10+V2a interneurons in spinal cord lamina VII, providing ipsilateral glutamatergic input to MNs, V0 interneurons, and inhibitory interneurons"
>
> — Li et al. (2022)

The final settling position of V2 subsets is further refined by Onecut and Pou2f2 transcription factors:

> "In the embryonic spinal cord, cardinal populations of interneurons diversify into specialized subsets and migrate to defined locations within the spinal parenchyma"
>
> — Harris et al. (2019)

> "the Onecut transcription factors are necessary for proper diversification and distribution of the V2 interneurons in the developing spinal cord"
>
> — Harris et al. (2019)

V2 sub-populations are also differentially distributed along the rostro-caudal axis:

> "each cardinal class of ventral interneurons can be subdivided into several subsets according to the combinatorial expression of different sets of transcription factors, and that these subsets are differentially distributed along the rostrocaudal axis of the spinal cord"
>
> — Francius et al. (2013)

### Developmental staging in HDCA and complementary human references

The HDCA V2 cluster is sampled at Carnegie stages 13–14 from whole-embryo dissociations (samples F137/F147/F158, n=14854 cells), at the earliest end of the V2 birthdating window. In mouse, V2 interneurons are first detectable from approximately the equivalent stage:

> "V2 interneurons are reported to be generated from e10.5 onward"
>
> — Francius et al. (2016)

> "the number of V2a or V2b identified by the presence of Chx10 or Gata3, respectively, was restricted at e9.5 (1-5 cells per hemisection)"
>
> — Francius et al. (2016)

This temporal context explains why GATA3/GATA2 (early-born V2b/V2c selectors) dominate the HDCA Table 9 signature while VSX2/CHX10 (the V2a selector) is below the top-20 threshold: the V2a subset is the later-born or less transcriptionally distinctive arm at CS13–14. Complementary human references at later spinal-cord timepoints — Rayon et al. (2021) at first trimester (CS 12, 14, 17, 19) and Yadav et al. (2023) in the adult — show how V2 heterogeneity sharpens with time:

> "Rayon and colleagues report the transcriptomic profiling of the cells that make up the developing human neural tube from gestational week 4 to 7 (CS 12,CS14,CS17 and CS19)"
>
> — Rayon et al. (2021)

> "the first single-cell atlas of the developing human neural tube to date"
>
> — Rayon et al. (2021)

> "Human and mouse cell types seem to share most of their transcriptional signature"
>
> — Rayon et al. (2021)

> "our work here revealed that dorsal-ventral location is the shared, fundamental axis of spinal neuron transcriptional diversity"
>
> — Yadav et al. (2023)

## Function

### V2a: locomotor central pattern generator (ipsilateral excitation)

V2a interneurons are the best-characterised V2 subtype functionally. They are the principal source of ipsilateral excitatory premotor drive in the spinal locomotor central pattern generator (CPG), controlling left–right alternation, locomotor rhythm, speed and forelimb–hindlimb coordination:

> "The V2a subclass has been identified as an ipsilateral, excitatory premotor interneuron"
>
> — Li et al. (2022)

> "The V2a interneurons constitute a subpopulation of the V2 class and express Chx10. The Chx10 neurons are exclusively glutamatergic and project ipsilaterally"
>
> — Dougherty & Kiehn (2010)

> "Previous studies have shown that a group of ventrally located neurons, designated V2a interneurons, play a key role in maintaining locomotor rhythmicity and in ensuring appropriate left–right alternation during locomotion"
>
> — Dougherty & Kiehn (2010)

> "These V2a interneurons express the transcription factor Chx10"
>
> — Dougherty & Kiehn (2010)

> "ablation of the Chx10 transcription factor, which is critical for V2a fate specification, leads to motor deficits in skilled reaching and diaphragmatic activity in mammals"
>
> — Li et al. (2022)

Genetic ablation of Chx10+ V2a neurons in mouse produces a speed-dependent gait phenotype, demonstrating their specific role in fast-speed left–right alternation:

> "left-right alternation is pro-gressively lost and replaced by synchronous galloping as Chx10::DTA mice run faster"
>
> — Crone et al. (2009)

> "V2a interneurons in the lower spinal cord are responsible for maintaining left-right alternation but only at faster speeds of locomotion"
>
> — Crone et al. (2009)

### V2b: ipsilateral inhibition and speed control

V2b interneurons — the GATA2+/GATA3+ subset that dominates the HDCA Table 9 signature — provide ipsilateral inhibitory premotor input. Recent zebrafish work has shown that V2b ipsilateral inhibition contributes specifically to locomotor speed control, complementing the V2a excitatory drive:

> "Given the persistent, distinguishing expression of Gata3 in both V2b-gly and V2b-mixed subtypes, our data are consistent with the designation of two subclasses within V2b"
>
> — Callahan et al. (2019)

The V2a–V2b–V2d division of labour underlies several distinct features of locomotor activity:

> "The differentiation of V2a/V2b interneurons ensures different aspects of the stereotypic pattern of locomotor activity, including left-right alternation (V2a), flexor-extensor alternation (V2b), and robustness and rhythmicity (V2d)"
>
> — Li et al. (2022)

### V2c and Arid3c+ subsets: late-emerging contributions to locomotor circuit refinement

The Sox1+ V2c subset and the recently-described Arid3c+ subset (which partially overlaps with V2c) make subtle contributions to locomotor circuit formation:

> "V2c subclasses can be defined by expression of Sox1, OC1, OC2, and OC3"
>
> — Lu et al. (2015)

> "its absence results in minor defects in locomotor execution, suggesting a possible function in subtle aspects of spinal locomotor circuit formation"
>
> — Renaux et al. (2024)

At CS13–14 the HDCA V2 cluster is unlikely to resolve these minor subsets transcriptionally; they will likely emerge as resolvable populations only in later-stage human spinal cord references such as Rayon et al. (2021) and Yadav et al. (2023).

## Developmental specification and structure

### Dorsoventral patterning and the p2 progenitor domain

V2 interneurons originate from the p2 progenitor domain of the ventral neural tube, located immediately dorsal to the pMN motor neuron domain. p2 progenitors are specified by graded Sonic hedgehog (Shh) signalling from the notochord and floor plate acting through the Nkx6.1/Irx3/Pax6 cross-repressive transcription-factor code:

> "Shh signaling is necessary for the generation of both classes of ventral interneurons"
>
> — Ericson et al. (1997)

> "the identity and position of generation of neuronal subtypes in the spinal cord is achieved by the exposure of ventral progenitor cells to different Shh-N concentrations"
>
> — Ericson et al. (1997)

Nkx6.1 is essential for V2 and motor neuron specification — its loss eliminates both populations and produces a compensatory ventral expansion of V1 interneurons:

> "These mutants show a dorsal-to-ventral switch in the identity of progenitors and in the fate of postmitotic neurons"
>
> — Sander et al. (2000)

> "At many axial levels there is a complete block in the generation of V2 interneurons and motor neurons and a compensatory ventral expansion in the domain of generation of V1 neurons"
>
> — Sander et al. (2000)

> "V2 and V3 interneurons are defined, respectively, by expression of Chx10 and Sim1"
>
> — Sander et al. (2000)

> "A severe loss of Chx10 V2 neurons was detected in Nkx6.1 mutants at spinal cord levels"
>
> — Sander et al. (2000)

The broader Sagner & Briscoe framework places V2 within the canonical 11-domain spinal cord progenitor scheme used by HDCA:

> "The resulting TF code defines 11 molecularly distinct types of neural progenitors (NPs), each of which gives rise to one or more distinct neuronal subtype"
>
> — Sagner & Briscoe (2019)

### Postmitotic V2a vs V2b binary fate: Notch–Delta and Foxn4

Once p2 progenitors exit the cell cycle, an asymmetric Notch–Delta signalling event between immediate neighbours initiates the binary V2a/V2b fate choice. Foxn4 is the upstream master regulator of V2b fate; it drives Dll4 expression in cells that signal Notch to their sisters, which then activate the V2b programme (Ascl1/Mash1 → Scl → GATA2/GATA3):

> "The asymmetry of V2a versus V2b interneuron fate is initiated by Notch-Delta signaling in immature postmitotic V2 progenitors"
>
> — Hori & Hoshino (2012)

> "Notch receptor ligand Dll4-expressing progenitors give rise to V2a interneurons, maintaining Lhx3 expression while repressing GATA2"
>
> — Hori & Hoshino (2012)

> "Forkhead transcription factor Foxn4 acts as a key regulator of V2b interneuron specification"
>
> — Hori & Hoshino (2012)

> "Foxn4-mutant mice show loss of Dll4 expression and subsequent cell fate change from V2b to V2a"
>
> — Hori & Hoshino (2012)

> "V2a interneurons originate from the p2 progenitor domain and are induced toward their fate by early Notch and TGF-β signals, which trigger the endogenous inhibition of MN fates"
>
> — Li et al. (2022)

> "Notch signaling is a subsequent driver of V2 fate in V2 progenitors"
>
> — Li et al. (2022)

> "the Foxn4 transcription factor cooperates with Mash1 to specify V2b in the early stages in transgenic mice"
>
> — Li et al. (2022)

Reciprocally, loss of Notch signalling drives the V2a fate:

> "V2b fate is specified by active Notch1, Foxn4, Mash1, and Scl"
>
> — Lu et al. (2015)

> "Lack of active Notch1 results in V2a fate, shown in an increase of V2a interneurons at the expense of V2b"
>
> — Lu et al. (2015)

GATA2/GATA3 then consolidate V2b identity downstream of Notch and Scl, and forced GATA2 is sufficient to drive ectopic V2b at the expense of V2a:

> "Forced expression of GATA2 in the chick neural tube induces ectopic formation of V2b interneurons while suppressing the generation of other neurons including V2a interneurons"
>
> — Hori & Hoshino (2012)

> "Mice lacking SCL exhibit downregulation of GATA2 and deficiency in V2b interneurons, accompanied by overproduction of V2a interneurons"
>
> — Hori & Hoshino (2012)

The very high logFC for both `GATA2` (4.39) and `GATA3` (4.50) in HDCA Table 16 is consistent with a V2 cluster transcriptionally dominated by the V2b/V2c arm of this fate decision at CS13–14.

### Intermediate V2 precursor compartment and broader V2 subtype diversity

Beyond the V2a/V2b binary, the p2 domain produces an intermediate precursor compartment marked by Vsx1 and Foxn4, from which all V2 subsets emerge:

> "we provide evidence that the p2 domain produces an intermediate V2 precursor compartment characterized by the transient expression of the transcriptional repressor Vsx1"
>
> — Francius et al. (2016)

> "A single ventral progenitor population named p2 generates at least five V2 interneuron subsets"
>
> — Francius et al. (2016)

The Sox1+ V2c subset and the more recently-described Arid3c+ subset (Renaux et al., 2024) add further molecular and functional diversity to the V2 class. At CS13–14 these minor subtypes are likely to be subsumed within the single HDCA `V2_INTERNEURON` cluster, accounting for the broad CL:0005000 assignment rather than a more specific V2a- or V2b-specific term.

## References

- HDCA consortium / Webb et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper)". *preprint (HDCA)*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Braun et al. (2023). "Comprehensive cell atlas of the first-trimester developing human brain". *Science*. DOI: [10.1126/science.adf1226](https://doi.org/10.1126/science.adf1226)
- Li et al. (2022). "Chx10+V2a interneurons in spinal motor regulation and spinal cord injury". *Frontiers in Cellular Neuroscience*. DOI: [10.3389/fncel.2022.1071815](https://doi.org/10.3389/fncel.2022.1071815)
- Dougherty & Kiehn (2010). "Firing and Cellular Properties of V2a Interneurons in the Rodent Spinal Cord". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.4821-09.2010](https://doi.org/10.1523/JNEUROSCI.4821-09.2010)
- Crone et al. (2009). "In mice lacking V2a interneurons, gait depends on speed of locomotion". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.1206-09.2009](https://doi.org/10.1523/JNEUROSCI.1206-09.2009)
- Zhong et al. (2010). "Electrophysiological Characterization of V2a Interneurons and Their Locomotor-Related Activity in the Neonatal Mouse Spinal Cord". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.4849-09.2010](https://doi.org/10.1523/JNEUROSCI.4849-09.2010)
- Hori & Hoshino (2012). "GABAergic Neuron Specification in the Spinal Cord, the Cerebellum, and the Cochlear Nucleus". *Frontiers in Neural Circuits*. DOI: [10.3389/fncir.2012.00045](https://doi.org/10.3389/fncir.2012.00045)
- Francius et al. (2016). "Vsx1 Transiently Defines an Early Intermediate V2 Interneuron Precursor Compartment in the Mouse Developing Spinal Cord". *Frontiers in Molecular Neuroscience*. DOI: [10.3389/fnmol.2016.00145](https://doi.org/10.3389/fnmol.2016.00145)
- Sander et al. (2000). "Ventral neural patterning by Nkx homeobox genes: Nkx6.1 controls somatic motor neuron and ventral interneuron fates". *Genes & Development*. DOI: [10.1101/gad.820400](https://doi.org/10.1101/gad.820400)
- Ericson et al. (1997). "Pax6 controls progenitor cell identity and neuronal fate in response to graded Shh signaling". *Cell* 90(1):169-180.
- Panayi et al. (2010). "Sox1 Is Required for the Specification of a Novel p2-Derived Interneuron Subtype in the Mouse Ventral Spinal Cord". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.2402-10.2010](https://doi.org/10.1523/JNEUROSCI.2402-10.2010)
- Lu, Niu & Alaynick (2015). "Molecular and cellular development of spinal cord locomotor circuitry". *Frontiers in Molecular Neuroscience*. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Callahan et al. (2019). "Spinal V2b neurons reveal a role for ipsilateral inhibition in speed control". *Neuron*. DOI: [10.1016/j.neuron.2019.05.030](https://doi.org/10.1016/j.neuron.2019.05.030)
- Sagner & Briscoe (2019). "Establishing neuronal diversity in the spinal cord: a time and a place". *Development*. DOI: [10.1242/dev.182154](https://doi.org/10.1242/dev.182154)
- Harris et al. (2019). "Onecut Factors and Pou2f2 Regulate the Distribution of V2 Interneurons in the Mouse Developing Spinal Cord". *eNeuro*. DOI: [10.1523/ENEURO.0246-18.2019](https://doi.org/10.1523/ENEURO.0246-18.2019)
- Francius et al. (2013). "Identification of Multiple Subsets of Ventral Interneurons and Differential Distribution along the Rostrocaudal Axis of the Developing Spinal Cord". *PLOS ONE*. DOI: [10.1371/journal.pone.0070325](https://doi.org/10.1371/journal.pone.0070325)
- Renaux et al. (2024). "Arid3c identifies an uncharacterized subpopulation of V2 interneurons during embryonic spinal cord development". *Frontiers in Cell and Developmental Biology*. DOI: [10.3389/fcell.2024.1466056](https://doi.org/10.3389/fcell.2024.1466056)
- Rayon et al. (2021). "Single-cell transcriptome profiling of the human developing spinal cord reveals a conserved genetic programme with human-specific features". *Development*. DOI: [10.1242/dev.199711](https://doi.org/10.1242/dev.199711)
- Yadav et al. (2023). "A Cellular Taxonomy of the Adult Human Spinal Cord". *Neuron*. DOI: [10.1016/j.neuron.2022.10.019](https://doi.org/10.1016/j.neuron.2022.10.019)
