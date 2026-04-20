# Regulatory T Cells (Treg) in Prenatal Human Skin

Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x))
Scope: fetal
Cell Ontology: [CD4-positive, CD25-positive, alpha-beta regulatory T cell](http://purl.obolibrary.org/obo/CL_0000792) (CL:0000792, exact match)

## Summary

Regulatory T cells (Tregs) are a FOXP3-expressing CD4+ T cell subset identified in the prenatal human skin atlas by Gopee et al. (2024). In fetal skin spanning 7-17 post-conception weeks (PCW), Tregs are recruited to developing hair follicles via CXCL14 chemotaxis and progressively accumulate during the second trimester. Unlike the predominantly memory phenotype of adult skin Tregs, fetal skin Tregs undergo a dynamic transition from a naive to an effector memory state during gestation, driven by antigen-dependent TCR signalling in the tissue (Dhariwala et al., 2020). These cells are thought to play a critical role in establishing immune tolerance to self-antigens and commensal microbiota during a defined developmental window, while also potentially facilitating hair follicle morphogenesis through immune-epithelial crosstalk.

## Markers

Tregs in prenatal skin are defined by the following markers, confirmed by scRNA-seq and spatial validation in the atlas:

- **FOXP3 (Forkhead box P3)**: The master transcription factor of Treg identity. In the prenatal skin dataset, Tregs have the highest expression of FOXP3 among all T cell populations (Gopee et al., 2024, Supplementary Reviewer Fig. 1.26a). RNAscope validates FOXP3+ cells localising around hair follicles at 15 PCW (Gopee et al., 2024, Fig. 2d). Fetal skin Tregs demonstrate higher expression of Foxp3 than their adult counterparts (Dhariwala et al., 2020).

- **IL2RA (CD25)**: The IL-2 receptor alpha chain, a canonical Treg surface marker. Tregs in the prenatal skin dataset show high IL2RA expression, distinguishing them from conventional T cells (Gopee et al., 2024, Supplementary Reviewer Fig. 1.26a).

- **CTLA4 (Cytotoxic T-Lymphocyte Antigen 4)**: An inhibitory receptor involved in Treg-mediated suppression. Expressed at high levels in prenatal skin Tregs in the scRNA-seq data (Gopee et al., 2024, Supplementary Reviewer Fig. 1.26a), although flow cytometry suggests reduced CTLA-4 protein in fetal versus adult skin Tregs (Dhariwala et al., 2020).

- **PD-1**: Elevated on fetal skin Tregs relative to adult counterparts, potentially marking heightened suppressive function and stability (Dhariwala et al., 2020).

- **CD45RO**: A memory marker that progressively increases on fetal skin Tregs during the second trimester, indicating antigen-driven acquisition of an effector memory phenotype (Dhariwala et al., 2020).

- **Ki-67**: A proliferation marker preferentially expressed by CD45RO+ fetal skin Tregs, indicating active local proliferation, especially among antigen-experienced cells (Dhariwala et al., 2020).

- **CD31**: Expressed at high levels on fetal skin T cells including Tregs, indicating enrichment for recent thymic emigrants (Dhariwala et al., 2020).

- **Nur77**: Elevated in fetal skin Tregs, consistent with antigen-dependent TCR signalling (Dhariwala et al., 2020).

## Location

### Prenatal Skin: Hair Follicle Association

Tregs in prenatal human skin localize preferentially around developing hair follicles. The atlas demonstrates this through RNAscope spatial validation:

> "peri-follicular (top right) and inter-follicular (bottom right) RNAscope images of prenatal skin (representative 15 PCW sample) demonstrating ORS (SLC26A7), matrix (SHH), dermal papilla (NDP) with Tregs (FOXP3) localising around the hair follicle"
>
> -- Gopee et al. (2024), Extended Data Fig. 3f / Fig. 2d

Quantification of FOXP3+ cells confirms preferential localization in peri-follicular versus inter-follicular areas of prenatal skin (Gopee et al., 2024, Supplementary Materials).

This peri-follicular localization is consistent with earlier findings from Dhariwala et al. (2020), who confirmed Tregs in close proximity to hair follicles by immunohistochemistry:

> "Immunohistochemical staining of fetal skin for Foxp3 and CD4 further confirmed the presence of Tregs in close proximity to hair follicles"
>
> -- Dhariwala et al. (2020)

Schuster et al. (2012) provided the earliest evidence that FoxP3+ cells are present in the prenatal dermis:

> "During midgestation, CD3+FoxP3- and CD3+FoxP3+ cells can exclusively be found in the dermis"
>
> -- Schuster et al. (2012)

### Dermal Restriction

During prenatal development, Tregs are confined to the dermal compartment. Unlike adult skin where Tregs can be found in both the epidermis and dermis, fetal skin Tregs are exclusively dermal (Schuster et al., 2012).

### Temporal Dynamics

Tregs progressively accumulate in fetal skin during the second trimester:

> "the average percentage of Foxp3 + regulatory T cells (Tregs) among CD4 + cells increased significantly between 17 and 23 weeks gestation and was higher at this later fetal time point than in adult skin"
>
> -- Dhariwala et al. (2020)

This accumulation is driven by both continued thymic egress (indicated by high CD31 expression) and local proliferation (indicated by Ki-67, especially among CD45RO+ cells) (Dhariwala et al., 2020). Notably, Treg accumulation tracks with hair follicle development in a cephalocaudal pattern: at any given fetal age, Treg percentages are higher in scalp compared to torso skin, reflecting the more advanced hair follicle maturation at cephalic sites (Dhariwala et al., 2020).

### Chemokine-Mediated Recruitment

The atlas identifies CXCL14, expressed by prenatal hair matrix cells, as a candidate chemokine for Treg recruitment:

> "Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells"
>
> -- Gopee et al. (2024)

> "T reg cells are known to localize around the HF in late second trimester (around 21 PCW) and in postnatal skin"
>
> -- Gopee et al. (2024)

In neonatal mice, CCL20 production by hair follicle epithelial cells facilitates skin Treg accumulation via the CCR6 receptor (Knoedler et al., 2023; Sharma and Rudra, 2018). Whether analogous CCL20-CCR6 or CXCL14-dependent mechanisms operate in human fetal skin remains to be fully elucidated, though CCL20 mRNA expression increases in human fetal skin explants upon exposure to cutaneous commensals (Sharma and Rudra, 2018).

## Function

### 1. Immune Tolerance Establishment

The primary proposed function of fetal skin Tregs is the establishment of immune tolerance during a critical developmental window:

> "Treg enrichment in the fetal immune system is thought to be critical for promoting tolerance to self and maternal antigens"
>
> -- Dhariwala et al. (2020)

> "This result highlighted the potential role of T reg cell accumulation and immune protection in the early stages of matrix differentiation"
>
> -- Gopee et al. (2024)

Schuster et al. (2012) found FoxP3+ cells at a frequency comparable to adult skin (~20% of T cells), supporting the concept that tolerance mechanisms are established early:

> "FoxP3 expression was found in 20.0% (SD 6.5%; n = 5) of all T cells (5.9 CD3+ cells cm-1, SD 2.9; n = 5), a frequency comparable to what is found in the adult skin"
>
> -- Schuster et al. (2012)

This tolerance extends into early childhood, as indicated by Treg enrichment in pediatric versus adult tissues and a time-limited window for promoting oral tolerance to food allergens (Dhariwala et al., 2020). The developing human fetus generates both tolerogenic and protective immune responses adapted to the unique requirements of gestation (Rackaityte and Halkias, 2020).

### 2. Hair Follicle Immune Protection

The atlas proposes that Treg accumulation around hair follicles provides immune protection during the early stages of hair matrix differentiation (Gopee et al., 2024). In adult and neonatal mouse skin, Tregs facilitate epithelial stem cell differentiation in hair follicles through Notch signalling via Jagged 1 (Ali et al., 2017):

> "Tregs provide notch ligand Jagged1 to the stem cells. Notch signaling triggers the active phase of hair growth cycle (anagen)"
>
> -- Sharma and Rudra (2018)

Whether this stem cell support function is already active in human fetal skin Tregs has not been directly demonstrated, but the co-localization of Tregs with developing hair follicles is consistent with such a role.

### 3. Commensal Tolerance

In neonatal mice, a wave of highly activated Tregs infiltrates the skin during a defined postnatal window, establishing dominant tolerance to skin commensal microbiota:

> "Scharschmidt et al. have demonstrated that, in murine skin, Tregs accumulate primarily during a defined one-week window of neonatal development"
>
> -- Knoedler et al. (2023)

> "In the skin of both mice and humans, Foxp3 + regulatory T (Treg) cells are present in the dermis, especially surrounding the hair follicles, where skin-resident microorganisms also reside"
>
> -- Park and Lee (2018)

The prenatal Treg accumulation observed in human fetal skin may represent the earliest phase of this commensal tolerance programme, preceding postnatal microbial colonization.

### 4. Contribution to Scarless Healing

Fetal skin is able to heal without scarring before 24 PCW. IL-10, a key anti-inflammatory cytokine produced by Tregs, is present in greater quantities in fetal compared to adult skin:

> "IL-10 is present in greater quantities in fetal skin compared with adult skin, and the fetal regenerative phenotype is dependent on IL-10 signaling"
>
> -- Short et al. (2021)

The downregulated immune milieu of prenatal skin, including the presence of immune-suppressive Tregs, may contribute to the scarless healing capacity characteristic of early fetal skin (Gopee et al., 2024).

## Structure / Morphology

Fetal skin Tregs are phenotypically distinct from their adult counterparts in several respects. They initially enter the skin as recent thymic emigrants (high CD31, CD45RA+) and progressively acquire an effector memory phenotype (CD45RO+) during the second trimester:

> "Tregs in fetal skin largely demonstrate an effector memory Treg phenotype, akin to Tregs in adult skin"
>
> -- Dhariwala et al. (2020)

> "the proportion of CD45RO + Tregs progressively increased during the second trimester"
>
> -- Dhariwala et al. (2020)

Key distinctions from adult skin Tregs include higher Foxp3 expression, elevated PD-1, reduced CTLA-4, and higher CD31 (Dhariwala et al., 2020). Among all fetal skin T cells, Tregs demonstrate the highest Ki-67 levels, particularly among CD45RO+ cells, and the highest Nur77 expression among CD45RA+ cells, suggesting preferential antigen-driven activation and proliferation (Dhariwala et al., 2020).

## References

- Ali N et al. (2017). "Regulatory T Cells in Skin Facilitate Epithelial Stem Cell Differentiation." *Cell*. DOI: [10.1016/j.cell.2017.05.002](https://doi.org/10.1016/j.cell.2017.05.002)
- Dhariwala MO et al. (2020). "Developing Human Skin Contains Lymphocytes Demonstrating a Memory Signature." *Cell Reports Medicine*. DOI: [10.1016/j.xcrm.2020.100132](https://doi.org/10.1016/j.xcrm.2020.100132)
- Gopee NH et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Knoedler S et al. (2023). "Regulatory T cells in skin regeneration and wound healing." *Military Medical Research*. DOI: [10.1186/s40779-023-00484-6](https://doi.org/10.1186/s40779-023-00484-6)
- Lee HT et al. (2017). "A Crucial Role of CXCL14 for Promoting Regulatory T Cells Activation in Stroke." *Theranostics*. DOI: [10.7150/thno.17558](https://doi.org/10.7150/thno.17558)
- Park YJ and Lee HK (2018). "The Role of Skin and Orogenital Microbiota in Protective Immunity and Chronic Immune-Mediated Inflammatory Disease." *Frontiers in Immunology*.
- Rackaityte E and Halkias J (2020). "Mechanisms of Fetal T Cell Tolerance and Immune Regulation." *Frontiers in Immunology*. DOI: [10.3389/fimmu.2020.00588](https://doi.org/10.3389/fimmu.2020.00588)
- Schuster C et al. (2012). "Phenotypic Characterization of Leukocytes in Prenatal Human Dermis." *The Journal of Investigative Dermatology*. DOI: [10.1038/jid.2012.187](https://doi.org/10.1038/jid.2012.187)
- Sharma A and Rudra D (2018). "Emerging Functions of Regulatory T Cells in Tissue Homeostasis." *Frontiers in Immunology*. DOI: [10.3389/fimmu.2018.00585](https://doi.org/10.3389/fimmu.2018.00585)
- Short WD et al. (2021). "The Role of T Lymphocytes in Cutaneous Scarring." *Advances in Wound Care*.
