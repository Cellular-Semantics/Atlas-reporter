# Review request: fetal skin atlas cell type reports and CL term requests

Hi Lloyd,

Enjoyed your CellGen talk the other day - for both scientific and Hip Hop content.

I'm wondering if you could help out with a quick review/spot of some of the work I've been doing. I'm hoping it might be relevant to your future atlas building. 

We've been running an agentic pipeline to generate structured cell type reports for the [Gopee et al. (2024) prenatal human skin atlas](https://doi.org/10.1038/s41586-024-08002-x). 

The aim is to generate accurate reports for each cell type, based on the atlas paper itself and the papers it cites. The preliminary plan, discussed with Dave H, is to serve these as pre-generated pages on the atlas portal. The reports come Cell Ontology mappings too - that we we can use to drive cross-atlas search.

Would you be able to spot-check some of this for quality? (do the biology the CL mappings and proposed new CL terms look right?).  I think your skin biology expertise will really help.  More specifically could you:


1. **Spot-check a few reports** — does the biology look right? Are there cases where the agent has misconstrued the evidence or missed something important? 
 - Some suggestions:
    c2.md; iron-recycling-macrophage; neuroendocrine cell.
 - All reports are in the [fetal_skin_atlas reports directory](https://github.com/Cellular-Semantics/Atlas-chat/tree/fetal_skin_atlas/projects/fetal_skin_atlas/reports).
 

2. **Review the three CL NTRs** — do the definitions, parent terms, and logical axioms look appropriate? ([#3611](https://github.com/obophenotype/cell-ontology/issues/3611), [#3612](https://github.com/obophenotype/cell-ontology/issues/3612), [#3613](https://github.com/obophenotype/cell-ontology/issues/3613))

I've included some more details of the workflow below.

If this looks useful, we plan to roll this out across other atlases. For HDCA and atlases undergoing annotation, I also have some additional tools for literature mining that you might find relevant.  Happy to chat about these sometime.

FInally - any good Hip Hop recommendations?  A  Most of my Hip Hop listening is 90s or more recent stuff in the same vein(). The only British Hop Hop I've listened to a lot in the past couple of years in Little Simz. But I'm always interested to hear something new.

Cheers,  
David 


Details below:

---

## Source of annotations

I scraped merged cell type annotations from the fetal skin atlas (Gopee et al. (2024) on https://cellatlas.io/) and used these as a source for my recently developed atlas chat workflow.  It mapped 207 annotations (probably excessive). Each report draws only on the atlas paper and the papers it directly cites.

---

## What the pipeline does

For each cell type label the pipeline:

1. **Resolves the name** — maps the atlas label to the author-defined cell identity, including following cross-references to integrated source atlases (e.g. F1 → Fb1 of Reynolds et al.)
2. **Traverses citations** — searches the atlas paper and its cited papers for evidence on markers, location, and function
3. **Synthesises a report** — all blockquoted text is a verbatim extract from the evidence corpus; every DOI in the report exists in the paper catalogue; the pipeline validates this before writing
4. **Maps to CL** — lexical search + definition comparison against OLS4; classifies as exact/broad match or flags a new term as needed
5. **Drafts CL new term requests** — for cell types with no satisfactory CL match, generates a structured NTR following CL definition guidelines

Every claim links back to a specific paper via inline citation, every quote is verifiable, and the evidence chain through citations is explicit. This is intended to make the reports useful and auditable rather than generically descriptive.

---

## Selected examples

### Iron-recycling macrophage — a well-supported fetal-specific cell type
[Report](https://github.com/Cellular-Semantics/Atlas-chat/blob/fetal_skin_atlas/projects/fetal_skin_atlas/reports/Iron-recycling_macrophage.md) | [NTR #3613](https://github.com/obophenotype/cell-ontology/issues/3613)

A prenatal tissue-resident macrophage defined by SLC40A1 (ferroportin)-mediated iron recycling from phagocytosed erythrocytes, first described across fetal organs by Suo et al. (2022) and characterised in prenatal skin by Gopee et al. (2024). In skin, spatially co-localised with endothelial cells in neurovascular microenvironments and specifically associated with endothelial cell chemotaxis. Closest postnatal counterparts are splenic red pulp macrophages and Kupffer cells, but this is a distinct prenatal cross-organ population — no current CL term covers it, so an NTR has been filed.

### Neuroendocrine → Merkel cell — resolving a vague atlas label
[Report](https://github.com/Cellular-Semantics/Atlas-chat/blob/fetal_skin_atlas/projects/fetal_skin_atlas/reports/Neuroendocrine.md)

The atlas annotation "Neuroendocrine" is opaque on its own. The pipeline traced this through the supplementary marker tables (CK20, synaptophysin, chromogranin A, PIEZO2) and resolved it unambiguously to Merkel cells — **CL:0000592, exact match**. The report covers their mechanosensory function, ATOH1-dependent epidermal origin, and fetal developmental timeline.

### Abbreviated Reynolds terms — decoding cluster labels
[F1 report](https://github.com/Cellular-Semantics/Atlas-chat/blob/fetal_skin_atlas/projects/fetal_skin_atlas/reports/F1.md) | [c1 report](https://github.com/Cellular-Semantics/Atlas-chat/blob/fetal_skin_atlas/projects/fetal_skin_atlas/reports/c1.md)

Labels like `F1`, `c1`, `VE2` are meaningless without the source atlas. The pipeline looked these up in Reynolds et al. (2021) (Fb1, undifferentiated basal keratinocytes, etc.) and generated full reports with correct biology. `c1` maps to **CL:0002187 basal cell of epidermis** (exact match); `F1` maps to **CL:0002620 skin fibroblast** (broad match — no current CL term for this dominant homeostatic fibroblast substate).

### Macrophage niche subtypes — NTRs for conserved but unnamed populations
[LYVE1++ NTR #3611](https://github.com/obophenotype/cell-ontology/issues/3611) | [MHCII+ NTR #3612](https://github.com/obophenotype/cell-ontology/issues/3612)

The Gopee et al. marker-based labels (LYVE1++, MHCII+) map to conserved cross-tissue macrophage niche populations described by Chakarov et al. (2019) and Dick et al. (2022). The NTRs use niche-based primary labels (**perivascular tissue-resident macrophage**, **nerve-associated tissue-resident macrophage**) with the marker names as synonyms, consistent with CL convention. Mouse functional evidence (Kolter 2019, Lim 2018, Ural 2020) is included. The nearest existing term, CL:0000881 perivascular macrophage, is CNS-restricted and cannot be applied here.

---

## Intended use

- **Atlas portal pages**: reports serve as pre-generated, evidence-grounded cell type descriptions that can be displayed alongside UMAP embeddings and marker tables.
- **Cross-atlas search**: CL mappings (exact or broad) enable query by ontology term across atlases on the web atlas platform.



---

