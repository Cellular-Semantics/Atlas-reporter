# Photoreceptors (PHOTORECEPTORS)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — Retina — n=7760 cells (broad: AUDIOVISUAL_NEURONAL)
Cell Ontology: [photoreceptor cell](http://purl.obolibrary.org/obo/CL_0000210) (CL:0000210, exact match)

## Summary

The PHOTORECEPTORS cluster in HDCA v2 (Webb et al., 2026) comprises 7,760 fetal retinal cells assigned to the audiovisual neuronal compartment and mapped exactly to the Cell Ontology term photoreceptor cell (CL:0000210). The cluster shows a strong, canonical photoreceptor signature: HDCA differential-expression analysis lists RCVRN, NRL, AIPL1, PDC, GNB3 and ROM1 among the top markers (HDCA Supp Table 16), and the HDCA marker signature for this type is summarised as RCVRN, NRL, GNB3, AIPL1, FABP7 (HDCA Supp Table 9).

Annotation labels were propagated from Sridhar et al. (2020) by HDCA's kNN classifier across the audiovisual system. The Sridhar crosswalk is 97.9% "Photoreceptors" plus 2.0% "Photo/Progen" — i.e. a small minor admixture of photoreceptor-committing progenitors. This is consistent with continued neurogenesis at fetal day 82–125 and is reflected in the presence of T3-transition markers (FABP7, DLL3) within the cluster.

## Annotation provenance

100% of PHOTORECEPTORS cells derive their labels from Sridhar et al. (2020, Cell Reports; DOI: 10.1016/j.celrep.2020.01.007). HDCA harmonised the audiovisual subatlas by training a kNN classifier on Sridhar's annotated fetal retina and projecting labels onto the HDCA manifold. The Sridhar crosswalk is dominated by "Photoreceptors" (97.9%) with a minor 2.0% contribution from "Photo/Progen", a transitional photoreceptor-committing progenitor state — users should treat this cluster as photoreceptor-enriched but containing a small commit-stage tail.

## Markers

HDCA top differentially expressed genes (Supp Table 16) include RCVRN (logFC=11.05), NRL (logFC=8.37), AIPL1 (logFC=8.60), PDC (logFC=8.82), GNB3 (logFC=6.81) and ROM1 (logFC=6.53); FABP7 (logFC=3.93) reflects the T3-transition admixture. The HDCA marker signature for this cluster (Supp Table 9) is:

> "RCVRN,NRL,GNB3,AIPL1,FABP7"

Sridhar et al. (2020) localised these and related markers histologically: OTX2/RCVRN co-expression defines photoreceptors in the outer nuclear layer (ONL):

> "photoreceptors (OTX2/RCVRN in the outer nuclear layer [ONL])"

and at later stages all canonical retinal layers are resolved:

> "PRs (OTX2/RCVRN) in the ONL, BCs (OTX2/ VSX2/RCVRN) in the INL, and HCs and ACs (AP2A/CALB1;"

## Location and function in fetal retina

Photoreceptors occupy the ONL of the developing neural retina and are the light-sensing input to the visual system. In the earliest stages Sridhar et al. (2020) examined (FD59), photoreceptors are sparse and the retina is dominated by progenitors and RGCs:

> "The two predominant cell types in the retina at this stage are retinal progenitors in the neuroblast layer (NBL; SOX2+/PAX6+) and retinal ganglion cells(RGCs;HUC/D+).Smallernumbersofamacrinecellsandhorizontal cells (TFAP2A+ and ONECUT2+, respectively) and some photoreceptors (OTX2+) are also present at this stage."

By FD125 photoreceptors are the dominant population in the central retina (Sridhar et al., 2020), consistent with the high cell count (n=7760) recovered here from pooled fetal stages.

## Developmental specification

Sridhar et al. (2020) identified a T3 transition state, marked by FABP7, OTX2 and DLL3, that lies between retinal progenitors and committed photoreceptors/bipolar cells:

> "T3 cells express FABP7 and are positioned between the progenitors, the BCs, and the PRs"

and the canonical T3 signature is summarised as:

> "T3 cells express high levels of FABP7, OTX2, and DLL3"

The detection of FABP7 among HDCA's top photoreceptor DEGs (Supp Table 16) is consistent with the 2% "Photo/Progen" tail flagged above — i.e. T3-stage commit cells co-clustering with mature photoreceptors. Photoreceptor subtype specification in this developmental window is regulated by thyroid hormone signalling, which Eldred et al. (2018) showed controls the cone temporal switch:

> "S cones are specified first, followed by L/M cones, and thyroid hormone signaling controls this temporal switch."

The HDCA atlas paper (Webb et al., 2026) extends this by noting a possible TRH role in cone subtype specification in vivo:

> "TRH signalling has been reported to specify cone subtypes in human retinal organoids74, and thus we provide further evidence in support of a role for TRH in the retina"

## References

- Webb S et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: 10.64898/2026.03.30.714220
- Sridhar A, Hoshino A, Finkbeiner CR, et al. (2020). Single-Cell Transcriptomic Comparison of Human Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal Cultures. Cell Reports 30:1644-1659.e4. DOI: 10.1016/j.celrep.2020.01.007
- Eldred KC et al. (2018). Thyroid hormone signaling specifies cone subtypes in human retinal organoids. Science 362. DOI: 10.1126/science.aau6348
