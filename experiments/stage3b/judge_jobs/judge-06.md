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


# Cases (batch 6)


## arm: asta-comb | id: G03-placode-function | kind: present

**Question:** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Reader's answer:** The placode expresses receptors (CXADR and EPHB6) for Dc-derived ligands FAM3C and EFNB1 that have been reported to promote cell migration and invasion, linking the placode to Dc invagination.

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion”


## arm: asta-comb | id: G05-macrophage-markers | kind: present

**Question:** Which genes mark macrophage?

**Intended answer:** MHCII genes (upregulated only after 11 PCW), TREM2 on the microglia-like subset with P2RY12, CX3CR1 and OLFML3; GAS6 and VEGFA and CXCL8 also macrophage-expressed.

**Hazard:** broad label; four subsets each have their own markers

**Reader's answer:** The paper identifies four macrophage subsets marked by LYVE1 and MHCII, alongside the TML and iron-recycling subsets.

**Reader's quote:** “the four macrophage subsets (LYVE1 + , MHCII + , TML and iron-recycling) expressed gene programs that drive angiogenesis”


## arm: asta-comb | id: G06-macrophage-location | kind: present

**Question:** Where in prenatal human skin is macrophage found?

**Intended answer:** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Reader's answer:** Macrophages in prenatal skin co-locate with endothelial cells in neurovascular microenvironments, and TML macrophages specifically co-locate with Schwann cells.

**Reader's quote:** “Visium deconvolution analysis predicted co-location of prenatal skin macrophages with endothelial cells ('early and late neurovascular microenvironments', ME1 and ME5) (Fig. 1d and Extended Data Fig. 1e).”


## arm: asta-comb | id: G07-macrophage-function | kind: present

**Question:** What function does the paper attribute to macrophage?

**Intended answer:** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Reader's answer:** Macrophages are attributed roles in prenatal skin angiogenesis (via co-location with endothelial cells and ligand-receptor interactions supporting chemotaxis and cell migration), in supporting establishment of the skin peripheral nervous system through interactions with Schwann cells, and possibly in scarless healing and tissue homeostasis, raising the question of a contribution to early skin morphogenesis.

**Reader's quote:** “Predicted ligandreceptor interactions were consistent with reciprocal communication between macrophages and endothelial cells to support angiogenesis, chemotaxis and cell migration (for example, CXCL8-ACKR1 and CCL8-ACKR1) 10,70 (Extended Data Fig. 9a and Supplementary Table 28).”

**Reader's quote:** “Our data suggested that macrophages contribute to prenatal skin angiogenesis.”

**Reader's quote:** “TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) 66 (Extended Data Fig. 8h and Supplementary Table 8).”

**Reader's quote:** “Together with evidence of their role in tissue homeostasis 6,7 and healing in mouse models 8,9 , this raises the question of whether macrophages contribute to human early skin morphogenesis.”


## arm: asta-comb | id: G08-wnt2fib-markers | kind: present

**Question:** Which genes mark WNT2+ fibroblast?

**Intended answer:** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Reader's answer:** WNT2+ fibroblasts show stage-dependent gene expression: late-gestation cells upregulate extracellular matrix/collagen genes such as COL1A1, early cells upregulate growth/differentiation genes such as SFRP1, and both WNT2+ and PEAR1+ fibroblasts express CDKN1A, IL1R1 and POSTN.

**Reader's quote:** “Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).”

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .”


## arm: asta-comb | id: G09-wnt2fib-location | kind: present

**Question:** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer:** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Reader's answer:** WNT2+ fibroblasts co-locate with LYVE1+ macrophages and, in early prenatal skin (6-8 PCW), with TML macrophages.

**Reader's quote:** “LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e)”

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)”


## arm: asta-comb | id: G11-tml-markers | kind: present

**Question:** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Reader's answer:** TML macrophages are TREM2+ and share an expression profile of P2RY12, CX3CR1 and OLFML3 with microglia-like macrophages elsewhere; they also co-express immunomodulatory genes such as CX3CR1 and SYT11.

**Reader's quote:** “We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads 57,58 (Extended Data Fig. 7e,f).”

**Reader's quote:** “Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) 59 (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 19-23).”


## arm: asta-comb | id: G12-tml-location | kind: present

**Question:** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Reader's answer:** TML macrophages are predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the 'early neurovascular microenvironment' (ME1).

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW)”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1)”


## arm: asta-comb | id: G13-tml-function | kind: present

**Question:** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Reader's answer:** TML macrophages are implicated in scarless healing through anti-inflammatory/anti-fibrogenic signalling with WNT2+ fibroblasts, in supporting establishment of the skin peripheral nervous system through interactions with Schwann cells (synapse formation and axon guidance), and in promoting sprouting angiogenesis.

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2 + fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a). This led us to infer a potential contribution of macrophages in scarless healing in prenatal skin.”

**Reader's quote:** “TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) 66 (Extended Data Fig. 8h and Supplementary Table 8).”

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages, blood vessel morphogenesis by LYVE1 + macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).”


## arm: asta-comb | id: G14-dc-markers | kind: present

**Question:** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Reader's answer:** The dermal condensate is marked by FOXD1 and SOX2, based on orthologous marker genes used to annotate it in human prenatal skin.

**Reader's quote:** “In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 .”


## arm: asta-comb | id: G15-dc-location | kind: present

**Question:** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer:** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Reader's answer:** The dermal condensate is found within the dermal compartment of prenatal skin, observed alongside HF-specialized fibroblasts and the dermal papilla from 12 PCW.

**Reader's quote:** “Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).”


## arm: asta-comb | id: G18-matrix-location | kind: present

**Question:** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Reader's answer:** Hair matrix cells arise from the epidermal placode, a prenatal-specific cell state not present in established adult hair follicles.

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e).”


## arm: asta-comb | id: G19-matrix-function | kind: present

**Question:** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Reader's answer:** Prenatal skin matrix cells had increased expression of chemotaxis genes such as CXCL14, previously reported to recruit regulatory T cells, and CD24, involved in control of autoimmunity, suggesting a role for matrix cells in Treg cell accumulation and immune protection during early hair follicle differentiation.

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .”

**Reader's quote:** “This result highlighted the potential role of T reg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).”


## arm: asta-comb | id: G21-lyve1-location | kind: present

**Question:** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Reader's answer:** LYVE1+ macrophages are found in close proximity to endothelial cells, as shown by RNAscope and immunofluorescence staining.

**Reader's quote:** “multiplex RNAscope and immunofluorescence staining showed LYVE1 + and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).”


## arm: asta-comb | id: G22-lyve1-function | kind: present

**Question:** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Reader's answer:** LYVE1+ macrophages are attributed roles in promoting sprouting angiogenesis and blood vessel morphogenesis, in maintaining prenatal skin dermal fibroblasts via growth factor interactions, and in inducing immunosuppression and tissue repair through GAS6-AXL signalling with WNT2+ fibroblasts.

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages, blood vessel morphogenesis by LYVE1 + macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).”

**Reader's quote:** “Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1 + macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.”

**Reader's quote:** “Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair 62,63 .”


## arm: asta-comb | id: G24-fibroblast-location | kind: present

**Question:** Where in prenatal human skin is fibroblast found?

**Intended answer:** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Reader's answer:** Fibroblasts are found in the dermal compartment of prenatal skin, described as dermal fibroblast subsets.

**Reader's quote:** “the temporal changes in composition and transcriptional profile of the dermal fibroblast subsets”


## arm: asta-comb | id: G25-fibroblast-function | kind: present

**Question:** What function does the paper attribute to fibroblast?

**Intended answer:** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Reader's answer:** The paper attributes to prenatal fibroblasts a role in favouring tissue regeneration over scarring, by downregulating genes involved in extracellular matrix formation, collagen deposition and inflammation during early gestation.

**Reader's quote:** “Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.”


## arm: asta-comb | id: G26-periderm-location | kind: present

**Question:** Where in prenatal human skin is periderm found?

**Intended answer:** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Reader's answer:** Periderm is one of the immature interfollicular epidermal (IFE) cell types, present as a superficial epidermal layer overlying the dermal stroma, and it sloughs from 11 PCW.

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).”


## arm: asta-comb | id: G28-periderm-structure | kind: present

**Question:** What does the paper say about the structure or morphology of periderm?

**Intended answer:** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Hazard:** thin - a layer description and a sloughing observation, not morphology proper

**Reader's answer:** Periderm is described as part of a layer of epidermal cells overlying the dermal stroma in early prenatal skin, which sloughs from 11 PCW.

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”


## arm: asta-comb | id: G29-hoxc5-location | kind: present

**Question:** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** The upper dermis.

**Reader's answer:** HOXC5+ early fibroblasts are located in the upper dermis and are abundant before 11 PCW.

**Reader's quote:** “HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths”


## arm: asta-comb | id: G30-hoxc5-function | kind: present

**Question:** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's answer:** HOXC5+ early fibroblasts act as a common fibroblast progenitor that differentiates along two trajectories: one forming hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp), and the other forming WNT2+ and PEAR1+ dermal fibroblasts.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).”

**Reader's quote:** “Additionally, similar to fibroblast differentiation in mouse skin, pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5 + early fibroblast) (Fig. 2e and Extended Data Fig. 4d).”


## arm: asta-comb | id: G31-dpysl2-markers | kind: present

**Question:** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Hazard:** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Reader's answer:** DPYSL2 itself defines this basal cell state, and the paper reports AGR2 as a newly identified gene upregulated by DPYSL2+ basal cells.

**Reader's quote:** “Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).”

**Reader's quote:** “Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26 (Extended Data Fig. 4b,c and Supplementary Table 7).”
