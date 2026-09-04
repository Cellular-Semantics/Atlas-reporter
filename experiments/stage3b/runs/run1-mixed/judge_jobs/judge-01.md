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


# Cases (batch 1)


## arm: whole | id: G01-placode-structure | kind: present

**Question:** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Reader's answer:** The placode is described as a focal thickening of the epidermal layer; histologically it is seen as budding of basal cells at 14-15 PCW, and its formation is accompanied by invagination into the dermis.

**Reader's quote:** “epidermal placodes (focal sites of epidermal layer thickening)”

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed”

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode”


## arm: whole | id: G02-placode-location | kind: present

**Question:** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Reader's answer:** The placode is an epidermal/epithelial structure in the basal epidermis of prenatal skin, appearing as budding basal cells from 14-15 PCW, and it is abutted by the dermal condensate beneath it.

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed”

**Reader's quote:** “aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode”

**Reader's quote:** “we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells”


## arm: whole | id: G03-placode-function | kind: present

**Question:** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Reader's answer:** The placode initiates hair follicle formation through interaction with the dermal condensate, and it gives rise to hair matrix cells; it lies on the IRS differentiation trajectory and receives migration/invasion-promoting signals from the Dc.

**Reader's quote:** “Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)”

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs”

**Reader's quote:** “IRS trajectory, involving placode, matrix, cuticle/cortex and IRS”


## arm: whole | id: G05-macrophage-markers | kind: present

**Question:** Which genes mark macrophage?

**Intended answer:** MHCII genes (upregulated only after 11 PCW), TREM2 on the microglia-like subset with P2RY12, CX3CR1 and OLFML3; GAS6 and VEGFA and CXCL8 also macrophage-expressed.

**Hazard:** broad label; four subsets each have their own markers

**Reader's answer:** The paper identifies macrophage subsets by marker genes rather than giving pan-macrophage markers: LYVE1+, MHCII+, TREM2+ microglia-like (TREM2, P2RY12, CX3CR1, OLFML3) and iron-recycling subsets.

**Reader's quote:** “the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis”

**Reader's quote:** “We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads”


## arm: whole | id: G06-macrophage-location | kind: present

**Question:** Where in prenatal human skin is macrophage found?

**Intended answer:** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Reader's answer:** Macrophages seed the skin from as early as 6 PCW and are present throughout gestation, co-locating with endothelial and neural cells in early and late neurovascular microenvironments (ME1 and ME5) and, for the LYVE1+ subset, with WNT2+ dermal fibroblasts.

**Reader's quote:** “immune cells such as macrophages seed the skin as early as 6 PCW and express a range of pro-inflammatory genes”

**Reader's quote:** “Macrophages co-located with endothelial and neural cells in 'early and late neurovascular microenvironments' (ME1 and ME5, respectively)”

**Reader's quote:** “Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e)”


## arm: whole | id: G07-macrophage-function | kind: present

**Question:** What function does the paper attribute to macrophage?

**Intended answer:** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Reader's answer:** Macrophages are proposed to support skin morphogenesis: maintaining dermal fibroblasts, contributing to scarless repair, supporting peripheral nerve development, and driving angiogenesis and vascular network remodelling (shown by adding iPS-derived macrophages to skin organoids).

**Reader's quote:** “Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.”

**Reader's quote:** “Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.”

**Reader's quote:** “These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin.”

**Reader's quote:** “Collectively, our findings demonstrate that interactions between macrophages and endothelial cells are required to support angiogenesis through blood vessel remodelling.”


## arm: whole | id: G08-wnt2fib-markers | kind: present

**Question:** Which genes mark WNT2+ fibroblast?

**Intended answer:** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Reader's answer:** Beyond WNT2 itself, the paper reports genes differentially expressed by this subset: late-gestation WNT2+ fibroblasts upregulate COL1A1, early ones SFRP1, and the subset expresses CDKN1A, IL1R1 and POSTN, with downregulated IL6 relative to adult fibroblasts.

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)”

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)”


## arm: whole | id: G09-wnt2fib-location | kind: present

**Question:** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer:** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Reader's answer:** WNT2+ fibroblasts are dermal fibroblasts of prenatal skin that become abundant in later gestation; they co-locate with LYVE1+ macrophages and, in early prenatal skin (6-8 PCW), with TML macrophages.

**Reader's quote:** “The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation”

**Reader's quote:** “Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e)”

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)”


## arm: whole | id: G10-wnt2fib-function | kind: present

**Question:** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer:** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Reader's answer:** WNT2+ fibroblasts form the dermal fibroblast branch of the fibroblast trajectory and shift function across gestation: early cells express growth and differentiation genes, whereas late cells deposit extracellular matrix and collagen and express senescence/cytokine genes characteristic of pathogenic fibrotic fibroblasts, linking them to the loss of scarless healing.

**Reader's quote:** “the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)”

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)”

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.”

**Reader's quote:** “were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts”


## arm: whole | id: G11-tml-markers | kind: present

**Question:** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Reader's answer:** TML macrophages are TREM2+ and share a microglial expression profile of P2RY12, CX3CR1 and OLFML3; they also co-express immunomodulatory genes such as CX3CR1 and SYT11, and express GAS6.

**Reader's quote:** “We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs”

**Reader's quote:** “co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)”


## arm: whole | id: G12-tml-location | kind: present

**Question:** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Reader's answer:** TML macrophages are found in early prenatal skin, where they are predicted to co-locate with WNT2+ fibroblasts (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1), and are seen close to endothelial cells.

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)”

**Reader's quote:** “multiplex RNAscope and immunofluorescence staining showed LYVE1+ and TML macrophages in close proximity to endothelial cells”


## arm: whole | id: G13-tml-function | kind: present

**Question:** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Reader's answer:** TML macrophages are yolk-sac derived, microglia-like cells implicated in immunomodulation and anti-fibrogenic/scarless healing (IL-6 regulation, GAS6-AXL signalling to fibroblasts), in supporting cutaneous neural development via interactions with Schwann cells, and in promoting sprouting angiogenesis.

**Reader's quote:** “co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)”

**Reader's quote:** “Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair”

**Reader's quote:** “TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1)”

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages”


## arm: whole | id: G14-dc-markers | kind: present

**Question:** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Reader's answer:** The dermal condensate is annotated as FOXD1+SOX2+ (arising from PDGFRA+FOXD1+SOX2low pre-Dc cells) and expresses FAM3C and EFNB1, with COL6A3, MFAP4 and PTK7 expressed as pre-Dc cells aggregate into the Dc.

**Reader's quote:** “In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode”

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1”

**Reader's quote:** “Genes implicated in collagen fibril formation and cell adhesion (COL6A3, MFAP4 and PTK7) were expressed as the pre-Dc cells aggregated into the Dc”


## arm: whole | id: G15-dc-location | kind: present

**Question:** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer:** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Reader's answer:** The Dc sits in the dermal compartment of prenatal skin from 12 PCW, as a hair-follicle-specialized fibroblast aggregate abutting the epithelial hair placode; after invagination it becomes encapsulated at the follicle base as the dermal papilla.

**Reader's quote:** “Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).”

**Reader's quote:** “In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,.”

**Reader's quote:** “Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).”


## arm: whole | id: G16-dc-function | kind: present

**Question:** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Reader's answer:** The Dc participates in mesenchymal-epithelial crosstalk driving hair follicle formation: its formation accompanies placode invagination, and it expresses FAM3C and EFNB1 predicted to signal to receptors on the placode and reported to promote cell migration and invasion. Prenatal hair follicle formation more broadly is initiated by interactions between epidermal placodes and dermal condensates.

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion, (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).”

**Reader's quote:** “Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts), whereas sebaceous glands develop from around 16 PCW.”


## arm: whole | id: G17-matrix-markers | kind: present

**Question:** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** SHH, and WNT10B; both described as known matrix markers.

**Hazard:** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Reader's answer:** Matrix cells are identified as SHH+, with SHH and WNT10B described as known matrix markers upregulated along the IRS trajectory. Relative to adult hair follicles, prenatal matrix cells also show increased CXCL14 and CD24 expression.

**Reader's quote:** “Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).”

**Reader's quote:** “AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B, were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7).”

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24).”


## arm: whole | id: G18-matrix-location | kind: present

**Question:** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Reader's answer:** Matrix cells are hair follicle epithelial cells detected in prenatal skin from 14 PCW; they arise from the epidermal placode and lie overlying the dermal papilla. They are a prenatal-specific state absent from established adult hair follicles.

**Reader's quote:** “Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).”

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e).”

**Reader's quote:** “Finally, RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells.”


## arm: whole | id: G19-matrix-function | kind: present

**Question:** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Reader's answer:** Matrix cells differentiate along the IRS trajectory towards cuticle/cortex and inner root sheath, and prenatal matrix cells express chemotactic and immune-regulatory genes (CXCL14, CD24) suggesting a role in Treg cell recruitment and immune protection during early matrix differentiation. Their differentiation is coordinated by Dp-derived signals (RSPO3, WNT5A), with RSPO3-LGR4/LGR6 contributing to proliferation of hair follicle epithelial cells.

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).”

**Reader's quote:** “Formation of the Dp was characterized by genes (RSPO3 and WNT5A) (Extended Data Fig. 4f and Supplementary Table 7) that coordinate the differentiation of adjacent hair matrix cells,.”

**Reader's quote:** “Finally, RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells.”


## arm: whole | id: G20-lyve1-markers | kind: present

**Question:** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** LYVE1; also expresses GAS6.

**Hazard:** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Reader's answer:** The subset is named for LYVE1 expression and is one of four prenatal skin macrophage subsets; the only other gene the context states it expresses is GAS6 (shared with TML macrophages). No full marker panel is given.

**Reader's quote:** “Gene ontology analysis showed that the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26).”

**Reader's quote:** “Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.”


## arm: whole | id: G21-lyve1-location | kind: present

**Question:** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Reader's answer:** LYVE1+ macrophages are found in prenatal skin co-located with WNT2+ fibroblasts, and imaging placed LYVE1+ macrophages in close proximity to endothelial cells; macrophage subsets more generally were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct microenvironments in early gestation.

**Reader's quote:** “Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).”

**Reader's quote:** “Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1+ and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).”

**Reader's quote:** “In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d).”


## arm: whole | id: G22-lyve1-function | kind: present

**Question:** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Reader's answer:** LYVE1+ macrophages are proposed to maintain prenatal skin dermal fibroblasts through PDGF, IGF1-IGF1R and GRN-EGFR interactions, and to promote angiogenesis - specifically sprouting angiogenesis and blood vessel morphogenesis. Their GAS6 is predicted to engage AXL on WNT2+ fibroblasts, an interaction linked to immunosuppression and tissue repair.

**Reader's quote:** “Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.”

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages, blood vessel morphogenesis by LYVE1+ macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).”

**Reader's quote:** “Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.”


## arm: whole | id: G23-fibroblast-markers | kind: present

**Question:** Which genes mark fibroblast?

**Intended answer:** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Hazard:** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Reader's answer:** Prenatal skin fibroblast subsets are defined by HOXC5 (early fibroblasts), WNT2, PEAR1 and FRZB; hair-specialized fibroblasts are marked by PDGFRA/FOXD1/SOX2low (pre-Dc), FOXD1+SOX2+ (Dc) and NDP+SOX2+ (Dp). Human prenatal fibroblasts did not significantly express the papillary fibroblast marker COL13A1.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).”

**Reader's quote:** “In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,.”

**Reader's quote:** “Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).”

**Reader's quote:** “Our human prenatal skin fibroblasts did not significantly express papillary fibroblast markers (for example, COL13A1) (Extended Data Fig. 5j), which suggested that the distinction between papillary and reticular fibroblasts emerges after 17 PCW.”


## arm: whole | id: G24-fibroblast-location | kind: present

**Question:** Where in prenatal human skin is fibroblast found?

**Intended answer:** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Reader's answer:** Fibroblasts are dermal cells: HOXC5+ early fibroblasts sit in the upper dermis, and hair-specialized fibroblasts (Dc, Dp) are found in the dermal compartment from 12 PCW; dermal condensates are aggregates of dermal fibroblasts abutting the epidermal placode. Mesoderm-derived cells including skin fibroblasts are present throughout gestation.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).”

**Reader's quote:** “Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).”

**Reader's quote:** “Mesoderm-derived cells, including skin fibroblasts and endothelial cells, and immune cells were present throughout gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).”


## arm: whole | id: G25-fibroblast-function | kind: present

**Question:** What function does the paper attribute to fibroblast?

**Intended answer:** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Reader's answer:** Fibroblasts produce the collagen whose aggregation causes scars, and prenatal fibroblasts instead upregulate immune suppression, inflammation regulation and tissue regeneration genes, which may favour scarless healing before they progressively acquire scar-promoting, pro-inflammatory profiles in later gestation. Hair-specialized fibroblasts also drive hair follicle morphogenesis through crosstalk with epidermal cells, including CXCL12-ACKR3-mediated pre-Dc migration.

**Reader's quote:** “Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.”

**Reader's quote:** “By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13-15).”

**Reader's quote:** “Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.”

**Reader's quote:** “We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c).”


## arm: whole | id: G26-periderm-location | kind: present

**Question:** Where in prenatal human skin is periderm found?

**Intended answer:** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Reader's answer:** Periderm is an ectoderm-derived immature interfollicular epidermal cell type of prenatal skin, present from 7 PCW and enriched in early gestation; it overlies the dermal stroma as part of the epidermal layer and is seen sloughing from 11 PCW.

**Reader's quote:** “Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).”

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).”


## arm: whole | id: G27-periderm-function | kind: present

**Question:** What function does the paper attribute to periderm?

**Intended answer:** Constitutes the first skin permeability barrier.

**Reader's answer:** The periderm constitutes the first skin permeability barrier.

**Reader's quote:** “Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).”


## arm: whole | id: G28-periderm-structure | kind: present

**Question:** What does the paper say about the structure or morphology of periderm?

**Intended answer:** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Hazard:** thin - a layer description and a sloughing observation, not morphology proper

**Reader's answer:** The only morphological statement is histological: the periderm is seen sloughing from 11 PCW, above the layer of epidermal cells overlying the dermal stroma; it is classed as an immature interfollicular epidermal cell state. No further structural description is given.

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).”


## arm: whole | id: G29-hoxc5-location | kind: present

**Question:** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** The upper dermis.

**Reader's answer:** HOXC5+ early fibroblasts are located in the upper dermis and are abundant before 11 PCW.

**Reader's quote:** “HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))”


## arm: whole | id: G30-hoxc5-function | kind: present

**Question:** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's answer:** They act as a common fibroblast progenitor, differentiating along a hair fibroblast trajectory (pre-Dc, Dc and Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)”

**Reader's quote:** “pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)”


## arm: whole | id: G31-dpysl2-markers | kind: present

**Question:** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Hazard:** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Reader's answer:** Mature basal interfollicular epidermal cells are marked by DPYSL2, and AGR2 is newly identified as upregulated by DPYSL2+ basal cells along the ORS/CL trajectory.

**Reader's quote:** “Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW”

**Reader's quote:** “we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)”


## arm: whole | id: G32-dpysl2-function | kind: present

**Question:** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Reader's answer:** DPYSL2+ basal cells are an intermediate state on the ORS/CL differentiation trajectory downstream of POSTN+ basal cells, upregulating AGR2 and genes related to outer root sheath differentiation.

**Reader's quote:** “predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL”

**Reader's quote:** “we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)”


## arm: whole | id: G34-caparteriole-function | kind: present

**Question:** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Reader's answer:** Capillary arteriole cells lie on the arteriolar differentiation pathway and in prenatal skin can differentiate further into arterioles; they also show an increased sprouting angiogenesis 'tip' cell signature, though SkO capillary arterioles cannot guide stalk cells for new vessel formation.

**Reader's quote:** “Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles”

**Reader's quote:** “sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells”


## arm: whole | id: G35-pear1-markers | kind: present

**Question:** Which genes mark PEAR1+ fibroblast?

**Intended answer:** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Reader's answer:** Beyond PEAR1 itself, the transition into PEAR1+ fibroblasts upregulates pro-inflammatory genes APOE, IGFBP7 and ITM2A, and PEAR1+ fibroblasts express CDKN1A, IL1R1 and POSTN.

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts”

**Reader's quote:** “WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)”


## arm: whole | id: G36-pear1-function | kind: present

**Question:** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer:** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Reader's answer:** PEAR1+ fibroblasts, abundant in later gestation, carry the adult-like pro-inflammatory and scar-promoting profile, expressing senescence, cytokine and collagen-deposition genes seen in pathogenic fibroblasts of fibrotic skin disorders.

**Reader's quote:** “The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation”

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.”


## arm: whole | id: G38-postn-function | kind: present

**Question:** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Reader's answer:** POSTN+ basal cells are the predicted origin of both the ORS/CL and IRS epidermal trajectories, and their increased cellular migration is suggested to contribute to placode specification and dermal invagination.

**Reader's quote:** “Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS”

**Reader's quote:** “Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.”


## arm: whole | id: G39-arteriole-markers | kind: present

**Question:** Which genes mark arteriole?

**Intended answer:** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Hazard:** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Reader's answer:** GJA5 is given as a characteristic gene of the arteriolar pathway (capillaries, capillary arterioles and arterioles).

**Reader's quote:** “early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)”


## arm: whole | id: G40-arteriole-function | kind: present

**Question:** What function does the paper attribute to arteriole?

**Intended answer:** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Reader's answer:** Arterioles are the endpoint of the arteriolar differentiation pathway from early endothelial cells and show increased sprouting angiogenesis ('tip' cell state) potential in prenatal skin.

**Reader's quote:** “early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules)”

**Reader's quote:** “sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells”


## arm: whole | id: G41-cuticle-location | kind: present

**Question:** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Part of the inner layers of the hair follicle.

**Reader's answer:** Cuticle and cortex cells form part of the inner layers of the hair follicle, identified in HF cells from 14 PCW.

**Reader's quote:** “we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: whole | id: G45-dermal-condensate-structure-absent | kind: absent

**Question:** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Not stated in this paper. Gopee et al. describe the transcriptional identity, location and inferred function of this cell type but not its morphology or ultrastructure.

**Reader's answer:** The dermal condensate is described structurally as an aggregate of dermal fibroblasts that abuts the epithelial hair placode, and after hair follicle invagination it becomes encapsulated at its base to form the dermal papilla.

**Reader's quote:** “dermal condensates (aggregates of dermal fibroblasts)”

**Reader's quote:** “the Dc becomes encapsulated at its base as the Dp”


## arm: whole | id: G55-cuticle-cortex-structure-absent | kind: absent

**Question:** What does the paper say about the structure or morphology of cuticle/cortex? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Not stated in this paper. Gopee et al. describe the transcriptional identity, location and inferred function of this cell type but not its morphology or ultrastructure.

**Reader's answer:** The only structural statement is positional: cuticle and cortex cells are described as forming part of the inner layers of the hair follicle. No morphological detail beyond this is given.

**Reader's quote:** “cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: local | id: G01-placode-structure | kind: present

**Question:** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Reader's answer:** The placode is described as a focal thickening of the epidermal layer, seen histologically at 14-15 PCW as budding of basal cells that precedes elongation of the hair follicle into hair pegs.

**Reader's quote:** “initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)”

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).”


## arm: local | id: G02-placode-location | kind: present

**Question:** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Reader's answer:** The placode is an epidermal structure — a focal thickening of the epidermal layer — that is abutted from below by the dermal condensate; placode cells were identified among hair follicle cells in scRNA-seq data from 14 PCW.

**Reader's quote:** “initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)”

**Reader's quote:** “transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode”

**Reader's quote:** “we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells”


## arm: local | id: G03-placode-function | kind: present

**Question:** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Reader's answer:** The placode is the epidermal origin of hair matrix cells and the first step of the IRS differentiation trajectory; its specification is linked to increased cellular migration in POSTN+ basal cells and to WNT and EDA signalling, and it receives dermal condensate signals (FAM3C and EFNB1 acting on LAMP1/CXADR and EPHB6) as invagination proceeds.

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e).”

**Reader's quote:** “IRS trajectory, involving placode, matrix, cuticle/cortex and IRS”

**Reader's quote:** “Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.”

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode”

**Reader's quote:** “Similar signalling pathways were upregulated, including WNT and EDA for hair placode specification”


## arm: local | id: G06-macrophage-location | kind: present

**Question:** Where in prenatal human skin is macrophage found?

**Intended answer:** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Reader's answer:** The context does not give a strict anatomical compartment, but it states macrophages seed prenatal skin from as early as 6 PCW and that macrophage subsets were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation, with LYVE1+ macrophages specifically co-located with WNT2+ fibroblasts.

**Reader's quote:** “immune cells such as macrophages seed the skin as early as 6 PCW and express a range of pro-inflammatory genes”

**Reader's quote:** “In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d).”

**Reader's quote:** “LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e)”


## arm: local | id: G07-macrophage-function | kind: present

**Question:** What function does the paper attribute to macrophage?

**Intended answer:** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Reader's answer:** The paper attributes to macrophages non-immune roles in skin morphogenesis: maintenance of dermal fibroblasts (via PDGF, IGF1-IGF1R, GRN-EGFR and GAS6-AXL interactions), a contribution to scarless wound healing (supported by an in vitro scratch assay), and promotion of angiogenesis and neurovascular development; antigen presentation is suggested not to be a key early function.

**Reader's quote:** “Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.”

**Reader's quote:** “This led us to infer a potential contribution of macrophages in scarless healing in prenatal skin.”

**Reader's quote:** “we demonstrated that scratch wound width closure was improved when fibroblasts were co-cultured with macrophages over 72 h (Extended Data Fig. 8g)”

**Reader's quote:** “Gene ontology analysis showed that the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26).”

**Reader's quote:** “Decoupling of the expression of pro-inflammatory genes from MHCII genes before 11 PCW suggests that antigen presentation may not be a key function of human macrophages during early gestation.”


## arm: local | id: G08-wnt2fib-markers | kind: present

**Question:** Which genes mark WNT2+ fibroblast?

**Intended answer:** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Reader's answer:** The context names WNT2 in the subset's label and reports genes expressed or upregulated in these cells rather than a formal defining marker panel: COL1A1 in late-gestation WNT2+ fibroblasts, SFRP1 in early WNT2+ fibroblasts, and CDKN1A, IL1R1 and POSTN in WNT2+ (and PEAR1+) prenatal fibroblasts.

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)”

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)”


## arm: local | id: G09-wnt2fib-location | kind: present

**Question:** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer:** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Reader's answer:** They are a dermal fibroblast subset, arising on the dermal fibroblast trajectory and abundant after 11 PCW; spatially they are described by co-location with LYVE1+ macrophages. The context gives no finer dermal compartment (e.g. upper versus lower dermis) for them.

**Reader's quote:** “the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)”

**Reader's quote:** “Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e)”


## arm: local | id: G10-wnt2fib-function | kind: present

**Question:** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer:** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Reader's answer:** Late-gestation WNT2+ fibroblasts are linked to extracellular matrix and collagen deposition and to scar-promoting/pro-inflammatory programs, while early WNT2+ fibroblasts show growth and differentiation genes and downregulated IL6, which the paper connects to scarless healing; they also receive macrophage signals.

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)”

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.”

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2+ fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a).”


## arm: local | id: G11-tml-markers | kind: present

**Question:** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Reader's answer:** TML macrophages are TREM2+ and share a microglia-like expression profile of P2RY12, CX3CR1 and OLFML3; they also co-express immunomodulatory genes such as CX3CR1 and SYT11.

**Reader's quote:** “We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs”

**Reader's quote:** “co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)”


## arm: local | id: G12-tml-location | kind: present

**Question:** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Reader's answer:** TML macrophages are located in prenatal skin where they are predicted to co-locate with WNT2+ fibroblasts in early gestation (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1).

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)”


## arm: local | id: G13-tml-function | kind: present

**Question:** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Reader's answer:** The paper attributes to TML macrophages immunomodulatory/anti-fibrogenic signalling supporting scarless healing (including GAS6-AXL interactions with WNT2+ fibroblasts), support of peripheral nervous system development via Schwann cell interactions in synapse formation and axon guidance, and promotion of sprouting angiogenesis.

**Reader's quote:** “Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts”

**Reader's quote:** “TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1)”

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages”


## arm: local | id: G14-dc-markers | kind: present

**Question:** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Reader's answer:** The Dc is defined by the mouse orthologous markers FOXD1 and SOX2 (FOXD1+SOX2+), which were used to annotate it in human prenatal skin; COL6A3, MFAP4 and PTK7 are expressed as pre-Dc cells aggregate into the Dc.

**Reader's quote:** “In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,. Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin,.”

**Reader's quote:** “Genes implicated in collagen fibril formation and cell adhesion (COL6A3, MFAP4 and PTK7) were expressed as the pre-Dc cells aggregated into the Dc”


## arm: local | id: G15-dc-location | kind: present

**Question:** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer:** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Reader's answer:** The dermal condensate sits in the dermal compartment of prenatal skin, observed from 12 PCW, and lies immediately beneath/abutting the epithelial hair placode; after hair follicle invagination it becomes encapsulated at the follicle base as the dermal papilla.

**Reader's quote:** “Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).”

**Reader's quote:** “In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,.”

**Reader's quote:** “Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).”


## arm: local | id: G16-dc-function | kind: present

**Question:** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Reader's answer:** The Dc is presented as a hair-follicle-specialised dermal population that takes part in dermal–epidermal crosstalk during hair follicle development: it forms by aggregation of pre-Dc cells next to the epithelial hair placode and subsequently becomes the dermal papilla, which expresses genes coordinating differentiation of adjacent hair matrix cells.

**Reader's quote:** “We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c).”

**Reader's quote:** “Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).”

**Reader's quote:** “Genes implicated in collagen fibril formation and cell adhesion (COL6A3, MFAP4 and PTK7) were expressed as the pre-Dc cells aggregated into the Dc (Extended Data Fig. 4f and Supplementary Table 7).”


## arm: local | id: G17-matrix-markers | kind: present

**Question:** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** SHH, and WNT10B; both described as known matrix markers.

**Hazard:** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Reader's answer:** SHH and WNT10B are cited as known matrix markers, upregulated along the IRS trajectory. Compared with adult hair follicles, prenatal matrix cells also showed increased expression of CXCL14 and CD24.

**Reader's quote:** “AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B, were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7).”

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24).”


## arm: local | id: G19-matrix-function | kind: present

**Question:** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Reader's answer:** Matrix cells are an epidermal-placode-derived, prenatal-specific state on the IRS differentiation trajectory (placode to matrix to cuticle/cortex to IRS). Their raised chemotaxis and autoimmunity-control gene expression is interpreted as a role in Treg cell accumulation and immune protection during early matrix differentiation, and their differentiation is coordinated by dermal papilla genes.

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e).”

**Reader's quote:** “This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).”

**Reader's quote:** “Formation of the Dp was characterized by genes (RSPO3 and WNT5A) (Extended Data Fig. 4f and Supplementary Table 7) that coordinate the differentiation of adjacent hair matrix cells,.”


## arm: local | id: G20-lyve1-markers | kind: present

**Question:** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** LYVE1; also expresses GAS6.

**Hazard:** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Reader's answer:** The context gives no marker gene list for this subset; besides LYVE1 in the subset's own name, the only gene explicitly stated to be expressed by LYVE1+ macrophages is GAS6 (shared with TML macrophages).

**Reader's quote:** “Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.”


## arm: local | id: G21-lyve1-location | kind: present

**Question:** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Reader's answer:** LYVE1+ macrophages are predicted to co-locate with WNT2+ fibroblasts in prenatal skin; more broadly, macrophage subsets co-locate with fibroblasts, neural and vascular cells in distinct tissue microenvironments in early gestation, including with endothelial cells in the early and late neurovascular microenvironments.

**Reader's quote:** “Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).”

**Reader's quote:** “In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d).”

**Reader's quote:** “Visium deconvolution analysis predicted co-location of prenatal skin macrophages with endothelial cells ('early and late neurovascular microenvironments', ME1 and ME5) (Fig. 1d and Extended Data Fig. 1e).”


## arm: local | id: G22-lyve1-function | kind: present

**Question:** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Reader's answer:** LYVE1+ macrophages are attributed a role in maintaining prenatal skin dermal fibroblasts, via growth-factor interactions with WNT2+ fibroblasts, and a pro-angiogenic role: they are predicted to promote sprouting angiogenesis and blood vessel morphogenesis.

**Reader's quote:** “Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.”

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages, blood vessel morphogenesis by LYVE1+ macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).”

**Reader's quote:** “Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.”


## arm: local | id: G23-fibroblast-markers | kind: present

**Question:** Which genes mark fibroblast?

**Intended answer:** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Hazard:** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Reader's answer:** The context gives no general marker set for fibroblasts as a class; it instead names genes that label particular prenatal skin fibroblast subsets or states — HOXC5 for the common early fibroblast progenitor, and WNT2 and PEAR1 for the two subsets that carry the adult-like expression profile. It also notes that the papillary fibroblast marker COL13A1 was not significantly expressed in these prenatal fibroblasts.

**Reader's quote:** “pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)”

**Reader's quote:** “The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation”

**Reader's quote:** “Our human prenatal skin fibroblasts did not significantly express papillary fibroblast markers (for example, COL13A1)”


## arm: local | id: G24-fibroblast-location | kind: present

**Question:** Where in prenatal human skin is fibroblast found?

**Intended answer:** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Reader's answer:** Fibroblasts are dermal cells; HOXC5+ early fibroblasts are specifically located in the upper dermis, and hair-specialized fibroblast derivatives (pre-Dc cells, Dc, Dp) sit adjacent to the epidermis as pre-Dc cells migrate towards it.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).”


## arm: local | id: G25-fibroblast-function | kind: present

**Question:** What function does the paper attribute to fibroblast?

**Intended answer:** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Reader's answer:** Fibroblasts are attributed roles in extracellular matrix and collagen deposition (and hence scarring, which early prenatal fibroblasts avoid by downregulating these programs), and hair-specialized fibroblasts coordinate hair follicle formation, including differentiation of adjacent hair matrix cells.

**Reader's quote:** “Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.”

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).”

**Reader's quote:** “Formation of the Dp was characterized by genes (RSPO3 and WNT5A) (Extended Data Fig. 4f and Supplementary Table 7) that coordinate the differentiation of adjacent hair matrix cells,.”

**Reader's quote:** “A combination of fibroblast and macrophage-associated molecular features potentially contribute to the ability of prenatal skin to heal without scarring, including the presence of fibroblast progenitors, a downregulated immune milieu and reduced collagen expression.”


## arm: local | id: G26-periderm-location | kind: present

**Question:** Where in prenatal human skin is periderm found?

**Intended answer:** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Reader's answer:** Periderm is an ectoderm-derived, immature interfollicular epidermal cell type forming the outermost layer of prenatal epidermis; it is present from 7 PCW, enriched in early gestation, and is seen sloughing from 11 PCW.

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).”

**Reader's quote:** “Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).”


## arm: local | id: G27-periderm-function | kind: present

**Question:** What function does the paper attribute to periderm?

**Intended answer:** Constitutes the first skin permeability barrier.

**Reader's answer:** The periderm is described as constituting the first skin permeability barrier.

**Reader's quote:** “Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).”


## arm: local | id: G28-periderm-structure | kind: present

**Question:** What does the paper say about the structure or morphology of periderm?

**Intended answer:** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Hazard:** thin - a layer description and a sloughing observation, not morphology proper

**Reader's answer:** The only structural/morphological observation given is histological: the periderm is part of the layer of epidermal cells overlying the dermal stroma in early prenatal skin and is seen sloughing from 11 PCW. It is classed among the immature interfollicular epidermal cells; no further morphological description is provided.

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).”


## arm: local | id: G29-hoxc5-location | kind: present

**Question:** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** The upper dermis.

**Reader's answer:** HOXC5+ early fibroblasts are located in the upper dermis of prenatal human skin, and are abundant before 11 PCW.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths”


## arm: local | id: G30-hoxc5-function | kind: present

**Question:** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's answer:** The paper casts HOXC5+ early fibroblast as the common fibroblast progenitor of prenatal skin dermal cells: it differentiates along a hair fibroblast trajectory (pre-Dc cells, Dc and Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's quote:** “pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)”

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)”


## arm: local | id: G31-dpysl2-markers | kind: present

**Question:** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Hazard:** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Reader's answer:** The population is defined by DPYSL2 expression (mature basal IFE cells), and along the ORS/CL trajectory these cells upregulate AGR2 as well as the ORS differentiation genes BARX2 and SOX9.

**Reader's quote:** “Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW”

**Reader's quote:** “Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)”


## arm: local | id: G32-dpysl2-function | kind: present

**Question:** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Reader's answer:** The only role attributed to DPYSL2+ basal cells is developmental: they form part of the ORS/CL differentiation trajectory arising from POSTN+ basal cells, upregulating AGR2 and ORS differentiation genes. No other function is stated in the supplied context.

**Reader's quote:** “Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS”

**Reader's quote:** “Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)”


## arm: local | id: G34-caparteriole-function | kind: present

**Question:** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Reader's answer:** Capillary arteriole cells are an intermediate stage of the arteriolar endothelial differentiation pathway; in prenatal skin (unlike in the skin organoid) they can differentiate further into arterioles, and they score highly for sprouting angiogenesis 'tip' cell potential.

**Reader's quote:** “Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)”

**Reader's quote:** “Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles”

**Reader's quote:** “However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells”


## arm: local | id: G35-pear1-markers | kind: present

**Question:** Which genes mark PEAR1+ fibroblast?

**Intended answer:** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Reader's answer:** Beyond PEAR1 itself, the paper reports that PEAR1+ prenatal fibroblasts express cellular senescence, cytokine and collagen deposition genes (CDKN1A, IL1R1, POSTN), and that pro-inflammatory genes APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ into PEAR1+ fibroblasts.

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)”

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts”


## arm: local | id: G36-pear1-function | kind: present

**Question:** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer:** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Reader's answer:** PEAR1+ fibroblasts are an abundant-after-11-PCW dermal fibroblast subset that acquires an adult-like pro-inflammatory phenotype and expresses senescence, cytokine and collagen-deposition genes of the kind found in pathogenic fibroblasts of fibrotic skin, so they are linked to the progressive acquisition of scar-promoting properties in later gestation.

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c).”

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.”


## arm: local | id: G38-postn-function | kind: present

**Question:** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Reader's answer:** POSTN+ basal cells act as an epidermal progenitor state that differentiates along two trajectories (ORS/CL and IRS), and their increased cellular migration is proposed to contribute to hair placode specification and dermal invagination.

**Reader's quote:** “Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7).”

**Reader's quote:** “Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.”


## arm: local | id: G39-arteriole-markers | kind: present

**Question:** Which genes mark arteriole?

**Intended answer:** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Hazard:** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Reader's answer:** GJA5 is given as a characteristic gene of the arteriolar pathway (capillaries, capillary arterioles and arterioles), in contrast to PLVAP for the venular pathway.

**Reader's quote:** “Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c).”


## arm: local | id: G40-arteriole-function | kind: present

**Question:** What function does the paper attribute to arteriole?

**Intended answer:** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Reader's answer:** The context attributes no distinct biological role to arterioles beyond their place in the endothelial differentiation scheme: they are the endpoint of the arteriolar pathway, and prenatal skin arterioles show increased sprouting angiogenesis potential when scored for the 'tip' cell state.

**Reader's quote:** “However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).”


## arm: local | id: G41-cuticle-location | kind: present

**Question:** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Part of the inner layers of the hair follicle.

**Reader's answer:** Cuticle and cortex cells are part of the inner layers of the hair follicle, and were identified in the scRNA-seq data from 14 PCW.

**Reader's quote:** “Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).”


## arm: local | id: G45-dermal-condensate-structure-absent | kind: absent

**Question:** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Not stated in this paper. Gopee et al. describe the transcriptional identity, location and inferred function of this cell type but not its morphology or ultrastructure.

**Reader's answer:** The dermal condensate is described structurally as an aggregate of dermal fibroblasts that forms by aggregation of pre-Dc cells and abuts the epithelial hair placode; after hair follicle invagination it becomes encapsulated at the base of the follicle as the dermal papilla.

**Reader's quote:** “dermal condensates (aggregates of dermal fibroblasts)”

**Reader's quote:** “In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode”

**Reader's quote:** “Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+)”
