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


# Cases (batch 3)


## arm: local | id: G11-tml-markers | kind: present

**Question:** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Reader's answer:** TML macrophages are marked by TREM2, and share an expression profile with microglia-like macrophages including P2RY12, CX3CR1 and OLFML3; they also co-express CX3CR1 and SYT11.

**Reader's quote:** “We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads, (Extended Data Fig. 7e,f).”

**Reader's quote:** “Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 19-23).”


## arm: local | id: G12-tml-location | kind: present

**Question:** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Reader's answer:** TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin, and separately with Schwann cells within an 'early neurovascular microenvironment' of prenatal skin.

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)”


## arm: local | id: G13-tml-function | kind: present

**Question:** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Reader's answer:** TML macrophages are predicted to interact with Schwann cells to support synapse formation and axon guidance, and along with LYVE1+ macrophages promote sprouting angiogenesis, contributing to establishment of the peripheral nervous system and vascular development in prenatal skin.

**Reader's quote:** “TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) (Extended Data Fig. 8h and Supplementary Table 8).”


## arm: local | id: G14-dc-markers | kind: present

**Question:** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Reader's answer:** The dermal condensate (Dc) is marked by FOXD1 and SOX2 (FOXD1+SOX2+), based on orthologous mouse marker genes.

**Reader's quote:** “In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,.”


## arm: local | id: G15-dc-location | kind: present

**Question:** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer:** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Reader's answer:** The dermal condensate is found within the dermal compartment of prenatal skin, from 12 PCW onward, where it abuts the epithelial hair placode.

**Reader's quote:** “Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW”

**Reader's quote:** “which abuts the epithelial hair placode”


## arm: local | id: G17-matrix-markers | kind: present

**Question:** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** SHH, and WNT10B; both described as known matrix markers.

**Hazard:** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Reader's answer:** The paper identifies SHH and WNT10B as known markers of the hair matrix.

**Reader's quote:** “known matrix markers such as SHH and WNT10B, were upregulated”


## arm: local | id: G18-matrix-location | kind: present

**Question:** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Reader's answer:** Hair matrix cells arise from the epidermal placode and are a prenatal-specific cell state not found in established adult hair follicles.

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e).”


## arm: local | id: G19-matrix-function | kind: present

**Question:** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Reader's answer:** The paper suggests that prenatal hair matrix cells, through increased expression of the chemokine CXCL14, may recruit regulatory T (Treg) cells, pointing to a potential role in Treg cell accumulation and immune protection during early matrix differentiation.

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24).”

**Reader's quote:** “This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation”


## arm: local | id: G20-lyve1-markers | kind: present

**Question:** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** LYVE1; also expresses GAS6.

**Hazard:** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Reader's answer:** The only gene explicitly indicated in the supplied context as marking this macrophage population is LYVE1 itself, as reflected in the population's name throughout the text.

**Reader's quote:** “LYVE1+ macrophages co-located with WNT2+ fibroblasts”


## arm: local | id: G21-lyve1-location | kind: present

**Question:** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Reader's answer:** LYVE1+ macrophages co-locate with WNT2+ fibroblasts.

**Reader's quote:** “LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e)”


## arm: local | id: G22-lyve1-function | kind: present

**Question:** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Reader's answer:** LYVE1+ macrophages co-locate and interact with WNT2+ fibroblasts via growth factor signalling, playing a part in maintaining prenatal skin dermal fibroblasts, and also promote sprouting angiogenesis and blood vessel morphogenesis.

**Reader's quote:** “Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.”


## arm: local | id: G23-fibroblast-markers | kind: present

**Question:** Which genes mark fibroblast?

**Intended answer:** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Hazard:** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Reader's answer:** Fibroblasts expressing COL7A1 are noted, with COL7A1 expression observed across several fibroblast subsets in prenatal skin and SkOs.

**Reader's quote:** “Gene therapy studies for dystrophic EB have identified fibroblasts expressing COL7A1 as a promising therapeutic strategy. We observed COL7A1 expression across several fibroblast subsets in prenatal skin and SkOs (Extended Data Fig. 6d), which lends support to the gene therapy approaches.”


## arm: local | id: G24-fibroblast-location | kind: present

**Question:** Where in prenatal human skin is fibroblast found?

**Intended answer:** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Reader's answer:** One fibroblast subtype, HOXC5+ early fibroblasts, is described as located in the upper dermis of prenatal skin.

**Reader's quote:** “HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))”


## arm: local | id: G26-periderm-location | kind: present

**Question:** Where in prenatal human skin is periderm found?

**Intended answer:** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Reader's answer:** The periderm forms the outer layer of prenatal skin overlying the dermal stroma up to 8 PCW, and is seen sloughing from 11 PCW.

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”


## arm: local | id: G27-periderm-function | kind: present

**Question:** What function does the paper attribute to periderm?

**Intended answer:** Constitutes the first skin permeability barrier.

**Reader's answer:** The periderm constitutes the first permeability barrier of the skin.

**Reader's quote:** “the periderm, which constitutes the first skin permeability barrier”


## arm: local | id: G28-periderm-structure | kind: present

**Question:** What does the paper say about the structure or morphology of periderm?

**Intended answer:** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Hazard:** thin - a layer description and a sloughing observation, not morphology proper

**Reader's answer:** The periderm is described as sloughing off from 11 PCW, a structural/morphological change in the epidermal layer.

**Reader's quote:** “with the periderm seen sloughing from 11 PCW”


## arm: local | id: G29-hoxc5-location | kind: present

**Question:** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** The upper dermis.

**Reader's answer:** HOXC5+ early fibroblasts are located in the upper dermis.

**Reader's quote:** “HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))”


## arm: local | id: G30-hoxc5-function | kind: present

**Question:** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's answer:** HOXC5+ early fibroblasts act as a common progenitor that differentiates along two paths: one forming hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the other forming WNT2+ and PEAR1+ dermal fibroblasts.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).”


## arm: local | id: G31-dpysl2-markers | kind: present

**Question:** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Hazard:** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Reader's answer:** DPYSL2+ basal cells are marked by DPYSL2 itself, and along the ORS/CL trajectory upregulate AGR2 as well as previously reported ORS-differentiation genes BARX2 and SOX9.

**Reader's quote:** “Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Extended Data Fig. 4b,c and Supplementary Table 7).”


## arm: local | id: G32-dpysl2-function | kind: present

**Question:** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Reader's answer:** DPYSL2+ basal cells lie along the ORS/CL differentiation trajectory, downstream of POSTN+ basal cells, contributing to formation of the outer root sheath and companion layer.

**Reader's quote:** “ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL”


## arm: local | id: G34-caparteriole-function | kind: present

**Question:** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Reader's answer:** The paper reports that capillary arteriole cells showed increased sprouting angiogenesis potential, based on scoring of a 'tip' cell state, alongside arteriole and capillary cells.

**Reader's quote:** “sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells”


## arm: local | id: G35-pear1-markers | kind: present

**Question:** Which genes mark PEAR1+ fibroblast?

**Intended answer:** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Reader's answer:** PEAR1+ fibroblasts are defined by PEAR1, and genes such as APOE, IGFBP7 and ITM2A are upregulated during the transition into this state.

**Reader's quote:** “the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)”

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts”
