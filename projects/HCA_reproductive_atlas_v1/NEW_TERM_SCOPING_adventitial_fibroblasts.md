# CL new-term scoping — adventitial / PI16+ universal fibroblasts

**Date:** 2026-08-03 · **Purpose:** decide what new Cell Ontology term(s) the
HCA reproductive-atlas adventitial fibroblast (AdvFib) cluster family needs,
using (a) the current CL state, (b) the atlas annotation, and (c) the ASTA
deepsearch report `inputs/ASTA_reports/Advent_fib_PI16.pdf` ("Adventitial
Fibroblasts and PI16+ Universal Fibroblasts Across Organs"). **Report only — no
NTR drafted or posted yet.**

---

## 1. What CL already has (checked on OLS4)

| Term | Definition | Note |
|---|---|---|
| **CL:4052030** adventitial fibroblast | "A fibroblast of the adventitia of a blood vessel…" | Broad parent. Purely vascular-adventitia; **no molecular characterisation.** |
| CL:1000306 fibroblast of tunica adventitia of artery | "A fibroblast that is part of the tunica adventitia of artery." | Only child of CL:4052030; artery-location-specific sibling. |

**Absent from CL** (searches returned nothing): any *universal fibroblast* /
*PI16+* term; any *CXCL12+ / COL15A1+ adventitial* term; any *fallopian-tube*
fibroblast/adventitial term. So every AdvFib subtype in the atlas currently
collapses to the single broad term CL:4052030.

---

## 2. What the deepsearch establishes (the picture that reshapes the ask)

The deepsearch (≈40 primary sources) supports three points that matter for term
design:

**(a) "Adventitial fibroblast" is a real, reproducible transcriptomic state, not
just a location** — a conserved vessel-associated fibroblast core centred on
**PI16, SFRP2, SERPINF1, DPT, CLEC3B, C3, PDGFRA** and ECM genes, and *defined
against* mural markers. This gives a clean differentia:

> "adventitial fibroblasts express matrix genes, including COL1A1/COL3A1, DCN, and PI16, but lack classic mural markers such as CSPG4/NG2, MCAM/CD146, RGS5, and ACTA2" (Lendahl et al., 2022, via deepsearch)

**(b) The adventitial compartment holds TWO stable universal-fibroblast
archetypes**, repeatedly recovered across organs — this is the crux:

> "these clusters resemble two universal fibroblast archetypes: PI16+ adventitial fibroblasts (structural, progenitor-like), which are quiescent in uninjured tissues, and CXCL12+ stromal niche fibroblasts (immune-interacting and paracrine hubs), which colocalize with lymphocytes and inflammatory macrophage" (Levy-Lambert et al., 2025, via deepsearch)

Same two-pole split appears in lung (Travaglini 2019: SFRP2+PI16+ adventitial vs
alveolar), aorta (Zhao 2025 AdvFib continuum with SMCs; Gao 2024 cross-tissue
517-sample atlas), and asthma (Zhou 2025: 19 subclusters → immune-activated
HLA-DRA/CD74 vs matrix/vascular MFAP5/COL3A1). **PI16+ = structural/progenitor
pole; CXCL12+/COL15A1+ = immune-niche/differentiated pole.**

**(c) The atlas's own continuum IS these archetypes.** Cohen et al. (2026) map
`AdvFib PI16hi → C7/COL15A1hi`, and the deepsearch explicitly ties this to the
universal-fibroblast concept:

> "adventitial fibroblasts emerged as a distinct transcriptomics compartment… Pan-reproductive adventitial fibroblasts are defined by expression of DPT, SFRP2 and C3, forming a transcriptional continuum from PI16 hi (named 'AdvFib PI16hi') to C7/COL15A1 hi states… consistent with the universal fibroblast populations previously described" (Cohen et al., 2026, via deepsearch)

---

## 3. How the atlas AdvFib leaves line up with the archetypes

| Atlas leaf (fine code) | n | Markers | Archetype pole | Current CL |
|---|---|---|---|---|
| `Mesen_AdvFibs_PI16hi` | 3,032 | PI16, CD34, DPP4, SFRP2, C3, IL33, MFAP5, SCARA5, SLPI | **PI16+ structural/progenitor** | CL:4052030 (broad) |
| `Mesen_AdvFibs_PI16low` | 18,360 | C3, ABCA10, C7 | COL15A1/C7 (differentiated / niche pole) | CL:4052030 (broad) |
| `Mesen_AdvFibsIntr` | 33,795 | ACSM3, C7 | intermediate → C7/COL15A1 pole | CL:4052030 (broad) |

So the family is **one broad CL term standing in for at least two distinct,
cross-tissue archetypes** — the classic trigger for new terms.

---

## 4. Reframing your "cross-tissue + fallopian-tube-specific" idea

Your instinct (≥1 new term, maybe 2) is right; the deepsearch just relocates the
*second* axis. The strongly-supported, broadly-reusable second term is **not**
"adventitial fibroblast of fallopian tube" — organ location is a property the
literature treats as a spatial annotation of a molecular archetype, not its own
class. The second reusable term is the **other molecular pole** (CXCL12+/COL15A1+
immune-niche adventitial fibroblast). The fallopian-tube specificity of the
atlas PI16hi cluster (99% FT subserosa) is real but is best carried as a
`located_in` annotation, or — only if CL curators want anatomical granularity —
as a thin location child *under* the PI16+ term.

---

## 5. Recommended new terms (for your decision)

**T1 — PI16-high adventitial fibroblast** *(strongly recommended; exact match for
`Mesen_AdvFibs_PI16hi`)*
- `is_a` CL:4052030 adventitial fibroblast
- Synonyms: PI16+ universal fibroblast; adventitial fibroblast progenitor; universal fibroblast (PI16+ pole)
- Defining positive markers: PI16, DPP4, CD34, DPT, SFRP2 (± MFAP5, CLEC3B, SERPINF1)
- Differentia / exclusions: lacks mural markers CSPG4/NG2, MCAM/CD146, RGS5, ACTA2
- Character: quiescent, stemness-enriched, perivascular/subserosal; structural progenitor reservoir
- Cross-tissue evidence: lung, skin, aorta/artery, gut, synovium, reproductive tract (Buechler 2021; Lendahl 2022; Muhl 2020; Travaglini 2019; Zhao 2025; Levy-Lambert 2025; Gao 2024; Cohen 2026)

**T2 — CXCL12+/COL15A1+ adventitial fibroblast** *(optional companion; covers the
sibling `Mesen_AdvFibs_PI16low` / `Mesen_AdvFibsIntr` pole)*
- `is_a` CL:4052030
- Synonyms: stromal niche adventitial fibroblast; COL15A1+ universal fibroblast (differentiated pole)
- Markers: COL15A1, C7, CXCL12 (± C3, ABCA10); immune-interacting/paracrine
- Evidence: Levy-Lambert 2025; Zhou 2025; Travaglini 2019; Cohen 2026
- ⚠️ Caveat: the COL15A1/differentiated pole is not always adventitial (Zeltz 2022: COL15A1 sits deeper in parenchyma), so parentage may need review — worth flagging to CL curators.

**T3 (only if location granularity wanted) — adventitial fibroblast of fallopian
tube** — `is_a` CL:4052030 (mirrors the CL:1000306 artery pattern), or a
location child of T1. Lower priority; the atlas cluster maps *exactly* to T1
already.

---

## 6. Recommendation

Draft **T1 now** (clean, high-confidence, exact match, broadly reusable — the
biggest win and the one this report's cell type needs). Offer **T2** as a
companion since the sibling leaves are already annotated and evidenced. Treat
**T3** as optional/deferred. This gives CL a molecular pair that generalises to
every atlas carrying universal fibroblasts, rather than a one-off organ term.

**Open decision for you (drives the NTR draft):** T1 only · T1+T2 · or add T3.
Once you pick, I'll draft the `cl_term_request.json` (+ issue-ready markdown) per
the schema — draft only, nothing posted.

*Sources: OLS4 (`cl`); `inputs/ASTA_reports/Advent_fib_PI16.pdf`; atlas Supp
Table 2; the validated report `reports/adventitial_fibroblast_PI16hi.md`.*
