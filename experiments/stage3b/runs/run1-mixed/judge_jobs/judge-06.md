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


## arm: asta-comb | id: G06-macrophage-location | kind: present

**Question:** Where in prenatal human skin is macrophage found?

**Intended answer:** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Reader's answer:** Macrophages are predicted and imaged to sit alongside endothelial cells in the early and late neurovascular microenvironments (ME1 and ME5), with LYVE1+ and TML macrophages in close proximity to endothelial cells; TML macrophages also co-locate with Schwann cells in ME1.

**Reader's quote:** “Visium deconvolution analysis predicted co-location of prenatal skin macrophages with endothelial cells ('early and late neurovascular microenvironments', ME1 and ME5) (Fig. 1d and Extended Data Fig. 1e).”

**Reader's quote:** “Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1 + and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)”


## arm: asta-comb | id: G07-macrophage-function | kind: present

**Question:** What function does the paper attribute to macrophage?

**Intended answer:** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Reader's answer:** Macrophages are attributed non-immune developmental roles in prenatal skin: driving angiogenesis and vascular network formation through communication with endothelial cells, supporting establishment of the skin peripheral nervous system via interaction with Schwann cells, and contributing to scarless healing and wound closure alongside fibroblasts. Antigen presentation is suggested not to be a key early function.

**Reader's quote:** “Gene ontology analysis showed that the four macrophage subsets (LYVE1 + , MHCII + , TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26).”

**Reader's quote:** “Our data suggested that macrophages contribute to prenatal skin angiogenesis.”

**Reader's quote:** “These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin 65 .”

**Reader's quote:** “Based on our data and previous studies, we also posit a potential role for early skin macrophages in conferring the distinct property of scarless healing in early prenatal skin.”

**Reader's quote:** “Using a scratch assay of SkO-derived fibroblasts cultured with or without iPS cell-derived macrophages, we demonstrated that scratch wound width closure was improved when fibroblasts were co-cultured with macrophages over 72 h (Extended Data Fig. 8g).”


## arm: asta-comb | id: G09-wnt2fib-location | kind: present

**Question:** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer:** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Reader's answer:** WNT2+ fibroblasts are a dermal fibroblast subset of prenatal skin; the context locates them by co-location, with LYVE1+ macrophages and, in early prenatal skin (6-8 PCW), TML macrophages, but gives no finer anatomical compartment.

**Reader's quote:** “Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).”

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2 + fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a).”


## arm: asta-comb | id: G10-wnt2fib-function | kind: present

**Question:** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer:** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Reader's answer:** WNT2+ fibroblasts change function across gestation: early ones express growth and differentiation genes while late ones upregulate extracellular matrix and collagen deposition genes, and together with PEAR1+ fibroblasts they acquire senescence, cytokine and collagen-deposition genes characteristic of pathogenic fibrotic fibroblasts. They are also partners of macrophages, receiving PDGF signals from co-located LYVE1+ macrophages.

**Reader's quote:** “Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).”

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .”

**Reader's quote:** “Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).”


## arm: asta-comb | id: G11-tml-markers | kind: present

**Question:** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Reader's answer:** TML macrophages are TREM2+ and share the microglia-like expression profile of P2RY12, CX3CR1 and OLFML3; they also co-express immunomodulatory genes such as CX3CR1 and SYT11.

**Reader's quote:** “We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads 57,58 (Extended Data Fig. 7e,f).”

**Reader's quote:** “Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) 59”


## arm: asta-comb | id: G12-tml-location | kind: present

**Question:** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Reader's answer:** TML macrophages are predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the 'early neurovascular microenvironment' (ME1); macrophages more generally were predicted to co-locate with endothelial cells in microenvironments ME1 and ME5.

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2 + fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a).”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g) and expressed genes related to cell migration and”

**Reader's quote:** “Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1 + and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).”


## arm: asta-comb | id: G13-tml-function | kind: present

**Question:** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Reader's answer:** TML macrophages are assigned immunomodulatory and anti-inflammatory roles that may support scarless healing (including GAS6-AXL signalling to WNT2+ fibroblasts inducing immunosuppression and tissue repair), support of the developing peripheral nervous system via interaction with Schwann cells, and promotion of sprouting angiogenesis.

**Reader's quote:** “Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) 59”

**Reader's quote:** “Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair 62,63 .”

**Reader's quote:** “TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) 66 (Extended Data Fig. 8h and Supplementary Table 8).”

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages, blood vessel morphogenesis by LYVE1 + macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).”


## arm: asta-comb | id: G14-dc-markers | kind: present

**Question:** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Reader's answer:** The dermal condensate is defined by FOXD1 and SOX2 expression, the mouse orthologous markers the authors used to annotate the Dc in human prenatal skin; the derived dermal papilla is NDP+ SOX2+.

**Reader's quote:** “In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 . Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin 28,29 .”


## arm: asta-comb | id: G15-dc-location | kind: present

**Question:** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer:** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Reader's answer:** The dermal condensate sits in the dermal compartment of prenatal skin, observed from 12 PCW; it forms from aggregating pre-Dc fibroblasts and abuts the epithelial hair placode, later becoming encapsulated at the base of the invaginating follicle as the dermal papilla.

**Reader's quote:** “Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).”

**Reader's quote:** “In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 . Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin 28,29 . Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP + , SOX2 + ) 26,28 (Fig. 2c and Extended Data Fig. 3h).”


## arm: asta-comb | id: G16-dc-function | kind: present

**Question:** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Reader's answer:** The dermal condensate is presented as a hair-follicle-specialized dermal cell state that takes part in dermal-epidermal crosstalk during hair follicle development; it forms from aggregating pre-Dc fibroblasts next to the hair placode and, after follicle invagination, becomes the dermal papilla.

**Reader's quote:** “We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c). In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 . Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin 28,29 . Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP + , SOX2 + ) 26,28 (Fig. 2c and Extended Data Fig. 3h).”


## arm: asta-comb | id: G17-matrix-markers | kind: present

**Question:** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** SHH, and WNT10B; both described as known matrix markers.

**Hazard:** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Reader's answer:** The context names SHH and WNT10B as known matrix markers, upregulated along the IRS trajectory, and reports that prenatal matrix cells have increased expression of CXCL14 and CD24 relative to adult hair follicles.

**Reader's quote:** “AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B 25,26 were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7).”

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .”


## arm: asta-comb | id: G18-matrix-location | kind: present

**Question:** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Reader's answer:** Hair matrix cells belong to the hair follicle epithelial compartment, arising from the epidermal placode, and are counted among the late epithelial cell states present from 12 PCW onwards. The context gives no finer spatial position within the follicle.

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e).”

**Reader's quote:** “late epithelial cells (≥12 PCW; DPYSL2 + basal, POSTN + basal, placode, matrix, ORS, CL, IRS, cuticle/cortex)”


## arm: asta-comb | id: G19-matrix-function | kind: present

**Question:** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Reader's answer:** Prenatal hair matrix cells upregulate chemotaxis genes such as CXCL14 (a chemokine reported to recruit regulatory T cells) and the autoimmunity-control gene CD24, which the authors interpret as a role for Treg cell accumulation and immune protection during early matrix differentiation. Matrix is also placed on the IRS differentiation trajectory downstream of placode, expressing matrix markers SHH and WNT10B.

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 . This result highlighted the potential role of T reg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).”

**Reader's quote:** “AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B 25,26 were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7).”


## arm: asta-comb | id: G20-lyve1-markers | kind: present

**Question:** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** LYVE1; also expresses GAS6.

**Hazard:** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Reader's answer:** The supplied context gives no marker gene list for this subset; the only gene it ties to the subset's identity is LYVE1 itself, used to name the macrophage subset, and it additionally reports GAS6 as expressed by LYVE1+ macrophages (shared with TML macrophages).

**Reader's quote:** “Gene ontology analysis showed that the four macrophage subsets (LYVE1 + , MHCII + , TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26).”

**Reader's quote:** “Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair 62,63 .”
