# V0 Interneuron (V0_INTERNEURON)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human fetal spinal cord (ventral neural-tube p0 domain derivative; whole-embryo dissociation at CS13–CS14, samples F137/F147/F158)
Cell Ontology: [spinal cord ventral column interneuron](http://purl.obolibrary.org/obo/CL_2000023) (CL:2000023, broad match — no exact CL term for the V0 cardinal class; NTR warranted)

## Summary

In the HDCA v2 integrated reference, the cell-type label `V0_INTERNEURON` resolves to the cardinal V0 class of ventral spinal interneurons within the `CNS_SPINAL_NEURON` broad class, captured from de novo whole-embryo scRNA-seq of three Carnegie-stage 13–14 embryos (F137, F147, F158; n=12,153 cells) (Webb et al., 2026). V0 cells are commissural interneurons derived from the dorsal-most ventral progenitor domain (p0), which is uniquely defined by the homeodomain transcription factor DBX1 (Pierani et al., 2001; Hori & Hoshino, 2012). Postmitotically the class splits into the excitatory V0V subtype (Evx1/2+, glutamatergic) and the inhibitory V0D subtype (Evx1-negative, mostly glycinergic/GABAergic), with a small cholinergic V0C subset (Pitx2+) and a rare V0G subset (Lu et al., 2015; Stachowski & Dougherty, 2021). The V0 class is essential for left–right alternation during locomotion: ablation of Dbx1+ V0 neurons in mouse switches left–right alternation to synchronisation (Lanuza et al., 2004; Grillner & El Manira, 2020). At CS13–14 the HDCA cluster captures a transcriptionally young postmitotic state in which the class-defining selectors DBX1/EVX1 are no longer the dominant discriminators; instead the curated HDCA Table 9 signature (DCX, GAP43, INA, STMN2, NEFL, TUBB4A, RAB3A, NEFM, ELAVL4, CRABP1, HOXB2, GNG3, SNCG, DPYSL4) reflects a generic postmitotic spinal-neuron / axonogenesis programme overlaid with a cervical-rostral HOX positional code (Webb et al., 2026; Lawrence et al., 2024). Because at this stage V0V and V0D subtypes may not yet be transcriptionally separable, the cluster is expected to represent a mixture of all V0 subtypes (Sagner & Briscoe, 2019).

## Markers

### HDCA curated signature (Supplementary Table 9)

HDCA assigns refined_celltype `V0_INTERNEURON` to ontology term CL:0005000 (spinal cord interneuron) and lists a curated 20-gene top signature for this population (Webb et al., 2026):

> "top_gene_signatures: DCX,GAP43,INA,STMN2,NEFL,TUBB4A,RAB3A,ATP1A3,NEFM,KIF5C,RTN1,ELAVL4,RGMB,CRABP1,BSCL2,ENO2,HOXB2,GNG3,SNCG,DPYSL4"
>
> — Webb et al. (2026), HDCA Supp. Table 9

This is essentially a postmitotic-neuron / axonogenesis programme shared with the other cardinal spinal-neuron classes captured at CS13–14: (i) **axonogenesis and growth-cone biology** — `GAP43` (the canonical growth-associated protein of extending axons), `DCX` (doublecortin), `STMN2` (stathmin-2, axonal microtubule dynamics) and `DPYSL4` (CRMP4, growth cone guidance); (ii) **neuronal cytoskeleton** — the neurofilament triplet (`NEFL`, `NEFM`, `INA`/alpha-internexin) and `TUBB4A`; (iii) **presynaptic / vesicle machinery** — `RAB3A`, `BSCL2`, `SNCG`, `GNG3`; (iv) **a single HOX gene, `HOXB2`**, consistent with a rostral cervical/hindbrain-adjacent positional identity at this stage; and (v) **`CRABP1`** (cellular retinoic acid binding protein 1), notable because Dbx-domain neurogenesis in the ventral cord is itself retinoid-driven (Pierani et al., 1999). The HDCA top-signature list does **not** include the class-defining transcription factors DBX1, EVX1 or EVX2, which is consistent with their expression earlier in the p0 lineage (progenitor and immediately-postmitotic windows) rather than as the dominant discriminators of the integrated CS13–14 cluster mean (Pierani et al., 1999; Lu et al., 2015).

### Statistical DEGs (Supplementary Table 16)

The top differentially-expressed genes from the integrated atlas mirror the curated signature, with very large effect sizes:

> "gene": "STMN2", "score": 36.1555, "logfc": 5.9947004, "pval_adj": 2.91120458503037e-282
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "CRABP1", "score": 33.280525, "logfc": 6.1703687, "pval_adj": 1.17558480394696e-239
>
> — Webb et al. (2026), HDCA Supp. Table 16

The leading DEGs (`TUBB3`, `STMN2`, `INA`, `CD24`, `GDI1`, `TUBB2B`, `NEFM`, `NEFL`, `TUBA1A`, `GDAP1L1`, `DCX`, `CRABP1`, `CRMP1`, `TUBB`, `TAGLN3`, `GPC2`, `MAP1B`, `TUBB4A`, `TUBB2A`, `GNG3`) confirm a postmitotic neuron in active axon outgrowth. `CRABP1` (logFC 6.2) is notable for V0 cells given that retinoic acid is the principal Shh-independent inductive cue for the Dbx+ p0 progenitor domain.

### Class-defining transcription factors and subtype markers

The classical molecular ID of the V0 class is established by transcription factors that are not the strongest discriminators at the CS13–14 cluster mean but are diagnostic of class identity (Pierani et al., 2001; Hori & Hoshino, 2012; Stachowski & Dougherty, 2021):

> "The V0 INs are commissural INs defined by the expression of the transcription factor Dbx1"
>
> — Stachowski & Dougherty (2021)

> "They are subdivided into dorsal (V0 D ) and ventral (V0 V ) populations based on the absence and presence of Evx1, respectively. The V0 V neurons are mainly excitatory and the V0 D INs are inhibitory, distinguished by presence of Dbx1 in the absence of Evx1 or the co-expression of Dbx1 and Pax2"
>
> — Stachowski & Dougherty (2021)

> "Progenitor cells of both V0 and V1 share a combinatorial expression of Pax6 and Dbx2"
>
> — Hori & Hoshino (2012)

> "Dbx1 is, however, uniquely expressed in V0 progenitor cells and is considered an essential factor for the specification of V0 interneurons"
>
> — Hori & Hoshino (2012)

V0 cells share LIM-homeodomain factors with V1 inhibitory cells:

> "V0 and V1 classes both express Lhx1 and Lhx5, markers of inhibitory spinal interneurons"
>
> — Lu et al. (2015)

Subtype phenotypes (V0V excitatory / V0D inhibitory) are summarised by Hori & Hoshino:

> "A majority of V0 interneurons derived from the ventral half of the p0 domain (described as V0 D interneurons) express vesicular inhibitory amino acid transporter (VIAAT) and represent both GABAergic and glycinergic neurons whereas one-third of V0 interneurons derived from the dorsal p0 progenitor domain (V0 V interneurons) show an excitatory neuronal phenotype that expresses VGLUT2"
>
> — Hori & Hoshino (2012)

Four V0 subclasses are described in the literature:

> "Four V0 interneuron subclasses have been described to date: V0 V , V0 D , V0 C , and V0 G"
>
> — Lu et al. (2015)

A small cholinergic V0 subset adds further heterogeneity:

> "a small population of cholinergic V0 cells (V0 C interneurons) originate from the Evx1-expressing V0 neurons, make monosynaptic contact onto ipsilateral motoneurons, and are presumed to modulate their firing frequency (Zagoraiou et al., 2009)"
>
> — Gosgnach et al. (2017)

At CS13–14 it is unlikely that V0V/V0D/V0C subtypes are transcriptionally fully resolved in human cord; the HDCA `V0_INTERNEURON` cluster therefore most plausibly represents a mixture of all V0 subtypes.

## Location

### CNS spinal cord (ventral horn, p0 derivative, lamina VIII)

HDCA Supplementary Table 9 assigns `V0_INTERNEURON` to broad_celltype `CNS_SPINAL_NEURON`, germlayer `ECTODERM` and system `NERVOUS_SYSTEM` (Webb et al., 2026). The cluster is absent from Table 17 (the PNS subset), corroborating its CNS identity. Developmentally V0 cells originate from the dorsal-most ventral progenitor domain (p0) of the neural tube:

> "The V0 class appears from a Pax6 + , Dbx1/2 + , Pax3/7 - domain that is the dorsal-most ventral progenitor domain"
>
> — Lu et al. (2015)

In mature spinal cord, V0 cell bodies localise to lamina VIII and project commissural axons:

> "Local projecting V0 neurons are a population of primarily contralateral, with some ipsilateral projecting neurons with inhibitory or excitatory identity that send axons 2-4 spinal segments rostrally"
>
> — Lu et al. (2015)

The same projection topology is observed across vertebrates:

> "ventral commissural interneurons, termed V0 neurons, derive from the p0 progenitor domain and are characterized by expression of the transcription factor DBX1, which is required for their development and commissural connectivity"
>
> — Wilson & Sweeney (2023)

> "they extend axons rostrally for two to four spinal cord segments, and either mono- or poly-synaptically synapse onto motor neurons, suggesting that they are important for diagonal coordination"
>
> — Wilson & Sweeney (2023)

### Developmental staging in HDCA and complementary human references

In the HDCA reference, the V0 population is sampled at Carnegie stages 13–14 (HsapDv:0000023 64.2%, HsapDv:0000024 35.8%) from whole-embryo dissociations (samples F137/F147/F158, n=12,153 cells), well before subtype consolidation is morphologically complete. Mouse work places the bulk of V0 neurogenesis between mid-organogenesis stages:

> "In mouse, the majority of Dbx1 + progenitors appear between E10 and E13 and give rise to V0 D and V0 V commissural interneurons"
>
> — Lu et al. (2015)

CS13–14 in human corresponds to the early end of this neurogenic window. Complementary human references at later spinal-cord timepoints — Andersen et al. (2021) at midgestation, and the spatial-transcriptomic spine atlas by Lawrence et al. (2024) — provide the trajectory along which V0 subtype identity may sharpen:

> "We profiled the midgestation human spinal cord with single cell-resolution and discovered, even at this fetal stage, remarkable heterogeneity across and within cell types"
>
> — Andersen et al. (2021)

> "In the axial plane of the spinal cord, we find distinct patterns in the ventral and dorsal domains, providing insights into motor pool organisation and loss of collinearity in HOXB genes."
>
> — Lawrence et al. (2024)

The Lawrence atlas provides the human spatial reference that anchors HDCA ventral interneuron classes (V0–V3) along the rostro-caudal axis. The presence of `HOXB2` in the HDCA Table 9 V0 signature is consistent with a rostral cervical-to-hindbrain positional bias at CS13–14. The first-trimester human brain atlas (Braun et al., 2023) provides the principal brain-side reference for HDCA neuronal annotations.

V0 cells along the rostrocaudal axis have stable overall proportions but molecularly distinguishable subsets:

> "V0 V and V0 D proportion did not significantly change along the rostrocaudal axis of the spinal cord, and each V0 subpopulation can be divided into several subsets according to a combinatorial code that includes Pax2, Prdm8, Pax6, Nurr1 or Onecut factors"
>
> — Francius et al. (2013)

## Function

### Left–right alternation in locomotor central pattern generators

The principal documented function of V0 commissural interneurons is to mediate left–right alternation during locomotion. Selective ablation of the V0 class (Dbx1 knockout) abolishes alternation:

> "mice lacking Dbx1 interneurons displayed aberrant locomotor activity, with contralateral motoneuronal populations drifting in and out of phase with one another (Lanuza et al., 2004), indicating that the two sides were operating independently"
>
> — Gosgnach et al. (2017)

> "in mice, genetic deletion of the transcription factor Dbx1 or DTA-induced ablation of Dbx1-expressing V0 interneurons switched the left-right alternation into synchronization"
>
> — Grillner & El Manira (2020)

Subtype-selective ablations have established a frequency-dependent division of labour between V0V and V0D:

> "The inhibitory V0d interneurons are responsible for coordination at slow but not at high speeds, while the excitatory V0v interneurons appear to be predominantly involved at higher but not at lower speeds"
>
> — Grillner & El Manira (2020)

> "The V0 INs are essential for left-right alternation during locomotion"
>
> — Stachowski & Dougherty (2021)

Conservation across vertebrates underscores the importance of this circuit motif:

> "V0 interneurons represent a major class of commissural interneurons, which is evolutionarily conserved from zebrafish to mice"
>
> — Grillner & El Manira (2020)

### Axon outgrowth at CS13–14

The dominance of growth-cone (`GAP43`), microtubule (`STMN2`, `DCX`, `TUBB3`, `TUBB4A`, `MAP1B`), neurofilament (`NEFL`, `NEFM`, `INA`) and presynaptic (`RAB3A`) genes in the HDCA Table 9 and Table 16 lists is consistent with a developmental window in which V0 commissural axons are actively crossing the midline and extending rostrally 2–4 segments toward their contralateral motor-pool targets (Webb et al., 2026; Lu et al., 2015).

## Developmental specification and structure

### Dorsoventral patterning: the p0 progenitor domain

V0 interneurons originate from the p0 (progenitor-zero) domain of the ventral neural tube — the dorsal-most of the five ventral progenitor domains (p0, p1, p2, pMN, p3) (Pierani et al., 2001; Hori & Hoshino, 2012; Lu et al., 2015). The p0 domain is uniquely defined by DBX1, with co-expression of DBX2 and PAX6 (but absence of NKX6.2 and PAX3/7) (Hori & Hoshino, 2012):

> "Dbx1 is, however, uniquely expressed in V0 progenitor cells and is considered an essential factor for the specification of V0 interneurons"
>
> — Hori & Hoshino (2012)

Loss of Dbx1 respecifies V0 progenitors into the neighbouring identities, demonstrating its switch function:

> "In mice lacking Dbx1, V0 interneurons are lost, and concomitantly V0 D and V0 V interneurons are respecified into Lbx1-positive dI6 dorsal interneurons and En1-positive V1 interneurons, respectively"
>
> — Hori & Hoshino (2012)

A distinctive feature of p0 induction is that it operates through a parallel Shh-independent, retinoid-activated pathway (Pierani et al., 1999):

> "Sonic hedgehog (Shh) is thought to control the generation of motor neurons and interneurons in the ventral CNS. We show here that a Shh-independent pathway of interneuron generation also operates in the ventral spinal cord."
>
> — Pierani et al. (1999)

> "Shh signaling is sufficient to induce Dbx cells and V0 and V1 neurons but is not required for their generation in vitro or in vivo. Retinoids appear to mediate this parallel pathway."
>
> — Pierani et al. (1999)

This retinoid-mediated induction provides a biological rationale for the prominence of `CRABP1` (cellular retinoic acid binding protein 1) in the HDCA V0 DEG list at CS13–14.

### Postmitotic V0V / V0D subtype split

Once p0 progenitors exit the cell cycle, the V0 class subdivides into V0V (dorsal-p0–derived, Evx1/2+, glutamatergic) and V0D (ventral-p0–derived, Evx1-negative, glycinergic/GABAergic) (Pierani et al., 2001; Lanuza et al., 2004; Lu et al., 2015):

> "the V0 population could be divided into a ventral subpopulation (V0 V cells) that express the transcription factor Evx1 and a dorsal subpopulation (V0 D cells) that do not express Evx1 but are derived from Pax7-expressing cells"
>
> — Lanuza et al. (2004)

> "Unlike the V0 V subclass, the more dorsal Dbx1 + progenitors of the glycinergic/GABAergic V0 D class do not express Evx1"
>
> — Lu et al. (2015)

At CS13–14 the HDCA cluster is dominated by the generic postmitotic axonogenesis programme and the V0V/V0D split is unlikely to be transcriptionally fully resolved; subtype-discriminating markers are expected to emerge at later human stages, similar to the diversification observed by Andersen et al. (2021) at midgestation.

### Rostrocaudal positional code

The HDCA Table 9 V0 signature includes the single HOX gene `HOXB2`, consistent with a rostral cervical/hindbrain-adjacent positional bias for at least a fraction of the captured cells. In the developing human spine, Lawrence et al. (2024) showed by spatial transcriptomics and in-situ sequencing that ventral and dorsal domains carry distinct HOX patterns with loss of HOXB collinearity, providing the human spatial framework against which HDCA's whole-embryo V0 cluster can be situated.

## References

- HDCA consortium / Webb et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper)". *preprint (HDCA)*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Braun et al. (2023). "Comprehensive cell atlas of the first-trimester developing human brain". *Science*. DOI: [10.1126/science.adf1226](https://doi.org/10.1126/science.adf1226)
- Lawrence et al. (2024). "HOX gene expression in the developing human spine". *Nature Communications*. DOI: [10.1038/s41467-024-54257-3](https://doi.org/10.1038/s41467-024-54257-3)
- Pierani et al. (1999). "A sonic hedgehog-independent, retinoid-activated pathway of neurogenesis in the ventral spinal cord". *Cell*.
- Pierani et al. (2001). "Control of interneuron fate in the developing spinal cord by the progenitor homeodomain protein Dbx1". *Neuron*.
- Lanuza et al. (2004). "Genetic identification of spinal interneurons that coordinate left-right locomotor activity necessary for walking movements". *Neuron*. DOI: [10.1016/j.neuron.2004.10.009](https://doi.org/10.1016/j.neuron.2004.10.009)
- Hori & Hoshino (2012). "GABAergic Neuron Specification in the Spinal Cord, the Cerebellum, and the Cochlear Nucleus". *Neural Plasticity*. DOI: [10.1155/2012/921732](https://doi.org/10.1155/2012/921732)
- Francius et al. (2013). "Identification of Multiple Subsets of Ventral Interneurons and Differential Distribution along the Rostrocaudal Axis of the Developing Spinal Cord". *PLoS ONE*. DOI: [10.1371/journal.pone.0070325](https://doi.org/10.1371/journal.pone.0070325)
- Lu et al. (2015). "Molecular and cellular development of spinal cord locomotor circuitry". *Frontiers in Molecular Neuroscience*. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Gosgnach et al. (2017). "Delineating the Diversity of Spinal Interneurons in Locomotor Circuits". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.1829-17.2017](https://doi.org/10.1523/JNEUROSCI.1829-17.2017)
- Sagner & Briscoe (2019). "Establishing neuronal diversity in the spinal cord: a time and a place". *Development*. DOI: [10.1242/dev.182154](https://doi.org/10.1242/dev.182154)
- Grillner & El Manira (2020). "Current Principles of Motor Control, with Special Reference to Vertebrate Locomotion". *Physiological Reviews*. DOI: [10.1152/physrev.00015.2019](https://doi.org/10.1152/physrev.00015.2019)
- Andersen et al. (2021). "Landscape of human spinal cord cell type diversity at midgestation". *bioRxiv*. DOI: [10.1101/2021.12.29.473693](https://doi.org/10.1101/2021.12.29.473693)
- Rayon et al. (2021). "Single-cell transcriptome profiling of the human developing spinal cord reveals a conserved genetic programme with human-specific features". *Development*. DOI: [10.1242/dev.199711](https://doi.org/10.1242/dev.199711)
- Stachowski & Dougherty (2021). "Spinal Inhibitory Interneurons: Gatekeepers of Sensorimotor Pathways". *International Journal of Molecular Sciences*. DOI: [10.3390/ijms22052667](https://doi.org/10.3390/ijms22052667)
- Wilson & Sweeney (2023). "Spinal cords: Symphonies of interneurons across species". *Frontiers in Neural Circuits*. DOI: [10.3389/fncir.2023.1146449](https://doi.org/10.3389/fncir.2023.1146449)
