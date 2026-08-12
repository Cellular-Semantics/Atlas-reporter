# Adventitial Fibroblasts PI16-high in the Human Female Reproductive Tract

Atlas: An integrated multimodal pan-organ atlas of the female reproductive system across the lifespan contextualises gynaecological pathologies (DOI: 10.64898/2026.06.10.731198)
Scope: adult (postnatal)
Tissue context: female reproductive tract, predominantly fallopian tube (ampulla and isthmus); also ovary, uterus and vagina
Cell Ontology: [adventitial fibroblast](http://purl.obolibrary.org/obo/CL_4052030) (CL:4052030, broad match — no exact CL term). New term requested: **PI16-high adventitial fibroblast** (is_a CL:4052030) — draft NTR at `traversal_output/adventitial_fibroblast_PI16hi/cl_term_request_T1_PI16hi.json`. A companion term for the sibling immune-niche pole (**CXCL12-positive adventitial fibroblast**, `…_T2_CXCL12_COL15A1.json`) is also drafted. Mapping: `…/cl_mapping.json`.

## Summary

Adventitial fibroblasts PI16-high (`Mesen_AdvFibs_PI16hi`; also "PI16-high adventitial fibroblast", "PI16+ universal fibroblast") are a rare, conserved mesenchymal state (n = 3,032 cells) identified across the human female reproductive system by Cohen et al. (2026). They sit at one extreme of a pan-reproductive adventitial fibroblast continuum defined by dermatopontin (DPT), SFRP2 and C3 expression, spanning from PI16-high cells to C7/COL15A1-high states (Cohen et al., 2026). The population expresses the canonical "universal fibroblast" markers PI16, CD34 and DPP4 together with SFRP2, C3, IL33 and MFAP5, matching the PI16+ universal/adventitial fibroblast described across many organs (McCartney et al., 2024; Yang et al., 2026). In the reproductive tract these cells are overwhelmingly localised to the subserosal (adventitial) connective tissue of the fallopian tube (Cohen et al., 2026). Across the wider literature, PI16+ adventitial fibroblasts are perivascular, stemness-enriched cells proposed to act as progenitors of specialised fibroblast lineages (Zeltz et al., 2022; De Martin et al., 2023).

## Markers

The atlas defines this population by positive expression of PI16, CD34, DPP4, SFRP2, C3, IL33, MFAP5, KCNB2, SCARA5 and SLPI, with the pan-adventitial core being DPT, SFRP2 and C3 and the PI16-high state marked additionally by high PI16 (Cohen et al., 2026). Cohen et al. (2026) describe this compartment as follows:

> "In contrast, adventitial fibroblasts emerged as a distinct transcriptomics compartment that had been largely overlooked in prior atlases, likely owing to their scarcity and their annotation as generic stromal fibroblasts (Extended Data Fig. 3a and Supplementary Note 2.1). Pan-reproductive adventitial fibroblasts are defined by expression of DPT, SFRP2 and C3, forming a transcriptional continuum from PI16 hi (named "AdvFib PI16hi") to C7/COL15A1 hi states (labeled "AdvFib PI16low" and "Adv Fib (Intr)"; Figure 2a,c), consistent with the universal fibroblast populations previously described 31,32 ."
>
> — Cohen et al. (2026)

The marker profile places this state squarely within the "universal fibroblast" / PI16+ adventitial fibroblast concept established in cross-tissue fibroblast atlases. Yang et al. (2026) summarise the two universal fibroblast subtypes and their markers:

> "Universal fibroblasts, also termed fibroblast progenitors, exist as two different subtypes, namely PI16 + fibroblasts and COL15A1 + fibroblasts (3) (Figure 1)."
>
> — Yang et al. (2026)

> "PI16 + fibroblasts were found in the lung, skin, stomach, colon, pancreas, kidney, breast, and synovium and express additional markers such as dipeptidyl peptidase 4 (DPP4), DPT, CD34, and LY6C1 (3, 4, 7) (Table 1)."
>
> — Yang et al. (2026)

A recurring, expanded marker list for this cell state — including DPP4, IL33 and the surface progenitor marker CD34 — is given by McCartney et al. (2024):

> "In silico analyses have revealed a list of marker genes that are expressed by Pi16+ fibroblasts, including Dpp4 (Dipeptidyl peptidase-4), Cd55, Ackr3 (atypical chemokine receptor, encodes CXCR7), Anxa3 (Annexin A3), and Il33 (See Table 1)."
>
> — McCartney et al. (2024)

Individual markers carry functional significance:

- **PI16 (peptidase inhibitor 16)** — the defining marker. De Martin et al. (2023) note it has direct immunomodulatory and matrix-remodelling activity: "The peptidase inhibitor PI16 has been shown to promote transendothelial migration of leukocytes 41 and to inhibit the extracellular matrix-cleaving enzyme matrix metallopeptidase 2 (ref. 42)."
- **DPP4/CD26 and CD34** — surface markers shared with adventitial/universal fibroblasts and used to prospectively identify the progenitor-like state (Yang et al., 2026; McCartney et al., 2024).
- **SFRP2 and MFAP5** — SFRP2 is part of the WNT-modulating SFRP family expressed prominently in reproductive-tract fibroblast clusters (Yıldız et al., 2023). SFRP2 and MFAP5, together with PI16, were independently identified as among the most specific markers of vascular adventitial fibroblasts in human arteries by Zhao et al. (2025):

> "Using scRNA-seq data, we additionally identified PI16, SFRP2, and MFAP5 as the most specific marker genes for this adventitial fibroblast population (Figures 3B-3D; Table S3)."
>
> — Zhao et al. (2025)

In human pleura, MFAP5 similarly co-marks PI16+ adventitial fibroblasts (Obacz et al., 2022):

> "PI16 expression has been reported for fibroblasts in vascular niches [11], while microfibril-associated protein 5 (MFAP5) is detected in vascular adventitial pulmonary fibroblasts [21]. In keeping with a vascular adventitial phenotype, MFAP5 was detected in many of the pleural PI16 + COL15A1 − fibroblasts (n=1864, figure 1e-g)."
>
> — Obacz et al. (2022)

- **IL33** — an alarmin cytokine and a listed PI16+ fibroblast marker (McCartney et al., 2024), consistent with an immune-interfacing role for this population (see Function).

## Location

### In the female reproductive tract

Within the reproductive atlas, the PI16-high state is strikingly restricted to the fallopian tube adventitia (Cohen et al., 2026):

> "AdvFib PI16 hi states are mostly found in the fallopian tube ampulla and isthmus (99% of PI16 hi cells; Extended Data Fig. 3b), where spatial transcriptomics localise them to its characteristic subserosal (adventitial) connective tissue in the ampulla (Figure 2d)."
>
> — Cohen et al. (2026)

The sibling, more differentiated states of the continuum (PI16-low and the intermediate/transitioning state) occupy broader anatomical niches, giving spatial context to where the PI16-high extreme sits relative to its lineage (Cohen et al., 2026):

> "In contrast, AdvFib PI16low and Adv Fib (Intr) (i.e. C7/COL15A1 hi states) are distributed across tissues occupying the mucosal interstitium of the fallopian tube, the subserosa region beneath the ovarian surface epithelium and adventitial positions around vasculature in the ovary, fallopian tube and the myometrium in the uterus (Figure 2d and Extended Data Fig. 3c)."
>
> — Cohen et al. (2026)

### Perivascular/adventitial localisation across organs

The reproductive-tract localisation matches the general biology of PI16+ universal fibroblasts, which are consistently found in the outermost (adventitial) vascular layer. Yang et al. (2026) note:

> "PI16 + fibroblasts are concentrated close to the vasculature in most tissues and are often described as adventitial fibroblasts though they can also be found away from the vasculature in some contexts (51)."
>
> — Yang et al. (2026)

In the mouse steady-state fibroblast atlas the two universal subsets are spatially separated by depth relative to vessels (Zeltz et al., 2022):

> "Pi16 + fibroblasts were found in perivascular niches and Col15a1 expression was noted deeper inside parenchymal tissues."
>
> — Zeltz et al. (2022)

Human arterial data reinforce the adventitia-exclusive localisation for the PI16/SFRP2/MFAP5+ adventitial fibroblast (Zhao et al., 2025):

> "Marker gene RNAscope studies for this population, along with spatial transcriptomics, localized this population exclusively to the adventitia (Figures 3B and 1D). Based on marker gene expression, we termed this population ''vascular adventitial fibroblast'' (AdvFib)."
>
> — Zhao et al. (2025)

## Function

### Structural, non-hormone-responsive scaffold

Cohen et al. (2026) place adventitial fibroblasts within a conserved, cycle-stable non-interstitial compartment, contrasting them with hormone-responsive interstitial fibroblasts and assigning them a structural role:

> "Cross-organ integration of the mesenchymal compartment revealed a conserved hierarchy of non-interstitial fibroblasts -adventitial fibroblasts, perivascular mural cells and smooth muscle cells -consistent with the universal fibroblast architecture described in mice 31 and extending it to the human reproductive system. Unlike interstitial fibroblasts, which are highly organspecific and temporally regulated by hormonal cycling, this non-interstitial compartment is relatively stable across the menstrual cycle, suggesting a structural rather than hormoneresponsive role."
>
> — Cohen et al. (2026)

### Progenitor / universal-fibroblast reservoir

Across tissues, PI16+ adventitial fibroblasts are proposed to be a quiescent, stemness-enriched reservoir that can give rise to specialised and activated fibroblast states. De Martin et al. (2023) articulate the universal-progenitor hypothesis:

> "It has been suggested that PI16 + fibroblasts of different tissues and tumors coexpressing CD34, HAS1 and PLIN2 represent an adventitial fibroblast subset that may serve as a 'universal' progenitor of fibroblast lineages 29 ."
>
> — De Martin et al. (2023)

McCartney et al. (2024) note their precursor potential and quiescent steady-state behaviour:

> "In some contexts, Pi16+ fibroblast-like cells have exhibited the potential to act as a precursor cell for fibroblasts and fibroblast-derived cells, including but not limited to myofibroblasts, adipocytes, and CAFs (Figure 1)."
>
> — McCartney et al. (2024)

> "Cells that exhibit the phenotype of Pi16+ fibroblasts were shown to be in a state of quiescence in the steady state, with minimal proliferation in uninjured tissues."
>
> — McCartney et al. (2024)

The stemness and progenitor status is supported by direct marker and pseudotime evidence in the muscle fibro/adipogenic progenitor literature (Wang et al., 2022):

> "The Ly6c1 hi clusters expressed the highest level of mesenchymal progenitor markers Cd34 and Ly6a/Sca-1 (Figure 6A), indicating their higher stemness than the other clusters. Pseudotime analysis confirmed the progenitor status of the Ly6c1 hi Pi16 hi cluster (Figure 5B), consistent with the finding by others."
>
> — Wang et al. (2022)

The original cross-tissue atlas interpretation, as recounted by Zeltz et al. (2022), likewise assigns high stemness and differentiation potential to the DPT+PI16+ universal fibroblast:

> "Buechler et al. showed that Dpt + Pi16 + fibroblasts expressed high levels of genes associated with stemness and predicted that these cells could differentiate into distinct fibroblast populations such as the Lrrc15 + cluster, a "perturbation-specific" cluster found in cancer tissues and not present in the steady-state tissues."
>
> — Zeltz et al. (2022)

This progenitor identity connects to the classical perivascular stem cell concept, in which CD34+ adventitial cells of the tunica adventitia are a distinct MSC source (Gomez-Salazar et al., 2020):

> "A population of fibroblast like progenitors located in the outermost layer of larger arteries and veins, the tunica adventitia, was also identified as a source of bona fide MSCs. Adventitial progenitors are phenotypically and anatomically distinct from pericytes."
>
> — Gomez-Salazar et al. (2020)

### Immune interaction and matrix remodelling

The PI16 marker itself has immunomodulatory and ECM-remodelling activity — promoting leukocyte transendothelial migration and inhibiting MMP2 (De Martin et al., 2023, quoted above). In secondary lymphoid tissue, PI16+ adventitial-type reticular cells organise T-cell niches, and adventitial fibroblast specialisation has been linked to T-cell retention in inflamed human tissue (Barron et al., 2018). IL33, a listed marker of this state (McCartney et al., 2024), is an alarmin that positions these cells to signal to immune cells upon tissue stress, though direct functional confirmation in the reproductive tract was not found in the traversed literature.

## Structure / Morphology

No dedicated ultrastructural or morphological description of the reproductive-tract PI16-high adventitial fibroblast was found in the traversed literature. Anatomically, the atlas localises these cells to the subserosal (adventitial) connective tissue of the fallopian tube ampulla (Cohen et al., 2026, quoted in Location), and the broader literature describes universal PI16+ fibroblasts as residing in perivascular/tunica adventitia niches of larger vessels (Zeltz et al., 2022; Gomez-Salazar et al., 2020).

## References

- Cohen CE, Parraga-Leo A, Rodríguez-Montes L, Garcia-Alonso L, Vento-Tormo R, et al. (2026). "An integrated multimodal pan-organ atlas of the female reproductive system across the lifespan contextualises gynaecological pathologies". *bioRxiv*. DOI: [10.64898/2026.06.10.731198](https://doi.org/10.64898/2026.06.10.731198)
- McCartney EE, Chung Y, Buechler M (2024). "Life of Pi: Exploring functions of Pi16+ fibroblasts". *F1000Research*. DOI: [10.12688/f1000research.143511.2](https://doi.org/10.12688/f1000research.143511.2)
- Yang X, Steffani M, Schwabe RF, et al. (2026). "Fibroblasts: a diverse population of cells balancing homeostasis, wound healing, regeneration, inflammation, fibrosis, and cancer across organs". *JCI Insight*. DOI: [10.1172/jci.insight.202529](https://doi.org/10.1172/jci.insight.202529)
- Zeltz C, Navab R, Gullberg D, et al. (2022). "Integrin α11β1 in tumor fibrosis: more than just another cancer-associated fibroblast biomarker?". *Journal of Cell Communication and Signaling*. DOI: [10.1007/s12079-022-00673-3](https://doi.org/10.1007/s12079-022-00673-3)
- Obacz J, Valer J, Marciniak S, et al. (2022). "Single-cell transcriptomic analysis of human pleura reveals stromal heterogeneity and informs in vitro models of mesothelioma". *European Respiratory Journal*. DOI: [10.1183/13993003.00143-2023](https://doi.org/10.1183/13993003.00143-2023)
- De Martin A, Stanossek Y, Ludewig B, et al. (2023). "PI16+ reticular cells in human palatine tonsils govern T cell activity in distinct subepithelial niches". *Nature Immunology*. DOI: [10.1038/s41590-023-01502-4](https://doi.org/10.1038/s41590-023-01502-4)
- Wang X, Chen J, Zhou L, et al. (2022). "Diverse effector and regulatory functions of fibro/adipogenic progenitors during skeletal muscle fibrosis in muscular dystrophy". *iScience*. DOI: [10.1016/j.isci.2022.105775](https://doi.org/10.1016/j.isci.2022.105775)
- Zhao Q, Pedroza AJ, Quertermous T, Cheng P, et al. (2025). "A cell and transcriptome atlas of human arterial vasculature". *Cell Genomics*. DOI: [10.1016/j.xgen.2025.101034](https://doi.org/10.1016/j.xgen.2025.101034)
- Barron AMS, Mantero JC, Browning J, et al. (2018). "Perivascular Adventitial Fibroblast Specialization Accompanies T Cell Retention in the Inflamed Human Dermis". *Journal of Immunology*. DOI: [10.4049/jimmunol.1801209](https://doi.org/10.4049/jimmunol.1801209)
- Gomez-Salazar M, Gonzalez-Galofre ZN, Péault B, et al. (2020). "Five Decades Later, Are Mesenchymal Stem Cells Still Relevant?". *Frontiers in Bioengineering and Biotechnology*. DOI: [10.3389/fbioe.2020.00148](https://doi.org/10.3389/fbioe.2020.00148)
- Yıldız Ş, Kinali M, Bulun S, et al. (2023). "Adenomyosis: single-cell transcriptomic analysis reveals a paracrine mesenchymal-epithelial interaction involving the WNT/SFRP pathway". *Fertility and Sterility*. DOI: [10.1016/j.fertnstert.2023.01.041](https://doi.org/10.1016/j.fertnstert.2023.01.041)
- Wu B, Li Y, Zou X, et al. (2022). "SFRP4+ stromal cell subpopulation with IGF1 signaling in human endometrial regeneration". *Cell Discovery*. DOI: [10.1038/s41421-022-00438-7](https://doi.org/10.1038/s41421-022-00438-7)
