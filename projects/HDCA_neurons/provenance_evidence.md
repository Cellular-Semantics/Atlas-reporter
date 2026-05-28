# HDCA_neurons — label provenance evidence (consolidated)

Source: zarr `obs` cross-tabs of `refined_celltype × original_author_annotation × study`
extracted from `hdca_v2_20260311_f2.zarr` on 2026-05-19.
Full machine-readable table: `label_provenance.json`.

## Key findings

1. **DL1–DL6 and PA1/PA2/PA3-4 neurons are 100% HDCA-whole-embryo cells**, NOT
   inherited from Braun. The naming convention (DL = dorsal "late" interneuron,
   pA = pallial/alar plate progenitor) reflects the classical
   **dI1–dI6 / pdA1–A4 dorsal spinal cord interneuron taxonomy**
   (Helms & Johnson 2003; Lai et al. 2016; Sagner & Briscoe 2019),
   not Braun's cortical/regional nomenclature (Braun's Subclass system is
   Neuron / Radial glia / Neuroblast / Glioblast / Neuronal IPC — no DL or pA
   labels appear anywhere in Braun Table S2).

2. **Retinal labels are 100% Sridhar et al. 2020 cells.** Every retinal cell
   type (`AMACRINE_CELL`, `BIPOLARS`, `PHOTORECEPTORS`, `RETINAL_GANGLION_CELL`,
   `RETINAL_HORIZONTAL_CELLS`, `RETINAL_PROGENITOR`, `RETINAL_TRANSITIONAL_CELL_T1`,
   `_T2`, `_T3`, `T1_RGC`) consists exclusively of cells from
   `Sridhar_et_al_2020_CellPress`. The single exception is
   `RETINAL_NEURAL_PROGENITOR` (n=767), which is 100% `whole_embryo`.

3. **HDCA retinal labels mirror Sridhar's nomenclature directly.** Author-label
   crosswalk:

   | HDCA `refined_celltype` | Sridhar `original_author_annotation` |
   |---|---|
   | AMACRINE_CELL | AC (98.7%) |
   | BIPOLARS | Bipolars (99.0%) |
   | PHOTORECEPTORS | Photoreceptors (97.9%) / Photo/Progen (2.0%) |
   | RETINAL_GANGLION_CELL | RGC (99.5%) |
   | RETINAL_HORIZONTAL_CELLS | HC (85.3%) |
   | RETINAL_PROGENITOR | Progenitors (58.0%) / Photo/Progen (37.2%) |
   | RETINAL_TRANSITIONAL_CELL_T1 | T1 (100%) |
   | RETINAL_TRANSITIONAL_CELL_T2 | T2 (87.7%) / T2/T3 (12.3%) |
   | RETINAL_TRANSITIONAL_CELL_T3 | T3 (99.4%) |
   | T1_RGC | T1/RGC (59.8%) / RGC (36.1%) |

   The **T1/T2/T3 transitional cell concept is a Sridhar-2020 innovation**:
   transitional retinal states they characterised as bridging neurogenic
   progenitors → committed neurons (T1) → committed bipolar/photoreceptor
   precursors (T2/T3).

4. **PNS/NCC labels are genuinely expert-pooled across multiple studies.**
   `AUTONOMIC_NCCS_SCPS` (n=15,860): 67% whole_embryo + 8% Suo + 5% Zhang + 5%
   Kanemaru + 5% Lawrence, drawing on author labels `NCC-SCP early autonomic`,
   `NCC-SCP early`, `Schwann cell precursors`, `fSGC_progenitor`, `GLIAL`,
   `PNS glia`. `SENSORY_NEURONAL` (n=4,815): primarily Lawrence_2024 (54%) +
   To_2024 (43%) with author labels `DORSAL ROOT GANGLIA` (52%) and `Neural`
   (43%). `SENSORY_NCCS_SCPS` (n=11,683): 92% whole_embryo, dominated by
   `NCC-SCP sensory` author label.

5. **Annotation impurities worth flagging in reports:**
   - **`DL3_NEURON`**: only 86% labeled "DL3 neuron" — 7.6% "sensory neuron",
     4% "pA3-4 neural progenitor", 2% "pA2 neural progenitor". May reflect
     incomplete separation from PA3-4 progenitor pool.
   - **`DL5_NEURON`**: 66% "DL5 neuron" — but **18% "radial glia"** + 9%
     "radial glia hindbrain" + 7% "excitatory neuron". A third of the cluster
     was originally annotated as progenitor.
   - **`PA1_NEURAL_PROGENITOR`**: 95% pA1 — 3% "radial glia midbrain", 1%
     "radial glia". Strong midbrain identity signal.
   - **`PA3_4_NEURAL_PROGENITOR`**: 70% pA3-4 — 25% "radial glia hindbrain".
     Strong hindbrain identity signal.
   - **`RETINAL_PROGENITOR`**: only 58% "Progenitors" — 37% "Photo/Progen"
     (cells in photoreceptor commitment) + 5% "Early Glia / imGlia". May
     conflate uncommitted retinal progenitors with photoreceptor-specifying
     cells.
   - **`T1_RGC`**: 60% "T1/RGC" + 36% "RGC". Suggests T1_RGC is a transitional
     state between Sridhar's T1 and committed RGC.

6. **`SENSORY_NEURONAL_EPIBRANCHIAL_PLACODE`** is misnamed:
   only 0.4% comes from author labels suggesting epibranchial placode
   identity. Composition is 47% "IPC forebrain" + 31% "IPC" + 21% "sympathetic
   neuron" — i.e. mostly intermediate progenitor cells that share transcriptome
   with sympathetic neurons. Likewise `SENSORY_NEURONAL_OTIC_PLACODE` is 45%
   "IPC forebrain" + 45% "Brain placode cells". Both labels were probably
   inferred from co-expression of placode markers, not from anatomical placement.

## Source paper map (20 studies feeding the community data)

For the lineages in this project:

| Cells used | Source paper | Citation |
|---|---|---|
| All retinal labels (incl. T1/T2/T3 transitional) | **Sridhar et al. 2020** | *Cell Reports* 30:1644-1659. DOI: [10.1016/j.celrep.2020.01.007](https://doi.org/10.1016/j.celrep.2020.01.007). PMC7901645. Reh lab + I. Glass (HDBR Seattle). |
| DL/PA-named whole_embryo cells | HDCA de novo whole-embryo scRNA-seq (3 samples, CS13-14) | Webb et al. 2026 *bioRxiv* |
| NCC/SCP, sensory neuronal labels | Pooled from Lawrence 2024, To 2024, Suo 2022 (Suo2022 + Elmentaite2020 + Park2020 + Jardine2021 + Popescu2019 + Stewart2019), Zhang 2020, Kanemaru 2024, plus HDCA whole_embryo | Multiple |

The naming convention DL1-DL6 / pA1-pA4 is **HDCA-internal terminology
borrowed from classical spinal-cord dorsal patterning** — the canonical
references are foundational developmental biology (not Braun, not any single
constituent atlas). Authoritative reviews:

- Helms AW & Johnson JE (2003). "Specification of dorsal spinal cord
  interneurons." *Curr Opin Neurobiol* 13:42-49.
- Lai HC, Seal RP, Johnson JE (2016). "Making sense out of spinal cord
  somatosensory development." *Development* 143:3434-3448. DOI: 10.1242/dev.139592
- Sagner A & Briscoe J (2019). "Establishing neuronal diversity in the spinal
  cord: a time and a place." *Development* 146:dev182154. DOI: 10.1242/dev.182154

## Atlas-level conclusions

- For retinal reports: cite Sridhar et al. 2020 as the *primary* source. The
  HDCA paper text describing "retinal" findings is a wrapper, not the
  annotation source.
- For DL/PA neuron reports: cite the spinal cord dorsal-interneuron
  developmental-biology literature for the nomenclature; cite HDCA Supp Table 9
  for the marker signature; flag that **Braun does NOT contribute cells to
  these labels** (correcting the impression created by HDCA Methods text
  "CNS cells retained the original fine-grained annotations from Braun et al.").
- For PNS/NCC reports: cite the relevant source paper(s) per the per-label
  study breakdown in `label_provenance.json`. These labels are genuinely
  multi-source expert pools.
