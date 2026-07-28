# VEGFA+ Epithelial Cell of the Human Tonsil

Atlas: Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci (King et al., 2021) (DOI: 10.1126/sciimmunol.abh3768)
Scope: adult
Tissue context: palatine tonsil epithelium (surface / crypt)
Cell Ontology: [epithelial cell](http://purl.obolibrary.org/obo/CL_0000066) (CL:0000066, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3673

## Summary
The "VEGFA+" annotation in the Azimuth `human_tonsil_v2` reference (derived from King et al., 2021) designates an epithelial cell of the human palatine tonsil distinguished by expression of *VEGFA* (vascular endothelial growth factor A). The tonsil epithelium is not a single cell type but two co-existing compartments — a lining surface stratified squamous epithelium and a specialised reticulated crypt epithelium (lymphoepithelium) that overlies the lymphoid tissue (Crowell et al., 2025; Arambula et al., 2021). VEGFA is a secreted, hypoxia-responsive angiogenic factor that is broadly produced but upregulated under low oxygen and can be expressed by mucosal epithelial cells at both transcript and protein level (Qi et al., 2022; Kitazawa et al., 2025). Within the atlas, VEGFA serves as the discriminating transcript marking this epithelial subset; the surrounding biology below is drawn from the broader tonsil-epithelial and VEGFA literature, because the atlas paper's ASTA-indexed text does not describe this subset directly.

## Markers
The atlas label itself names the defining marker, **VEGFA** (vascular endothelial growth factor A) — a secreted signalling protein rather than a structural cell-surface antigen. VEGFA is the founding and best-characterised member of the VEGF family and acts principally through the receptor VEGFR2:

> "VEGFA mediates in vivo angiogenic responses primarily through the activation of VEGFR2 [76]."
>
> — Qi et al. (2022)

Its expression is not restricted to a single lineage but is broadly distributed and induced by hypoxia:

> "VEGFA is produced by most cells in the body but is upregulated in hypoxia."
>
> — Qi et al. (2022)

Direct evidence that a **mucosal epithelium** can express VEGFA at both the transcript and the protein level comes from spatial transcriptomics of superficial gastric mucosa, where VEGFA mRNA was abundant and VEGFA protein was confirmed by immunohistochemistry in epithelial cells (Kitazawa et al., 2025):

> "In the superficial mucosa, mRNA expression of VEGFA and FLT1 was found to be abundant (Figs. 5A and 5B), prompting further immunohistochemical analysis of these factors."
>
> — Kitazawa et al. (2025)

> "VEGFA was localized to both tumor cells and inflammatory cells (mainly macrophages) in the superficial mucosa (Fig. 8B)."
>
> — Kitazawa et al. (2025)

Because VEGFA is a secreted factor, its detection as a single-cell transcript (as in the atlas) does not by itself localise the protein; the mucosal evidence above is drawn from a different tissue and should be read as supporting the plausibility of epithelial VEGFA expression rather than as direct tonsil data.

Beyond VEGFA, the two tonsil epithelial compartments are distinguished in the wider literature by keratin (cytokeratin) profiles at the protein level. Surface epithelium is marked by K5 and K14:

> "K5 and K14 were strongly expressed in the surface epithelium."
>
> — Okda et al. (2021)

whereas the reticulated crypt epithelium is distinguished by simple keratins:

> "However, tonsil surface and crypt epithelia undergo alternative differentiation programmes and in particular, there are marked differences in their keratin profiles [74]. Cytokeratin 8 (CK8), normally partnered with CK18 is weakly expressed in keratinocytes of the surface tonsil epithelium (and in basal keratinocytes), but is strongly expressed in the reticulated crypt, particularly in the cells of the upper layers [74]."
>
> — Roberts et al. (2019)

> "Another cytokeratin that distinguishes crypt from surface epithelia is the transitional/junctional epithelia marker CK7."
>
> — Roberts et al. (2019)

These keratin markers are protein-level (antibody / immunohistochemical) findings and describe the epithelial compartments generally; they are not VEGFA-specific.

## Location
This cell type is located in the epithelium of the human palatine tonsil, which comprises two compartments. Both are described in the spatial-transcriptomic tonsil map of Crowell et al. (2025):

> "Tonsil epithelium consist of two different types of actively differentiating epithelium: lining (surface) stratified squamous epithelium; and, reticulated crypts -deep invaginations of the tonsil in which the continuity of the outer surface epithelium is disrupted."
>
> — Crowell et al. (2025)

The surface epithelium is continuous with the oral mucosa and folds inward to form the crypts (Sarmiento Varón et al., 2021; Bucolo et al., 2013):

> "Anatomically, the surface epithelium of the palatine tonsils is an extension of the stratified squamous epithelium of the oral mucosa (Figure 3A, Supplementary Figures 6, 7)."
>
> — Sarmiento Varón et al. (2021)

> "The tonsil surface is usually covered by stratified squamous epithelium that envelops tonsils to form the crypts. There are generally some 20-30 crypts for tonsil. Within the crypt epithelium is not tightly arranged and presents macrophages, dendritic cells and lymphocytes to epithelial cells interspersed."
>
> — Bucolo et al. (2013)

The crypts are lined by a mixture of the two epithelial types (Arambula et al., 2021):

> "The crypts themselves are lined by a non-uniform distribution of stratified squamous epithelium and reticulated crypt epithelium."
>
> — Arambula et al. (2021)

Notably, the surface (stratified squamous) compartment was resolved only in adult tonsil sections in the spatial map (Crowell et al., 2025), consistent with the adult scope of this atlas annotation.

## Function
The tonsil epithelium has a dual barrier-and-transport role, protecting the mucosal surface while conveying antigen to the underlying lymphoid tissue (Sarmiento Varón et al., 2021):

> "The tonsillar epithelium provides protection as well as serving to transport foreign material from the lumen to the lymphoid compartment."
>
> — Sarmiento Varón et al. (2021)

The reticulated crypt epithelium is specifically adapted for antigen sampling, with an incomplete basal layer and porous basement membrane that permit passage of immune cells (Ferris & Westra, 2023):

> "These tonsillar crypts are lined by a highly specialized epithelium known as the reticulated (net-like) epithelium that is uniquely structured to facilitate transport of foreign antigens from the external environment of the oropharynx to the tonsillar lymphoid tissue (Figure 1).The basal cell layer is incomplete and its supporting basement membrane is disrupted and porous, thus allowing for the direct passage of lymphocytes and antigen-presenting cells."
>
> — Ferris & Westra (2023)

The functional significance of the VEGFA marker itself relates to angiogenesis and vascular permeability. As a secreted factor, VEGFA drives endothelial responses (Li et al., 2025):

> "VEGF-A elicits transient vasodilatation and augments vascular permeability via the liberation of nitric oxide (NO), thereby stimulating the proliferation, directional migration, and differentiation of vascular endothelial cells."
>
> — Li et al. (2025)

VEGFA is the archetypal VEGF-family ligand (Li et al., 2025):

> "Notably, VEGF-A was the inaugural member of this family to be discovered and remains the most extensively researched to date."
>
> — Li et al. (2025)

Its induction by hypoxia (Qi et al., 2022, quoted above) provides a plausible explanation for VEGFA expression in tonsil epithelium: the crypt microenvironment, densely infiltrated by immune cells and metabolically active, may create local hypoxic conditions favouring VEGFA transcription. This mechanistic link is inferred from the general VEGFA literature and is not directly demonstrated in the atlas.

The crypt "epithelial" compartment of the tonsil also overlaps transcriptionally with antigen-sampling microfold (M) cells; a recent single-cell study noted that in the tonsil epithelial atlas, M-cell markers were detected within a subset termed "crypt cells" (Alvarez-Arguedas et al., 2025):

> "Nevertheless, expression of canonical M cell markers such as SPIB and MARCKSL1 was detected in a subset of epithelial cells termed 'crypt cells'."
>
> — Alvarez-Arguedas et al. (2025)

This is transcript-level evidence and concerns crypt cells generally rather than the VEGFA+ subset specifically.

## Structure / Morphology
The reticulated crypt epithelium is structurally distinct from the orderly surface epithelium, being loosely arranged and interspersed with non-epithelial cells (Arambula et al., 2021):

> "Reticulated epithelium is less orderly than stratified squamous epithelium and contains both epithelial and non-epithelial cells, particularly lymphoid cells. This epithelial layer can be quite thin and even lack a basement membrane in some regions."
>
> — Arambula et al. (2021)

Both compartments are actively differentiating and rich in keratins that provide mechanical strength (Crowell et al., 2025; Okda et al., 2021):

> "Both surface and crypt epithelial cells contain keratins, a protein family that forms intermediate filaments and maintains cell structure and function, contributing to mechanical strength and protection from stress."
>
> — Crowell et al. (2025)

> "Human tonsil epithelium cells (HTEC) are a heterogeneous group of actively differentiating cells comprising stratified squamous epithelial and reticulated crypt cells with abundant keratin expression."
>
> — Okda et al. (2021)

The confirmation that the tonsil epithelium comprises both compartments is protein-level, established with keratin antibody panels (Okda et al., 2021):

> "By using a panel of antibodies specific to different keratins, we confirmed that the tonsil epithelium consists of both stratified surface and reticulated crypt epithelial cells."
>
> — Okda et al. (2021)

## References
- King HW, Wells KL, Shipony Z, et al. (2021). "Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci". *Science Immunology*. DOI: [10.1126/sciimmunol.abh3768](https://doi.org/10.1126/sciimmunol.abh3768)
- Arambula AM, Brown JR, Neff LL (2021). "Anatomy and physiology of the palatine tonsils, adenoids, and lingual tonsils". *World Journal of Otorhinolaryngology - Head and Neck Surgery*. DOI: [10.1016/j.wjorl.2021.04.003](https://doi.org/10.1016/j.wjorl.2021.04.003)
- Ferris R, Westra W (2023). "Oropharyngeal Carcinoma with a Special Focus on HPV-Related Squamous Cell Carcinoma". *Annual Review of Pathology*. DOI: [10.1146/annurev-pathmechdis-031521-041424](https://doi.org/10.1146/annurev-pathmechdis-031521-041424)
- Okda FA, Sakr A, Webster R, Webby R (2021). "Tropism, susceptibility, infectivity, and cytokine releases of differentiated human tonsillar epithelial cells by different Influenza viruses". *bioRxiv*. DOI: [10.1101/2021.05.03.442542](https://doi.org/10.1101/2021.05.03.442542)
- Roberts S, Evans D, Mehanna H, Parish JL (2019). "Modelling human papillomavirus biology in oropharyngeal keratinocytes". *Philosophical Transactions of the Royal Society B*. DOI: [10.1098/rstb.2018.0289](https://doi.org/10.1098/rstb.2018.0289)
- Crowell HL, Llaó-Cid L, Frigola G, et al. (2025). "A Transcriptional Map of Human Tonsil Architecture: Beyond the Sum of (Single Cell) Parts". *European Journal of Immunology*. DOI: [10.1002/eji.70121](https://doi.org/10.1002/eji.70121)
- Bucolo S, Torre V, Romano G, et al. (2013). "Effects of Tonsillectomy on Psoriasis and Tonsil Histology-Ultrastructure". *InTech*. DOI: [10.5772/55978](https://doi.org/10.5772/55978)
- Alvarez-Arguedas S, Mazhar K, Wangzhou A, et al. (2025). "Single cell transcriptional analysis of human adenoids identifies molecular features of airway microfold cells". *Mucosal Immunology*. DOI: [10.1016/j.mucimm.2025.07.006](https://doi.org/10.1016/j.mucimm.2025.07.006)
- Kitazawa S, Takeshita E, Tomida H, et al. (2025). "Spatial transcriptomic analysis of foveolar-type gastric adenoma with raspberry-like appearance". *Virchows Archiv*. DOI: [10.1007/s00428-025-04302-3](https://doi.org/10.1007/s00428-025-04302-3)
- Qi S, Deng S, Lian Z, Yu K (2022). "Novel Drugs with High Efficacy against Tumor Angiogenesis". *International Journal of Molecular Sciences*. DOI: [10.3390/ijms23136934](https://doi.org/10.3390/ijms23136934)
- Li Z, Zeng L, Huang W, et al. (2025). "Angiogenic Factors and Inflammatory Bowel Diseases". *Biomedicines*. DOI: [10.3390/biomedicines13051154](https://doi.org/10.3390/biomedicines13051154)
- Sarmiento Varón L, De Rosa J, Rodriguez R, et al. (2021). "Role of Tonsillar Chronic Inflammation and Commensal Bacteria in the Pathogenesis of Pediatric OSA". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2021.648064](https://doi.org/10.3389/fimmu.2021.648064)
