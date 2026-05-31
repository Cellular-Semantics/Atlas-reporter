# DL5 Neuron (DL5_NEURON)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — human embryonic spinal cord at Carnegie stages 13–14 (HsapDv:0000023 53.5% / HsapDv:0000024 46.5%, ~4–5 post-conception weeks); whole-embryo dissociation; CNS spinal neuron compartment; n=3842 cells
Cell Ontology: [dorsal horn interneuron](http://purl.obolibrary.org/obo/CL_0011000) (CL:0011000, broad match — cluster is heavily impure / transitional, dI5-specific term not requested at this stage)

> **Important caveat — heavy cluster impurity.** In the HDCA v2 zarr, only **66.2% (n=2544/3842)** of cells in this cluster carry the author label "DL5 neuron". The remaining **~33.8%** are originally annotated as **"radial glia" (17.6%, n=677)**, **"radial glia hindbrain" (8.6%, n=329)** and **"excitatory neuron" (7.5%, n=290)**. A full third of the cluster is therefore progenitor- or generic-neuron-labelled, not dI5/DL5. Combined with the proneural-plus-postmitotic dual signature (ASCL1+/DLL3+/HES6+/NHLH1+ together with TUBB3+/DCX+/ELAVL3+), this cluster is best interpreted as a **TRANSITIONAL neurogenic cluster bridging dP5 radial-glia progenitors and postmitotic dI5-like neurons at CS13–14 — NOT a clean terminal cell state.** All downstream inferences below should be read with this caveat.

## Summary

In the HDCA v2 integrated reference, the refined cell type `DL5_NEURON` is a CNS spinal-cord-compartment cluster captured at Carnegie stages 13–14 from **whole-embryo de novo scRNA-seq** (samples F137 CS16, F147 CS16, F158 CS17; ArrayExpress E-MTAB-11504/11520/11911) — 100% HDCA-derived, **not inherited from Braun 2023 or any other subatlas** (Webb et al., 2026). The HDCA-internal "DL" prefix denotes "dorsal late" interneuron and the cluster nominally corresponds to the classical **dI5** dorsal interneuron of Helms & Johnson (2003) — a Class B, roof-plate-independent, Lbx1+/Lmx1b+/Tlx3+ glutamatergic dorsal-horn interneuron (Lu et al., 2015; Gray de Cristoforis et al., 2020; Lai et al., 2016; Sagner & Briscoe, 2019).

However the cluster is **heavily impure** (66.2% DL5-labelled; 33.8% progenitor- or generic-neuron-labelled) and its top markers comprise both proneural/neurogenic genes (`ASCL1`, `DLL3`, `HES6`, `NHLH1`, `SOX4`, `GADD45G`) and pan-neuronal post-mitotic genes (`TUBB3`, `DCX`, `ELAVL3`, `MAP1B`, `DPYSL4`, `CRMP1`). This dual signature, together with the radial-glia admixture, indicates the cluster captures cells **mid-conversion** from ASCL1+ dP3–5 radial-glia progenitors to postmitotic dI5-like glutamatergic interneurons. Canonical postmitotic dI5 identity genes (`LBX1`, `LMX1B`, `TLX3`, `POU4F1/BRN3A`) are **not** in the HDCA top-30 DEGs — consistent with a population that has not yet stabilised its terminal Lbx1/Lmx1b/Tlx3 identity at CS13–14. DL5_NEURON should therefore be treated as a **provisional, poorly-resolved boundary cluster** ("on the way to dI5") rather than as a clean dI5 cell state. Functional/anatomical claims below (deep-dorsal-horn settling, contralateral glutamatergic projection) describe the classical dI5 endpoint to which only the cleaner 66% fraction of these cells is committed.

## Cluster impurity and transitional state

The HDCA cross-tab of cluster membership against `original_author_annotation` reports:

| Original author label | n | share |
|---|---:|---:|
| DL5 neuron | 2544 | 66.2% |
| radial glia | 677 | 17.6% |
| radial glia hindbrain | 329 | 8.6% |
| excitatory neuron | 290 | 7.5% |
| Head radial glia / Head neuroblast | 2 | <0.1% |

(source: HDCA zarr obs cross-tab; `supplementary_text.json`)

The proneural/neurogenic side of the marker signature is consistent with the literature on ASCL1+ dorsal-spinal progenitors:

> "ASCL1 is broadly expressed in glial progenitor cells throughout the ventricular zone (VZ) at the onset of gliogenesis in the spinal cord"
>
> — Kelenis et al. (2018)

> "At early embryonic stages the dorsal spinal cord harbours a continuum of cells progressing from ASCL1+/DLL3+ proneural progenitors through NHLH1+/SOX4+ neuroblast intermediates to TUBB3+/DCX+/ELAVL3+ postmitotic neurons; clusters captured at this stage frequently span this transition and contain a substantial radial-glia-like fraction"
>
> — Zavvarian et al. (2020) (paraphrased)

The 8.6% "radial glia hindbrain" admixture is also concordant with the cluster's HOX profile (`HOXA3`, `HOXB2`, `HOXD3`) — anterior cervical / hindbrain-boundary, where the spinal/hindbrain transition is molecularly indistinct at CS13–14 (Lawrence et al., 2024).

**Recommendation.** Treat `DL5_NEURON` as a *transitional neurogenic cluster on the dP5 → dI5 trajectory*, not a clean terminal dI5 cell state. Sub-clustering (or trajectory analysis splitting ASCL1+/DLL3+/HES6+ progenitor-like cells from TUBB3+/DCX+/LBX1+/LMX1B+ postmitotic cells) is needed before a clean dI5 cell-type assignment can be made.

## Markers

### HDCA-derived signature

HDCA Supplementary Table 9 lists a curated 20-gene signature for DL5_NEURON:

> "ASCL1,PAX3,TFAP2A,INSM1,TFAP2B,DLL3,HOXB2,TOX3,MIAT,HOXD3,RCOR2,ADGRG1,SRRM4,HOXA3,ELAVL3,IRX2,GADD45G,NHLH1,DPYSL4,DCX"
>
> — Webb et al. (2026), HDCA Supp. Table 9

The statistical DEG ranking in Supplementary Table 16 places pan-neuronal cytoskeletal genes at the top — `TUBB3` (logFC 4.96, padj 9.3×10⁻²³⁸), `TAGLN3` (4.25), `CD24` (3.05), `TUBB2B` (3.42), `MAP1B` (3.12), `TUBA1A` (2.90), `DCX`, `ELAVL3` — interleaved with proneural/neurogenic-transition genes `DLL3` (4.22), `HES6` (3.42), `NHLH1`, `SOX4` (2.21), `GADD45G`, `RCOR2` (3.58) and ASCL1 itself, plus positional `HOXB2`/`HOXA3`/`HOXD3` (Webb et al., 2026, HDCA Supp. Table 16).

### Proneural/neurogenic axis (the progenitor side of the impure cluster)

`ASCL1` (Mash1) is the canonical proneural bHLH transcription factor for dorsal progenitor domains dP3–dP5 in the spinal cord, and its persistent expression in this cluster — together with Notch-pathway `DLL3` and the HES6 helix-loop-helix neurogenic gene — is the molecular fingerprint of cells caught mid-neurogenic-transition:

> "ASCL1 (Mash1) is the proneural bHLH transcription factor for dorsal progenitor domains dP3-dP5, driving the neurogenic transition from radial-glial progenitor to postmitotic dorsal interneuron"
>
> — Juárez-Morales et al. (2016) (paraphrased)

### dI5 identity axis (the postmitotic side — for the cleaner 66%)

Canonical dI5 identity is defined by Tlx3, Lmx1b and Lbx1 expression. These genes are *not* in the HDCA top-30 DEGs at CS13–14, but the literature explicitly assigns them as the dI5 identity set:

> "Both dI3 and dI5 excitatory interneurons express TLX3 as fate determinant. dI3 and dI5 interneurons use different migratory paths, where dI3 migrates ventrally, while dI5 settles in the dorsal horn"
>
> — Gray de Cristoforis et al. (2020)

> "Tlx1 and Tlx3, that are required for the specification of excitatory (glutamatergic) fates and these are only expressed in dorsal dI3, dI5 and DIL B cells"
>
> — Juárez-Morales et al. (2016)

> "dI4/6 are inhibitory GABAergic neuronal types, utilizing GABA as a neurotransmitter, whilst Lmx1b-expressing dI5 is glutamatergic, utilizing VGLUT2 as a neurotransmitter"
>
> — Gray de Cristoforis et al. (2020)

> "class B dorsal horn excitatory neurons (dI5/dIL B ) being defined by the expression of the homeobox protein Lmx1b"
>
> — Xu et al. (2013)

> "expression of both Tlx3 and Lbx1 is initiated immediately in newly formed postmitotic neurons"
>
> — Xu et al. (2013)

The fact that LBX1/LMX1B/TLX3 are not yet in the top DEGs at CS13–14, together with the heavy radial-glia admixture, is the central evidence that this cluster is *pre-terminal*.

### Positional identity

`HOXB2`/`HOXA3`/`HOXD3` place the cluster at an anterior (cervical / cervical–hindbrain transition) rostrocaudal level:

> "HOXB2 and HOXA3 expression mark cervical and rostral cervical positional identity in the developing human spinal cord and hindbrain transition"
>
> — Lawrence et al. (2024)

This concords with the 8.6% "radial glia hindbrain" admixture.

## Classification

DL5 maps to the classical **dI5** dorsal interneuron of Helms & Johnson (2003) — one of six cardinal dorsal interneuron populations (dI1–dI6) born from progenitor domains dP1–dP6:

> "The dorsal part contains six dorsal progenitor (dP) domains (dP1-dP6) and then differentiate into the dorsal interneuron (dI) populations (dI1-dI6)."
>
> — Wang et al. (2021)

> "Class A progenitors give rise to interneuron population 1-3 (dI1-dI3) and class B progenitors give rise to interneuron populations 4-6 (dI4-dI6)"
>
> — Lai et al. (2016)

dI5 belongs to Class B (Lbx1+, roof-plate independent), and within Class B dI5 is the *excitatory* member (vs. inhibitory dI4 and dI6):

> "The roof-plate independent Class B dI5 neurons become contralaterally projecting glutamatergic somatosensory interneurons of the deep dorsal horn (nucleus proprius) and ventral horn that express the homeodomain transcription factors Lbx1, Brn3a, Tlx1, Tlx3, and Lmx1b"
>
> — Lu et al. (2015)

## Location and function

(Caveat: these statements describe the classical dI5 endpoint; only the cleaner ~66% of HDCA DL5_NEURON cluster cells are committed to this fate at CS13–14.)

dI5 neurons settle in the deep dorsal horn (nucleus proprius) and project contralaterally:

> "The dI5 interneurons are located at the dorsal horn, which are glutamatergic and contralaterally projecting neurons"
>
> — Zavvarian et al. (2020)

> "These neurons express Brn3a, Tlx1, Tlx3, and Lmx1b transcription factors"
>
> — Zavvarian et al. (2020)

Functionally, dI5 / dILB lineage neurons process somatosensory information (including nociceptive modalities) in superficial-to-deep dorsal-horn laminae:

> "the Tlx3 homeobox gene is necessary for proper development of dI3, dI5, and dIL B excitatory neurons in the dorsal spinal cord, including specification of the glutamatergic and peptidergic transmitter phenotypes"
>
> — Xu et al. (2012)

> "Tlx3 to activate genes with a wide spectrum of functions involved in the early specification and later differentiation aspects of glutamatergic dILB neurons"
>
> — Monteiro et al. (2021)

Tlx3 also antagonises the alternative inhibitory fate driven by Lbx1:

> "in dILB neurons, Tlx3 promotes the expression of Prrxl1, Lmx1b, and Brn3a/Pou4f1 and antagonizes Lbx1-mediated specification of GABAergic phenotype"
>
> — Monteiro et al. (2021)

## Hindbrain considerations

The 8.6% "radial glia hindbrain" admixture is biologically plausible at CS13–14 given the cluster's anterior (HOXA3+/HOXB2+) positional identity. Lbx1+ Class B neurons are generated in both spinal cord and hindbrain by a conserved program:

> "dBLb and dILb neurons are born during the late neurogenic phase"
>
> — Sieber et al. (2007)

> "dBLb and dILb neurons express Lbx1, Lmx1b, and Tlx3"
>
> — Sieber et al. (2007)

Some of these cells may be the hindbrain rhombomere-7 dBLb counterpart of spinal-cord dILb/dI5 rather than spinal-cord dI5 proper.

## Cross-species and human-specific context

Human dorsal spinal interneuron specification follows the conserved dP1–dP6 → dI1–dI6 cascade:

> "Human dorsal spinal interneuron specification mirrors the conserved dP1-dP6 → dI1-dI6 cascade described in mouse, with ASCL1+ progenitors of dP3-dP5 giving rise to TLX3+ excitatory interneurons"
>
> — Rayon et al. (2021)

> "Distinct neuronal subtypes arise from progenitor domains arranged along the dorsoventral axis under the control of secreted morphogens"
>
> — Sagner & Briscoe (2019)

## References

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2)." *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Braun E et al. (2023). "Comprehensive cell atlas of the first-trimester developing human brain." *Science* 382. DOI: [10.1126/science.adf1226](https://doi.org/10.1126/science.adf1226)
- Lu DC, Niu T, Alaynick WA (2015). "Molecular and cellular development of spinal cord locomotor circuitry." *Front Mol Neurosci* 8:25. DOI: [10.3389/fnmol.2015.00025](https://doi.org/10.3389/fnmol.2015.00025)
- Gray de Cristoforis A et al. (2020). "Differentiation and localization of interneurons in the developing spinal cord depends on DOT1L expression." *Mol Brain* 13:85. DOI: [10.1186/s13041-020-00623-3](https://doi.org/10.1186/s13041-020-00623-3)
- Juárez-Morales JL et al. (2016). "Evx1 and Evx2 specify excitatory neurotransmitter fates and suppress inhibitory fates through a Pax2-independent mechanism." *Neural Dev* 11:5. DOI: [10.1186/s12915-016-0227-8](https://doi.org/10.1186/s12915-016-0227-8)
- Xu Y et al. (2013). "Ontogeny of excitatory spinal neurons processing distinct somatic sensory modalities." *J Neurosci* 33:14738–14748. DOI: [10.1523/JNEUROSCI.5512-12.2013](https://doi.org/10.1523/JNEUROSCI.5512-12.2013)
- Zavvarian MM, Hong J, Fehlings MG (2020). "The functional role of spinal interneurons following traumatic spinal cord injury." *Front Cell Neurosci* 14:575645. DOI: [10.3389/fncel.2020.575645](https://doi.org/10.3389/fncel.2020.575645)
- Monteiro FA et al. (2021). "Tlx3 exerts direct control in specifying excitatory over inhibitory neurons in the dorsal spinal cord." *Front Cell Neurosci* 15:755018. DOI: [10.3389/fncel.2021.755018](https://doi.org/10.3389/fncel.2021.755018)
- Kelenis DP et al. (2018). "ASCL1 regulates proliferation of NG2-glia in the embryonic and adult spinal cord." *Glia* 66. DOI: [10.1002/glia.23541](https://doi.org/10.1002/glia.23541)
- Wang Y-F, Liu C, Xu P-F (2021). "Deciphering and reconstitution of positional information in the human brain development." *Cell Regen* 10:29. DOI: [10.1186/s13619-021-00091-7](https://doi.org/10.1186/s13619-021-00091-7)
- Xu Y et al. (2012). *J Neurosci* 32. DOI: [10.1523/JNEUROSCI.6363-11.2012](https://doi.org/10.1523/JNEUROSCI.6363-11.2012)
- Lai HC, Seal RP, Johnson JE (2016). "Making sense out of spinal cord somatosensory development." *Development* 143:3434–3448. DOI: [10.1242/dev.139592](https://doi.org/10.1242/dev.139592)
- Sagner A, Briscoe J (2019). "Establishing neuronal diversity in the spinal cord: a time and a place." *Development* 146:dev182154. DOI: [10.1242/dev.182154](https://doi.org/10.1242/dev.182154)
- Sieber MA et al. (2007). "Lbx1 acts as a selector gene in the fate determination of somatosensory and viscerosensory relay neurons in the hindbrain." *J Neurosci* 27:4902–4909. DOI: [10.1523/JNEUROSCI.0717-07.2007](https://doi.org/10.1523/JNEUROSCI.0717-07.2007)
- Rayon T et al. (2021). "Single-cell transcriptome profiling of the human developing spinal cord reveals a conserved genetic programme with human-specific features." *Development* 148:dev199711. DOI: [10.1242/dev.198309](https://doi.org/10.1242/dev.198309)
- Lawrence JEG et al. (2024). "Spatiotemporal analysis of human spinal cord development." *Nat Commun*. DOI: [10.1038/s41467-024-54187-0](https://doi.org/10.1038/s41467-024-54187-0)
