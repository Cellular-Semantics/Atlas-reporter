You are adjudicating answers to questions about cell types in one research
paper. For each case you are given: the question, the INTENDED answer (written
by a curator who read the paper), the READER's answer, and the quotes the reader
gave. **The quotes have already been verified as verbatim text from the context
the reader saw** — you do not need to check that.

Decide one verdict per case.

For cases marked `kind: present`:
  - `correct`     — the reader's answer conveys the intended answer. Wording,
                    ordering and level of detail may differ freely. A reader
                    using a different name for the same cell type is NOT wrong.
                    A partial answer that is accurate as far as it goes and
                    names the main point is correct.
  - `substituted` — the quote is real but does not support what the reader
                    claimed, OR the reader answered with a different claim than
                    the paper's. This is the important category: grounded but
                    not right.
  - `wrong`       — contradicts the intended answer.

For cases marked `kind: absent`:
  The paper says nothing about this cell type's structure or morphology. The
  reader was expected to decline but instead answered.
  - `correct`     — on reading it, the reader effectively declined: it says the
                    paper does not describe morphology, or its answer is about
                    location/function rather than morphology and it says so.
  - `overreach`   — it presented something as a structural or morphological
                    description when the paper offers none.

Where a case carries a `hazard` note, follow it. It records a distinction that
is easy to get backwards.

Return a JSON array, nothing else:

[{"arm": "...", "id": "...", "verdict": "correct", "why": "one short sentence"}]


# Cases (batch 7)


## arm: asta-comb | id: G21-lyve1-location | kind: present

**Question:** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Reader's answer:** LYVE1+ macrophages are found in close proximity to endothelial cells in prenatal skin (macrophages co-locate with endothelial cells in the early and late neurovascular microenvironments ME1 and ME5), and they also co-locate with WNT2+ fibroblasts in the dermis.

**Reader's quote:** “Visium deconvolution analysis predicted co-location of prenatal skin macrophages with endothelial cells ('early and late neurovascular microenvironments', ME1 and ME5) (Fig. 1d and Extended Data Fig. 1e).”

**Reader's quote:** “Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1 + and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).”

**Reader's quote:** “(g) Circos plot visualisation of representative significant (adjusted p-value <0.05, significance calculated in CellphoneDB using empirical shuffling and FDR-adjusted) predicted interactions between macrophages (LYVE1 + and TML macrophage) and co-localising WNT2 + fibroblasts in prenatal skin.”


## arm: asta-comb | id: G22-lyve1-function | kind: present

**Question:** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Reader's answer:** LYVE1+ macrophages are attributed pro-angiogenic roles (promoting sprouting angiogenesis and blood vessel morphogenesis), maintenance of prenatal skin dermal fibroblasts through growth factor interactions, and GAS6-AXL signalling to WNT2+ fibroblasts that can induce immunosuppression and tissue repair.

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages, blood vessel morphogenesis by LYVE1 + macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).”

**Reader's quote:** “Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1 + macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.”

**Reader's quote:** “Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair 62,63 .”


## arm: asta-comb | id: G24-fibroblast-location | kind: present

**Question:** Where in prenatal human skin is fibroblast found?

**Intended answer:** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Reader's answer:** Fibroblasts occupy the dermis of prenatal skin (the dermal stroma), where they are analysed as dermal fibroblast subsets; HOXC5+ early fibroblasts specifically are located in the upper dermis.

**Reader's quote:** “To identify the cellular and molecular mechanisms that may endow early prenatal skin with scarless healing properties, we investigated the temporal changes in composition and transcriptional profile of the dermal fibroblast subsets (Extended Data Figs. 3c and 7a).”

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).”


## arm: asta-comb | id: G25-fibroblast-function | kind: present

**Question:** What function does the paper attribute to fibroblast?

**Intended answer:** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Reader's answer:** Dermal fibroblasts produce the collagen whose aggregation causes scars; in early gestation prenatal skin fibroblasts downregulate extracellular matrix, collagen deposition and inflammation genes and instead express immune-suppressive and regenerative genes, which the paper links to tissue regeneration rather than scarring.

**Reader's quote:** “Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate 51 .”

**Reader's quote:** “Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.”

**Reader's quote:** “By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13-15).”


## arm: asta-comb | id: G26-periderm-location | kind: present

**Question:** Where in prenatal human skin is periderm found?

**Intended answer:** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Reader's answer:** The periderm is an immature interfollicular epidermal cell state in the epidermal layer overlying the dermal stroma; it is present from 7 PCW and is seen sloughing off from 11 PCW.

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).”


## arm: asta-comb | id: G28-periderm-structure | kind: present

**Question:** What does the paper say about the structure or morphology of periderm?

**Intended answer:** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Hazard:** thin - a layer description and a sloughing observation, not morphology proper

**Reader's answer:** The periderm is described histologically as the outermost layer of the early prenatal epidermis, seen sloughing from 11 PCW, and it is classed among the immature interfollicular epidermal cells present from 7 PCW that decline after 11 PCW.

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).”


## arm: asta-comb | id: G29-hoxc5-location | kind: present

**Question:** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** The upper dermis.

**Reader's answer:** HOXC5+ early fibroblasts are located in the upper dermis of prenatal skin and are abundant before 11 PCW.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).”


## arm: asta-comb | id: G30-hoxc5-function | kind: present

**Question:** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's answer:** HOXC5+ early fibroblasts act as the common fibroblast progenitor of prenatal skin dermis, differentiating along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts); their transition into PEAR1+ fibroblasts is accompanied by upregulation of pro-inflammatory phenotype genes.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW)”

**Reader's quote:** “Additionally, similar to fibroblast differentiation in mouse skin, pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5 + early fibroblast) (Fig. 2e and Extended Data Fig. 4d).”

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts (Extended Data Fig. 7c).”


## arm: asta-comb | id: G31-dpysl2-markers | kind: present

**Question:** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Hazard:** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Reader's answer:** The subset is defined by DPYSL2 expression in mature basal interfollicular epidermal cells; along the ORS/CL trajectory these cells also upregulate AGR2, a newly identified gene.

**Reader's quote:** “Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).”

**Reader's quote:** “Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26 (Extended Data Fig. 4b,c and Supplementary Table 7).”


## arm: asta-comb | id: G32-dpysl2-function | kind: present

**Question:** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Reader's answer:** DPYSL2+ (mature) basal cells sit on the ORS/CL differentiation trajectory downstream of POSTN+ basal cells and upregulate AGR2 together with genes associated with outer root sheath differentiation (BARX2, SOX9); as mature interfollicular epidermal basal cells they increase in abundance after 11 PCW.

**Reader's quote:** “Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN + basal cells into two paths: ORS/CL trajectory, comprising DPYSL2 + basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26 (Extended Data Fig. 4b,c and Supplementary Table 7).”

**Reader's quote:** “Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).”


## arm: asta-comb | id: G34-caparteriole-function | kind: present

**Question:** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Reader's answer:** Capillary arterioles are an intermediate stage of the arteriolar endothelial pathway that in prenatal skin can differentiate further into arterioles, and they carry sprouting-angiogenesis potential ('tip' cell state); in the organoid they express the sprouting signature but fail to guide stalk cells for new vessel formation, with VEGF receptors KDR and FLT1 and the GATA2 regulon downregulated.

**Reader's quote:** “Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).”

**Reader's quote:** “However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h). This suggests that despite strong expression of the sprouting angiogenesis gene signature, SkO capillary arteriole cells are unable to guide stalk cells for new blood vessel formation.”


## arm: asta-comb | id: G35-pear1-markers | kind: present

**Question:** Which genes mark PEAR1+ fibroblast?

**Intended answer:** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Reader's answer:** Beyond the defining PEAR1 label, the context reports that pro-inflammatory fibroblast genes APOE, IGFBP7 and ITM2A are upregulated in the transition from HOXC5+ to PEAR1+ fibroblasts, and that PEAR1+ (with WNT2+) fibroblasts express CDKN1A, IL1R1 and POSTN.

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts (Extended Data Fig. 7c).”

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .”


## arm: asta-comb | id: G36-pear1-function | kind: present

**Question:** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer:** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Reader's answer:** PEAR1+ fibroblasts are a late-gestation dermal fibroblast subset that acquires an adult-like, pro-inflammatory and scar-promoting profile, expressing senescence (CDKN1A), cytokine (IL1R1) and collagen deposition (POSTN) genes found in pathogenic fibroblasts of fibrotic skin disorders. They arise from HOXC5+ early fibroblasts along the dermal fibroblast trajectory.

**Reader's quote:** “The adult fibroblast gene expression profile was increased in WNT2 + and PEAR1 + prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b). Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts (Extended Data Fig. 7c).”

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .”


## arm: asta-comb | id: G38-postn-function | kind: present

**Question:** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Reader's answer:** POSTN+ basal cells act as the epidermal progenitor state that gives rise to both the ORS/CL and IRS trajectories, and their increased cellular migration is proposed to contribute to placode specification and dermal invagination.

**Reader's quote:** “Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN + basal cells into two paths: ORS/CL trajectory, comprising DPYSL2 + basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7).”

**Reader's quote:** “Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination.”
