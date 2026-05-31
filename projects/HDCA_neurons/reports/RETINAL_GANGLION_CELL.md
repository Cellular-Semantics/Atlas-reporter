# Retinal Ganglion Cell (RETINAL_GANGLION_CELL)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — Retina — n=2633 cells (broad: AUDIOVISUAL_NEURONAL)
Cell Ontology: [retinal ganglion cell](http://purl.obolibrary.org/obo/CL_0000740) (CL:0000740, exact match)

## Summary

Retinal ganglion cells (RGCs) are the output projection neurons of the retina, residing in the ganglion cell layer (GCL) and conveying visual information via the optic nerve. In the HDCA v2 atlas (Webb et al., 2026), 2,633 cells were annotated as RGCs within the audiovisual neuronal compartment of the fetal retina. RGCs are among the earliest-born retinal neurons and dominate retinal cell composition at the earliest fetal stages sampled: Sridhar et al. (2020) report that at fetal day 59 (FD59), retinal progenitors and RGCs are the two predominant cell types, and:

> "RGCs are more highly represented at FD59; the many yellow dots in Figure 3D show that FD59 cells overlap well with RGCs"

RGC specification depends on the bHLH transcription factor ATOH7 (Math5), and the HDCA paper notes that the embryonic retina is characterised by ATOH7 expression as required for RGC development (Webb et al., 2026; Ghiasvand et al., 2011).

## Annotation provenance

100% of RETINAL_GANGLION_CELL cells in HDCA v2 originate from Sridhar et al. (2020) (DOI: 10.1016/j.celrep.2020.01.007). The HDCA audiovisual system was harmonised using a kNN classifier that propagated Sridhar's published labels onto the integrated atlas, with the Sridhar crosswalk mapping "RGC" labels at 99.5% concordance. Sridhar's original RGC clusters were defined by ATOH7+ T1 transition cells feeding into postmitotic ganglion-cell-layer neurons identified by markers including HUC/D, SNCG, and BRN3 (POU4F1):

> "it is possible to visualize the threelayered structure with BRN3+ RGCs, PAX6+ progenitors, and RCVRN+ PRs"

and

> "occasionally overlap with the ganglion cell marker SNCG"

(Sridhar et al., 2020).

## Markers

HDCA Supplementary Table 16 reports the top differentially expressed genes for the RGC cluster; these are dominated by pan-neuronal cytoskeletal and growth-cone genes together with RGC-enriched markers (HDCA Supp Table 16):

| Gene | logFC | padj |
|------|------|------|
| SNCG | 5.94 | 3.7e-212 |
| RTN1 | 5.86 | 9.6e-283 |
| STMN2 | 5.75 | 1.4e-259 |
| NEFL | 5.73 | 2.8e-193 |
| CRABP1 | 5.57 | 5.3e-213 |
| NRN1 | 5.29 | 4.9e-174 |
| PCSK1N | 5.18 | 1.5e-258 |
| GAP43 | 4.78 | 1.0e-182 |
| SCG5 | 4.72 | 4.9e-187 |
| SNCA | 4.61 | 2.0e-153 |
| NEFM | 4.56 | 4.1e-145 |
| NSG1 | 4.48 | 8.5e-208 |
| TUBB2B | 4.42 | 1.4e-259 |
| TUBB2A | 4.15 | 4.0e-230 |

The HDCA-curated 20-gene RGC signature (HDCA Supp Table 9) is:

> "GAP43,PAX6,SNCG,NEFL,NRN1,STMN2,ISL1,INA,MAPT,PRPH,SNCA,NEFM,SNAP25,OLFM1,RTN1,CRABP1,SCG5,SYT4,TSPAN7,GNG3"

This signature includes the classic RGC-enriched genes SNCG (γ-synuclein), NEFL/NEFM (neurofilaments), GAP43 (axon-growth), STMN2 and ISL1 (Webb et al., 2026).

## Location and function in fetal retina

In the developing human retina, RGCs occupy the ganglion cell layer (GCL) — the innermost retinal layer — and are detectable by HUC/D immunoreactivity in the GCL from the earliest stages assayed by Sridhar et al. (2020):

> "The two predominant cell types in the retina at this stage are retinal progenitors in the neuroblast layer (NBL; SOX2+/PAX6+) and retinal ganglion cells(RGCs;HUC/D+)"

RGC axons form the optic nerve, and human loss of RGCs has severe developmental consequences (Ghiasvand et al., 2011):

> "ATOH7 (Math5), a bHLH transcription factor gene that is required for retinal ganglion cell (RGC) and optic nerve development. In humans, the absence of RGCs stimulates massive neovascular growth of fetal blood vessels in the vitreous and early retinal detachment."

## Developmental specification

RGCs are the earliest-born retinal cell class and emerge from ATOH7-expressing T1 transition cells located in the neuroblast layer, which act as a postmitotic "root" for all retinal lineages at early fetal stages (Sridhar et al., 2020):

> "ATOH7+ T1 cells form a root for all retinal lineages at the early ages of retinal development but are nearly absent from central retina in the older samples"

ATOH7 is expressed transiently in newly postmitotic neurogenic cells of the neuroblast layer and is downregulated upon GCL entry (Sridhar et al., 2020):

> "ATOH7-expressing cells are located in the NBL but not the ganglion cell layer"

The HDCA paper places this in the broader retinal developmental program alongside PRDM13 (amacrine fate; Watanabe et al., 2015), GADD45A (early neurogenic cells), and TRH (cone subtype specification; Eldred et al., 2018):

> "embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone"

By later fetal stages (~FD125), ATOH7+ T1 cells have largely disappeared from central retina and the cellular composition shifts toward later-born types (photoreceptors, bipolar cells, Müller glia), consistent with the established birth-order of vertebrate retinal neurogenesis (Sridhar et al., 2020).

## References

- Webb S et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Sridhar A, Hoshino A, Finkbeiner CR, et al. (2020). Single-Cell Transcriptomic Comparison of Human Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal Cultures. Cell Reports 30:1644-1659.e4. DOI: [10.1016/j.celrep.2020.01.007](https://doi.org/10.1016/j.celrep.2020.01.007)
- Ghiasvand NM et al. (2011). Deletion of a remote enhancer near ATOH7 disrupts retinal neurogenesis, causing NCRNA disease. Nat Neurosci 14. DOI: [10.1038/nn.2776](https://doi.org/10.1038/nn.2776)
- Watanabe S et al. (2015). Prdm13 Regulates Subtype Specification of Retinal Amacrine Interneurons and Modulates Visual Sensitivity. J Neurosci 35. DOI: [10.1523/JNEUROSCI.0089-15.2015](https://doi.org/10.1523/JNEUROSCI.0089-15.2015)
- Eldred KC et al. (2018). Thyroid hormone signaling specifies cone subtypes in human retinal organoids. Science 362. DOI: [10.1126/science.aau6348](https://doi.org/10.1126/science.aau6348)
