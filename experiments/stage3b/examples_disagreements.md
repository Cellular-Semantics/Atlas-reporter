# Judged reads, for human review

Source paper: **gopee2024** — every quote below is text from this paper and
nothing else. The reader saw only the context block named under each case.

Each case had its outcome set by an Opus judge rather than by string matching.
The readers' quotes were machine-verified as verbatim before the judge saw them,
so the judge was ruling only on whether the answer *meant* the right thing.
In run 1 the judge was Opus grading Opus's own answers; that is the main reason
to check these by hand.

`verbatim` on a quote means it is an exact substring of that item's own context,
by the same test the scorer used. `leaked` means it is real text from the paper
that reached the reader through a different question batched with this one —
a flaw in how the batch was built, not a fabrication by the reader.

---

## Context: whole

### G03-placode-function — function, expect present

**Question** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Gold span** (paragraph 11 of 37)

> We evaluated hair matrix cells, which arise from the epidermal placode

**The gold span in its paragraph**

> ## Epidermal placode and matrix formation We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity ( …

**Opus/Fable** → `correct` — judge: *States initiation of hair follicle formation with the dermal condensate and origin of hair matrix cells; extra trajectory detail is additive.*

> The placode initiates hair follicle formation through interaction with the dermal condensate, and it gives rise to hair matrix cells; it lies on the IRS differentiation trajectory and receives migration/invasion-promoting signals from the Dc.

- *verbatim, paragraph 1 — **not the gold span's paragraph (11)***

  > Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

- *verbatim, paragraph 11 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs

- *verbatim, paragraph 12 — **not the gold span's paragraph (11)***

  > IRS trajectory, involving placode, matrix, cuticle/cortex and IRS

**Sonnet** → `substituted` — judge: *Quote is real but the answer describes Dc-to-placode ligand signalling rather than the placode's role in initiating hair follicle formation.*

> The placode expresses receptors (LAMP1/CXADR and EPHB6) for Dc-derived FAM3C and EFNB1, interactions reported to promote cell migration and invasion.

- *verbatim, paragraph 16 — **not the gold span's paragraph (11)***

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion, (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G09-wnt2fib-location — location, expect present

**Question** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Gold span** (paragraph 24 of 37)

> Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts

**The gold span in its paragraph**

> … e of macrophages in promoting wound healing has been described in postnatal mouse skin and in adult human skin. In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d). Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8). Interactions between macrophages and fibroblasts maintain tissue homeostasis in diverse organs such as s …

**Opus/Fable** → `correct` — judge: *Dermal, co-locating with LYVE1+ macrophages and with TML macrophages at 6-8 PCW, as intended.*

> WNT2+ fibroblasts are dermal fibroblasts of prenatal skin that become abundant in later gestation; they co-locate with LYVE1+ macrophages and, in early prenatal skin (6-8 PCW), with TML macrophages.

- *verbatim, paragraph 23 — **not the gold span's paragraph (24)***

  > The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation

- *verbatim, paragraph 24 — same paragraph as the gold span*

  > Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e)

- *verbatim, paragraph 25 — **not the gold span's paragraph (24)***

  > TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW) (Fig. 3c,d)

**Sonnet** → `miss`

> The supplied context does not state a spatial location for WNT2+ fibroblasts.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G10-wnt2fib-function — function, expect present

**Question** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Gold span** (paragraph 23 of 37)

> we observed differences within the WNT2+ fibroblast population across gestation time

**The gold span in its paragraph**

> … b). Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary  …

**Opus/Fable** → `correct` — judge: *Captures the early growth/differentiation to late ECM-collagen shift and acquisition of a senescent, pro-inflammatory adult-like profile.*

> WNT2+ fibroblasts form the dermal fibroblast branch of the fibroblast trajectory and shift function across gestation: early cells express growth and differentiation genes, whereas late cells deposit extracellular matrix and collagen and express senescence/cytokine genes characteristic of pathogenic fibrotic fibroblasts, linking them to the loss of scarless healing.

- *verbatim, paragraph 14 — **not the gold span's paragraph (23)***

  > the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

- *verbatim, paragraph 23 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

- *verbatim, paragraph 23 — same paragraph as the gold span*

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

- *verbatim, paragraph 24 — **not the gold span's paragraph (23)***

  > were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts

**Sonnet** → `miss`

> The supplied context does not explicitly attribute a function to WNT2+ fibroblasts; it only describes genes they upregulate at different gestational stages.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G19-matrix-function — function, expect present

**Question** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Gold span** (paragraph 11 of 37)

> increased expression of genes involved in chemotaxis, such as CXCL14

**The gold span in its paragraph**

> ## Epidermal placode and matrix formation We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f). Treg cells are known to localize around the HF  …

**Opus/Fable** → `correct` — judge: *Gives the CXCL14/CD24 chemotaxis and Treg immune-protection role; added differentiation detail is also supported.*

> Matrix cells differentiate along the IRS trajectory towards cuticle/cortex and inner root sheath, and prenatal matrix cells express chemotactic and immune-regulatory genes (CXCL14, CD24) suggesting a role in Treg cell recruitment and immune protection during early matrix differentiation. Their differentiation is coordinated by Dp-derived signals (RSPO3, WNT5A), with RSPO3-LGR4/LGR6 contributing to proliferation of hair follicle epithelial cells.

- *verbatim, paragraph 11 — same paragraph as the gold span*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).

- *verbatim, paragraph 14 — **not the gold span's paragraph (11)***

  > Formation of the Dp was characterized by genes (RSPO3 and WNT5A) (Extended Data Fig. 4f and Supplementary Table 7) that coordinate the differentiation of adjacent hair matrix cells,.

- *verbatim, paragraph 16 — **not the gold span's paragraph (11)***

  > Finally, RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells.

**Sonnet** → `substituted` — judge: *Grounded quote but answers with RSPO3-LGR proliferation signalling instead of the intended chemotaxis and immune-protection role.*

> Matrix cells are predicted to receive RSPO3 signalling from the dermal papilla via LGR4/LGR6, contributing to proliferation of HF epithelial cells.

- *verbatim, paragraph 16 — **not the gold span's paragraph (11)***

  > Finally, RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G23-fibroblast-markers — markers, expect present

**Question** Which genes mark fibroblast?

**Intended answer** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Gold span** (paragraph 22 of 37)

> prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200)

**The gold span in its paragraph**

> … sets expressed high levels of inflammatory cytokines and receptors (for example, IL6 and IL1RA) and genes involved in antigen presentation (for example, HLA-A), innate immune and inflammatory responses (for example, CD55 and PTGES) and cellular senescence (CDKN1A) (Fig. 3a and Supplementary Tables 13-15). By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13-15).

**Hazard note given to the judge** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Opus/Fable** → `correct` — judge: *Subset-specific marker answer is licensed by the hazard note and it captures the COL13A1-negative point.*

> Prenatal skin fibroblast subsets are defined by HOXC5 (early fibroblasts), WNT2, PEAR1 and FRZB; hair-specialized fibroblasts are marked by PDGFRA/FOXD1/SOX2low (pre-Dc), FOXD1+SOX2+ (Dc) and NDP+SOX2+ (Dp). Human prenatal fibroblasts did not significantly express the papillary fibroblast marker COL13A1.

- *verbatim, paragraph 14 — **not the gold span's paragraph (22)***

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

- *verbatim, paragraph 13 — **not the gold span's paragraph (22)***

  > In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,.

- *verbatim, paragraph 13 — **not the gold span's paragraph (22)***

  > Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).

- *verbatim, paragraph 18 — **not the gold span's paragraph (22)***

  > Our human prenatal skin fibroblasts did not significantly express papillary fibroblast markers (for example, COL13A1) (Extended Data Fig. 5j), which suggested that the distinction between papillary and reticular fibroblasts emerges after 17 PCW.

**Sonnet** → `miss`

> The supplied context does not give marker genes for fibroblasts as a general cell type (only for specific fibroblast subsets).

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G25-fibroblast-function — function, expect present

**Question** What function does the paper attribute to fibroblast?

**Intended answer** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Gold span** (paragraph 27 of 37)

> may favour tissue regeneration over scarring

**The gold span in its paragraph**

> ## Scarless healing and potential macrophage contribution Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring. Based on our data and previous studies, we also posit a potential role for early skin macrophages in conferring the distinct property of scarless healing in early prenatal skin. However, further studies are required to fully elucidate the interactions between macrophages and fibroblasts in human prenatal skin and to  …

**Opus/Fable** → `correct` — judge: *States the regeneration-over-scarring conclusion with the ECM/collagen/inflammation downregulation.*

> Fibroblasts produce the collagen whose aggregation causes scars, and prenatal fibroblasts instead upregulate immune suppression, inflammation regulation and tissue regeneration genes, which may favour scarless healing before they progressively acquire scar-promoting, pro-inflammatory profiles in later gestation. Hair-specialized fibroblasts also drive hair follicle morphogenesis through crosstalk with epidermal cells, including CXCL12-ACKR3-mediated pre-Dc migration.

- *verbatim, paragraph 22 — **not the gold span's paragraph (27)***

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.

- *verbatim, paragraph 22 — **not the gold span's paragraph (27)***

  > By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13–15).

- *verbatim, paragraph 27 — same paragraph as the gold span*

  > Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

- *verbatim, paragraph 13 — **not the gold span's paragraph (27)***

  > We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c).

**Sonnet** → `substituted` — judge: *Quote is real background about scarring but the answer is a different claim than the paper's finding on early fibroblast downregulation of ECM and inflammation.*

> The paper attributes collagen production to dermal fibroblasts, noting that aggregation of this collagen (along with failed epidermal regeneration) is what produces scars.

- *verbatim, paragraph 22 — **not the gold span's paragraph (27)***

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G32-dpysl2-function — function, expect present

**Question** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Gold span** (paragraph 12 of 37)

> ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL

**The gold span in its paragraph**

> ## Epidermal placode and matrix formation Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Exten …

**Opus/Fable** → `correct` — judge: *Places the cell type on the ORS/CL trajectory downstream of POSTN+ basal cells as intended.*

> DPYSL2+ basal cells are an intermediate state on the ORS/CL differentiation trajectory downstream of POSTN+ basal cells, upregulating AGR2 and genes related to outer root sheath differentiation.

- *verbatim, paragraph 12 — same paragraph as the gold span*

  > predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL

- *verbatim, paragraph 12 — same paragraph as the gold span*

  > we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)

**Sonnet** → `miss`

> The supplied context does not state a function for DPYSL2+ basal cells; it only notes them as a marker-defined mature basal cell population and mentions AGR2 (a gene they upregulate) promoting cell migration, but no function is attributed to the DPYSL2+ basal cells themselves.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G33-caparteriole-markers — markers, expect present

**Question** Which genes mark capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer** Arteriolar identity is marked by GJA5. In the organoid comparison, KDR and FLT1 (VEGF receptors) and the GATA2/NFATC1 regulons with targets such as VWF are downregulated in SkO capillary arterioles relative to prenatal skin.

**Gold span** (paragraph 32 of 37)

> their receptors (KDR and FLT1) on SkO capillary arterioles were downregulated compared to prenatal skin

**The gold span in its paragraph**

> … re highly expressed in SkO, whereas pro-angiogenic genes (for example, CXCL8) were upregulated in prenatal skin and primarily expressed by macrophages (Extended Data Fig. 11a and Supplementary Tables 30-34). Although expression of vascular endothelial growth factors (VEGF), VEGFA and VEGFB were increased in SkO cells, their receptors (KDR and FLT1) on SkO capillary arterioles were downregulated compared to prenatal skin (Extended Data Fig. 11b,c). These receptors are known downstream targets of GATA2, which has a key role in angiogenesis during development and regulates VEGF-induced endothelial cell migration and sprouting in vitro. Regulon analysis showed that GATA2 and related regulons (for example, NFATC1) were downregulated in Sk …

**Opus/Fable** → `miss`

> The supplied context does not give marker genes specific to capillary arteriole cells.

*No quotes given.*

**Sonnet** → `correct` — judge: *GJA5 arteriolar identity is accurate, a partial answer omitting the organoid comparison genes.*

> Capillary arterioles belong to the arteriolar differentiation pathway, characterised by expression of GJA5.

- *verbatim, paragraph 30 — **not the gold span's paragraph (32)***

  > early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a–c).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G55-cuticle-cortex-structure-absent — structure, expect absent

**Question** What does the paper say about the structure or morphology of cuticle/cortex? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer** decline — the paper says nothing about this cell type's structure or morphology.

**Opus/Fable** → `correct` — judge: *Notes the statement is merely positional and says no morphological detail is given.*

> The only structural statement is positional: cuticle and cortex cells are described as forming part of the inner layers of the hair follicle. No morphological detail beyond this is given.

- *verbatim, paragraph 10*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

**Sonnet** → `overreach` — judge: *Offers a positional statement as a structural description without noting that morphology is not described.*

> Cuticle/cortex cells are described as part of the inner layers of the hair follicle.

- *verbatim, paragraph 10*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

## Context: local

### G03-placode-function — function, expect present

**Question** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Gold span** (paragraph 2 of 11)

> We evaluated hair matrix cells, which arise from the epidermal placode

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity ( …

**Opus/Fable** → `correct` — judge: *Names the placode as origin of hair matrix cells, WNT/EDA specification and dermal condensate signalling during invagination, matching the intended answer.*

> The placode is the epidermal origin of hair matrix cells and the first step of the IRS differentiation trajectory; its specification is linked to increased cellular migration in POSTN+ basal cells and to WNT and EDA signalling, and it receives dermal condensate signals (FAM3C and EFNB1 acting on LAMP1/CXADR and EPHB6) as invagination proceeds.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e).

- *verbatim, paragraph 3 — **not the gold span's paragraph (2)***

  > IRS trajectory, involving placode, matrix, cuticle/cortex and IRS

- *verbatim, paragraph 4 — **not the gold span's paragraph (2)***

  > Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

- *verbatim, paragraph 9 — **not the gold span's paragraph (2)***

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode

- *verbatim, paragraph 10 — **not the gold span's paragraph (2)***

  > Similar signalling pathways were upregulated, including WNT and EDA for hair placode specification

**Sonnet** → `substituted` — judge: *Quotes are real but the answer is about Dc and Dp signalling rather than the placode initiating hair follicle formation.*

> The Dc's interaction with the placode (via FAM3C/EFNB1 and receptors on the placode) has been reported to promote cell migration and invasion, and RSPO3 from the dermal papilla interacts with matrix cells overlying the placode to contribute to proliferation of HF epithelial cells, which includes the placode-derived matrix.

- *verbatim, paragraph 9 — **not the gold span's paragraph (2)***

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G03-placode-function.txt`*

---

### G09-wnt2fib-location — location, expect present

**Question** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Gold span** (paragraph 7 of 10)

> Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts

**The gold span in its paragraph**

> … e of macrophages in promoting wound healing has been described in postnatal mouse skin and in adult human skin. In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d). Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8). Interactions between macrophages and fibroblasts maintain tissue homeostasis in diverse organs such as s …

**Opus/Fable** → `correct` — judge: *Dermal location with LYVE1+ macrophage co-location is accurate; omitting the TML co-location is a permitted partial.*

> They are a dermal fibroblast subset, arising on the dermal fibroblast trajectory and abundant after 11 PCW; spatially they are described by co-location with LYVE1+ macrophages. The context gives no finer dermal compartment (e.g. upper versus lower dermis) for them.

- *verbatim, paragraph 1 — **not the gold span's paragraph (7)***

  > the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e)

**Sonnet** → `miss`

> The supplied context does not give a spatial location for WNT2+ fibroblasts, only their temporal abundance and gene expression.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G09-wnt2fib-location.txt`*

---

### G16-dc-function — function, expect present

**Question** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Gold span** (**not in this context** — the retriever never supplied it)

> have been reported to promote cell migration and invasion

**Opus/Fable** → `correct` — judge: *Conveys aggregation from pre-Dc cells and dermal-epidermal crosstalk in hair follicle development; omission of FAM3C/EFNB1 migration detail is a partial, not an error.*

> The Dc is presented as a hair-follicle-specialised dermal population that takes part in dermal–epidermal crosstalk during hair follicle development: it forms by aggregation of pre-Dc cells next to the epithelial hair placode and subsequently becomes the dermal papilla, which expresses genes coordinating differentiation of adjacent hair matrix cells.

- *verbatim, paragraph 7*

  > We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c).

- *verbatim, paragraph 7*

  > Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).

- *verbatim, paragraph 9*

  > Genes implicated in collagen fibril formation and cell adhesion (COL6A3, MFAP4 and PTK7) were expressed as the pre-Dc cells aggregated into the Dc (Extended Data Fig. 4f and Supplementary Table 7).

**Sonnet** → `honest_miss`

> The supplied context describes formation and origin of the dermal condensate but does not state a function attributed to it.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G16-dc-function.txt`*

---

### G18-matrix-location — location, expect present

**Question** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Gold span** (paragraph 4 of 11)

> a prenatal-specific cell state absent in established adult HFs

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell a …

**Opus/Fable** → `miss`

> The supplied context does not state where in prenatal skin hair matrix cells are located; it only says they arise from the epidermal placode and are a prenatal-specific state absent from established adult hair follicles.

*No quotes given.*

**Sonnet** → `correct` — judge: *Placode origin and prenatal-specific state are accurate; omitting 14 PCW is only detail.*

> Hair matrix cells arise from the epidermal placode and are a prenatal-specific cell state not found in established adult hair follicles.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G18-matrix-location.txt`*

---

### G23-fibroblast-markers — markers, expect present

**Question** Which genes mark fibroblast?

**Intended answer** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Gold span** (paragraph 7 of 10)

> prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200)

**The gold span in its paragraph**

> By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13-15).

**Hazard note given to the judge** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Opus/Fable** → `correct` — judge: *Per the hazard note a subset-specific answer is legitimate; the HOXC5/WNT2/PEAR1 markers are accurate for this paper's fibroblast subsets and it also states the COL13A1 negative from the intended answer.*

> The context gives no general marker set for fibroblasts as a class; it instead names genes that label particular prenatal skin fibroblast subsets or states — HOXC5 for the common early fibroblast progenitor, and WNT2 and PEAR1 for the two subsets that carry the adult-like expression profile. It also notes that the papillary fibroblast marker COL13A1 was not significantly expressed in these prenatal fibroblasts.

- *verbatim, paragraph 3 — **not the gold span's paragraph (7)***

  > pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation

- *verbatim, paragraph 4 — **not the gold span's paragraph (7)***

  > Our human prenatal skin fibroblasts did not significantly express papillary fibroblast markers (for example, COL13A1)

**Sonnet** → `substituted` — judge: *Quote is real but concerns gene therapy relevance of COL7A1, not the paper's fibroblast marker profile.*

> Fibroblasts expressing COL7A1 are noted, with COL7A1 expression observed across several fibroblast subsets in prenatal skin and SkOs.

- *verbatim, paragraph 5 — **not the gold span's paragraph (7)***

  > Gene therapy studies for dystrophic EB have identified fibroblasts expressing COL7A1 as a promising therapeutic strategy. We observed COL7A1 expression across several fibroblast subsets in prenatal skin and SkOs (Extended Data Fig. 6d), which lends support to the gene therapy approaches.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G23-fibroblast-markers.txt`*

---

### G25-fibroblast-function — function, expect present

**Question** What function does the paper attribute to fibroblast?

**Intended answer** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Gold span** (**not in this context** — the retriever never supplied it)

> may favour tissue regeneration over scarring

**Opus/Fable** → `correct` — judge: *States early fibroblasts downregulate ECM/collagen programs favouring scarless healing, the intended point.*

> Fibroblasts are attributed roles in extracellular matrix and collagen deposition (and hence scarring, which early prenatal fibroblasts avoid by downregulating these programs), and hair-specialized fibroblasts coordinate hair follicle formation, including differentiation of adjacent hair matrix cells.

- *verbatim, paragraph 7*

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.

- *verbatim, paragraph 8*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16–18).

- *verbatim, paragraph 2*

  > Formation of the Dp was characterized by genes (RSPO3 and WNT5A) (Extended Data Fig. 4f and Supplementary Table 7) that coordinate the differentiation of adjacent hair matrix cells,.

- *verbatim, paragraph 9*

  > A combination of fibroblast and macrophage-associated molecular features potentially contribute to the ability of prenatal skin to heal without scarring, including the presence of fibroblast progenitors, a downregulated immune milieu and reduced collagen expression.

**Sonnet** → `leaked`

> Fibroblasts (in early gestation) downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring; combined with macrophage interactions, this contributes to scarless healing.

- ***leaked** — from another question's context*

  > Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G25-fibroblast-function.txt`*

---

### G55-cuticle-cortex-structure-absent — structure, expect absent

**Question** What does the paper say about the structure or morphology of cuticle/cortex? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer** decline — the paper says nothing about this cell type's structure or morphology.

**Opus/Fable** → `correct_decline`

> The supplied context does not describe the structure or morphology of cuticle/cortex cells; it names them among the identified hair follicle cell types and places them on the IRS trajectory, without any morphological description.

*No quotes given.*

**Sonnet** → `overreach` — judge: *Offers a location statement as a structural description without declining.*

> The paper describes cuticle/cortex cells as part of the inner layers of the hair follicle.

- *verbatim, paragraph 6*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G55-cuticle-cortex-structure-absent.txt`*

---

## Context: local-comb

### G15-dc-location — location, expect present

**Question** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Gold span** (paragraph 8 of 11)

> Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW

**The gold span in its paragraph**

> Accordingly, sebocyte progenitors are present from day 133 of SkO differentiation. Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

**Opus/Fable** → `correct` — judge: *Names the dermal compartment from 12 PCW; omitting the placode adjacency is a permissible partial.*

> The dermal condensate is found in the dermal compartment of prenatal skin, as an aggregate of dermal fibroblasts, observed from 12 PCW.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

- *verbatim, paragraph 1 — **not the gold span's paragraph (8)***

  > initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

**Sonnet** → `leaked`

> The dermal condensate is found within the dermal compartment of prenatal skin, first observed from 12 PCW, and it abuts the epithelial hair placode.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW

- ***leaked** — from another question's context*

  > the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G15-dc-location.txt`*

---

### G18-matrix-location — location, expect present

**Question** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Gold span** (paragraph 6 of 11)

> a prenatal-specific cell state absent in established adult HFs

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell a …

**Opus/Fable** → `correct` — judge: *Places matrix in the hair follicle arising from the placode, from 14 PCW, as intended.*

> Hair matrix cells are part of the hair follicle: they arise from the epidermal placode and are identified among the hair follicle cell states present from 14 PCW.

- *verbatim, paragraph 5 — **not the gold span's paragraph (6)***

  > we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs

**Sonnet** → `miss`

> The supplied context states that hair matrix cells arise from the epidermal placode but does not give their spatial location within prenatal skin.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G18-matrix-location.txt`*

---

### G23-fibroblast-markers — markers, expect present

**Question** Which genes mark fibroblast?

**Intended answer** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Gold span** (**not in this context** — the retriever never supplied it)

> prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200)

**Hazard note given to the judge** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Opus/Fable** → `correct` — judge: *Subset-specific markers are legitimate for this broad label per the hazard note.*

> The context gives no single pan-fibroblast marker, but prenatal skin fibroblast subsets are distinguished by marker genes: FRZB (FRZB+ fibroblasts), HOXC5 (HOXC5+ early fibroblasts), and WNT2 and PEAR1 (WNT2+ and PEAR1+ fibroblasts).

- *verbatim, paragraph 1*

  > We excluded FRZB+ fibroblasts, which were primarily observed in one sample from the earliest gestation stage (7 PCW)

- *verbatim, paragraph 1*

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

**Sonnet** → `honest_miss`

> The supplied context does not say. It only lists markers for specific fibroblast subsets (e.g. HOXC5+, WNT2+, PEAR1+, FRZB+), not a generic fibroblast marker.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G23-fibroblast-markers.txt`*

---

### G25-fibroblast-function — function, expect present

**Question** What function does the paper attribute to fibroblast?

**Intended answer** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Gold span** (paragraph 7 of 9)

> may favour tissue regeneration over scarring

**The gold span in its paragraph**

> Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring. Based on our data and previous studies, we also posit a potential role for early skin macrophages in conferring the distinct property of scarless healing in early prenatal skin. However, further studies are required to fully elucidate the interactions between macrophages and fibroblasts in human prenatal skin and to  …

**Opus/Fable** → `correct` — judge: *States the early-gestation downregulation of ECM/collagen/inflammation favouring regeneration.*

> Dermal fibroblasts produce collagen, whose aggregation causes scarring; early prenatal fibroblasts downregulate extracellular matrix, collagen and inflammation genes, which may favour scarless tissue regeneration, and later-gestation WNT2+ fibroblasts upregulate extracellular matrix and collagen deposition genes.

- *verbatim, paragraph 5 — **not the gold span's paragraph (7)***

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Sonnet** → `substituted` — judge: *Quote is real but describes scar formation generally rather than the paper's claim about early-gestation downregulation favouring regeneration.*

> Dermal fibroblasts produce the collagen that aggregates to form scars when the overlying epidermis fails to regenerate.

- *verbatim, paragraph 5 — **not the gold span's paragraph (7)***

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G25-fibroblast-function.txt`*

---

### G28-periderm-structure — structure, expect present

**Question** What does the paper say about the structure or morphology of periderm?

**Intended answer** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Gold span** (paragraph 6 of 11)

> consisted of a layer of epidermal cells overlying the dermal stroma

**The gold span in its paragraph**

> Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

**Hazard note given to the judge** thin - a layer description and a sloughing observation, not morphology proper

**Opus/Fable** → `correct` — judge: *Conveys the thin layer description plus sloughing from 11 PCW that the paper offers.*

> Histologically the periderm is described as being seen sloughing from 11 PCW, overlying the layer of epidermal cells of early prenatal skin, and it is counted among the immature interfollicular epidermal cells.

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

- *verbatim, paragraph 7 — **not the gold span's paragraph (6)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

**Sonnet** → `miss`

> The supplied context does not describe the structure or morphology of the periderm, only its function and the timing of its sloughing.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G28-periderm-structure.txt`*

---

### G32-dpysl2-function — function, expect present

**Question** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Gold span** (paragraph 8 of 10)

> ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL

**The gold span in its paragraph**

> Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Exten …

**Opus/Fable** → `correct` — judge: *Places the cells on the ORS/CL trajectory towards ORS and companion layer, with correct attribution of BARX2/SOX9 as ORS-differentiation genes.*

> DPYSL2+ (mature) basal cells lie on the ORS/CL differentiation trajectory, where they upregulate new genes such as AGR2 and genes related to outer root sheath differentiation (BARX2 and SOX9), indicating a role in differentiating towards the outer root sheath and companion layer.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Extended Data Fig. 4b,c and Supplementary Table 7).

**Sonnet** → `miss`

> The supplied context does not attribute a specific function to DPYSL2+ basal cells; it only describes their place in the ORS/CL differentiation trajectory and genes they upregulate.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G32-dpysl2-function.txt`*

---

### G35-pear1-markers — markers, expect present

**Question** Which genes mark PEAR1+ fibroblast?

**Intended answer** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Gold span** (paragraph 7 of 10)

> were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

**The gold span in its paragraph**

> The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b). Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extrace …

**Opus/Fable** → `miss`

> The supplied context does not state which genes mark PEAR1+ fibroblasts; it only describes genes upregulated during the transition into them and genes shared with WNT2+ fibroblasts, not defining markers.

*No quotes given.*

**Sonnet** → `correct` — judge: *APOE, IGFBP7, ITM2A in the HOXC5+ transition plus the shared senescence/collagen genes.*

> PEAR1+ fibroblasts upregulate a pro-inflammatory phenotype including APOE, IGFBP7 and ITM2A during their transition from HOXC5+ fibroblasts, and (together with WNT2+ fibroblasts) express CDKN1A, IL1R1 and POSTN.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G35-pear1-markers.txt`*

---

### G36-pear1-function — function, expect present

**Question** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Gold span** (paragraph 1 of 10)

> formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

**The gold span in its paragraph**

> … lysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

**Opus/Fable** → `correct` — judge: *Later-gestation adult pro-inflammatory profile with senescence and collagen deposition genes.*

> PEAR1+ fibroblasts, abundant in later gestation, acquire an adult pro-inflammatory, scar-promoting profile, expressing genes involved in cellular senescence, cytokine pathways and collagen deposition that are characteristic of pathogenic fibroblasts in fibrotic skin disorders.

- *verbatim, paragraph 8 — **not the gold span's paragraph (1)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

- *verbatim, paragraph 7 — **not the gold span's paragraph (1)***

  > The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b).

**Sonnet** → `miss`

> The supplied context does not say. It describes PEAR1+ fibroblasts in terms of gene expression changes (senescence, cytokine pathway, collagen deposition genes) and their emergence after 11 PCW, but does not state a specific function attributed to them.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G36-pear1-function.txt`*

---

### G40-arteriole-function — function, expect present

**Question** What function does the paper attribute to arteriole?

**Intended answer** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 7 of 10)

> differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles)

**The gold span in its paragraph**

> …  fewer and less heterogeneous endothelial cells in the immunodeficient SkOs compared to prenatal skin, despite the formation of well-developed HFs, epidermis and neural cells (Fig. 4b,c, Extended Data Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig …

**Opus/Fable** → `correct` — judge: *Accurate partial: names the tip-cell sprouting angiogenesis potential attributed to arterioles.*

> The paper attributes sprouting angiogenesis potential to prenatal skin arteriole cells: they showed an increased 'tip' cell state score, indicating capacity for new blood vessel growth.

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > However, sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).

**Sonnet** → `miss`

> The supplied context does not describe a function for arteriole itself; it only describes arterioles as an endpoint of the differentiation trajectory of endothelial cells.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G40-arteriole-function.txt`*

---

## Context: asta-sep

### G03-placode-function — function, expect present

**Question** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Gold span** (**not in this context** — the retriever never supplied it)

> We evaluated hair matrix cells, which arise from the epidermal placode

**Opus/Fable** → `correct` — judge: *Names the main point - the placode is the epithelial partner instructing early hair follicle formation - accurate though partial.*

> The context describes the placode only as the epithelial partner in the mesenchymal-epithelial interactions that instruct early hair follicle formation, bearing receptors (LAMP1 or CXADR and EPHB6) for Dc-derived ligands reported to promote cell migration and invasion.

- *verbatim, paragraph 5*

  > We explored the mesenchymal-epithelial interactions that instruct early HF formation.

- *verbatim, paragraph 5*

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion

**Sonnet** → `substituted` — judge: *Quote is real but describes Dc-to-placode signalling, not the placode's role in initiating hair follicle formation.*

> The placode is a site of ligand-receptor signalling (via EPHB6, among others) that is reported to promote cell migration and invasion.

- *verbatim, paragraph 5*

  > EPHB6 on the placode, and have been reported to promote cell migration and invasion

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G03-placode-function.txt`*

---

### G05-macrophage-markers — markers, expect present

**Question** Which genes mark macrophage?

**Intended answer** MHCII genes (upregulated only after 11 PCW), TREM2 on the microglia-like subset with P2RY12, CX3CR1 and OLFML3; GAS6 and VEGFA and CXCL8 also macrophage-expressed.

**Gold span** (paragraph 9 of 9)

> share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages

**The gold span in its paragraph**

> We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads 57,58 (Extended Data Fig. 7e,f). Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory recep …

**Hazard note given to the judge** broad label; four subsets each have their own markers

**Opus/Fable** → `correct` — judge: *Correctly notes there is no pan-macrophage panel and gives subset-level markers, as the hazard anticipates.*

> The context gives no pan-macrophage marker list; it names the genes that define subsets - TREM2 with a P2RY12, CX3CR1 and OLFML3 microglia-like profile, and LYVE1, MHCII and iron-recycling subsets.

- *verbatim, paragraph 9 — same paragraph as the gold span*

  > We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads 57,58 (Extended Data Fig. 7e,f).

- *verbatim, paragraph 2 — **not the gold span's paragraph (9)***

  > Gene ontology analysis showed that the four macrophage subsets (LYVE1 + , MHCII + , TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26).

**Sonnet** → `miss`

> The supplied context does not list specific genes marking macrophages generally; it only refers to unnamed 'marker genes' used to annotate macrophage subsets without naming them.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G05-macrophage-markers.txt`*

---

### G17-matrix-markers — markers, expect present

**Question** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** SHH, and WNT10B; both described as known matrix markers.

**Gold span** (**not in this context** — the retriever never supplied it)

> known matrix markers such as SHH and WNT10B, were upregulated

**Hazard note given to the judge** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Opus/Fable** → `correct` — judge: *Gives SHH as the annotating marker; the added CXCL14/CD24 comparison is supported and does not misstate the paper.*

> The matrix population is annotated as SHH+; relative to adult hair follicles, prenatal matrix cells also show increased CXCL14 and CD24 expression.

- *verbatim, paragraph 10*

  > Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

- *verbatim, paragraph 4*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .

**Sonnet** → `substituted` — judge: *SHH is right but CXCL14 and CD24 are presented as markers when the quote gives them as chemotaxis/autoimmunity genes raised versus adult.*

> Hair matrix cells are marked by SHH, and matrix-specific genes include CXCL14 and CD24, which are increased compared with adult hair follicles.

- *verbatim, paragraph 10*

  > which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).

- *verbatim, paragraph 4*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G17-matrix-markers.txt`*

---

### G20-lyve1-markers — markers, expect present

**Question** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** LYVE1; also expresses GAS6.

**Gold span** (**not in this context** — the retriever never supplied it)

> GAS6, expressed by TML macrophages and LYVE1+ macrophages

**Hazard note given to the judge** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Opus/Fable** → `correct` — judge: *Correctly reports LYVE1 plus GAS6 and flags the thin body-text evidence, as the hazard anticipates.*

> The supplied context gives no marker gene list for this subset beyond the defining LYVE1 label; the only gene it explicitly states is expressed by LYVE1+ macrophages is GAS6.

- *verbatim, paragraph 5*

  > Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts

**Sonnet** → `substituted` — judge: *Quotes are antibody-panel method lines; CD45/CD31 are staining reagents, not markers of this subset, and GAS6 is missed.*

> The paper identifies LYVE1+ macrophages by LYVE1 protein expression, using anti-LYVE1 immunofluorescence/RNAscope staining alongside other markers such as CD45 and CD31 to detect these cells.

- *verbatim, paragraph 7*

  > n = 1 biological replicate with n = 2 technical replicates for immunofluorescence slides with anti-LYVE1, anti-CD45 and anti-VIM (Fig. 3e)

- *verbatim, paragraph 7*

  > n = 3 biological replicates for prenatal skin whole-mount immunofluorescence with anti-CD31 and anti-LYVE1 (Fig. 4a)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G20-lyve1-markers.txt`*

---

### G23-fibroblast-markers — markers, expect present

**Question** Which genes mark fibroblast?

**Intended answer** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Gold span** (paragraph 5 of 9)

> prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200)

**The gold span in its paragraph**

> … sets expressed high levels of inflammatory cytokines and receptors (for example, IL6 and IL1RA) and genes involved in antigen presentation (for example, HLA-A), innate immune and inflammatory responses (for example, CD55 and PTGES) and cellular senescence (CDKN1A) (Fig. 3a and Supplementary Tables 13-15). By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13-15).

**Hazard note given to the judge** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Opus/Fable** → `correct` — judge: *Legitimately subset-specific per the hazard, and correctly states no general panel is given.*

> The context does not give a general fibroblast marker panel; it reports PDGFRalpha and PDGFRbeta receptors expressed on fibroblasts, and subset-level genes such as COL1A1, SFRP1, CDKN1A, IL1R1 and POSTN in WNT2+ and PEAR1+ prenatal fibroblasts.

- *verbatim, paragraph 4 — **not the gold span's paragraph (5)***

  > Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).

- *verbatim, paragraph 3 — **not the gold span's paragraph (5)***

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b)

**Sonnet** → `miss`

> The supplied context does not say which genes generically mark fibroblasts; it only discusses genes specific to particular fibroblast subsets (e.g. WNT2+, PEAR1+, HOXC5+).

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G23-fibroblast-markers.txt`*

---

### G25-fibroblast-function — function, expect present

**Question** What function does the paper attribute to fibroblast?

**Intended answer** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Gold span** (**not in this context** — the retriever never supplied it)

> may favour tissue regeneration over scarring

**Opus/Fable** → `correct` — judge: *Conveys the reduced collagen/inflammation early profile favouring scarless healing.*

> Fibroblasts are attributed extracellular matrix and collagen deposition (in late gestation WNT2 + fibroblasts) versus cellular growth and differentiation programmes in early gestation, and fibroblast features are proposed to underlie the capacity of prenatal skin to heal without scarring.

- *verbatim, paragraph 1*

  > Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

- *verbatim, paragraph 5*

  > A combination of fibroblast and macrophage-associated molecular features potentially contribute to the ability of prenatal skin to heal without scarring, including the presence of fibroblast progenitors, a downregulated immune milieu and reduced collagen expression.

**Sonnet** → `leaked`

> Prenatal skin fibroblasts are attributed roles in immune suppression, regulation of inflammation, and tissue regeneration, based on upregulated genes CD200, RAMP2 and MDK.

- ***leaked** — from another question's context*

  > prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G25-fibroblast-function.txt`*

---

### G32-dpysl2-function — function, expect present

**Question** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Gold span** (**not in this context** — the retriever never supplied it)

> ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL

**Opus/Fable** → `correct` — judge: *Places the cell on the ORS/CL differentiation trajectory as intended, with accurate supporting detail.*

> DPYSL2+ (mature) basal cells sit on the ORS/CL differentiation trajectory, upregulating AGR2 and outer root sheath differentiation genes (BARX2, SOX9), and they increase in the interfollicular epidermis after 11 PCW.

- *verbatim, paragraph 1*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26 (Extended Data Fig. 4b,c and Supplementary Table 7).

- *verbatim, paragraph 4*

  > Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).

**Sonnet** → `honest_miss`

> The supplied context describes DPYSL2+ basal cells' place in a differentiation trajectory and their upregulated genes, but does not attribute a specific function to them.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G32-dpysl2-function.txt`*

---

### G37-postn-location — location, expect present

**Question** Where in prenatal human skin is POSTN+ basal cell found? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer** Basal epidermis; present throughout gestation, unlike mature DPYSL2+ basal and suprabasal IFE cells which increase after 11 PCW.

**Gold span** (**not in this context** — the retriever never supplied it)

> whereas POSTN+ basal cells were present throughout gestation

**Opus/Fable** → `correct` — judge: *Epidermal basal cells present throughout gestation, contrasted with DPYSL2+ mature basal after 11 PCW.*

> The context places POSTN+ basal cells among the epidermal basal cells and states they are present throughout gestation, unlike mature basal and suprabasal IFE cells that increase after 11 PCW; no finer spatial compartment is given.

- *verbatim, paragraph 4*

  > Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).

**Sonnet** → `honest_miss`

> The supplied context only states when POSTN+ basal cells are present (throughout gestation), not their spatial location.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G37-postn-location.txt`*

---

### G40-arteriole-function — function, expect present

**Question** What function does the paper attribute to arteriole?

**Intended answer** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 1 of 9)

> differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles)

**The gold span in its paragraph**

> …  fewer and less heterogeneous endothelial cells in the immunodeficient SkOs compared to prenatal skin, despite the formation of well-developed HFs, epidermis and neural cells (Fig. 4b,c, Extended Data Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig …

**Opus/Fable** → `correct` — judge: *Partial but accurate: names the tip-cell sprouting angiogenesis role, omitting only the pathway-endpoint framing.*

> Prenatal skin arterioles are among the endothelial cell types scored as having increased sprouting angiogenesis ('tip' cell state) potential, i.e. a role in new blood vessel formation.

- *verbatim, paragraph 2 — **not the gold span's paragraph (1)***

  > However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).

**Sonnet** → `miss`

> The supplied context does not attribute a specific function to arteriole cells themselves; it discusses their differentiation trajectory and marker genes but no functional role.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G40-arteriole-function.txt`*

---

### G45-dermal-condensate-structure-absent — structure, expect absent

**Question** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** decline — the paper says nothing about this cell type's structure or morphology.

**Opus/Fable** → `correct_decline`

> The supplied context does not describe the structure or morphology of the dermal condensate itself.

*No quotes given.*

**Sonnet** → `overreach` — judge: *Presents abutting the placode and encapsulation as a structural description where the paper offers no morphology.*

> The dermal condensate is described structurally as abutting the epithelial hair placode, and after HF invagination it becomes encapsulated at its base to form the dermal papilla.

- *verbatim, paragraph 1*

  > which abuts the epithelial hair placode

- *verbatim, paragraph 1*

  > the Dc becomes encapsulated at its base as the Dp

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G45-dermal-condensate-structure-absent.txt`*

---

### G55-cuticle-cortex-structure-absent — structure, expect absent

**Question** What does the paper say about the structure or morphology of cuticle/cortex? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer** decline — the paper says nothing about this cell type's structure or morphology.

**Opus/Fable** → `correct_decline`

> The supplied context does not describe the structure or morphology of cuticle/cortex cells.

*No quotes given.*

**Sonnet** → `overreach` — judge: *Offers a location statement as the structural description without flagging that morphology is absent.*

> The paper describes cuticle/cortex cells as part of the inner layers of the hair follicle.

- *verbatim, paragraph 3*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G55-cuticle-cortex-structure-absent.txt`*

---

## Context: asta-comb

### G02-placode-location — location, expect present

**Question** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Gold span** (**not in this context** — the retriever never supplied it)

> which abuts the epithelial hair placode

**Opus/Fable** → `correct` — judge: *Locates the placode in the epidermal basal layer as budding basal cells, consistent with the intended answer.*

> The hair placode appears in the epidermal basal layer of prenatal skin as budding basal cells, observed histologically at 14-15 PCW, with HF cells including placode detected in scRNA-seq from 14 PCW.

- *verbatim, paragraph 2*

  > At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).

- *verbatim, paragraph 3*

  > Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).

**Sonnet** → `substituted` — judge: *Quote is real but answers timing/morphogenesis rather than where the placode sits in the epidermis.*

> Hair placode was observed at 14-15 PCW as budding of basal cells, elongating into hair follicles.

- *verbatim, paragraph 2*

  > At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G02-placode-location.txt`*

---

### G03-placode-function — function, expect present

**Question** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Gold span** (paragraph 8 of 8)

> We evaluated hair matrix cells, which arise from the epidermal placode

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoi …

**Opus/Fable** → `correct` — judge: *States matrix cells arise from the placode and it initiates the IRS trajectory with Dc crosstalk; omits only WNT/EDA.*

> The placode is the prenatal-specific epidermal cell state that gives rise to hair matrix cells and sits on the inner root sheath differentiation trajectory; its invagination accompanies dermal condensate formation, and it receives migration/invasion-promoting signals (FAM3C, EFNB1) from the Dc via LAMP1/CXADR and EPHB6.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e).

- *verbatim, paragraph 5 — **not the gold span's paragraph (8)***

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion 37,38 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).

- *verbatim, paragraph 4 — **not the gold span's paragraph (8)***

  > IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7)

**Sonnet** → `substituted` — judge: *Quote is real but describes Dc-derived ligands and placode receptors, not the placode's own role in initiating HF formation.*

> The placode expresses receptors (CXADR and EPHB6) for Dc-derived ligands FAM3C and EFNB1 that have been reported to promote cell migration and invasion, linking the placode to Dc invagination.

- *verbatim, paragraph 5 — **not the gold span's paragraph (8)***

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G03-placode-function.txt`*

---

### G05-macrophage-markers — markers, expect present

**Question** Which genes mark macrophage?

**Intended answer** MHCII genes (upregulated only after 11 PCW), TREM2 on the microglia-like subset with P2RY12, CX3CR1 and OLFML3; GAS6 and VEGFA and CXCL8 also macrophage-expressed.

**Gold span** (**not in this context** — the retriever never supplied it)

> share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages

**Hazard note given to the judge** broad label; four subsets each have their own markers

**Opus/Fable** → `honest_miss`

> The supplied context does not give marker genes for macrophages; it names four subsets (LYVE1+, MHCII+, TML and iron-recycling) and refers to marker genes used for annotation without listing them.

*No quotes given.*

**Sonnet** → `correct` — judge: *Names MHCII and the marker-defined subsets accurately, a fair partial answer for this broad label.*

> The paper identifies four macrophage subsets marked by LYVE1 and MHCII, alongside the TML and iron-recycling subsets.

- *verbatim, paragraph 1*

  > the four macrophage subsets (LYVE1 + , MHCII + , TML and iron-recycling) expressed gene programs that drive angiogenesis

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G05-macrophage-markers.txt`*

---

### G08-wnt2fib-markers — markers, expect present

**Question** Which genes mark WNT2+ fibroblast?

**Intended answer** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Gold span** (**not in this context** — the retriever never supplied it)

> Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition

**Opus/Fable** → `honest_miss`

> The supplied context does not give marker genes for WNT2+ fibroblasts. It reports genes differentially expressed within the subset across gestation (COL1A1, SFRP1) and genes shared with PEAR1+ fibroblasts (CDKN1A, IL1R1, POSTN), but none is presented as a marker defining the cell type.

*No quotes given.*

**Sonnet** → `correct` — judge: *Reports WNT2, COL1A1/ECM late, SFRP1 early, plus CDKN1A, IL1R1 and POSTN.*

> WNT2+ fibroblasts show stage-dependent gene expression: late-gestation cells upregulate extracellular matrix/collagen genes such as COL1A1, early cells upregulate growth/differentiation genes such as SFRP1, and both WNT2+ and PEAR1+ fibroblasts express CDKN1A, IL1R1 and POSTN.

- *verbatim, paragraph 1*

  > Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).

- *verbatim, paragraph 1*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G08-wnt2fib-markers.txt`*

---

### G10-wnt2fib-function — function, expect present

**Question** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Gold span** (**not in this context** — the retriever never supplied it)

> we observed differences within the WNT2+ fibroblast population across gestation time

**Opus/Fable** → `correct` — judge: *Early growth/differentiation versus late ECM and collagen deposition, plus the pro-inflammatory/senescence profile.*

> WNT2+ fibroblasts change function across gestation: early ones express growth and differentiation genes while late ones upregulate extracellular matrix and collagen deposition genes, and together with PEAR1+ fibroblasts they acquire senescence, cytokine and collagen-deposition genes characteristic of pathogenic fibrotic fibroblasts. They are also partners of macrophages, receiving PDGF signals from co-located LYVE1+ macrophages.

- *verbatim, paragraph 1*

  > Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).

- *verbatim, paragraph 1*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .

- *verbatim, paragraph 2*

  > Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).

**Sonnet** → `honest_miss`

> The supplied context does not say. It describes gene expression changes in WNT2+ fibroblasts across gestation and their co-location with macrophages, but does not state a function attributed to WNT2+ fibroblasts themselves.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G10-wnt2fib-function.txt`*

---

### G16-dc-function — function, expect present

**Question** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Gold span** (**not in this context** — the retriever never supplied it)

> have been reported to promote cell migration and invasion

**Opus/Fable** → `correct` — judge: *Aggregation from pre-Dc cells and dermal-epidermal crosstalk in HF development conveys the intended role.*

> The dermal condensate is presented as a hair-follicle-specialized dermal cell state that takes part in dermal-epidermal crosstalk during hair follicle development; it forms from aggregating pre-Dc fibroblasts next to the hair placode and, after follicle invagination, becomes the dermal papilla.

- *verbatim, paragraph 8*

  > We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c). In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 . Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin 28,29 . Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP + , SOX2 + ) 26,28 (Fig. 2c and Extended Data Fig. 3h).

**Sonnet** → `honest_miss`

> The supplied context does not state a specific function for the dermal condensate; it only describes how pre-Dc cells aggregate to form the Dc and its spatial relationship to the hair placode.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G16-dc-function.txt`*

---

### G17-matrix-markers — markers, expect present

**Question** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** SHH, and WNT10B; both described as known matrix markers.

**Gold span** (**not in this context** — the retriever never supplied it)

> known matrix markers such as SHH and WNT10B, were upregulated

**Hazard note given to the judge** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Opus/Fable** → `correct` — judge: *SHH and WNT10B named as known matrix markers, with the hair-matrix sense correctly identified.*

> The context names SHH and WNT10B as known matrix markers, upregulated along the IRS trajectory, and reports that prenatal matrix cells have increased expression of CXCL14 and CD24 relative to adult hair follicles.

- *verbatim, paragraph 8*

  > AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B 25,26 were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7).

- *verbatim, paragraph 4*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .

**Sonnet** → `leaked`

> Hair matrix cells are marked by SHH, and known matrix markers SHH and WNT10B were found upregulated along the IRS trajectory.

- *verbatim, paragraph 8*

  > known matrix markers such as SHH and WNT10B 25,26 were upregulated

- ***leaked** — from another question's context*

  > matrix (SHH + )

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G17-matrix-markers.txt`*

---

### G20-lyve1-markers — markers, expect present

**Question** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** LYVE1; also expresses GAS6.

**Gold span** (**not in this context** — the retriever never supplied it)

> GAS6, expressed by TML macrophages and LYVE1+ macrophages

**Hazard note given to the judge** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Opus/Fable** → `correct` — judge: *LYVE1 itself plus GAS6, with an honest note that the context carries no fuller marker panel.*

> The supplied context gives no marker gene list for this subset; the only gene it ties to the subset's identity is LYVE1 itself, used to name the macrophage subset, and it additionally reports GAS6 as expressed by LYVE1+ macrophages (shared with TML macrophages).

- *verbatim, paragraph 1*

  > Gene ontology analysis showed that the four macrophage subsets (LYVE1 + , MHCII + , TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26).

- *verbatim, paragraph 4*

  > Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair 62,63 .

**Sonnet** → `honest_miss`

> The supplied context does not list specific marker genes that define LYVE1+ macrophage identity beyond LYVE1 itself; it only notes that marker genes were used to annotate macrophage subsets without naming them.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G20-lyve1-markers.txt`*

---

### G33-caparteriole-markers — markers, expect present

**Question** Which genes mark capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer** Arteriolar identity is marked by GJA5. In the organoid comparison, KDR and FLT1 (VEGF receptors) and the GATA2/NFATC1 regulons with targets such as VWF are downregulated in SkO capillary arterioles relative to prenatal skin.

**Gold span** (paragraph 4 of 8)

> their receptors (KDR and FLT1) on SkO capillary arterioles were downregulated compared to prenatal skin

**The gold span in its paragraph**

> … re highly expressed in SkO, whereas pro-angiogenic genes (for example, CXCL8) were upregulated in prenatal skin and primarily expressed by macrophages (Extended Data Fig. 11a and Supplementary Tables 30-34). Although expression of vascular endothelial growth factors (VEGF), VEGFA and VEGFB were increased in SkO cells, their receptors (KDR and FLT1) on SkO capillary arterioles were downregulated compared to prenatal skin (Extended Data Fig. 11b,c). These receptors are known downstream targets of GATA2, which has a key role in angiogenesis during development and regulates VEGF-induced endothelial cell migration and sprouting in vitro 72 . Regulon analysis showed that GATA2 and related regulons (for example, NFATC1) were downregulated i …

**Opus/Fable** → `miss`

> The supplied context does not give marker genes for capillary arterioles. It names GJA5 as characteristic of the arteriolar pathway as a whole and discusses genes downregulated in SkO capillary arterioles (KDR, FLT1, VWF), but no genes are stated to mark this cell type.

*No quotes given.*

**Sonnet** → `correct` — judge: *Gives GJA5 as the arteriolar characteristic gene, the main point of the intended answer.*

> The paper reports GJA5 as a characteristic gene of the arteriolar pathway, which includes capillary arterioles (as opposed to PLVAP marking the venular pathway).

- *verbatim, paragraph 1 — **not the gold span's paragraph (4)***

  > Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G33-caparteriole-markers.txt`*

---
