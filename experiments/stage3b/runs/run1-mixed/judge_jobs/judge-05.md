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


# Cases (batch 5)


## arm: asta-sep | id: G30-hoxc5-function | kind: present

**Question:** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's answer:** HOXC5+ early fibroblasts are described as the common fibroblast progenitor of prenatal skin dermal and hair-follicle fibroblasts, giving rise along two trajectories to pre-Dc/Dc/Dp cells and to WNT2+ and PEAR1+ fibroblasts.

**Reader's quote:** “Additionally, similar to fibroblast differentiation in mouse skin, pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5 + early fibroblast) (Fig. 2e and Extended Data Fig. 4d).”

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW)”


## arm: asta-sep | id: G31-dpysl2-markers | kind: present

**Question:** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Hazard:** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Reader's answer:** Along the ORS/CL trajectory the paper reports AGR2 as a newly identified gene upregulated by DPYSL2+ basal cells, alongside previously reported ORS differentiation genes BARX2 and SOX9.

**Reader's quote:** “Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26 (Extended Data Fig. 4b,c and Supplementary Table 7).”


## arm: asta-sep | id: G32-dpysl2-function | kind: present

**Question:** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Reader's answer:** DPYSL2+ (mature) basal cells sit on the ORS/CL differentiation trajectory, upregulating AGR2 and outer root sheath differentiation genes (BARX2, SOX9), and they increase in the interfollicular epidermis after 11 PCW.

**Reader's quote:** “Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26 (Extended Data Fig. 4b,c and Supplementary Table 7).”

**Reader's quote:** “Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).”


## arm: asta-sep | id: G34-caparteriole-function | kind: present

**Question:** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Reader's answer:** Capillary arterioles are an intermediate stage of the arteriolar endothelial pathway that in prenatal skin can differentiate further into arterioles, and they score highly for sprouting angiogenesis ('tip' cell) potential, i.e. new blood vessel formation.

**Reader's quote:** “Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).”

**Reader's quote:** “However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).”


## arm: asta-sep | id: G35-pear1-markers | kind: present

**Question:** Which genes mark PEAR1+ fibroblast?

**Intended answer:** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Reader's answer:** Beyond the defining PEAR1 label, the context lists genes upregulated in these fibroblasts rather than a formal marker set: APOE, IGFBP7 and ITM2A during the transition from HOXC5+ fibroblasts, plus CDKN1A, IL1R1 and POSTN shared with WNT2+ fibroblasts.

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts (Extended Data Fig. 7c).”

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .”


## arm: asta-sep | id: G36-pear1-function | kind: present

**Question:** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer:** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Reader's answer:** PEAR1+ fibroblasts are late-gestation dermal fibroblasts with a pro-inflammatory, scar-promoting profile: they express senescence, cytokine and collagen-deposition genes characteristic of pathogenic fibroblasts in fibrotic skin disorders.

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts (Extended Data Fig. 7c).”

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .”


## arm: asta-sep | id: G37-postn-location | kind: present

**Question:** Where in prenatal human skin is POSTN+ basal cell found? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Basal epidermis; present throughout gestation, unlike mature DPYSL2+ basal and suprabasal IFE cells which increase after 11 PCW.

**Reader's answer:** The context places POSTN+ basal cells among the epidermal basal cells and states they are present throughout gestation, unlike mature basal and suprabasal IFE cells that increase after 11 PCW; no finer spatial compartment is given.

**Reader's quote:** “Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).”


## arm: asta-sep | id: G38-postn-function | kind: present

**Question:** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Reader's answer:** POSTN+ basal cells act as an epidermal progenitor that gives rise to both the ORS/CL and IRS trajectories, and their increased cellular migration is suggested to contribute to placode specification and dermal invagination.

**Reader's quote:** “Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN + basal cells into two paths: ORS/CL trajectory, comprising DPYSL2 + basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7).”

**Reader's quote:** “Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination.”


## arm: asta-sep | id: G39-arteriole-markers | kind: present

**Question:** Which genes mark arteriole?

**Intended answer:** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Hazard:** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Reader's answer:** GJA5 is given as the characteristic gene of the arteriolar pathway (as opposed to PLVAP for the venular pathway).

**Reader's quote:** “Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c).”


## arm: asta-sep | id: G40-arteriole-function | kind: present

**Question:** What function does the paper attribute to arteriole?

**Intended answer:** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Reader's answer:** Prenatal skin arterioles are among the endothelial cell types scored as having increased sprouting angiogenesis ('tip' cell state) potential, i.e. a role in new blood vessel formation.

**Reader's quote:** “However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).”


## arm: asta-sep | id: G41-cuticle-location | kind: present

**Question:** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Part of the inner layers of the hair follicle.

**Reader's answer:** Cuticle and cortex cells are hair follicle cells forming part of the inner layers of the follicle, identified in prenatal skin from 14 PCW.

**Reader's quote:** “Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: asta-comb | id: G01-placode-structure | kind: present

**Question:** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Reader's answer:** Morphologically the hair placode appears as budding of basal cells at 14-15 PCW, seen alongside germ cells and elongating hair pegs; the placode subsequently invaginates, an event accompanying dermal condensate formation.

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).”

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion 37,38 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).”


## arm: asta-comb | id: G02-placode-location | kind: present

**Question:** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Reader's answer:** The hair placode appears in the epidermal basal layer of prenatal skin as budding basal cells, observed histologically at 14-15 PCW, with HF cells including placode detected in scRNA-seq from 14 PCW.

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).”

**Reader's quote:** “Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).”


## arm: asta-comb | id: G03-placode-function | kind: present

**Question:** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Reader's answer:** The placode is the prenatal-specific epidermal cell state that gives rise to hair matrix cells and sits on the inner root sheath differentiation trajectory; its invagination accompanies dermal condensate formation, and it receives migration/invasion-promoting signals (FAM3C, EFNB1) from the Dc via LAMP1/CXADR and EPHB6.

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e).”

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion 37,38 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).”

**Reader's quote:** “IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7)”
