# TML (TREM2+ Microglia-Like) Macrophages in Prenatal Human Skin

Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x))
Scope: fetal
Cell Ontology: [CL:4047053](http://purl.obolibrary.org/obo/CL_4047053) "TREM2-positive macrophage" (broad match -- new term request pending for microglia-like TREM2-positive macrophage)

## Summary

TML (TREM2+ Microglia-Like) macrophages are a yolk-sac-derived macrophage subset identified in prenatal human skin (7--17 PCW) by Gopee et al. (2024). They are one of four macrophage subsets in the prenatal skin atlas, alongside LYVE1+, MHCII+, and iron-recycling macrophages, annotated using marker genes from a cross-organ developmental immune atlas (Suo et al., 2022). TML macrophages share a transcriptomic profile with embryonic brain microglia, and logistic regression modelling showed they had the highest correspondence to Mac4 (embryonic brain microglia) among prenatal skin myeloid subsets (Gopee et al., 2024). Their identification in skin expands previous observations of TREM2+ microglia-like macrophages in developing gonads (Garcia-Alonso et al., 2022) and across multiple prenatal organs from yolk-sac origin (Goh et al., 2023; Bian et al., 2020), indicating that these cells have broader morphogenetic functions outside the central nervous system during early gestation.

## Markers

**Defining markers:** TREM2, P2RY12, CX3CR1, OLFML3 -- these markers are shared with brain microglia and microglia-like macrophages from other developing organs (Gopee et al., 2024; Suo et al., 2022).

**Immunomodulatory genes:** CX3CR1 (immune-inhibitory receptor), SYT11 (regulator of IL-6 production; Du et al., 2017), GAS6 (ligand for AXL receptors on fibroblasts).

**Functional genes:** VEGFA, SEMA3C, SEMA3E (angiogenesis and axon guidance ligands).

The atlas used marker genes from Suo et al. (2022) to annotate macrophage subsets. TML macrophages were distinguished from other macrophage subsets by their microglia-like expression profile, which includes co-expression of immunomodulatory genes:

> "Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)" (Gopee et al., 2024)

## Location

TML macrophages were identified in prenatal human skin from 7--17 PCW. Spatial analysis predicted their co-location in specific tissue microenvironments:

- **ME1 (early neurovascular microenvironment):** Co-located with Schwann cells and endothelial cells (Gopee et al., 2024).
- **ME5 (late neurovascular microenvironment):** Co-located with endothelial cells (Gopee et al., 2024).
- **WNT2+ fibroblast niche:** Predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6--8 PCW) (Gopee et al., 2024).

Multiplex RNAscope and immunofluorescence staining confirmed TML macrophages in close proximity to endothelial cells (Gopee et al., 2024). TREM2+ macrophages with microglia-like signatures have also been identified in developing gonads (Garcia-Alonso et al., 2022), yolk sac (Goh et al., 2023), and other prenatal organs (Suo et al., 2022), consistent with a conserved yolk-sac-derived population distributed across developing tissues.

## Function

### Sprouting angiogenesis

> "Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages" (Gopee et al., 2024)

All four macrophage subsets expressed pro-angiogenic gene programs, but TML macrophages were specifically implicated in sprouting angiogenesis. Macrophage-expressed VEGFA was identified as a top upstream ligand regulating endothelial GATA2 expression (Gopee et al., 2024). Consistent with these findings, TREM2+ macrophages promote angiogenesis and tissue regeneration in xenogeneic skin transplantation models (Henn et al., 2021).

### Scarless wound healing and immunomodulation

TML macrophages co-expressed immunomodulatory genes including immune-inhibitory receptors and regulators of IL-6 production. SYT11, a gene that inhibits cytokine secretion in microglia (Du et al., 2017), was expressed by TML macrophages. Since downregulation of inflammation and IL-6 confers anti-fibrogenic properties in fetal wounds (Gopee et al., 2024), TML macrophages are inferred to contribute to the scarless healing phenotype of prenatal skin.

GAS6 expressed by TML macrophages was predicted to interact with AXL receptors on WNT2+ fibroblasts, and these interactions can induce immunosuppression and tissue repair (Gopee et al., 2024). This is consistent with studies showing TREM2-dependent macrophages play a protective role against skin fibrosis, with disease-associated TREM2+ macrophages exhibiting overlapping gene signatures with fetal skin counterparts (Liang et al., 2024). Additionally, macrophage-specific Trem2 promotes anti-inflammatory polarization and wound healing through IL-4/Trem2/MAPK signaling (Zhu et al., 2024).

### Neural development support

> "TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) and expressed genes related to cell migration and neural development" (Gopee et al., 2024)

TML macrophages were predicted to interact with Schwann cells through VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, and SEMA3E-PLXND1 ligand-receptor pairs, contributing to synapse formation and axon guidance (Gopee et al., 2024). These functions mirror those of brain microglia and peripheral nerve-associated macrophages in mouse skin (Kolter et al., 2020). The atlas paper concluded:

> "This is in part contributed to by yolk-sac derived TML macrophages, which suggests that these cells have broader functions outside the central nervous system in early gestation" (Gopee et al., 2024)

## References

- Bian, Z. et al. (2020) Deciphering human macrophage development at single-cell resolution. *Nature*. DOI: [10.1038/s41586-020-2316-7](https://doi.org/10.1038/s41586-020-2316-7)
- Du, C. et al. (2017) Synaptotagmin-11 inhibits cytokine secretion and phagocytosis in microglia. *Glia*. DOI: [10.1002/glia.23186](https://doi.org/10.1002/glia.23186)
- Garcia-Alonso, L. et al. (2022) Single-cell roadmap of human gonadal development. *Nature*. DOI: [10.1038/s41586-022-04918-4](https://doi.org/10.1038/s41586-022-04918-4)
- Goh, I. et al. (2023) Yolk sac cell atlas reveals multiorgan functions during human early development. *Nature*. DOI: [10.1038/s41586-023-06816-9](https://doi.org/10.1038/s41586-023-06816-9)
- Gopee, N. et al. (2024) A prenatal skin atlas reveals immune regulation of human skin morphogenesis. *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Henn, D. et al. (2021) Xenogeneic skin transplantation promotes angiogenesis and tissue regeneration through activated Trem2+ macrophages. *Science Advances*. DOI: [10.1126/sciadv.abi4528](https://doi.org/10.1126/sciadv.abi4528)
- Kolter, J. et al. (2020) Origin and Differentiation of Nerve-Associated Macrophages. *Journal of Immunology*. DOI: [10.4049/jimmunol.1901077](https://doi.org/10.4049/jimmunol.1901077)
- Liang, Y. et al. (2024) Dynamic pathological analysis reveals a protective role against skin fibrosis for TREM2-dependent macrophages. *Theranostics*. DOI: [10.7150/thno.94121](https://doi.org/10.7150/thno.94121)
- Suo, C. et al. (2022) Mapping the developing human immune system across organs. *Science*. DOI: [10.1126/science.abo0510](https://doi.org/10.1126/science.abo0510)
- Zhu, X. et al. (2024) Trem2 acts as a non-classical receptor of interleukin-4 to promote diabetic wound healing. *Clinical and Translational Medicine*. DOI: [10.1002/ctm2.70026](https://doi.org/10.1002/ctm2.70026)
