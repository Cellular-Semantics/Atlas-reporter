# Retinal Transitional Cell T1 (RETINAL_TRANSITIONAL_CELL_T1)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — Retina — n=1633 cells (broad: AUDIOVISUAL_NEURONAL)
Cell Ontology: [retinal progenitor cell](http://purl.obolibrary.org/obo/CL_0002672) (CL:0002672, broad match — no exact CL term; T1 is a Sridhar 2020 transitional state not yet represented in CL)

## Summary

T1 is **not** a generic retinal progenitor: it is a conceptual innovation introduced by Sridhar et al. (2020), defining a postmitotic, ATOH7+/HES6+ bipotent transitional state that sits between SOX2+ retinal progenitors and committed retinal neurons. In Sridhar's analysis, T1 cells acted as a "root" feeding the retinal ganglion cell (RGC) lineage and, via further transitional states, the amacrine/horizontal and photoreceptor/bipolar lineages. The HDCA v2 atlas (Webb et al., 2026) propagates this Sridhar 2020 label by kNN harmonisation onto 1633 fetal retina cells and assigns the broad-match CL:0002672 because no exact CL term yet exists for T1.

The HDCA cluster signature for T1 — SPP1, RORB, RGS16, MAB21L1, CRABP1, MIAT (Webb et al., 2026) — is consistent with the early-neurogenic / RGC-fated character of Sridhar's T1, while supplementary DEGs include the canonical Sridhar T1 marker HES6.

## Annotation provenance

The "T1" label is propagated 100% from Sridhar et al. (2020), the primary definitional source for the T1/T2/T3 transitional-cell concept. In HDCA v2 (Webb et al., 2026), the audiovisual compartment was harmonised by kNN propagation of Sridhar's labels; the crosswalk for "T1" is 100% Sridhar. Sridhar et al. (2020) describe how the cluster was originally named:

> The cells in this cluster do not express high levels of progenitor markers (e.g., SOX2) but are also not yet expressing definitive markers of specific neuronal types (e.g., ONECUT2, NEFL; see also Figure S1). We named the cells in this cluster transition cell population 1 (T1).

Because T1 is a transcriptomically defined transitional state rather than a terminal cell type, the Cell Ontology mapping (CL:0002672, retinal progenitor cell) is flagged as a **broad** match only.

## Markers

The HDCA-derived T1 signature (Webb et al., 2026, Supp Table 9):

> SPP1,RORB,RGS16,MAB21L1,CRABP1,MIAT

HDCA T1 top DEGs (Webb et al., 2026, Supp Table 16) include RORB (logFC=5.72), RGS16 (logFC=5.01), SPP1 (logFC=5.00), MAB21L1 (logFC=4.88), CKB (logFC=4.51), **HES6 (logFC=4.47)**, MIAT (logFC=4.14), CRABP1 (logFC=3.54) and RBP1 (logFC=3.25). HES6 is the canonical Sridhar 2020 T1 marker.

The defining transcriptional features in Sridhar et al. (2020) are ATOH7 co-expressed with HES6, together with DLL3:

> in addition to ATOH7, T1 cells express HES6, whereas PRDM13+ cells express PTF1A and HSPB1, and T3 cells express high levels of FABP7, OTX2, and DLL3

> it is therefore quite interesting that one of the most characteristic genes of the T1 cell population is HES6, which inhibits the function of HES1/5

> T1 and T3 cells also express DLL3, which inhibits Notch in a cell-autonomous manner by targeting it for lysosomal degradation in the late endocytic compartment

ATOH7 is the proneural anchor of the state (Sridhar et al., 2020; Ghiasvand et al., 2011):

> ATOH7 (Math5), a bHLH transcription factor gene that is required for retinal ganglion cell (RGC) and optic nerve development.

The HDCA paper (Webb et al., 2026) independently corroborates ATOH7 as a defining feature of early human fetal retina:

> embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone

## Location and developmental position

Sridhar et al. (2020) place T1 spatially in the neuroblastic layer (NBL) and developmentally between SOX2+ progenitors and differentiating retinal neurons:

> ATOH7-expressing cells are located in the NBL but not the ganglion cell layer (Figure 1C, top right). IF analysis shows that most of the ATOH7+ cells (red) are not positive for VSX2 (blue, white arrows), a progenitor marker, but occasionally overlap with the ganglion cell marker SNCG (green). The T1 population appears to represent an intermediate developmental state.

Pseudotime analyses (Monocle and Slingshot) confirm the intermediate position and the earliest pseudotime among the transitional clusters:

> Figures 2D and 2D[0] show that the transition cell clusters are located between the progenitors and the differentiated neurons in their pseudotime values, with T1 cells having slightly earlier pseudotime values than T2 and T3 cells.

T1 is predominantly an early fetal phenomenon — abundant at FD59 and largely absent from central retina by FD125 (Sridhar et al., 2020):

> the T1 population predominates at FD59, with only a relatively small number of T3 cells. However, by FD125, ATOH7+ cells are not detected in the central retina

## Lineage relationships

In Sridhar's Figure 2F summary, T1 acts as a bipotent/multipotent transitional hub: amacrine cells transit through T1 → T2, while photoreceptors transit through T1 → T3 (Sridhar et al., 2020):

> ACs appear to go through both a T1 and T2 transition state; however, PR cells appear to go through both the T1 and T3 states.

> In our data, ATOH7+ T1 cells form a root for all retinal lineages at the early ages of retinal development but are nearly absent from central retina in the older samples.

Mechanistically, the three transition populations each adopt a different Notch-inhibition "exit strategy" from the progenitor pool — T1 cells using HES6 (and DLL3) to release the HES1/5-mediated progenitor block (Sridhar et al., 2020), consistent with their role as the gateway to RGC and (via T2) amacrine/horizontal fates. PRDM13 itself marks the downstream amacrine arm (Watanabe et al., 2015):

> the Prdm13 transcriptional regulator is specifically expressed in developing and mature amacrine cells in the mouse retina.

## References

- Webb S et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: 10.64898/2026.03.30.714220
- Sridhar A, Hoshino A, Finkbeiner CR, et al. (2020). Single-Cell Transcriptomic Comparison of Human Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal Cultures. Cell Reports 30:1644-1659.e4. DOI: 10.1016/j.celrep.2020.01.007
- Ghiasvand NM et al. (2011). Deletion of a remote enhancer near ATOH7 disrupts retinal neurogenesis, causing NCRNA disease. Nat Neurosci 14. DOI: 10.1038/nn.2776
- Watanabe S et al. (2015). Prdm13 Regulates Subtype Specification of Retinal Amacrine Interneurons and Modulates Visual Sensitivity. J Neurosci 35. DOI: 10.1523/JNEUROSCI.0089-15.2015
- Eldred KC et al. (2018). Thyroid hormone signaling specifies cone subtypes in human retinal organoids. Science 362. DOI: 10.1126/science.aau6348
