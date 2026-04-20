# LYVE1++ Macrophages in Prenatal Human Skin

Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x))
Scope: fetal
Cell Ontology: tissue-resident macrophage ([CL:0000864](https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0000864)) -- broad match; new term requested (see NTR)

## Summary

LYVE1++ macrophages are one of four macrophage subsets (alongside MHCII+, TML, and iron-recycling) identified in prenatal human skin between 7 and 17 post-conception weeks (PCW), annotated using marker genes from a cross-organ developmental immune atlas (Suo et al., 2022). They correspond to the LYVE1 hi interstitial macrophage subset described across multiple tissues including dermis, lung, heart, and adipose tissue (Chakarov et al., 2019). In prenatal skin, these macrophages are characterized by perivascular localization, pro-angiogenic gene programs driving sprouting angiogenesis and blood vessel morphogenesis, and growth factor signaling that supports dermal fibroblast maintenance and scarless wound healing. They are enriched in early gestation and show high self-renewal potential.

## Markers

**Primary markers (from atlas annotation):** LYVE1, SPP1, F13A1

These markers were used to annotate macrophage subsets in prenatal skin based on the classification established by Suo et al. (2022). The LYVE1 hi phenotype corresponds to the Lyve1 hi MHCII lo CX3CR1 lo interstitial macrophage subset identified by Chakarov et al. (2019) across multiple organs. In adult skin, perivascular macrophages of this class are additionally characterized as CCR2-negative, CD206-high, and CD86-high (Sim et al., 2022).

**Functionally relevant expressed genes:** LYVE1++ macrophages in prenatal skin express GAS6, which mediates immunosuppressive interactions with fibroblasts via AXL receptors, and growth factors IGF1 and GRN, which support fibroblast homeostasis. They also express pro-angiogenic chemokines including CXCL8 and CCL8, which interact with endothelial ACKR1 to support angiogenesis and cell migration.

## Location

LYVE1++ macrophages co-localize with endothelial cells in prenatal skin neurovascular microenvironments, specifically in early (ME1) and late (ME5) neurovascular niches identified by Visium spatial transcriptomics deconvolution (Gopee et al., 2024). Multiplex RNAscope and immunofluorescence staining confirmed this spatial relationship:

> "multiplex RNAscope and immunofluorescence staining showed LYVE1 + and TML macrophages in close proximity to endothelial cells" (Gopee et al., 2024)

3D volume rendering further demonstrated close physical contact between LYVE1+ macrophages and CD31+ endothelial vasculature. This spatial relationship is consistent with the broader finding that Lyve1 hi macrophages preferentially localize near blood vessels across tissues (Chakarov et al., 2019; Lim et al., 2018).

## Function

**Angiogenesis.** LYVE1++ macrophages are the principal macrophage subset driving blood vessel morphogenesis in prenatal skin and, together with TML macrophages, promote sprouting angiogenesis:

> "Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages, blood vessel morphogenesis by LYVE1 + macrophages and endothelial cell chemotaxis by iron-recycling macrophages" (Gopee et al., 2024)

Predicted ligand-receptor interactions between macrophages and endothelial cells (CXCL8-ACKR1, CCL8-ACKR1) were consistent with reciprocal communication supporting angiogenesis. The importance of macrophages for vascular development was confirmed experimentally: skin organoids lacking immune cells had markedly reduced endothelial cell heterogeneity and quantity, while addition of iPSC-derived macrophages enhanced vascular network remodeling.

**Fibroblast homeostasis.** LYVE1++ macrophages support dermal fibroblast maintenance through growth factor signaling:

> "Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) suggests that LYVE1 + macrophages play a part in the maintenance of prenatal skin dermal fibroblasts" (Gopee et al., 2024)

**Immunosuppression and tissue repair.** GAS6-AXL signaling between LYVE1++ macrophages and WNT2+ fibroblasts may contribute to the immunosuppressive environment that enables scarless healing in prenatal skin:

> "GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts, and these interactions can induce immunosuppression and tissue repair" (Gopee et al., 2024)

**Vascular homeostasis (broader context).** Beyond prenatal skin, LYVE-1+ perivascular macrophages in adult tissues regulate arterial tone through hyaluronan-mediated control of smooth muscle cell collagen deposition, and their deletion causes ECM abnormalities and impeded blood flow (Lim et al., 2018). Depletion of the Lyve1 hi macrophage subset exacerbates fibrosis in lung and heart models (Chakarov et al., 2019).

## References

1. Gopee N, Winheim E, Olabi B, et al. A prenatal skin atlas reveals immune regulation of human skin morphogenesis. *Nature* 635, 679-689 (2024). DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
2. Suo C, Dann E, Goh I, et al. Mapping the developing human immune system across organs. *Science* 376, eabo0510 (2022). DOI: [10.1126/science.abo0510](https://doi.org/10.1126/science.abo0510)
3. Chakarov S, Lim HY, Tan L, et al. Two distinct interstitial macrophage populations coexist across tissues in specific subtissular niches. *Science* 363, eaau0964 (2019). DOI: [10.1126/science.aau0964](https://doi.org/10.1126/science.aau0964)
4. Lim HY, Lim SY, Tan CK, et al. Hyaluronan Receptor LYVE-1-Expressing Macrophages Maintain Arterial Tone through Hyaluronan-Mediated Regulation of Smooth Muscle Cell Collagen. *Immunity* 49, 326-341 (2018). DOI: [10.1016/j.immuni.2018.06.008](https://doi.org/10.1016/j.immuni.2018.06.008)
5. Buechler MB, Fu W, Turley SJ. Fibroblast-macrophage reciprocal interactions in health, fibrosis, and cancer. *Immunity* 54, 903-915 (2021). DOI: [10.1016/j.immuni.2021.04.021](https://doi.org/10.1016/j.immuni.2021.04.021)
6. Wang Z, Wu Z, Wang H, et al. An immune cell atlas reveals the dynamics of human macrophage specification during prenatal development. *Cell* (2023). DOI: [10.1016/j.cell.2023.08.019](https://doi.org/10.1016/j.cell.2023.08.019)
7. Sim SL, Kumari S, Kaur S, Khosrotehrani K. Macrophages in Skin Wounds: Functions and Therapeutic Potential. *Biomolecules* 12, 1659 (2022). DOI: [10.3390/biom12111659](https://doi.org/10.3390/biom12111659)
