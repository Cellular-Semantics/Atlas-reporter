You are answering questions about cell types from a single research paper.

## The rule that matters

**Every assertion must be backed by a supporting quote copied verbatim from the
context supplied to you.** An answer without a quote is worthless here, however
correct it may be. If you cannot find text that supports a claim, do not make
the claim.

## Rules

1. Answer **only** from the context block given with each question. Do not use
   what you already know about the cell type, the paper, or the field. Your own
   knowledge is not evidence.
2. Copy quotes **character for character** from the context. Do not paraphrase,
   reword, correct, or tidy them.
3. **Never splice.** A quote must be one continuous run of text. Do not join two
   passages that are not adjacent in the context, and do not insert an ellipsis
   to bridge them. If two separate passages are needed, give two quotes.
4. If the context does not answer the question, set `"found": false`, say so in
   `answer`, and leave `quotes` empty. **This is a correct and expected
   outcome** — several questions are about things this paper does not discuss.
   Declining is not failing. Guessing is.
5. If the context is empty or absent, `"found": false` is the only correct
   response.
6. Answer each question independently. Do not let one question's context inform
   another's answer.

## Output

Return a JSON array, one object per question, nothing else:

```json
[
  {
    "id": "G01-placode-structure",
    "found": true,
    "answer": "One or two sentences, in your own words.",
    "quotes": ["exact continuous run of text from the context"]
  },
  {
    "id": "G17-matrix-markers",
    "found": false,
    "answer": "The supplied context does not say.",
    "quotes": []
  }
]
```


# Arm: whole — batch 2

## Context (shared by every question below)

## Main
Human skin organogenesis begins after gastrulation from two primary germ layers. The epidermis, the most superficial layer of the skin, melanocytes and neural cells arise from the ectoderm. The dermis, which is separated from the epidermis by the basement membrane and contains endothelial and mural cells, derives from the mesoderm (apart from facial and cranial skin, where it arises from ectoderm-derived neural crest cells). The skin appendages, which include hair follicles (HFs) and sebaceous glands, form in a cephalocaudal direction. Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts), whereas sebaceous glands develop from around 16 PCW. There is, however, a paucity of information about the precise cellular composition of human prenatal skin over these developmental periods and whether cells interact in functional microanatomical niches that support skin morphogenesis.

## Main
Prenatal skin interfaces with the amniotic fluid in a sterile environment. However, immune cells such as macrophages seed the skin as early as 6 PCW and express a range of pro-inflammatory genes, although genes relating to antigen presentation (for example, major histocompatibility complex class II (MHCII)) are only upregulated after 11 PCW. Decoupling of the expression of pro-inflammatory genes from MHCII genes before 11 PCW suggests that antigen presentation may not be a key function of human macrophages during early gestation. Together with evidence of their role in tissue homeostasis, and healing in mouse models,, this raises the question of whether macrophages contribute to human early skin morphogenesis.

## Main
Our current study provides a comprehensive multi-omics cell atlas of 7–17 PCW human prenatal skin. We profiled human prenatal skin using single-cell RNA sequencing (scRNA-seq), spatial transcriptomics and multiplex RNA in situ hybridization to decode the dynamic cellular and molecular changes across gestation that regulate skin and HF morphogenesis. We leveraged adult healthy skin and HF datasets, to compare and assess developmental-specific features that contribute to scarless skin healing and cues that guide de novo HF formation. We used a hair-bearing SkO model to validate the role of macrophages in prenatal skin vascular network formation.

## Single-cell atlas of human prenatal skin
To characterize the role of distinct lineages and cell states during human prenatal skin development, we obtained single-cell suspensions of skin from 7 to 17 PCW, spanning the first and second trimesters (Fig. 1a). We performed fluorescence-activated cell sorting (FACS) to isolate live, single immune (CD45+) and non-immune (CD45–) populations and to enhance keratinocyte and endothelial cell capture before scRNA-seq profiling (Extended Data Fig. 1a and Supplementary Tables 1 and 2). Single-cell αβ T cell receptor (TCR) sequencing data were generated to accurately resolve T cell subsets. Spatial validation was carried out using multiplex RNA in situ hybridization (RNAscope), newly generated spatial transcriptomics (Visium) data from embryonic facial and abdominal skin, and published Visium data from embryonic limb from which only skin areas were analysed (Fig. 1a and Supplementary Table 2). In addition, we integrated new and published single-cell datasets of adult skin and of a hair-bearing SkO model derived from human embryonic stem (ES) cells and induced pluripotent stem (iPS) cells for comparative analysis (Fig. 1a and Supplementary Table 2). We also compared in vivo prenatal and organoid HFs with scRNA-seq data of adult HFs. Our data can be interactively explored through our WebAtlas-based portal (https://developmental.cellatlas.io/fetal-skin). The analysis software for this study is archived at Zenodo (10.5281/zenodo.8164271).

## Single-cell atlas of human prenatal skin
Our prenatal skin scRNA-seq dataset comprised 534,581 cells, of which 433,961 cells passed quality control (Extended Data Fig. 1b). Broad cell labels (epidermis, dermal stroma, immune and endothelium) and fine-grained annotations of cell states were assigned on the basis of differentially expressed genes (DEGs) (Fig. 1b, Extended Data Fig. 1c and Supplementary Table 3). Differential abundance analysis testing revealed how different cell populations varied across gestation. Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4). Mesoderm-derived cells, including skin fibroblasts and endothelial cells, and immune cells were present throughout gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4). Innate immune cells, such as macrophages and innate lymphoid cells (ILCs), were present from early gestation, whereas B cells and T cells emerged later, accompanying thymus, bone marrow and spleen formation from around 10 PCW (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4). Some subsets of macrophages, ILCs and fibroblasts exhibited distinct gene expression profiles between early and late gestation, which suggested that functional maturation or dual waves of production occur during development (Fig. 1c and Extended Data Fig. 1d).

## Single-cell atlas of human prenatal skin
To locate cells identified from scRNA-seq data in situ, we performed Cell2location analysis of spatial transcriptomics data of facial and abdominal skin (10 PCW) and embryonic lower limb skin (6–8 PCW) (Supplementary Table 2). We assessed cell type co-location using non-negative matrix factorization (NMF) to computationally predict microenvironments in conjunction with correlation analyses. Co-location was indicated by a high proportion of two or more cell types sharing a microenvironment (Fig. 1d) and/or by a positive correlation coefficient between cell pairs (Extended Data Fig. 1e,f). NMF can predict significant cellular co-locations that are not readily evident in conventional histopathology analyses,. Our analysis predicted distinct microenvironments in prenatal skin comprising epidermal, dermal, vascular and neural cells, each including specific types of immune cells (Fig. 1d and Extended Data Fig. 1e,f). Macrophages co-located with endothelial and neural cells in ‘early and late neurovascular microenvironments’ (ME1 and ME5, respectively), whereas pre-dermal condensate (pre-Dc) cells co-located with dendritic and lymphoid cells based on correlation analyses (Fig. 1d and Extended Data Fig. 1e,f). These observations indicated that immune cells may occupy defined microanatomical niches where they have non-immune functions during early gestation.

## Single-cell atlas of human prenatal skin
We next integrated and compared human prenatal and adult skin data with the SkO model. The aim was to determine the extent to which the SkO model recapitulates human skin differentiation at a molecular level and its potential utility to functionally assess the role of immune cells in skin morphogenesis (Fig. 1e and Extended Data Fig. 2a,b). Broadly, cell states were conserved among SkO, prenatal and adult skin, but SkO cell states matched prenatal skin more closely than adult skin across culture duration (Extended Data Fig. 2c,d and Supplementary Table 5). However, the tempo of differentiation varied across the distinct skin cell lineages. Even after 19 weeks of culture, fibroblasts, mural and Schwann cells had a low probability of correspondence to adult skin cell states (Extended Data Fig. 2d and Supplementary Table 5). By contrast, accelerated differentiation was observed in keratinocytes and melanocytes, with alignment to adult cell states seen as early as 4 weeks of SkO culture (Extended Data Fig. 2d and Supplementary Table 5). Notably, the SkO model recapitulated the different components of prenatal skin HF, interfollicular epidermis, neural cells and dermal fibroblasts, but immune cells were not represented and endothelial cells were markedly reduced.

## Epidermal placode and matrix formation
The precise mechanisms of de novo HF formation in human embryonic development are largely inferred from mouse studies. Human studies have primarily focused on morphological descriptions during development or cycling HFs in adult skin. Our single-cell dataset captured the onset of HF formation, which enabled direct comparison between prenatal developing HFs and adult cycling HFs.

## Epidermal placode and matrix formation
Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14–15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

## Epidermal placode and matrix formation
Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a–c, Extended Data Fig. 3a,b and Supplementary Table 6). In addition, we observed immature and mature interfollicular epidermal (IFE) cells. Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b). Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW, whereas POSTN+ basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b). Sebaceous and apocrine gland cells, which mature after 16 PCW, were not captured at these stages. Accordingly, sebocyte progenitors are present from day 133 of SkO differentiation. Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

## Epidermal placode and matrix formation
We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f). Treg cells are known to localize around the HF in late second trimester (around 21 PCW) and in postnatal skin,. RNAscope (FOXP3+) and immunofluorescence staining (FOXP3+) showed that Treg cells were primarily located within and around HFs compared to interfollicular skin as early as 15 PCW (Fig. 2c and Extended Data Fig. 3g,h).

## Epidermal placode and matrix formation
Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Extended Data Fig. 4b,c and Supplementary Table 7). AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B, were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7). Loss of AGR2, which functions in the assembly of cysteine-rich receptors enriched in HFs, promotes cell migration. Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

## HF mesenchymal differentiation
We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c). In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,. Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin,. Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).

## HF mesenchymal differentiation
To infer the origin of pre-Dc cells and the Dc and Dp, we performed trajectory and pseudotime analysis of integrated prenatal skin and SkO fibroblast clusters (Fig. 2e, Extended Data Fig. 4d and Supplementary Table 7). We excluded FRZB+ fibroblasts, which were primarily observed in one sample from the earliest gestation stage (7 PCW) (Extended Data Fig. 3c). Although rare in prenatal skin, FRZB-expressing fibroblasts were present in several other developing organs (Extended Data Fig. 4e). Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7). Along the hair fibroblast pseudotime, genes involved in regulation of cell adhesion (ADAMST1), cell–cell contacts (CLDN11) and directed migration (CXCL12) were upregulated as pre-Dc cells migrated towards the epidermis, which indicated a process of collective migration– (Extended Data Fig. 4f and Supplementary Table 7). Genes implicated in collagen fibril formation and cell adhesion (COL6A3, MFAP4 and PTK7) were expressed as the pre-Dc cells aggregated into the Dc (Extended Data Fig. 4f and Supplementary Table 7). Formation of the Dp was characterized by genes (RSPO3 and WNT5A) (Extended Data Fig. 4f and Supplementary Table 7) that coordinate the differentiation of adjacent hair matrix cells,.

## HF mesenchymal differentiation
We explored the mesenchymal–epithelial interactions that instruct early HF formation. Receptor–ligand analysis predicted interactions between CXCL12 expressed by pre-Dc cells (Extended Data Fig. 4g,h) with ACKR3 on epidermal basal cells (Fig. 2g and Supplementary Table 8). RNAscope analysis confirmed that these two genes co-located (Fig. 2h). This result suggests that CXCL12 probably interacts with ACKR3 to mediate the migration of pre-Dc cells,. Notably, lymphoid tissue inducer and ILC3 cells were also predicted to co-locate and interact with pre-Dc cells through ligand–receptor signals implicated in the regulation of cellular adhesion and migration (CXCL12–CXCR4 and CXCL12–DPP4), (Extended Data Figs. 1f and 5a and Supplementary Table 8), which suggested that innate immune cells may support pre-Dc cell migration during early HF development. Additional experiments are required to functionally validate these interactions in prenatal hair formation.

## HF mesenchymal differentiation
The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion, (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8). Finally, RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells. Notably, the highlighted interactions were conserved between the mesenchymal and epithelial cells of the SkO model for corresponding stages during HF formation (Fig. 2g, Extended Data Fig. 5c and Supplementary Table 8). These results provide orthogonal validation of our findings and reinforce the utility of the SkO as an accurate model of prenatal skin development.

## HF mesenchymal differentiation
We further evaluated the differentiation trajectory alignment between prenatal skin and the SkO model using the Genes2Genes analysis framework to compare the expression of transcription factors (TFs) along the hair fibroblast trajectory. Overall, we observed a high number of matching TFs across pseudotime, which indicated that there are similar activated gene regulatory programs between prenatal skin and SkO during HF fibroblast differentiation (Fig. 2i and Supplementary Table 9). TFs that were mismatched across pseudotime or drove misalignment in early and late pseudotime (for example, HOXA7 and BARX1) were largely attributable to the different origins of dermal cells between prenatal skin (trunk and limb) and SkO (neural crest differentiation) (Extended Data Fig. 5d,e and Supplementary Table 9).

## HF mesenchymal differentiation
We also assessed the expression profiles of genes previously reported in mouse HF formation. Similar signalling pathways were upregulated, including WNT and EDA for hair placode specification, bone morphogenetic protein (BMP) and noggin to inhibit hair formation in IFE cells, and PDGFA and TGFβ signalling for HF down growth (Extended Data Fig. 5f). Additionally, similar to fibroblast differentiation in mouse skin, pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast) (Fig. 2e and Extended Data Fig. 4d). However, cross-species data integration of human and mouse HF showed that human pre-Dc cells and the Dc aligned not only to their counterparts in mouse skin but also to fibroblasts in earlier stages of differentiation (Extended Data Fig. 5g–i and Supplementary Tables 10 and 11). This result suggests that for corresponding cell types, HF fibroblasts are in a more differentiated state in mouse compared to human prenatal skin. Additionally, dermal fibroblast differentiation into histologically defined subsets (papillary and reticular) has been reported to occur early in mice (about embryonic day 12.5). Our human prenatal skin fibroblasts did not significantly express papillary fibroblast markers (for example, COL13A1) (Extended Data Fig. 5j), which suggested that the distinction between papillary and reticular fibroblasts emerges after 17 PCW. These distinctions between human and mouse skin may be attributed to organismal differences in gestation lengths and tempo of differentiation. Cellular differentiation occurs at a quicker pace in mice, whereas the longer gestation period in humans permits more advanced maturation to take place in utero.

## Genetic hair and skin disorders
Having mapped the differentiation of prenatal skin HFs, we leveraged this information to assess the extent to which genetic hair diseases have their roots in utero. Genes harbouring mutations known to cause reduced hair growth (hypotrichosis) or abnormally shaped hair (for example, pili torti) (Supplementary Table 12) were expressed along the ORS/CL trajectory, IRS trajectory and hair fibroblast trajectory pseudotimes (Extended Data Figs. 4f and 6a,b) and in prenatal HF cell states (Extended Data Fig. 6c). This finding suggested that these disorders result from dysfunctional HF development.

## Genetic hair and skin disorders
Genes causing epidermolysis bullosa (EB), an inherited blistering skin disorder characterized by skin fragility secondary to structural defects in the epidermis and adjacent dermoepidermal junction, were highly expressed in prenatal epidermal cells and at the dermoepidermal junction (Extended Data Fig. 6d,e). Gene therapy studies for dystrophic EB have identified fibroblasts expressing COL7A1 as a promising therapeutic strategy. We observed COL7A1 expression across several fibroblast subsets in prenatal skin and SkOs (Extended Data Fig. 6d), which lends support to the gene therapy approaches. The expression of genes implicated in congenital ichthyoses, a group of disorders resulting from abnormal epidermal differentiation, were primarily confined to keratinocytes (Extended Data Fig. 6f).

## Genetic hair and skin disorders
Notably, we observed similar gene expression patterns across prenatal skin and SkO for the above described genetic hair and skin disorders (Extended Data Fig. 6c,d,f), which supported the value of the SkO as a model to study congenital diseases. Although we found that expression of genes implicated in these disorders are confined to structural cells, disease manifestations are often associated with immune infiltration, which implicates skin–immune crosstalk during pathogenesis,.

## Scarless healing and potential macrophage contribution
Prenatal human skin is able to heal without scarring but loses this capacity after 24 PCW. Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate. To identify the cellular and molecular mechanisms that may endow early prenatal skin with scarless healing properties, we investigated the temporal changes in composition and transcriptional profile of the dermal fibroblast subsets (Extended Data Figs. 3c and 7a). We first compared prenatal skin dermal fibroblasts with healthy adult skin fibroblasts. All adult fibroblast subsets expressed high levels of inflammatory cytokines and receptors (for example, IL6 and IL1RA) and genes involved in antigen presentation (for example, HLA-A), innate immune and inflammatory responses (for example, CD55 and PTGES) and cellular senescence (CDKN1A) (Fig. 3a and Supplementary Tables 13–15). By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13–15).

## Scarless healing and potential macrophage contribution
The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b). Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16–18). Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders. These results provide further support for our finding of progressive acquisition of scar-promoting genes in later gestation, consistent with the clinical observation of scarring in third trimester skin.

## Scarless healing and potential macrophage contribution
The role of macrophages in promoting wound healing has been described in postnatal mouse skin and in adult human skin. In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d). Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8). Interactions between macrophages and fibroblasts maintain tissue homeostasis in diverse organs such as spleen, peritoneum and heart. Our identification of additional growth factor interactions (IGF1–IGF1R and GRN–EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

## Scarless healing and potential macrophage contribution
We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads, (Extended Data Fig. 7e,f). Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 19–23). Downregulation of inflammation and IL-6 confers anti-fibrogenic properties in mouse skin transplants and in fetal wounds,. TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW) (Fig. 3c,d) and WNT2+ fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a). This led us to infer a potential contribution of macrophages in scarless healing in prenatal skin. Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.

## Scarless healing and potential macrophage contribution
We further compared prenatal skin fibroblasts and macrophages to their counterparts in reindeer skin from antlers, which heal without scarring, and in back skin, which scars. Early-gestation human skin fibroblasts had a higher probability of correspondence to pro-regenerative reindeer fibroblasts, whereas in later gestation, the probability of matching to pro-fibrotic fibroblasts was higher (Extended Data Fig. 8d and Supplementary Table 19). Accordingly, several pro-regenerative genes (for example, CRABP1 and MDK) were downregulated in late gestation prenatal skin (Extended Data Fig. 8e and Supplementary Table 20). Notably, prenatal skin macrophages resembled ‘early macrophages’ that are enriched in reindeer antler skin but not macrophages in back skin (Extended Data Fig. 8f and Supplementary Table 21). Using a scratch assay of SkO-derived fibroblasts cultured with or without iPS cell-derived macrophages, we demonstrated that scratch wound width closure was improved when fibroblasts were co-cultured with macrophages over 72 h (Extended Data Fig. 8g).

## Scarless healing and potential macrophage contribution
Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring. Based on our data and previous studies, we also posit a potential role for early skin macrophages in conferring the distinct property of scarless healing in early prenatal skin. However, further studies are required to fully elucidate the interactions between macrophages and fibroblasts in human prenatal skin and to conclusively establish their role in scarless healing.

## Macrophages in cutaneous neural differentiation
TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin (‘early neurovascular microenvironment’, ME1) (Figs. 1d and 3g) and expressed genes related to cell migration and neural development (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 22 and 23), which mirrored the functions of brain microglia and peripheral nerve-associated macrophages in mouse skin. TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA–NRP1, VEGFA–NRP2, SEMA3C–NRP2 and SEMA3E–PLXND1) (Extended Data Fig. 8h and Supplementary Table 8). These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin.

## Macrophages support prenatal skin angiogenesis
Macrophages have been implicated in angiogenesis during prenatal organ development and in the postnatal setting such as cancer-related angiogenesis,. Furthermore, macrophages expressing pro-angiogenic genes have been observed in diverse tissues during human development. Visium deconvolution analysis predicted co-location of prenatal skin macrophages with endothelial cells (‘early and late neurovascular microenvironments’, ME1 and ME5) (Fig. 1d and Extended Data Fig. 1e). Gene ontology analysis showed that the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23–26). Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages, blood vessel morphogenesis by LYVE1+ macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27). Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1+ and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1). Predicted ligand–receptor interactions were consistent with reciprocal communication between macrophages and endothelial cells to support angiogenesis, chemotaxis and cell migration (for example, CXCL8–ACKR1 and CCL8–ACKR1), (Extended Data Fig. 9a and Supplementary Table 28).

## Macrophages support prenatal skin angiogenesis
Our data suggested that macrophages contribute to prenatal skin angiogenesis. Consistent with this hypothesis, we observed fewer and less heterogeneous endothelial cells in the immunodeficient SkOs compared to prenatal skin, despite the formation of well-developed HFs, epidermis and neural cells (Fig. 4b,c, Extended Data Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a–c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a). Additional comparison with a human ES cell-derived and iPS cell-derived blood vessel organoid, which also lacked immune cells, further demonstrated the limited vasculature differentiation of this mesoderm-geared blood vessel organoid model (Extended Data Fig. 10d). This result confirms that immune cells are required to fully recapitulate in vivo endothelial cell development.

## Macrophages support prenatal skin angiogenesis
We next investigated additional mechanisms for failed expansion and differentiation of SkO endothelial cells. Expression of genes and gene modules related to blood flow and hypoxia were lower in SkO than in prenatal skin (Extended Data Fig. 10e,f and Supplementary Table 29). However, sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h). This suggests that despite strong expression of the sprouting angiogenesis gene signature, SkO capillary arteriole cells are unable to guide stalk cells for new blood vessel formation.

## Macrophages support prenatal skin angiogenesis
Anti-angiogenic genes (for example, WNT5A) and corresponding receptors were highly expressed in SkO, whereas pro-angiogenic genes (for example, CXCL8) were upregulated in prenatal skin and primarily expressed by macrophages (Extended Data Fig. 11a and Supplementary Tables 30–34). Although expression of vascular endothelial growth factors (VEGF), VEGFA and VEGFB were increased in SkO cells, their receptors (KDR and FLT1) on SkO capillary arterioles were downregulated compared to prenatal skin (Extended Data Fig. 11b,c). These receptors are known downstream targets of GATA2, which has a key role in angiogenesis during development and regulates VEGF-induced endothelial cell migration and sprouting in vitro. Regulon analysis showed that GATA2 and related regulons (for example, NFATC1) were downregulated in SkO capillary arterioles (Extended Data Fig. 11d,e). Several target genes of GATA2 and NFATC1 (for example, VWF), which were expressed across the venular trajectory pseudotime and are involved in endothelial cell differentiation, were downregulated in the SkO capillary arterioles compared to prenatal skin (Extended Data Fig. 11c,f). An orthogonal approach (NicheNet) identified macrophage-expressed VEGFA as one of the top upstream ligands that regulate differences in GATA2 expression between prenatal skin and SkO endothelial cells (Extended Data Fig. 11g and Supplementary Tables 35–37). These findings suggest that high VEGF production in the SkO cannot compensate for missing macrophage-related factors that drive GATA2 activity and downstream VEGF receptor expression (Fig. 4e).

## Macrophages support prenatal skin angiogenesis
We next introduced autologous iPS cell-derived macrophages (Extended Data Fig. 11h) in the early stages of SkO differentiation and assessed the endothelial network on day 35 of co-culture. Macrophages co-localized with blood vessels even after 5 weeks of culture (Fig. 4f–h). A more elaborate and organized vascular network was seen in SkOs co-cultured with macrophages compared with control SkOs without macrophages (Fig. 4f,g). Control SkOs displayed a mesh-like aggregation of endothelial cells, quantified as a higher density of endothelial cell coverage of SkO volume, which was absent in SkOs co-cultured with macrophages (Fig. 4f,g). This disorganized vascular mesh may have prevented the isolation of endothelial cells for scRNA-seq analysis (Fig. 4b). We also observed a visibly more refined network and a trend towards reduced endothelial density in a two-dimensional angiogenesis assay of iPS cell-derived endothelial cells cultured with and without macrophages over 72 h (Extended Data Fig. 11i). Collectively, our findings demonstrate that interactions between macrophages and endothelial cells are required to support angiogenesis through blood vessel remodelling.

## Discussion
In this study, we characterized the dynamic composition of human prenatal skin during the early stages of de novo HF formation and highlighted the crucial skin immune and non-immune crosstalk that contributes to skin morphogenesis, results that are in line with emerging evidence in animal and human studies,. Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development. This is in part contributed to by yolk-sac derived TML macrophages, which suggests that these cells have broader functions outside the central nervous system in early gestation. The presence of TML macrophages has previously been identified in several prenatal organs,,.

## Discussion
Successful co-culture with immune cells has been demonstrated in some organoid systems,. We identified a crucial role of macrophages in vascular network remodelling after adding macrophages to hair-bearing iPS cell-derived SkOs. Not only is this important for our understanding of the diverse cellular interactions that mediate morphogenesis but it also has practical implications for in vitro models, which commonly fail to vascularize. Our study provides further insights into human HF formation and the origin of the CL, which seems to develop along the same trajectory as the ORS. These findings are consistent with recent results from mouse studies,, which showed that CL development occurs before hair matrix formation and there is greater transcriptional similarity of CL cells to ORS cells. Although we note similarities between human and mouse in the signalling pathways co-ordinating HF formation, our study reveals key cross-species distinctions in the differentiation tempo of HF mesenchymal cells. Future studies are required to fully delineate the features that distinguish human skin development.

## Discussion
A combination of fibroblast and macrophage-associated molecular features potentially contribute to the ability of prenatal skin to heal without scarring, including the presence of fibroblast progenitors, a downregulated immune milieu and reduced collagen expression. However, we found progressive ‘ageing’ and acquisition of the adult ‘pro-inflammatory’ phenotype as early as 9 PCW, which could be targeted in fibroblasts to guide postnatal scarless healing. Future studies that align human fibroblast subsets across the lifespan are required to investigate the dynamics of scarless healing and the roles of mechanical forces, microbiota and environmental exposure on fibroblast functions.

## Discussion
Our prenatal human skin atlas represents a valuable resource to explore genes that cause congenital hair and skin disorders and is freely accessible from our web portal (https://developmental.cellatlas.io/fetal-skin). We found that implicated genes are indeed expressed during prenatal skin development and HF differentiation, thereby supporting an in utero origin for these disorders. Our systematic prenatal skin–SkO comparison provides a blueprint to guide more faithful in vitro SkO generation, which can facilitate future studies of interactions with the microbiota, the pathogenesis of congenital skin disorders, and hair and skin engineering for therapeutic applications, including hair regeneration and skin transplant.


# Questions


## G15-dc-location

Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)


## G16-dc-function

What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)


## G17-matrix-markers

Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)


## G18-matrix-location

Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)


## G19-matrix-function

What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)


## G20-lyve1-markers

Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)


## G21-lyve1-location

Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)


## G22-lyve1-function

What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)


## G23-fibroblast-markers

Which genes mark fibroblast?


## G24-fibroblast-location

Where in prenatal human skin is fibroblast found?


## G25-fibroblast-function

What function does the paper attribute to fibroblast?


## G26-periderm-location

Where in prenatal human skin is periderm found?


## G27-periderm-function

What function does the paper attribute to periderm?


## G28-periderm-structure

What does the paper say about the structure or morphology of periderm?
