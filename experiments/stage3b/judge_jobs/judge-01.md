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

**Reader's answer:** The paper describes hair placodes as focal sites of epidermal layer thickening.

**Reader's quote:** “epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)”


## arm: whole | id: G02-placode-location | kind: present

**Question:** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Reader's answer:** Hair placodes are focal sites of epidermal layer thickening, situated in the epidermis where they interact with underlying dermal condensates.

**Reader's quote:** “epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)”


## arm: whole | id: G03-placode-function | kind: present

**Question:** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Reader's answer:** The placode expresses receptors (LAMP1/CXADR and EPHB6) for Dc-derived FAM3C and EFNB1, interactions reported to promote cell migration and invasion.

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion, (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).”


## arm: whole | id: G05-macrophage-markers | kind: present

**Question:** Which genes mark macrophage?

**Intended answer:** MHCII genes (upregulated only after 11 PCW), TREM2 on the microglia-like subset with P2RY12, CX3CR1 and OLFML3; GAS6 and VEGFA and CXCL8 also macrophage-expressed.

**Hazard:** broad label; four subsets each have their own markers

**Reader's answer:** Macrophage subsets are marked by LYVE1, MHCII, TML (TREM2+), and iron-recycling markers.

**Reader's quote:** “the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis”


## arm: whole | id: G06-macrophage-location | kind: present

**Question:** Where in prenatal human skin is macrophage found?

**Intended answer:** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Reader's answer:** Macrophages co-locate with endothelial and neural cells within 'early and late neurovascular microenvironments' in prenatal skin.

**Reader's quote:** “Macrophages co-located with endothelial and neural cells in 'early and late neurovascular microenvironments' (ME1 and ME5, respectively), whereas pre-dermal condensate (pre-Dc) cells co-located with dendritic and lymphoid cells based on correlation analyses (Fig. 1d and Extended Data Fig. 1e,f).”


## arm: whole | id: G07-macrophage-function | kind: present

**Question:** What function does the paper attribute to macrophage?

**Intended answer:** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Reader's answer:** Macrophages are attributed roles in scarless skin repair, fibroblast homeostasis, and neurovascular (angiogenesis and nerve) development in prenatal skin.

**Reader's quote:** “Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.”


## arm: whole | id: G08-wnt2fib-markers | kind: present

**Question:** Which genes mark WNT2+ fibroblast?

**Intended answer:** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Reader's answer:** Late gestation WNT2+ fibroblasts upregulate COL1A1, while early WNT2+ fibroblasts upregulate SFRP1.

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1)”

**Reader's quote:** “early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)”


## arm: whole | id: G11-tml-markers | kind: present

**Question:** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Reader's answer:** TML macrophages are marked by TREM2, and share an expression profile with P2RY12, CX3CR1 and OLFML3; they also co-express CX3CR1 and SYT11.

**Reader's quote:** “yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages”

**Reader's quote:** “co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)”


## arm: whole | id: G12-tml-location | kind: present

**Question:** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Reader's answer:** TML macrophages are predicted to co-locate with WNT2+ fibroblasts in early prenatal skin and with Schwann cells in the 'early neurovascular microenvironment' (ME1).

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW)”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1)”


## arm: whole | id: G13-tml-function | kind: present

**Question:** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Reader's answer:** TML macrophages are attributed roles in promoting sprouting angiogenesis and in interacting with Schwann cells to support synapse formation and axon guidance.

**Reader's quote:** “sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages”

**Reader's quote:** “TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance”


## arm: whole | id: G14-dc-markers | kind: present

**Question:** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Reader's answer:** The dermal condensate is marked by FOXD1 and SOX2.

**Reader's quote:** “the Dc (FOXD1+SOX2+)”


## arm: whole | id: G15-dc-location | kind: present

**Question:** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer:** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Reader's answer:** The dermal condensate is found within the dermal compartment, observed from 12 PCW alongside other HF-specialized fibroblasts and the dermal papilla.

**Reader's quote:** “Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).”


## arm: whole | id: G16-dc-function | kind: present

**Question:** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Reader's answer:** The Dc expresses FAM3C and EFNB1, predicted to interact with receptors on the placode (LAMP1/CXADR and EPHB6), interactions reported to promote cell migration and invasion during HF invagination.

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion”


## arm: whole | id: G17-matrix-markers | kind: present

**Question:** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** SHH, and WNT10B; both described as known matrix markers.

**Hazard:** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Reader's answer:** Hair matrix cells are marked by SHH, and SHH and WNT10B are described as known matrix markers.

**Reader's quote:** “matrix (SHH+)”

**Reader's quote:** “known matrix markers such as SHH and WNT10B, were upregulated”


## arm: whole | id: G18-matrix-location | kind: present

**Question:** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Reader's answer:** Hair matrix cells are located overlying the dermal papilla (Dp).

**Reader's quote:** “RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells.”


## arm: whole | id: G19-matrix-function | kind: present

**Question:** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Reader's answer:** Matrix cells are predicted to receive RSPO3 signalling from the dermal papilla via LGR4/LGR6, contributing to proliferation of HF epithelial cells.

**Reader's quote:** “Finally, RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells.”


## arm: whole | id: G20-lyve1-markers | kind: present

**Question:** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** LYVE1; also expresses GAS6.

**Hazard:** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Reader's answer:** GAS6 is expressed by LYVE1+ macrophages, according to the supplied context.

**Reader's quote:** “GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.”


## arm: whole | id: G21-lyve1-location | kind: present

**Question:** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Reader's answer:** LYVE1+ macrophages co-locate with WNT2+ fibroblasts, and were also shown by imaging to lie in close proximity to endothelial cells.

**Reader's quote:** “LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e)”

**Reader's quote:** “multiplex RNAscope and immunofluorescence staining showed LYVE1+ and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1)”


## arm: whole | id: G22-lyve1-function | kind: present

**Question:** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Reader's answer:** LYVE1+ macrophages are proposed to help maintain dermal fibroblasts via growth factor signalling, and their gene expression programme is associated with blood vessel morphogenesis and sprouting angiogenesis.

**Reader's quote:** “suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts”

**Reader's quote:** “blood vessel morphogenesis by LYVE1+ macrophages”


## arm: whole | id: G24-fibroblast-location | kind: present

**Question:** Where in prenatal human skin is fibroblast found?

**Intended answer:** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Reader's answer:** Fibroblasts are found within the dermal compartment, including HOXC5+ early fibroblasts located in the upper dermis.

**Reader's quote:** “Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW.”

**Reader's quote:** “HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f)”


## arm: whole | id: G25-fibroblast-function | kind: present

**Question:** What function does the paper attribute to fibroblast?

**Intended answer:** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Reader's answer:** The paper attributes collagen production to dermal fibroblasts, noting that aggregation of this collagen (along with failed epidermal regeneration) is what produces scars.

**Reader's quote:** “Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.”


## arm: whole | id: G26-periderm-location | kind: present

**Question:** Where in prenatal human skin is periderm found?

**Intended answer:** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Reader's answer:** Periderm is one of the immature interfollicular epidermal cell types present from 7 PCW, and it sloughs off starting at 11 PCW.

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin”

**Reader's quote:** “with the periderm seen sloughing from 11 PCW”
