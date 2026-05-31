# V3 Interneuron (V3_INTERNEURON)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human fetal spinal cord (neural-tube-derived CNS spinal neuron; whole-embryo dissociation at CS13–CS14, samples F137/F147/F158)
Cell Ontology: [spinal cord ventral column interneuron](http://purl.obolibrary.org/obo/CL_2000023) (CL:2000023, broad match — no exact CL term)

## Summary

In the HDCA v2 integrated reference, the cell-type label `V3_INTERNEURON` resolves to V3 spinal interneurons (spinal cord interneuron, CL:0005000) within the CNS_SPINAL_NEURON broad class, captured from de novo whole-embryo scRNA-seq of three Carnegie-stage 13–14 embryos (F137, F147, F158; n=4537 cells; 57.5% CS13 / 42.5% CS14) (Webb et al., 2026). V3 is the ventral-most cardinal class of spinal interneurons, derived from the Nkx2.2+ p3 progenitor domain and defined postmitotically by the PAS-bHLH transcription factor Sim1; the mature V3 population is glutamatergic, predominantly commissural, and required for stable, balanced locomotor rhythm in rodents (Zhang et al., 2008; Borowska et al., 2013; Lu et al., 2015). The HDCA `V3_INTERNEURON` cluster sits at the very beginning of this lineage: at CS13–14 the cells are immediately postmitotic and dominated by pan-neuronal cytoskeleton (`TUBB3, TUBA1A, TUBB2B, TUBB4A, MAP1B, NEFL, NEFM, INA`), growth-cone (`GAP43, STMN2, DCX, CRMP1, DPYSL4`) and synaptic-vesicle (`SNAP25, RAB3A`) genes, with no V3-specific selector (SIM1, NKX2-2) appearing among the top differential markers — consistent with a single grouping cluster that precedes the resolution of the adult-style V3 dorsal (V3D), ventral (V3V) and central (V3C) subtypes described in mouse (Borowska et al., 2013; Francius et al., 2013; Deska-Gauthier et al., 2020).

## Markers

### HDCA curated signature (Supplementary Table 9)

HDCA assigns refined_celltype `V3_INTERNEURON` to ontology term CL:0005000 (spinal cord interneuron) and lists a curated 20-gene top signature for this population (Webb et al., 2026):

> "top_gene_signatures": "GAP43,DCX,INA,STMN2,NEFL,TUBB4A,BSCL2,ATP1A3,ELAVL4,RTN1,NEFM,ELAVL3,KIF5C,RAB3A,ENO2,DPYSL4,SNAP25,GNG3,STMN4,NRN1"
>
> — Webb et al. (2026), HDCA Supp. Table 9

This signature is dominated by three programmes. (i) **Axonogenesis and growth-cone biology**: `GAP43` (the canonical growth-associated protein of extending axons), `DCX` (doublecortin, microtubule binding in migrating/extending neurons), `STMN2/STMN4` (stathmin-2/-4, axonal microtubule dynamics), `DPYSL4` (CRMP4, axon guidance) and `NRN1` (neuritin, axon growth and synaptogenesis). (ii) **Neuronal cytoskeleton**: the type-IV intermediate filaments `NEFL`, `NEFM` and `INA` (alpha-internexin), the tubulin `TUBB4A`, and the kinesin `KIF5C` (anterograde axonal transport). (iii) **Pan-neuronal / synaptic machinery**: `SNAP25` (presynaptic SNARE), `RAB3A` (synaptic vesicle exocytosis), the neuronal glycolytic enzyme `ENO2`, the Na/K-ATPase α3 subunit `ATP1A3`, and the HuC/HuD-family RNA-binding proteins `ELAVL3/ELAVL4`. The signature therefore reflects a postmitotic, just-born neuron that is actively extending an axon — a state shared with other HDCA CS13–14 spinal-neuron clusters (notably `MN`, with which `V3_INTERNEURON` shares `GAP43`, `STMN2`, `INA`, `NEFL`, `NEFM`, `TUBB4A`, `RTN1`, `DCX`, `ATP1A3`, `BSCL2`, `KIF5C`, `ENO2`, `RAB3A`). The classical V3 selector `SIM1` and the progenitor marker `NKX2-2` do **not** appear in the HDCA Table 9 V3 signature, consistent with literature reports that `Sim1` is transiently expressed in postmitotic V3 neurons (Borowska et al., 2013) and that progenitor `NKX2-2` is downregulated before the neuronal state.

### Statistical DEGs (Supplementary Table 16)

The top differentially-expressed genes from the integrated atlas mirror the curated signature, with very large effect sizes dominated by the neuronal cytoskeleton:

> "gene": "TUBB3", "score": 36.359535, "logfc": 5.6910944, "pval_adj": 3.54672962545404e-285
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "STMN2", "score": 34.875164, "logfc": 5.743495, "pval_adj": 1.68936411029008e-262
>
> — Webb et al. (2026), HDCA Supp. Table 16

> "gene": "GAP43", "score": 31.4594, "logfc": 4.655947, "pval_adj": 3.13771440154231e-214
>
> — Webb et al. (2026), HDCA Supp. Table 16

`TUBB3` (logFC 5.7) leads the DEG ranking, followed by `STMN2`, `GDI1`, `TUBA1A`, `MAP1B`, `TUBB2B`, `INA`, `GPC2`, `CRMP1`, `CD24`, `MLLT11`, `STMN1`, `DCX`, `TUBB4A`, `GNG3`, `NEFM`, `TUBB`, `NEFL`, `GAP43`, `TUBB2A`, `NNAT`, `TAGLN3`, `NREP`, `APLP1`, `DPYSL4`, `RTN1`, `GDAP1L1`, `VAT1`, `NGRN`, `UCHL1`. The combined neurofilament triplet (`NEFL/NEFM/INA`), pan-neuronal tubulins (`TUBB3/TUBA1A/TUBB2A/TUBB2B/TUBB4A`) and growth-cone genes (`GAP43/STMN1/STMN2/DCX/CRMP1/DPYSL4/MLLT11`) is diagnostic of postmitotic newly born neurons; it overlaps strongly with the HDCA `MN` cluster and does not by itself discriminate V3 from other ventral interneuron classes — a known limitation at this early Carnegie-stage window in which lineage selectors are transient and cluster identity rests on the integrated atlas labelling rather than on the marker list alone.

### Canonical V3 markers from the literature

The HDCA marker list reflects the postmitotic state at CS13–14 (when neurofilament and axon-growth genes dominate) rather than the V3 lineage selectors used in the developmental literature. The canonical V3 fate determinants are `Nkx2.2` in the p3 progenitor domain and `Sim1` postmitotically:

> "V3 neurons are marked by the transient expression of the Sim1 transcription factor and arise from the p3 progenitor domain"
>
> — Borowska et al. (2013)

> "V3 INs are defined by the expression of the Sim1 transcription factor and comprise a major group of excitatory commissural neurons in the ventral spinal cord"
>
> — Borowska et al. (2013)

> "They originate from the most ventral progenitor domain, p3, where the transcription factor Nkx2.2 is expressed"
>
> — Borowska et al. (2013)

> "V3 INs characterized by Sim1 and Nkx2.2 expression arise from p3 progenitors defined by Nkx2.2"
>
> — Francius et al. (2013)

These Nkx2.2 → Sim1 logic and glutamatergic-commissural phenotype have been corroborated in a human ESC-derived V3 differentiation system, in which `NKX2-2+` p3 progenitors mature into `SIM1+` postmitotic V3 interneurons:

> "V3 progenitors enriched with this method matured in culture to postmitotic SIM1 + V3-interneurons."
>
> — Berzanskyte et al. (2023)

The glutamatergic and commissural identity is established at the postmitotic stage:

> "The Sim1 + VGluT2 + glutamatergic V3 interneurons send projections predominantly contralaterally and caudally"
>
> — Lu et al. (2015)

> "V3 interneurons, defined by their post-mitotic expression of the transcription factor single-minded homolog 1 (Sim1), are excitatory, and the majority of them project to the contralateral side of the spinal cord"
>
> — Danner et al. (2019)

## Location

### CNS spinal cord (ventral horn, originating just above the floor plate)

HDCA Supplementary Table 9 assigns `V3_INTERNEURON` to broad_celltype `CNS_SPINAL_NEURON`, germlayer `ECTODERM` and system `NERVOUS_SYSTEM`, with `organ = whole_embryo` (Webb et al., 2026). The cells are absent from Table 17 (the PNS subset), corroborating their CNS identity. V3 neurons are born immediately above the floor plate from the most ventral p3 progenitor domain:

> "Between E10 and E11, postmitotic V3 INs that express Sim1 were identified immediately above the floor plate"
>
> — Borowska et al. (2013)

> "These V3 interneurons arise from the ventral-most p3 progenitor domain defined by homeobox transcription factors Nkx2.2 and Nkx2.9 and the PAS-bHLH transcription factor Sim1"
>
> — Lu et al. (2015)

After birth they migrate dorsally and laterally and, in the mature mouse spinal cord, are organised into spatially distinct subgroups (V3D dorsal, V3V ventral, with additional central/V3C populations reported electrophysiologically) that resolve only after the developmental window sampled by HDCA:

> "We identified two V3 subpopulations with distinct intrinsic properties and spatial distribution patterns. Ventral V3 INs, primarily located in lamina VIII, possess a few branching processes and were capable of generating rapid tonic firing spikes. By contrast, dorsal V3 INs exhibited a more complex morphology and relatively slow average spike frequency with strong adaptation, and they also displayed large sag voltages and post-inhibitory rebound potentials."
>
> — Borowska et al. (2013)

> "These cells are broadly distributed along the dorsal-ventral and rostral-caudal axes in the postnatal spinal cord and are found, not only in laminae VII and VIII, where most ventral commissural neurons reside, but also in clusters in laminae IV and V of the deep dorsal horn in the lower thoracic and rostral lumbar segments"
>
> — Gosgnach et al. (2017)

> "These excitatory commissural neurons diversify into V3 D and V3 V according to their location and their respective electrophysiological characteristics"
>
> — Francius et al. (2013)

### Developmental staging in HDCA and complementary human references

In the HDCA reference, the V3 population is sampled at Carnegie stages 13–14 from whole-embryo dissociations (samples F137/F147/F158, n=4537 cells, 57.5% CS13 / 42.5% CS14) (Webb et al., 2026). This is the earliest developmental window of V3 neurogenesis — well before the dorsoventral migration and electrophysiological diversification documented in Borowska et al. (2013) and Francius et al. (2013), and before the early-born / late-born neurogenic waves resolved in mouse:

> "V3 INs were organized into either early-born [embryonic day 9.5 (E9.5) to E10.5] or late-born (E11.5-E12.5) neurogenic waves. Early-born V3 INs displayed both ascending and descending commissural projections and clustered into subgroups across dorsoventral spinal laminae. In contrast, late-born V3 INs became fate-restricted to ventral laminae and displayed mostly descending and local commissural projections and uniform membrane properties."
>
> — Deska-Gauthier et al. (2020)

CS13–14 in humans (HsapDv:0000023 / HsapDv:0000024) is therefore most comparable to mouse E9.5–E10.5, when V3 neurogenesis has just begun and the V3 grouping cluster has not yet resolved into V3D/V3V/V3C subtypes. Complementary human references covering later spinal-cord timepoints — Rayon et al. (2021) at first trimester, and the HDCA-linked human spine spatial reference Lawrence et al. (2024) — show how spinal interneuron diversity sharpens with time:

> "focused on first trimester spinal cord derived from four human embryos, and identified diverse progenitor and neuronal populations, and performed a systematic comparison with the spinal cord cell types of the developing mouse spinal cord"
>
> — Rayon et al. (2021)

> "In the axial plane of the spinal cord, we find distinct patterns in the ventral and dorsal domains, providing insights into motor pool organisation and loss of collinearity in HOXB genes."
>
> — Lawrence et al. (2024)

The Braun et al. (2023) first-trimester human brain atlas covers the hindbrain and rostral cord and provides the principal brain-side reference for HDCA neuronal annotations:

> "The adult human brain is divided into hundreds of spatial domains, each comprising tens or hundreds of distinct neuronal, glial, and other cell types. This complex arrangement of cells is initially established during the first trimester of development"
>
> — Braun et al. (2023)

## Function

### Glutamatergic commissural excitation and locomotor robustness

In the mature mouse spinal cord, V3 interneurons are excitatory commissural neurons that provide mutual excitation between the left and right halves of the cord and are required for a robust, balanced locomotor rhythm rather than for left–right alternation per se:

> "The V3 interneurons are glutamatergic, predominantly commissural, and necessary for locomotion"
>
> — Zavvarian et al. (2020)

> "Genetic deletion of V3 interneurons did not affect left-right alternation, but caused unstable gaits in walking mice, and generated imbalanced and less robust rhythmic fictive locomotion in isolated neonatal spinal cords"
>
> — Danner et al. (2019)

> "Genetic suppression of the activity of the entire V3 population in mice causes animals to exhibit unstable and uncoordinated gaits"
>
> — Borowska et al. (2013)

> "Blocking synaptic transmission or acute suppression of V3 neuron excitability in the isolated mouse spinal cord preparation resulted in incoherent, weak rhythmic activity and asymmetric locomotor outputs on the left and rights sides."
>
> — Gosgnach et al. (2017)

Quantitative connectivity in the postnatal mouse cord places V3 axons onto a large fraction of ventral excitatory synapses on V1 Ia interneurons, Renshaw cells and lateral motor column motor neurons:

> "Sim1 + V3 interneurons form 24% of glutamatergic connections on V1 Ia, 27% on Renshaw subclasses, 22% of glutamatergic synapses on lateral motor column motor neurons, as well as connections on Lhx3 + V2 interneurons, and lamina VIII commissural interneurons"
>
> — Lu et al. (2015)

At CS13–14, axons have only just begun to extend (consistent with the HDCA Table 9 dominance of `GAP43`/`STMN2`/`DCX`/`DPYSL4`); the functional connectivity above is therefore not yet established in HDCA-sampled cells but represents the eventual mature phenotype.

### Axon outgrowth and pathfinding at CS13–14

The dominance of growth-cone (`GAP43`), microtubule (`STMN1`, `STMN2`, `DCX`, `TUBB3`, `TUBB4A`, `MAP1B`, `CRMP1`, `DPYSL4`) and pan-neuronal assembly (`NEFL`, `NEFM`, `INA`, `SNAP25`, `RAB3A`) genes in the HDCA Table 9/16 signatures is consistent with a developmental window in which V3 axons are actively being extended toward the floor plate prior to commissural crossing. Sim1 is essential for the postmitotic phase of this process — for proper migration into V3 subgroups and for guidance of the contralateral axon projection:

> "In Sim1 mutants, V3 INs are produced normally and maintain a similar position and organization as in wild types before E12.5. Further temporal analysis revealed that the V3 INs in the mutants failed to migrate properly to form V3 subgroups along the dorsoventral axis of the spinal cord."
>
> — Blacklaws et al. (2015)

> "loss of Sim1 led to a reduction in extension of contralateral axon projections both at E14.5 and P0 without affecting ipsilateral axon projections"
>
> — Blacklaws et al. (2015)

> "These results demonstrate that Sim1 is essential for proper migration and the guidance of commissural axons of the spinal V3 INs."
>
> — Blacklaws et al. (2015)

## Developmental specification and structure

### Dorsoventral patterning and the p3 progenitor domain

V3 interneurons originate from the ventral-most p3 progenitor domain of the neural tube, specified by the highest, longest-duration Sonic hedgehog (Shh) exposure and defined by the homeodomain transcription factors Nkx2.2/Nkx2.9:

> "These V3 interneurons arise from the ventral-most p3 progenitor domain defined by homeobox transcription factors Nkx2.2 and Nkx2.9 and the PAS-bHLH transcription factor Sim1"
>
> — Lu et al. (2015)

> "induction of nkx2.2, a marker for the ventral V3 precursor domain, requires a higher concentration and a longer duration of Shh signaling compared to olig2, a marker for the more dorsal MN precursor domain"
>
> — Huang et al. (2012)

> "The combinatorial expression of these transcription factors defines distinct progenitor domains along the dorsal-ventral axis that give rise to V0, V1, V2 interneurons, motor neurons (MN), V3 interneurons, and the floor plate"
>
> — Huang et al. (2012)

The p3 progenitor domain sits immediately ventral to the pMN (motor-neuron) domain, and the cross-repressive OLIG2/NKX2.2 boundary is what decides MN vs V3 fate. Loss of Nkx2.2 mis-specifies p3 progenitors as motor neurons, and loss of both Nkx2.2 and Nkx2.9 eliminates V3 entirely:

> "in Nkx2.2 mutants in which the entire p3 domain was transformed into pMN domain and V3 interneurons were mis-specified into motor neurons"
>
> — Liu et al. (2014)

> "Mice that are mutant for Nkx2.2 and Nkx2.9 lose V3 interneurons"
>
> — Lu et al. (2015)

The MN–V3 progenitor boundary is reinforced by Groucho/TLE-mediated transcriptional corepression:

> "TLE overexpression causes increased numbers of p3 progenitors and promotes the V3 interneuron fate while suppressing the motor neuron fate."
>
> — Todd et al. (2012)

> "TLE is important to promote the formation of the p3 domain and subsequent generation of V3 interneurons"
>
> — Todd et al. (2012)

### Postmitotic specification: Sim1 and the commissural / glutamatergic phenotype

Once p3 progenitors exit the cell cycle and downregulate Nkx2.2, they switch on the PAS-bHLH transcription factor Sim1, which is the defining postmitotic marker of V3:

> "The V3 cells are a group of excitatory commissural interneurons that emerge from the most ventral Nkx2.2-expressing progenitor domain of the neural tube and express the transcription factor Sim1 postmitotically"
>
> — Gosgnach et al. (2017)

Sim1 is required not for initial fate specification (V3 neurons are still produced in Sim1 mutants), but for the subsequent dorsoventral migration of V3 subgroups and for the contralateral axon-guidance decision (Blacklaws et al., 2015, quoted above). The Sim1+ V3 cells are uniformly glutamatergic at maturity (`VGluT2+`) and project predominantly contralaterally and caudally (Lu et al., 2015; Danner et al., 2019). Within the HDCA `V3_INTERNEURON` cluster at CS13–14, this Sim1 → migration → commissural-axon programme is just being initiated.

### Subtype diversification and temporal logic

In the mature mouse cord, V3 interneurons split into anatomically and electrophysiologically distinct V3D (dorsal, complex morphology, slow-adapting firing, sag/PIR currents) and V3V (ventral lamina VIII, simple morphology, rapid tonic firing) subtypes, with additional central V3C and deep dorsal-horn populations reported (Borowska et al., 2013, quoted above). Subtype identity is set in part by birth-date, with early-born V3 (E9.5–E10.5 in mouse) clustering across dorsoventral laminae and late-born V3 (E11.5–E12.5) becoming fate-restricted to ventral laminae:

> "V3 INs were organized into either early-born [embryonic day 9.5 (E9.5) to E10.5] or late-born (E11.5-E12.5) neurogenic waves."
>
> — Deska-Gauthier et al. (2020)

> "the postmitotic transcription factor, Sim1, although expressed in all V3 INs, exclusively regulated the dorsal clustering and electrophysiological diversification of early-born, but not late-born, V3 INs"
>
> — Deska-Gauthier et al. (2020)

CS13–14 in humans corresponds roughly to mouse E9.5–E10.5 (early-born wave), so the HDCA `V3_INTERNEURON` cluster is best interpreted as a grouping cluster representing newly postmitotic V3 neurons that precede V3D/V3V/V3C resolution — these subtypes are expected to emerge in later-stage human spinal-cord references (Rayon et al., 2021; Lawrence et al., 2024) rather than within the HDCA CS13–14 sampling window. The HDCA Table 9 V3 signature should therefore be interpreted as the molecular state of the V3 lineage at first commitment, not as a marker of mature V3 subtype identity.

## References

- HDCA consortium / Webb et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development (HDCA atlas paper)". *preprint (HDCA)*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Braun et al. (2023). "Comprehensive cell atlas of the first-trimester developing human brain". *Science*. DOI: [10.1126/science.adf1226](https://doi.org/10.1126/science.adf1226)
- Zhang et al. (2008). "V3 spinal neurons establish a robust and balanced locomotor rhythm during walking". *Neuron*. DOI: [10.1016/j.neuron.2008.08.009](https://doi.org/10.1016/j.neuron.2008.08.009)
- Borowska et al. (2013). "Functional Subpopulations of V3 Interneurons in the Mature Mouse Spinal Cord". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.2005-13.2013](https://doi.org/10.1523/JNEUROSCI.2005-13.2013)
- Blacklaws et al. (2015). "Sim1 is required for the migration and axonal projections of V3 interneurons in the developing mouse spinal cord". *Developmental Neurobiology*. DOI: [10.1002/dneu.22266](https://doi.org/10.1002/dneu.22266)
- Deska-Gauthier et al. (2020). "The Temporal Neurogenesis Patterning of Spinal p3-V3 Interneurons into Divergent Subpopulation Assemblies". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.1518-19.2019](https://doi.org/10.1523/JNEUROSCI.1518-19.2019)
- Danner et al. (2019). "Spinal V3 Interneurons and Left-Right Coordination in Mammalian Locomotion". *Frontiers in Cellular Neuroscience*. DOI: [10.3389/fncel.2019.00516](https://doi.org/10.3389/fncel.2019.00516)
- Lu et al. (2015). "Molecular and cellular development of spinal cord locomotor circuitry". *Frontiers in Molecular Neuroscience*. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Francius et al. (2013). "Identification of Multiple Subsets of Ventral Interneurons and Differential Distribution along the Rostrocaudal Axis of the Developing Spinal Cord". *PLoS ONE*. DOI: [10.1371/journal.pone.0070325](https://doi.org/10.1371/journal.pone.0070325)
- Berzanskyte et al. (2023). "Enrichment of human embryonic stem cell-derived V3 interneurons using an Nkx2-2 gene-specific reporter". *Scientific Reports*. DOI: [10.1038/s41598-023-29132-8](https://doi.org/10.1038/s41598-023-29132-8)
- Gosgnach et al. (2017). "Delineating the Diversity of Spinal Interneurons in Locomotor Circuits". *Journal of Neuroscience*. DOI: [10.1523/JNEUROSCI.1829-17.2017](https://doi.org/10.1523/JNEUROSCI.1829-17.2017)
- Zavvarian et al. (2020). "The Functional Role of Spinal Interneurons Following Traumatic Spinal Cord Injury". *Frontiers in Cellular Neuroscience*. DOI: [10.3389/fncel.2020.00150](https://doi.org/10.3389/fncel.2020.00150)
- Liu et al. (2014). "Olig3 Is Not Involved in the Ventral Patterning of Spinal Cord". *PLoS ONE*. DOI: [10.1371/journal.pone.0089353](https://doi.org/10.1371/journal.pone.0089353)
- Huang et al. (2012). "Attenuation of Notch and Hedgehog Signaling Is Required for Fate Specification in the Spinal Cord". *PLoS Genetics*. DOI: [10.1371/journal.pgen.1002762](https://doi.org/10.1371/journal.pgen.1002762)
- Todd et al. (2012). "Establishment of Motor Neuron-V3 Interneuron Progenitor Domain Boundary in Ventral Spinal Cord Requires Groucho-Mediated Transcriptional Corepression". *PLoS ONE*. DOI: [10.1371/journal.pone.0031176](https://doi.org/10.1371/journal.pone.0031176)
- Rayon et al. (2021). "Single-cell transcriptome profiling of the human developing spinal cord reveals a conserved genetic programme with human-specific features". *Development*. DOI: [10.1242/dev.199711](https://doi.org/10.1242/dev.199711)
- Lawrence et al. (2024). "HOX gene expression in the developing human spine". *Nature Communications*. DOI: [10.1038/s41467-024-54257-3](https://doi.org/10.1038/s41467-024-54257-3)
