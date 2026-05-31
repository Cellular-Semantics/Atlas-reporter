# DL6 Neuron (DL6_NEURON)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human fetal spinal cord (CNS_SPINAL_NEURON; dorsal neural tube, class B [roof-plate-independent] lineage; whole-embryo dissociation at CS13–CS14, samples F137/F147/F158; n=1522 cells; 99.9% cluster purity)
Cell Ontology: [dorsal horn interneuron](http://purl.obolibrary.org/obo/CL_0011000) (CL:0011000, broad match — no exact CL term for dI6/DMRT3+; NTR drafted)

## Summary

In the HDCA v2 integrated reference, the cell-type label `DL6_NEURON` resolves to a clean (99.9% purity), human-fetal dorsal-late spinal interneuron population captured at Carnegie stages 13–14 from de novo whole-embryo scRNA-seq of three embryos (F137, F147, F158; n=1522 cells), assigned to broad_celltype `CNS_SPINAL_NEURON` and to the non-informative parent ontology term CL:0000540 (neuron) (Webb et al., 2026). The HDCA-internal `DL` prefix denotes "dorsal late" interneuron and the `DL1–DL6` series follows classical dorsal spinal cord interneuron taxonomy (Helms & Johnson, 2003; Lai et al., 2016; Sagner & Briscoe, 2019). On that mapping `DL6` corresponds to mouse **dI6** — the most ventral of the dorsal-interneuron classes, a class-B (PTF1A-dependent, roof-plate-independent) commissural GABA/glycinergic inhibitory class defined by LBX1+/PAX2+ and, in mouse, by the dI6 subset selector DMRT3 (Lu et al., 2015; Gosgnach et al., 2017; Andersson et al., 2012; Roman et al., 2024). The HDCA Table 9 curated 20-gene signature is consistent with this assignment: it carries the dorsal-class-B inhibitory selectors `PAX2` and `GAD2` together with the commissural-axon midline-crossing cue `SLIT1`, plus pan-neurogenic axonogenesis genes (`DCX, INA, STMN2, NEFL, NEFM, TUBB4A, DNER, KIF5C, L1CAM, ELAVL4, ATP1A3, RAB3A, RTN1, ENO2, GNG3`) and the rostral cervical HOX paralogues `HOXB2/HOXD3` (Webb et al., 2026). Top DEGs in Table 16 are dominated by `LAMP5` (logFC 6.89), `INA`, `TUBB3`, `TUBB4A`, `NEFM`, `NEFL`, `STMN2`, `DCX` and `HOXB2`, with very large effect sizes (Webb et al., 2026). The canonical dI6-subset selector `DMRT3` — the "horse gait" gene whose loss disrupts left–right alternation (Andersson et al., 2012) — is not in the HDCA DL6 top 20 / top 30 lists at CS13–14, which is consistent with DMRT3 being upregulated only after the cells exit the cell cycle (around mouse E11.5) and only in a subset of dI6 neurons (Andersson et al., 2012; Perry et al., 2019). In the mature mouse spinal cord, dI6 interneurons settle in laminae VII/VIII around the central canal, fractionate into at least three subsets (DMRT3+, WT1+, and DMRT3+/WT1+), and contribute to left–right alternation and locomotor coordination (Andersson et al., 2012; Gosgnach, 2023; Perry et al., 2019; Haque & Gosgnach, 2019). At CS13–14, DL6_NEURON is best understood as a recently postmitotic dorsal class-B inhibitory commissural interneuron population at — or just after — the onset of dI6 specification, before postnatal DMRT3+/WT1+ subset resolution. **Curatorial note**: HDCA labels `DL1, DL2, DL3, DL5, DL6` — `DL4` is absent (HDCA did not resolve a distinct DL4 cluster at CS13–14, most likely because the class-B inhibitory dI4/dI6/dILA cells are not yet fully transcriptionally separable at this stage and merge with another DL/DB cluster; see also the HDCA `DB1_NEURON` report).

## Markers

### HDCA curated signature (Supplementary Table 9)

HDCA assigns refined_celltype `DL6_NEURON` to the non-informative parent ontology term CL:0000540 (neuron) and lists a curated 20-gene top signature (Webb et al., 2026):

> "top_gene_signatures": "DCX,PAX2,INA,STMN2,NEFL,TUBB4A,DNER,KIF5C,ELAVL4,ATP1A3,RAB3A,L1CAM,ENO2,HOXB2,SLIT1,GAD2,NEFM,RTN1,GNG3,HOXD3"
>
> — Webb et al. (2026), HDCA Supp. Table 9

This signature decomposes into four programmes. (i) **Dorsal class-B inhibitory selectors**: `PAX2` (the canonical specifier of GABAergic/glycinergic inhibitory fate in dorsal-spinal interneurons of the class-B lineage that gives rise to dI4, dI6 and the late-born dILA cells) and `GAD2` (glutamate decarboxylase 2 / GAD65, the GABA-synthesising enzyme) — together diagnostic of an inhibitory commissural dorsal-interneuron identity (Lu et al., 2015; Roman et al., 2024). (ii) **Commissural axon-guidance**: `SLIT1` (a midline-crossing repulsive guidance cue) and `L1CAM` (adhesion / axon-guidance), `DNER` (Delta/Notch-like EGF-repeat axon-guidance ligand) — consistent with the commissural projection pattern documented for mouse dI6 (Gosgnach et al., 2017; Perry et al., 2019). (iii) **Rostro-caudal positional code**: `HOXB2` and `HOXD3`, marking rostral cervical / upper-thoracic axial levels (Lawrence et al., 2024). (iv) **Pan-neurogenic axonogenesis**: the neurofilament triplet `INA/NEFL/NEFM`, the tubulin `TUBB4A`, the doublecortin `DCX`, the synaptic-vesicle / signalling genes `RAB3A/GNG3`, the kinesin `KIF5C`, the Na/K-ATPase α3 subunit `ATP1A3`, the neuronal enolase `ENO2`, the reticulon `RTN1`, the stathmin `STMN2` and the RNA-binding protein `ELAVL4` — a postmitotic-neuron axonogenesis signature shared with neighbouring postmitotic dorsal and ventral classes at CS13–14.

### Statistical DEGs (Supplementary Table 16)

The top differentially-expressed genes from the integrated atlas reinforce the curated signature, with very large effect sizes:

> "gene": "LAMP5", "score": 37.084232, "logfc": 6.8903775, "pval_adj": 9.63122079037693e-297
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "INA", "score": 36.502045, "logfc": 5.586835, "pval_adj": 9.82509494615732e-288
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "HOXB2", "score": 33.616096, "logfc": 4.717777, "pval_adj": 1.86382263397847e-244
>
> — Webb et al. (2026), HDCA Supp. Table 16

`LAMP5` has the largest log-fold change (6.89) — interestingly, LAMP5 is best known in adult cortex as a marker of a subset of GABAergic interneurons, and is also the top DEG in the sibling HDCA V1 cluster; here it again emerges as a top discriminator of an embryonic inhibitory spinal-interneuron cluster, suggesting a previously underappreciated role for LAMP5 in inhibitory-interneuron differentiation in the developing human spine. The combined `INA/STMN2/TUBB3/DCX/NEFL/NEFM/TUBB4A` block is shared with the other HDCA `DL` and `DB` dorsal-interneuron clusters and reflects general postmitotic-neuron axonogenesis at CS13–14; what distinguishes DL6 from the other dorsal clusters at this stage is the strong enrichment of `PAX2`, `GAD2` and `SLIT1` in the curated signature, the absence of class-A dorsal markers (e.g. `LHX9, BARHL1/2, POU4F1/BRN3A, TLX3`) that mark `DA1/DA2/DA3` (= dI1/dI2/dI3), and the absence of motor-neuron-specific genes (`ISL1, MNX1, ECEL1`) that distinguish the HDCA `MN` cluster.

### Classical dI6 selector transcription factors

The dI6 cardinal class is defined across vertebrates by `LBX1+/PAX2+/LHX1/5+` with two postmitotic subsets defined by `DMRT3` and `WT1`:

> "The roof-plate independent Class B dI6 commissural inhibitory interneurons express Lbx1, Lhx1, Lhx5, and are Pax2 positive, indicating a GABAergic fate. These cells may also use glycine for neurotransmission. Although arising from a dorsal progenitor pool, and not being part of the 'V' interneurons, the dI6 group of interneurons gives rise to more than one subtype and appears to contribute to motor function. These inhibitory neurons are reported in unpublished observations to be commissural and may be involved in right-left alternation. Dmrt3, a novel marker in dl6 interneuron was traced to play a key role in locomotor circuitry and in development of commissural interneurons, and mutation in dmrt3 result in divergent in gait pattern in mice models"
>
> — Lu et al. (2015)

> "In class B progenitors, Ascl1 expression gives way to Lbx1 expression. Further specification can be seen in expression of Pax2 by dI4s, Lhx1/5 by dI5s, and co-expression of Pax2 and Bhlhb5 in dI6s."
>
> — Roman et al. (2024)

> "Group 1 was composed of the cardinal spinal cord neuron types clearly identified by classical marker genes including dI1 (Barhl2), dI2 (Foxd3+Slc17a6), dI3 (Isl1+Otp), dI4 (inhibitory Lbx1+ without Dmrt3), dI5 (Phox2a), dI6 (Dmrt3)"
>
> — Roome et al. (2025)

The HDCA DL6 curated signature carries `PAX2` and `GAD2` prominently, but at CS13–14 `LBX1`, `LHX1/5`, `BHLHE22 (BHLHB5)`, `DMRT3` and `WT1` are not in the top 20 / top 30 lists. This is the expected state because (i) LBX1 is shared across all class-B dorsal interneurons (dI4/dI5/dI6/dILA/dILB) and is therefore not cluster-specific (Zavvarian et al., 2020); (ii) DMRT3 is induced only in postmitotic dI6 cells around mouse E11.5 and only in a fraction of them (Andersson et al., 2012; Kikkawa & Osumi, 2021):

> "Dmrt3 is not expressed in NSPCs but in dI6 neurons, originating from dI6 progenitors at around E11.5 (Andersson et al., 2012). These dI6 neurons have two populations: Dmrt3- and Wt1-expressing interneurons."
>
> — Kikkawa & Osumi (2021)

At human CS13–14 (~5 pcw) the equivalent dorsal-interneuron specification window has only just begun, so cluster-defining LFCs for DMRT3 are not expected — its identity is inferred via the PAX2+/GAD2+/SLIT1+ signature plus the class-B "dorsal late" categorical assignment.

## Location

### CNS spinal cord — dorsal class-B lineage, ventromedial migratory destination

HDCA Supplementary Table 9 assigns `DL6_NEURON` to broad_celltype `CNS_SPINAL_NEURON`, germlayer `ECTODERM` and system `NERVOUS_SYSTEM` (Webb et al., 2026). The cells are absent from Table 17 (the PNS subset), corroborating their CNS spinal-cord identity. dI6 cells originate dorsally but migrate ventromedially to settle around the central canal in laminae VII/VIII:

> "The dI6 interneurons originate from progenitor cells immediately dorsal to the V0 population and migrate to take up a position in the ventromedial spinal cord shortly before birth. To date, no single genetic marker has been identified that exclusively labels the entire dI6 population; however, they express the transcription factor Lbx1, a marker also expressed by other dorsal interneuronal populations. dI6 interneurons have been divided into at least three subsets based on postmitotic transcription factor expression: those that express Dmrt3, those that express WT1, and those that express both Dmrt3 and WT1"
>
> — Gosgnach et al. (2017)

> "At e10.5, dI6 interneurons in control embryos were initially located in a medio-lateral region of the spinal cord. At e11.5 these cells progressively migrated in a medio-ventral direction and intimately intermingled with ventral interneurons characterized by the presence of Lhx1/5 without Lbx1. At e12.5 in control embryos, dI6 interneurons settled in the ventromedial region of the spinal cord."
>
> — Kabayiza et al. (2017)

At CS13–14 the HDCA DL6 cluster is captured at a stage equivalent to early mouse E10.5–E11.5, when dI6 cells have just become postmitotic and are still migrating from a dorsal medio-lateral starting position toward their adult ventromedial destination. No dorsal-horn laminar architecture exists yet.

### Rostro-caudal axis

The HDCA DL6 curated signature contains the HOX paralogues `HOXB2` and `HOXD3`, with `HOXB2` enriched as a top DEG in Table 16 (logFC 4.72; Webb et al., 2026). These mark rostral cervical / upper-thoracic axial levels and are consistent with the whole-embryo CS13–14 sampling. The human-specific spatial context for HOX-coded segmental identity in the developing spine is provided by Lawrence et al. (2024) — a principal HDCA subatlas:

> "Positional coding along the anterior-posterior axis is regulated by HOX genes, whose 3' to 5' expression correlates with location along this axis. In the axial plane of the spinal cord, we find distinct patterns in the ventral and dorsal domains, providing insights into motor pool organisation and loss of collinearity in HOXB genes."
>
> — Lawrence et al. (2024)

## Function

### Commissural inhibitory contribution to the locomotor central pattern generator

dI6 interneurons are inhibitory commissural cells that contribute to the spinal locomotor central pattern generator (CPG), with documented roles in left–right alternation and coordinated limb movement:

> "Locomotion in mammals relies on a central pattern-generating circuitry of spinal interneurons established during development that coordinates limb movement. These networks produce left–right alternation of limbs as well as coordinated activation of flexor and extensor muscles. Here we show that a premature stop codon in the DMRT3 gene has a major effect on the pattern of locomotion in horses. Examination of wild-type and Dmrt3-null mice demonstrates that Dmrt3 is expressed in the dI6 subdivision of spinal cord neurons, takes part in neuronal specification within this subdivision, and is critical for the normal development of a coordinated locomotor network controlling limb movements. Our discovery positions Dmrt3 in a pivotal role for configuring the spinal circuits controlling stride in vertebrates."
>
> — Andersson et al. (2012)

> "In the mouse spinal cord, Dmrt3 defines a subset of inhibitory dI6 interneurons located around the central canal in laminae VII and VIII that are primed to contribute to locomotion. Dmrt3-Cre neurons project both ipsilaterally and contralaterally, ascending or descending the spinal cord or both. During fictive locomotion, these neurons are active at a wide range of frequencies. Dmrt3-Cre neurons have commissural, ascending, and descending fibers, receive diverse synaptic inputs, are glycinergic and synapse onto motor neurons."
>
> — Perry et al. (2019)

### The "horse gait" cells: DMRT3 and gait selection

The Andersson et al. (2012) Nature paper is the key functional citation for the dI6 class: a naturally occurring nonsense mutation in horse `DMRT3` ("Gait-keeper" allele) is permissive for ambling gaits (tölt, pace) used by Icelandic and other gaited horse breeds, and Dmrt3-null mice show defects in left–right alternation:

> "the DMRT3 subset of dI6 cells is primarily situated in lamina VIII of the postnatal spinal cord, and project commissural axons which release the neurotransmitter glycine. Synaptic contacts from this population were observed on motoneurons as well as on premotor neurons in laminae IX (presumably Renshaw cells which belong to the V1 population), as well as cholinergic V0 cells (derived from the V0 V subpopulation) surrounding the central canal. The aforementioned gait abnormalities observed in horses lacking DMRT3 cells are strongly suggestive of a role for these subset of the dI6 population in left-right alternation."
>
> — Gosgnach (2023)

The role is evolutionarily conserved: zebrafish *dmrt3a*-expressing neurons are also rhythmically active during locomotion and provide midcycle inhibition to contralateral motor neurons (Del Pozo et al., 2020; Iglesias González et al., 2022).

### WT1+ subset and partial subset overlap

A partially overlapping `WT1+` subset of dI6 cells is also commissural and inhibitory, and silencing it produces left–right alternation defects:

> "dI6 neurons express the transcription factors WT1 or DMRT3 at postmitotic time points, and settle in lamina VII/VIII of the postnatal spinal cord. The DMRT3 subset of dI6 neurons is an inhibitory population which projects axons to both ipsilateral and contralateral targets. This population has been predicted to play a critical role during locomotion based on data indicating that they are rhythmically active during stepping, as well as defects observed in left-right alternation in their absence. Like the DMRT3-expressing subset of dI6 cells, the WT1+ neurons are inhibitory. WT1-expressing neurons recorded during fictive locomotion were rhythmically-active and silencing this subpopulation produced left-right coordination defects."
>
> — Haque & Gosgnach (2019)

The HDCA DL6 cluster at CS13–14 almost certainly contains a mixture of as-yet-unresolved subset precursors (DMRT3+, WT1+, and double-positive), since DMRT3 and WT1 are only induced postmitotically and have not yet diverged into cluster-defining markers at this stage. The 1522 cells in DL6 therefore represent an integrated dI6 cardinal-class signal in which the inhibitory commissural identity (PAX2/GAD2/SLIT1) is already detectable but subset diversity is not.

### Functional context: not yet integrated at CS13–14

At CS13–14 the HDCA DL6 cells are far from functional integration into a working locomotor CPG. Motor axons are only beginning to extend, motor pools have not yet acquired their adult positions, the dorsal-ventral migration of dI6 cells has only just started (Kabayiza et al., 2017), and the commissural axon decussation across the floor plate is still in progress. The future role of these cells — left–right alternation, glycinergic inhibition of contralateral motor neurons, modulation of gait — is therefore the principal reason for their genetic identification at this stage rather than a functional readout at sampling.

## Developmental specification

### Dorsal class B (PTF1A-dependent, roof-plate-independent) progenitors

dI6 cells originate from the most ventral of the six dorsal progenitor domains (dp6) of the neural tube. The six dorsal classes split into two groups: class A (dI1–dI3, roof-plate-BMP-dependent, ATOH1+/OLIG3+ excitatory) and class B (dI4–dI6, roof-plate-independent, ASCL1+/PTF1A-dependent inhibitory):

> "Class A dorsal progenitors, which are dependent on roof plate signaling for appropriate specification, predominantly express AtOH1 and Olig3. Class B dorsal progenitors rely more on a combination of homeobox and bHLH expression, including Ascl1, Pax7, and Ngn2. Class A progenitors give rise to interneuron population 1-3 (dI1-dI3) and class B progenitors give rise to interneuron populations 4-6 (dI4-dI6). In class B progenitors, Ascl1 expression gives way to Lbx1 expression. Further specification can be seen in expression of Pax2 by dI4s, Lhx1/5 by dI5s, and co-expression of Pax2 and Bhlhb5 in dI6s."
>
> — Roman et al. (2024)

### Postmitotic dI6 identity: LBX1 → PAX2/LHX1/LHX5 → DMRT3 / WT1 subsets

Postmitotic dI6 cells switch on `LBX1` as part of the class-B dorsal cohort, then acquire `PAX2` and `LHX1/5` as inhibitory-class selectors, and finally segregate into `DMRT3+` and `WT1+` subsets:

> "At e12.5 and e14.5, two partially overlapping dI6 subpopulations are characterized by the presence of Dmrt3 or WT1, respectively. control Dmrt3+ dI6 INs were located in the ventro-medial part of the spinal cord. In control embryos at e12.5, the WT1+ dI6 subset was located, similarly to the Dmrt3+ subpopulation, in the ventro-medial part of the spinal cord."
>
> — Masgutova et al. (2019)

> "Dmrt3 is not expressed in NSPCs but in dI6 neurons, originating from dI6 progenitors at around E11.5. These dI6 neurons have two populations: Dmrt3- and Wt1-expressing interneurons. Their Dmrt3 KO mice showed an increased number of Wt1+ neurons, suggesting a fate change in the Dmrt3+ population within a specific subset of dI6 neurons."
>
> — Kikkawa & Osumi (2021)

### Subset diversification: DMRT3, WT1, and double-positive cells

The dI6 cardinal class is not homogeneous; it fractionates into at least three (and possibly more) molecular subsets:

> "One cardinal class, the dI6 interneurons, have been shown to coordinate gaits and speed transitions in horses, mice and zebrafish, demonstrating their pivotal role within the locomotor network. Mutations in Doublesex and mab-3 related transcription factor 3 (Dmrt3), expressed in dI6 neurons, give rise to aberrant locomotor output."
>
> — Iglesias González et al. (2022)

> "The mid-phased dI4 to dl6 interneurons express Lbx1. In Lbx1 knock out animals, there is disrupted sensory transmission and excessive generation of commissural neurons. The dI6 interneurons are located in the ventromedial spinal cord and are subdivided to neurons with either Wt1 or Dmrt3 expression. Wt1 deletion alters forelimb hindlimb coordination in mice. In contrast, Dmrt3 knock out mice exhibit altered stride length and swing time."
>
> — Zavvarian et al. (2020)

At human CS13–14 these subsets are not transcriptionally resolved in HDCA — the DL6 cluster captures the cardinal class as a single, recently postmitotic, ventromedially migrating population dominated by axonogenesis genes plus the PAX2/GAD2/SLIT1 inhibitory-commissural signature.

### Curatorial note: DL4 absence and class-B dorsal-interneuron resolution at CS13–14

HDCA's `DL` series labels DL1, DL2, DL3, DL5 and DL6 but NOT DL4. The most likely interpretation is that at CS13–14 the class-B dorsal inhibitory cells of mouse dI4 are not transcriptionally separable from neighbouring class-B clusters (DL5, DL6, or the DB1 cluster, which already captures a generic PAX2+/TFAP2A+/TFAP2B+/GAD2+ class-B inhibitory population — see the HDCA DB1_NEURON report). Roman et al. (2024) note that class-B specification proceeds Ascl1 → Lbx1 → Pax2/Lhx1-5, and finer-grain dI4-vs-dI6 resolution requires postmitotic markers (`Bhlhb5`, `Dmrt3`, `Wt1`) that have not yet reached cluster-defining LFCs at this very early stage. This is a curatorial absence (an unresolved cluster), not a biological absence of dI4 cells.

### Connection to other HDCA spinal-neuron clusters

HDCA captures the dorsal-interneuron cardinal classes as `DA1/DA2/DA3` (class-A, dI1/dI2/dI3-like excitatory) and `DL1/DL2/DL3/DL5/DL6` (class-A & class-B late-born / dILA-dILB-like and dI6) plus a `DB1_NEURON` generic dorsal-class-B inhibitory cluster. The DL6 cluster is therefore the most ventrally-migrating dorsal class — the human-fetal correlate of the canonical commissural inhibitory locomotor-CPG dI6 (Andersson et al., 2012; Gosgnach et al., 2017). It is complementary to: the dI1/dI2/dI3 alar class-A clusters (DA1/DA2/DA3); the PAX2+/TFAP2A+ generic class-B inhibitory dorsal cluster (DB1, which most likely captures a mixture of dI4/dI6/dILA cells); and the ventral V0/V1/V2/V3 cardinal classes plus motor neurons (`MN`).

## References

- HDCA consortium / Webb et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper)". *preprint (HDCA)*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Helms AW, Johnson JE (2003). "Specification of dorsal spinal cord interneurons". *Current Opinion in Neurobiology*. DOI: [10.1002/cne.10570](https://doi.org/10.1002/cne.10570)
- Lai HC, Seal RP, Johnson JE (2016). "Making sense out of spinal cord somatosensory development". *Development*. DOI: [10.1242/dev.139592](https://doi.org/10.1242/dev.139592)
- Sagner A, Briscoe J (2019). "Establishing neuronal diversity in the spinal cord: a time and a place". *Development*. DOI: [10.1242/dev.182154](https://doi.org/10.1242/dev.182154)
- Andersson LS, Larhammar M, Memic F, Wootz H, Schwochow D, Rubin C-J, Patra K, Arnason T, Wellbring L, Hjalm G, Imsland F, Petersen JL, McCue ME, Mickelson JR, Cothran G, Ahituv N, Roepstorff L, Mikko S, Vallstedt A, Lindgren G, Andersson L, Kullander K (2012). "Mutations in DMRT3 affect locomotion in horses and spinal circuit function in mice". *Nature*. DOI: [10.1038/nature11399](https://doi.org/10.1038/nature11399)
- Lu DC, Niu T, Alaynick WA (2015). "Molecular and cellular development of spinal cord locomotor circuitry". *Frontiers in Molecular Neuroscience*. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Kabayiza KU, Masgutova G, Harris A, Rucchin V, Jacob B, Clotman F (2017). "The Onecut Transcription Factors Regulate Differentiation and Distribution of Dorsal Interneurons during Spinal Cord Development". *Frontiers in Cellular Neuroscience*. DOI: [10.3389/fncel.2017.00157](https://doi.org/10.3389/fncel.2017.00157)
- Gosgnach S, Bikoff JB, Dougherty KJ, El Manira A, Lanuza GM, Zhang Y (2017). "Delineating the Diversity of Spinal Interneurons in Locomotor Circuits". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.1829-17.2017](https://doi.org/10.1523/JNEUROSCI.1829-17.2017)
- Perry S, Larhammar M, Vieillard J, Nagaraja C, Hilscher M, Tafreshiha A, Rofo F, Caixeta F, Kullander K (2019). "Characterization of Dmrt3-Derived Neurons Suggest a Role within Locomotor Circuits". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.0326-18.2018](https://doi.org/10.1523/JNEUROSCI.0326-18.2018)
- Haque F, Gosgnach S (2019). "Mapping Connectivity Amongst Interneuronal Components of the Locomotor CPG". *Frontiers in Neural Circuits*. DOI: [10.3389/fncir.2019.00059](https://doi.org/10.3389/fncir.2019.00059)
- Masgutova G, Harris A, Jacob B, Corcoran LM, Clotman F (2019). "Pou2f2 Regulates the Distribution of Dorsal Interneurons in the Mouse Developing Spinal Cord". *Frontiers in Cellular Neuroscience*. DOI: [10.3389/fncel.2019.00506](https://doi.org/10.3389/fncel.2019.00506)
- Zavvarian M-M, Hong J, Fehlings MG (2020). "The Functional Role of Spinal Interneurons Following Traumatic Spinal Cord Injury". *Frontiers in Cellular Neuroscience*. DOI: [10.3389/fncel.2020.00127](https://doi.org/10.3389/fncel.2020.00127)
- Del Pozo Cano A, Manuel R, Iglesias González AB, Koning HK, Habicher J, Zhang H, Allalou A, Kullander K, Boije H (2020). "Behavioral Characterization of dmrt3a Mutant Zebrafish Reveals Crucial Aspects of Vertebrate Locomotion through Phenotypes Related to Acceleration". *Frontiers in Neuroscience*. DOI: [10.3389/fnins.2020.00427](https://doi.org/10.3389/fnins.2020.00427)
- Kikkawa T, Osumi N (2021). "Multiple Functions of the Dmrt Genes in the Development of the Central Nervous System". *International Journal of Molecular Sciences*. DOI: [10.3390/ijms222313095](https://doi.org/10.3390/ijms222313095)
- Iglesias González AB, Jakobsson JET, Vieillard J, Lagerström MC, Kullander K, Boije H (2022). "Single Cell Transcriptomic Analysis of Spinal Dmrt3 Neurons in Zebrafish and Mouse Identifies Distinct Subtypes and Reveal Novel Subpopulations Within the dI6 Domain". *Frontiers in Cellular Neuroscience*. DOI: [10.3389/fncel.2021.781197](https://doi.org/10.3389/fncel.2021.781197)
- Gosgnach S (2023). "Spinal inhibitory interneurons: regulators of coordination during locomotor activity". *Frontiers in Neural Circuits*. DOI: [10.3389/fncir.2023.1167197](https://doi.org/10.3389/fncir.2023.1167197)
- Lawrence JEG, Roberts K, Tuck E, Li T, Mamanova L, Balogh P, Usher I, Piapi A, Mazin P, Anderson ND, Bolt L, Richardson L, Prigmore E, He X, Barker RA, Flanagan AM, Young MD, Teichmann SA, Bayraktar O, Behjati S (2024). "HOX gene expression in the developing human spine". *Nature Communications*. DOI: [10.1038/s41467-024-54187-0](https://doi.org/10.1038/s41467-024-54187-0)
- Roman A, Huntemer-Silveira A, Waldron MA, Khalid Z, Blake J, Parr AM, Low WC (2024). "Cell Transplantation for Repair of the Spinal Cord and Prospects for Generating Region-Specific Exogenic Neuronal Cells". *Cells*. DOI: [10.3390/cells13030255](https://doi.org/10.3390/cells13030255)
- Roome RB, Yadav A, Flores L, Puarr A, Nardini D, Richardson A, Waclaw RR, Arkell RM, Menon V, Johnson JE, Levine AJ (2025). "Ontogeny of the spinal cord dorsal horn". *preprint (bioRxiv)*. DOI: [10.1101/2024.04.10.588851](https://doi.org/10.1101/2024.04.10.588851)
