# V1 Interneuron (V1_INTERNEURON)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human fetal spinal cord (CNS_SPINAL_NEURON; ventral neural tube p1 domain; whole-embryo dissociation at CS13–CS14, samples F137/F147/F158, n=7504 cells)
Cell Ontology: [spinal cord ventral column interneuron](http://purl.obolibrary.org/obo/CL_2000023) (CL:2000023, broad match — no exact CL term for V1 cardinal class; NTR needed)

## Summary

In the HDCA v2 integrated reference, the cell-type label `V1_INTERNEURON` resolves to V1 spinal interneurons — the cardinal class of Engrailed-1 (EN1)+ ipsilateral inhibitory interneurons that originate from the p1 progenitor domain of the ventral neural tube (Saueressig et al., 1999; Sapir et al., 2004; Hori & Hoshino, 2012). HDCA captures these cells at Carnegie stages 13–14 from de novo whole-embryo scRNA-seq of three embryos (F137, F147, F158; n=7504 cells), assigns them to broad_celltype `CNS_SPINAL_NEURON` and ontology term CL:0005000 (spinal cord interneuron), and lists a curated Table 9 top-20 signature in which the canonical V1 selector transcription factor **EN1** appears together with the V1-associated forkhead TF **FOXD3**, the cellular retinoic-acid-binding protein **CRABP1**, rostro-caudal HOX patterning genes **HOXB2/HOXD3**, and pan-neurogenic axon-growth markers (Webb et al., 2026). Statistical DEGs in Table 16 are dominated by `LAMP5`, `CRABP1`, `INA`, `STMN2`, `TUBB3`, `DCX` and `HOXB2`, all with very large effect sizes (Webb et al., 2026). In the mature mouse spinal cord, the V1 cardinal class fractionates into at least four mutually exclusive clades — Renshaw (MafA+), Pou6f2, Foxp2, and Sp8 — that organise recurrent and reciprocal inhibition of motor neurons and control locomotor rhythm frequency and flexor–extensor burst duration (Benito-Gonzalez & Alvarez, 2012; Bikoff et al., 2016; Chapman et al., 2024; Worthy et al., 2024). At CS13–14 the HDCA V1 cluster represents a stage *before* full clade resolution: postmitotic V1 neurons have only just emerged from p1, EN1 has been switched on, and the curated signature carries FOXD3 (a pan-V1 postmitotic marker) but not yet the FoxP2/MafA/Pou6f2/Sp8 clade selectors that segregate postnatally (Benito-Gonzalez & Alvarez, 2012; Chapman et al., 2024). V1_INTERNEURON is absent from HDCA Supplementary Table 17 (the PNS subset), confirming a CNS spinal-interneuron identity (Webb et al., 2026).

## Markers

### HDCA curated signature (Supplementary Table 9)

HDCA assigns refined_celltype `V1_INTERNEURON` to ontology term CL:0005000 and lists a curated 20-gene top signature for this population (Webb et al., 2026):

> "top_gene_signatures": "DCX,INA,STMN2,TUBB4A,NEFL,EN1,RAB3A,KIF5C,ATP1A3,ELAVL4,DNER,CRABP1,FOXD3,HOXB2,L1CAM,HOXD3,SNCG,NEFM,GNG3,ENO2"
>
> — Webb et al. (2026), HDCA Supp. Table 9

This signature combines three programmes. (i) **V1-specific selectors** — `EN1` (Engrailed-1, the canonical postmitotic marker of all V1 interneurons) and `FOXD3` (a broadly expressed postmitotic V1 forkhead TF that is also required for Renshaw cell differentiation) (Saueressig et al., 1999; Sapir et al., 2004; Lu et al., 2015). (ii) **Rostro-caudal positional code** — `HOXB2` and `HOXD3`, consistent with the cervical/upper-thoracic levels sampled at CS13–14 (Francius et al., 2013). (iii) **Pan-neurogenic identity** — the neurofilament triplet `NEFL/NEFM/INA`, the tubulin `TUBB4A`, the doublecortin `DCX`, the synaptic-vesicle and signalling genes `RAB3A/GNG3`, the axon-guidance ligand-receptor `DNER`, the adhesion molecule `L1CAM`, the kinesin `KIF5C`, the Na/K-ATPase α3 subunit `ATP1A3` and the neuronal RNA-binding protein `ELAVL4` — together a postmitotic-neuron axonogenesis signature. The presence of `CRABP1` (cellular retinoic-acid-binding protein 1) reflects the active retinoic-acid environment of the cervical neural tube at this stage.

### Statistical DEGs (Supplementary Table 16)

The top differentially-expressed genes from the integrated atlas reinforce and extend the curated signature, with very large effect sizes:

> "gene": "INA", "score": 36.527443, "logfc": 5.604483, "pval_adj": 7.76770834609366e-288
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "CRABP1", "score": 35.991486, "logfc": 6.926262, "pval_adj": 9.49231768002139e-280
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "LAMP5", "score": 35.983948, "logfc": 7.1272464, "pval_adj": 9.49231768002139e-280
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "HOXB2", "score": 31.343296, "logfc": 4.2067566, "pval_adj": 1.43282545899151e-212
>
> — Webb et al. (2026), HDCA Supp. Table 16

`LAMP5` has the largest log-fold change (7.1) — an interesting finding because in adult cortex LAMP5 marks a subset of GABAergic interneurons; here it appears among the most V1-specific genes in the human fetal spinal cord. The combination `INA`/`STMN2`/`TUBB3`/`DCX` is shared with neighbouring postmitotic ventral neurons (see HDCA MN report) and reflects general postmitotic-neuron axonogenesis; what distinguishes V1 from MN at CS13–14 is the strong enrichment of `CRABP1`, `LAMP5` and `HOXB2`, the presence of `EN1` and `FOXD3` in the curated signature, and the *absence* of motor-neuron-specific genes (e.g. `ECEL1`, `MNX1`, `ISL1`, `NEFL` super-high effect sizes) that distinguish the HDCA MN cluster.

### V1 selector transcription factors and their downstream clades

The HDCA Table 9 entry of `EN1` matches the canonical postmitotic V1 selector documented across vertebrates:

> "V1 interneurons, marked by Engrailed-1 (En1) and Foxd3 expression, are inhibitory neurons that project axons ipsilaterally and rostrally. The V1 interneurons are initially generated as a homogeneous GABAergic interneuron population in developing neural tubes but subsequently differentiate into a range of inhibitory interneuron cell types, including Renshaw cells (RCs) and putative reciprocal Ia inhibitory interneurons"
>
> — Hori & Hoshino (2012)

> "V1-INs originate from p1 progenitors and, after they become postmitotic, specifically express the transcription factor engrailed-1, a property that permits genetic labeling of V1 lineages from embryo to adult."
>
> — Benito-Gonzalez & Alvarez (2012)

> "V1 neurons derive from the p1 progenitor domain, express the transcription factor Engrailed-1 (EN1) and the neurotransmitters GABA and/or glycine, and target ipsilateral motor neurons and other ipsilateral inhibitory neurons"
>
> — Wilson & Sweeney (2023)

Postnatally, the V1 cardinal class resolves into four mutually exclusive clades:

> "V1 interneurons fractionate into at least four mutually exclusive subsets (clades) defined by differential expression of the transcription factors Foxp2, MafA, Pou6f2, and Sp8 in the neonatal lumbar and thoracic spinal cord"
>
> — Chapman et al. (2024)

> "Sequential neurogenesis delineates different V1 subsets: two early born (Renshaw and Pou6f2) and two late born (Foxp2 and Sp8). Early born Renshaw cells and late born Foxp2-V1 interneurons are tightly coupled to motoneurons, while early born Pou6f2-V1 and late born Sp8-V1 interneurons are not"
>
> — Worthy et al. (2024)

At CS13–14 the HDCA V1 cluster is captured at — or just after — the very onset of postmitotic V1 differentiation, before this clade resolution is molecularly visible. The Table 9 signature is therefore consistent with the pan-V1 / shared-V1 state: EN1 plus FOXD3 are present, but MafA/Foxp2/Pou6f2/Sp8 are not enriched as cluster markers. This is the expected state because clade-specific TFs appear with neurogenesis and migration:

> "MafB and FoxP2 are upregulated shortly after cellular birth. MafB upregulates in RCs during cell migration; FoxP2 is upregulated in late-generated V1-INs as they exit the progenitor zone. Moreover, early-generated V1-INs differ from FoxP2 V1-INs by the early upregulation of calbindin expression. These observations suggest that the differentiation of early and late V1-INs and their subgroups (RCs within the early group) starts at the time of birth (i.e., there is no homogeneous V1 population in the early embryo that later diversifies). Thus, time of neurogenesis is immediately translated into different V1 phenotypes, ruling out integration into synaptic circuits as a major factor determining V1-IN diversity."
>
> — Benito-Gonzalez & Alvarez (2012)

Other V1-subset transcription factors documented in the literature (but not enriched in HDCA Table 9 / Table 16 for this CS13–14 cluster) include calbindin (`CALB1`), `MafB`, `OC1/OC2/OC3` (Onecut), `Pax2`, `Pou4F1` and `Prdm8` (Francius et al., 2013).

## Location

### CNS spinal cord — ventral horn (p1 progenitor domain)

HDCA Supplementary Table 9 assigns `V1_INTERNEURON` to broad_celltype `CNS_SPINAL_NEURON`, germlayer `ECTODERM` and system `NERVOUS_SYSTEM` (Webb et al., 2026). The cells are absent from Table 17 (the PNS subset), corroborating their CNS identity. Within the ventral spinal cord, V1 interneurons are p1-domain-derived and project ipsilaterally:

> "Progenitor cells of both V0 and V1 share a combinatorial expression of Pax6 and Dbx2. Dbx1 is, however, uniquely expressed in V0 progenitor cells and is considered an essential factor for the specification of V0 interneurons. In mice lacking Dbx1, V0 interneurons are lost, and concomitantly V0_D and V0_V interneurons are respecified into Lbx1-positive dI6 dorsal interneurons and En1-positive V1 interneurons, respectively. In contrast, Nkx6.2 is expressed in V1 progenitor cells and is required for the specification of V1 neuronal fate, also it represses the generation of V0 interneurons."
>
> — Hori & Hoshino (2012)

> "Pax6 controls progenitor cell identity and neuronal fate in response to graded Shh signaling."
>
> — Ericson et al. (1997)

Pax6 is essential for upstream patterning of the p1 domain and also for Renshaw-cell development specifically (Sapir et al., 2004). Within the embryonic ventral horn at CS13–14, postmitotic V1 neurons emerge from p1, migrate laterally, and begin to settle into stereotyped positions; clade-specific positions (Renshaw cells near the motor-axon exit, FoxP2-V1 cells closer to the motor pools) consolidate only later in development (Benito-Gonzalez & Alvarez, 2012).

### Rostro-caudal axis

The HDCA V1 curated signature contains the HOX genes `HOXB2` and `HOXD3` (with `HOXB2` also a top DEG in Table 16; Webb et al., 2026). These mark rostral cervical/upper-thoracic levels and are consistent with the whole-embryo CS13–14 sampling. Rostro-caudal differences in V1 subset distribution have been documented for embryonic V1 interneurons:

> "A survey in E12.5 mice showed that several V1 subclasses can be defined by expression of Calbindin, OC1, OC2, OC3, Foxd3, En1, MafB, FoxP2, Foxd3, Foxp4, Pax2, Arx, Evx1, Nurr1, BhlhB5, Pou4F1, Pou3F1, and Prdm8"
>
> — Francius et al. (2013) / quoted via Lu et al. (2015)

## Function

### Ipsilateral inhibitory motor control

V1 interneurons are local-circuit inhibitory neurons that synapse onto ipsilateral motor neurons and other ipsilateral interneurons:

> "V1 interneurons (INs), an embryonic class of interneurons that transiently express the En1 transcription factor, differentiate as local circuit inhibitory interneurons and form synapses with motor neurons. Furthermore, we show that a subset of V1 INs differentiates as Renshaw cells, the interneuronal cell type that mediates recurrent inhibition of motor neurons."
>
> — Sapir et al. (2004)

> "Engrailed-1 expression uniquely marks a class of ascending interneurons, called circumferential ascending (CiA) interneurons, with ipsilateral axonal projections in both motor and sensory regions of spinal cord. These cells express the glycine transporter 2 gene and are the only known ipsilateral interneurons positive for this marker of inhibitory transmission."
>
> — Higashijima et al. (2004)

This zebrafish work establishes the ancestral En1+/glycinergic identity from which mammalian V1 interneurons diversify into Renshaw cells, Ia inhibitory interneurons, and the postnatal Pou6f2/Sp8 clades.

### Renshaw cells: recurrent inhibition of motor neurons

The classic Renshaw cell is a V1-derived recurrent-inhibitory interneuron that receives motor-axon-collateral excitatory input and inhibits the same motor neurons that excite it:

> "Renshaw cells use both glycine and GABA as neurotransmitters, transiently express Gad65 early in embryonic development and have both motor neurons and Ia interneurons as targets. They also express calbindin D28K embryonically and continue to express this marker into adulthood. They receive input from motor neuron collaterals that release acetylcholine, glutamate, and aspartate. Genetic tracing studies showed that Renshaw cells are derived from an En1+ progenitor pool and, although they are not lost in the absence of En1, they do have fewer motor neuron recurrent inputs. They are, however, lost in the absence of Pax6. Recent study showed that selective activation of the Onecut transcription factors Oc1 and Oc2 during the first wave of V1 interneuron neurogenesis is a key step in the Renshaw cell differentiation; furthermore Renshaw cell development is dependent on the forkhead transcription factor Foxd3, which is more broadly expressed in post-mitotic V1 interneurons"
>
> — Lu et al. (2015)

The presence of `FOXD3` in the HDCA V1 curated signature is consistent with the requirement of Foxd3 for V1/Renshaw differentiation (Lu et al., 2015; Stam et al., 2012, cited in Lu et al.).

### Ia inhibitory interneurons (reciprocal inhibition of antagonist motor neurons)

A second classical V1 subtype is the Ia inhibitory interneuron:

> "Although Ia interneurons have been rediscovered as a V1 subclass, like Renshaw cells, the Ia INs were functionally described before the advent of molecular genetic dissection of interneuron development. These inhibitory glycinergic cells receive input from muscle spindle Ia proprioceptive afferents carrying muscle length information and provide inhibitory input onto motor neurons innervating antagonist muscles. Like motor neurons, Ia receive inhibitory inputs from Renshaw cells. In neonatal mice, disynaptic glycinergic reciprocal inhibition is mediated by Ia interneurons."
>
> — Lu et al. (2015)

In the modern four-clade scheme, Foxp2-V1 interneurons contain the bulk of Ia inhibitory interneurons:

> "the V1 Foxp2 clade has been suggested to contain Ia interneurons (Ia INs) that mediate reciprocal inhibition of flexor motor neurons"
>
> — Chapman et al. (2024)

### Locomotor rhythm and flexor–extensor pattern

At the network level, V1 interneurons regulate the frequency of the locomotor rhythm and shape flexor–extensor burst patterning:

> "V1 interneurons are an inhibitory interneuron population implicated in motor control; they project axons into the ipsilateral side and express the homeodomain transcription factor En1. Genetic ablation or silencing of V1 neurons induces a marked decrease in locomotor frequency. Reciprocally connected Ia interneurons form a minimal inhibitory network required to produce flexor-extensor alternation during locomotion. Flexor-extensor motor activity is encoded by the combinatorial actions of V1 and V2b interneurons."
>
> — Gosgnach et al. (2017)

> "In the mouse spinal cord, V1 interneurons are a heterogeneous population of inhibitory spinal interneurons that have been implicated in regulating the frequency of the locomotor rhythm and in organizing flexor and extensor alternation... Hyperpolarizing V1 neurons resulted in an equalization of the duty cycle in flexor and extensors from an asymmetrical pattern in control recordings in which the extensor bursts were longer than the flexor bursts. We hypothesize that one function of the V1 population is to set the burst durations of muscles to be appropriate to their biomechanical function."
>
> — Falgairolle & O'Donovan (2019)

At CS13–14 the HDCA V1 cells are far from functional integration into a locomotor central pattern generator — motor axons are still extending, and reciprocal/recurrent circuits have not yet formed — but this future role is the principal reason for genetic V1 identification.

## Developmental specification and structure

### p1 progenitor domain — Pax6/Dbx2/Nkx6.2 patterning

V1 interneurons originate from the p1 progenitor domain of the ventral neural tube. The p1 domain shares Pax6 and Dbx2 expression with the more dorsal V0/p0 domain, but is distinguished from V0 by the absence of Dbx1 and the presence of Nkx6.2 (Hori & Hoshino, 2012, quoted above). The Pax6/Shh patterning logic that establishes these ventral progenitor domains was originally defined by:

> "Pax6 controls progenitor cell identity and neuronal fate in response to graded Shh signaling."
>
> — Ericson et al. (1997)

### Postmitotic V1 identity: En1 and downstream targets

Postmitotic V1 neurons switch on Engrailed-1 immediately after exiting the cell cycle, and En1 then controls multiple aspects of V1 connectivity:

> "Embryonic V1-INs express the transcription factor engrailed-1 at the onset of postmitotic differentiation, and this has allowed development of animal models to label V1-lineages throughout development. In neonates, several subclasses of V1-derived INs, including RCs or IaINs, are recognizable according to morphology, connections, and expression of calcium-buffering proteins. Moreover, reciprocal and recurrent inhibition can be functionally demonstrated in late embryos and neonates in mice and humans."
>
> — Benito-Gonzalez & Alvarez (2012)

Saueressig et al. (1999) originally showed that En1, in cooperation with netrin-1, regulates the axonal pathfinding of V1 association interneurons toward motor neurons; Sapir et al. (2004) then showed that En1 is specifically required for the formation of inhibitory synapses between Renshaw cells and motor neurons (rather than for the cell-fate decision itself, which is upstream of En1 and depends on Pax6).

### Clade diversification at the time of neurogenesis

A central conceptual point relevant to the HDCA CS13–14 V1 cluster is that V1 diversity is not a downstream refinement of a single homogeneous embryonic V1 pool — instead clade fate is decided at neurogenesis:

> "the differentiation of early and late V1-INs and their subgroups (RCs within the early group) starts at the time of birth (i.e., there is no homogeneous V1 population in the early embryo that later diversifies). Thus, time of neurogenesis is immediately translated into different V1 phenotypes, ruling out integration into synaptic circuits as a major factor determining V1-IN diversity."
>
> — Benito-Gonzalez & Alvarez (2012)

Thus the HDCA CS13–14 V1 cluster almost certainly contains a mixture of nascent clades (likely dominated by the earliest-born V1 cells — Renshaw-clade and Pou6f2-clade precursors — since at CS13–14 most postmitotic V1 neurons have only just been born). The 7504 cells in this cluster therefore represent an integrated V1 cardinal-class signal in which clade-specific transcription factors (MafA, Foxp2, Pou6f2, Sp8) are either not yet upregulated or are present in too small a fraction of the cells to dominate the cluster signature.

### Connection to other HDCA spinal-neuron clusters

HDCA captures the other three ventral-interneuron cardinal classes as separate refined_celltype clusters (`V0_INTERNEURON`, `V2_INTERNEURON`, `V3_INTERNEURON`) and also `MN` (somatic motor neurons; see the HDCA MN report). The V1 cluster is therefore the ventral inhibitory ipsilateral counterpart of the V2 inhibitory ipsilateral (`V2b`, GATA3+) population, complementary to the V0 commissural and V3 commissural populations:

> "In zebrafish and mice, ipsilateral inhibitory neurons fall into two types: the V1 and V2b inhibitory classes. V1 neurons derive from the p1 progenitor domain, express the transcription factor Engrailed-1 (EN1) and the neurotransmitters GABA and/or glycine, and target ipsilateral motor neurons and other ipsilateral inhibitory neurons"
>
> — Wilson & Sweeney (2023)

## References

- HDCA consortium / Webb et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper)". *preprint (HDCA)*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Saueressig H, Burrill J, Goulding M (1999). "Engrailed-1 and netrin-1 regulate axon pathfinding by association interneurons that project to motor neurons". *Development*. DOI: [10.1242/dev.126.19.4201](https://doi.org/10.1242/dev.126.19.4201)
- Sapir T, Geiman EJ, Wang Z, Velasquez T, Mitsui S, Yoshihara Y, Frank E, Alvarez FJ, Goulding M (2004). "Pax6 and Engrailed 1 Regulate Two Distinct Aspects of Renshaw Cell Development". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.3187-03.2004](https://doi.org/10.1523/JNEUROSCI.3187-03.2004)
- Higashijima S, Masino MA, Mandel G, Fetcho J (2004). "Engrailed-1 Expression Marks a Primitive Class of Inhibitory Spinal Interneuron". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.5342-03.2004](https://doi.org/10.1523/JNEUROSCI.5342-03.2004)
- Hori K, Hoshino M (2012). "GABAergic Neuron Specification in the Spinal Cord, the Cerebellum, and the Cochlear Nucleus". *Neural Plasticity*. DOI: [10.1155/2012/921732](https://doi.org/10.1155/2012/921732)
- Benito-Gonzalez A, Alvarez FJ (2012). "Renshaw cells and Ia inhibitory interneurons are generated at different times from p1 progenitors and differentiate shortly after exiting the cell cycle". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.3630-12.2012](https://doi.org/10.1523/JNEUROSCI.3630-12.2012)
- Francius C, Harris A, Rucchin V, Hendricks TJ, Stam F, Barber M, Kurek D, Grosveld F, Pierani A, Goulding M, Clotman F (2013). "Identification of Multiple Subsets of Ventral Interneurons and Differential Distribution along the Rostrocaudal Axis of the Developing Spinal Cord". *PLoS ONE*. DOI: [10.1371/journal.pone.0070325](https://doi.org/10.1371/journal.pone.0070325)
- Lu DC, Niu T, Alaynick W (2015). "Molecular and cellular development of spinal cord locomotor circuitry". *Frontiers in Molecular Neuroscience*. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Bikoff JB, Gabitto M, Rivard A, Drobac E, Machado TA, Miri A, Brenner-Morton S, Famojure E, Diaz C, Alvarez FJ, Mentis G, Jessell T (2016). "Spinal inhibitory interneuron diversity delineates variant motor microcircuits". *Cell*. DOI: [10.1016/j.cell.2016.01.027](https://doi.org/10.1016/j.cell.2016.01.027)
- Gosgnach S, Bikoff JB, Dougherty KJ, El Manira A, Lanuza G, Zhang Y (2017). "Delineating the Diversity of Spinal Interneurons in Locomotor Circuits". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.1829-17.2017](https://doi.org/10.1523/JNEUROSCI.1829-17.2017)
- Falgairolle M, O'Donovan MJ (2019). "V1 interneurons regulate the pattern and frequency of locomotor-like activity in the neonatal mouse spinal cord". *PLoS Biology*. DOI: [10.1371/journal.pbio.3000447](https://doi.org/10.1371/journal.pbio.3000447)
- Wilson A, Sweeney LB (2023). "Spinal cords: Symphonies of interneurons across species". *Frontiers in Neural Circuits*. DOI: [10.3389/fncir.2023.1146449](https://doi.org/10.3389/fncir.2023.1146449)
- Worthy AE, Anderson JT, Lane AR, Gomez-Perez LJ, Wang A, Griffith RW, Rivard AF, Bikoff JB, Alvarez FJ (2024). "Spinal V1 inhibitory interneuron clades differ in birthdate, projections to motoneurons, and heterogeneity". *eLife*. DOI: [10.7554/eLife.95172](https://doi.org/10.7554/eLife.95172)
- Chapman P, Kulkarni AS, Trevisan AJ, Han K, Hinton JM, Deltuvaite P, Fenno L, Ramakrishnan C, Patton MH, Schwarz LA, Zakharenko SS, Deisseroth K, Bikoff JB (2024). "A brain-wide map of descending inputs onto spinal V1 interneurons". *Neuron*. DOI: [10.1016/j.neuron.2024.11.019](https://doi.org/10.1016/j.neuron.2024.11.019)
- Ericson J, Rashbass P, Schedl A, Brenner-Morton S, Kawakami A, van Heyningen V, Jessell T, Briscoe J (1997). "Pax6 controls progenitor cell identity and neuronal fate in response to graded Shh signaling". *Cell* 90(1):169-180. PMID: 9230312
