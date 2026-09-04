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


# Arm: local (single item)

## G06-macrophage-location

Where in prenatal human skin is macrophage found?

### Context

Human skin organogenesis begins after gastrulation from two primary germ layers. The epidermis, the most superficial layer of the skin, melanocytes and neural cells arise from the ectoderm. The dermis, which is separated from the epidermis by the basement membrane and contains endothelial and mural cells, derives from the mesoderm (apart from facial and cranial skin, where it arises from ectoderm-derived neural crest cells). The skin appendages, which include hair follicles (HFs) and sebaceous glands, form in a cephalocaudal direction. Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts), whereas sebaceous glands develop from around 16 PCW.

There is, however, a paucity of information about the precise cellular composition of human prenatal skin over these developmental periods and whether cells interact in functional microanatomical niches that support skin morphogenesis.

Prenatal skin interfaces with the amniotic fluid in a sterile environment. However, immune cells such as macrophages seed the skin as early as 6 PCW and express a range of pro-inflammatory genes, although genes relating to antigen presentation (for example, major histocompatibility complex class II (MHCII)) are only upregulated after 11 PCW. Decoupling of the expression of pro-inflammatory genes from MHCII genes before 11 PCW suggests that antigen presentation may not be a key function of human macrophages during early gestation. Together with evidence of their role in tissue homeostasis, and healing in mouse models,, this raises the question of whether macrophages contribute to human early skin morphogenesis.

Our current study provides a comprehensive multi-omics cell atlas of 7–17 PCW human prenatal skin. We profiled human prenatal skin using single-cell RNA sequencing (scRNA-seq), spatial transcriptomics and multiplex RNA in situ hybridization to decode the dynamic cellular and molecular changes across gestation that regulate skin and HF morphogenesis. We leveraged adult healthy skin and HF datasets, to compare and assess developmental-specific features that contribute to scarless skin healing and cues that guide de novo HF formation. We used a hair-bearing SkO model to validate the role of macrophages in prenatal skin vascular network formation.

This result suggests that for corresponding cell types, HF fibroblasts are in a more differentiated state in mouse compared to human prenatal skin. Additionally, dermal fibroblast differentiation into histologically defined subsets (papillary and reticular) has been reported to occur early in mice (about embryonic day 12.5). Our human prenatal skin fibroblasts did not significantly express papillary fibroblast markers (for example, COL13A1) (Extended Data Fig. 5j), which suggested that the distinction between papillary and reticular fibroblasts emerges after 17 PCW. These distinctions between human and mouse skin may be attributed to organismal differences in gestation lengths and tempo of differentiation. Cellular differentiation occurs at a quicker pace in mice, whereas the longer gestation period in humans permits more advanced maturation to take place in utero.

The role of macrophages in promoting wound healing has been described in postnatal mouse skin and in adult human skin. In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d). Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8). Interactions between macrophages and fibroblasts maintain tissue homeostasis in diverse organs such as spleen, peritoneum and heart. Our identification of additional growth factor interactions (IGF1–IGF1R and GRN–EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

We further compared prenatal skin fibroblasts and macrophages to their counterparts in reindeer skin from antlers, which heal without scarring, and in back skin, which scars. Early-gestation human skin fibroblasts had a higher probability of correspondence to pro-regenerative reindeer fibroblasts, whereas in later gestation, the probability of matching to pro-fibrotic fibroblasts was higher (Extended Data Fig. 8d and Supplementary Table 19). Accordingly, several pro-regenerative genes (for example, CRABP1 and MDK) were downregulated in late gestation prenatal skin (Extended Data Fig. 8e and Supplementary Table 20). Notably, prenatal skin macrophages resembled ‘early macrophages’ that are enriched in reindeer antler skin but not macrophages in back skin (Extended Data Fig. 8f and Supplementary Table 21).

Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring. Based on our data and previous studies, we also posit a potential role for early skin macrophages in conferring the distinct property of scarless healing in early prenatal skin. However, further studies are required to fully elucidate the interactions between macrophages and fibroblasts in human prenatal skin and to conclusively establish their role in scarless healing.

In this study, we characterized the dynamic composition of human prenatal skin during the early stages of de novo HF formation and highlighted the crucial skin immune and non-immune crosstalk that contributes to skin morphogenesis, results that are in line with emerging evidence in animal and human studies,. Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development. This is in part contributed to by yolk-sac derived TML macrophages, which suggests that these cells have broader functions outside the central nervous system in early gestation. The presence of TML macrophages has previously been identified in several prenatal organs,,.

A combination of fibroblast and macrophage-associated molecular features potentially contribute to the ability of prenatal skin to heal without scarring, including the presence of fibroblast progenitors, a downregulated immune milieu and reduced collagen expression. However, we found progressive ‘ageing’ and acquisition of the adult ‘pro-inflammatory’ phenotype as early as 9 PCW, which could be targeted in fibroblasts to guide postnatal scarless healing. Future studies that align human fibroblast subsets across the lifespan are required to investigate the dynamics of scarless healing and the roles of mechanical forces, microbiota and environmental exposure on fibroblast functions.

Our prenatal human skin atlas represents a valuable resource to explore genes that cause congenital hair and skin disorders and is freely accessible from our web portal (https://developmental.cellatlas.io/fetal-skin). We found that implicated genes are indeed expressed during prenatal skin development and HF differentiation, thereby supporting an in utero origin for these disorders. Our systematic prenatal skin–SkO comparison provides a blueprint to guide more faithful in vitro SkO generation, which can facilitate future studies of interactions with the microbiota, the pathogenesis of congenital skin disorders, and hair and skin engineering for therapeutic applications, including hair regeneration and skin transplant.
