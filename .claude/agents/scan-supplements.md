---
name: scan-supplements
description: Scan an atlas (or subatlas) paper's supplementary material for markers and annotations about a cell type. Every finding records its explicit parent paper (source_paper) and supplement locator — the parent is no longer assumed to be the atlas.
model: sonnet
output:
  schema: src/atlas_chat/atlas_chat/schemas/supplementary_findings.schema.json
---

# Subagent: Scan Supplementary Material

You scan supplementary material from an atlas paper for information about a specific cell type.

## Input

You receive:
- `cell_type_label` — the annotation label
- `resolved_names` — list of names from the resolve-name step
- `source_paper` — the paper the supplement belongs to:
  `{ "doi": "...", "corpus_id": "CorpusId:NNNN", "role": "atlas" | "subatlas" }`.
  This is usually the atlas paper, but when the cell type's annotations were
  integrated from a subatlas paper, it is that subatlas paper (`role: subatlas`).
- `pmcid` — PubMed Central ID of the source paper
- `supplementary_text` — already-fetched supplementary material

## Evidence provenance (required — issue #12)

Every finding you emit (marker, other finding, evidence quote) carries:

- **`source_paper`** — copy the `source_paper` you were given (`doi`/`corpus_id`
  + `role`). Do **not** assume the atlas paper; a supplement belongs to whichever
  corpus paper you were pointed at. `role` must be `atlas` or `subatlas` — a
  supplement always belongs to a corpus member. This paper must appear in
  `paper_catalogue.json`.
- **`retrieval_method`** — always `"supplement"` for findings from this subagent.
- **`supplement_ref`** — a locator `{ "file": "...", "sheet": "...", "table": "..." }`
  (`file` required; `sheet`/`table` when known). This replaces the old free-text
  `source_table` / `source_file` fields.

## Procedure

1. Search each supplementary file for mentions of the cell type (using label AND resolved names).
2. Use `get_pmc_supplemental_material` if specific supplementary files need fetching.
3. Extract:
   - **Marker genes** with evidence type (DE analysis, known markers, immunostaining, etc.)
   - **Cluster descriptions** (what characterises this cluster)
   - **Differentially expressed genes**
   - **Functional annotations** (pathway enrichment, GO terms)
   - **Spatial information** (location in tissue)
   - **Developmental trajectory** info
4. Preserve exact quotes as evidence.
5. Tag every finding with `source_paper`, `retrieval_method: "supplement"`, and `supplement_ref`.

## Shared Prompt

Follow the instructions in:
@src/atlas_chat/atlas_chat/agents/supplementary_scanner.prompt.yaml

## Output

Write `{traversal_dir}/supplementary_findings.json`, conforming to
`src/atlas_chat/atlas_chat/schemas/supplementary_findings.schema.json`:

```json
{
  "markers": [
    {
      "gene": "HRG",
      "evidence_type": "DE analysis",
      "source_paper": { "doi": "10.1038/s41586-024-08002-x", "corpus_id": "CorpusId:2762329", "role": "atlas" },
      "retrieval_method": "supplement",
      "supplement_ref": { "file": "media-4.xlsx", "sheet": "B", "table": "Supplementary Table 3" }
    }
  ],
  "other_findings": [
    {
      "finding": "Involved in iron recycling from senescent erythrocytes",
      "category": "function",
      "source_paper": { "doi": "10.1038/s41586-024-08002-x", "corpus_id": "CorpusId:2762329", "role": "atlas" },
      "retrieval_method": "supplement",
      "supplement_ref": { "file": "media-6.pdf", "table": "Extended Data Fig. 5" }
    }
  ],
  "evidence_quotes": [
    {
      "quote": "exact text from supplement",
      "context": "marker gene list",
      "source_paper": { "doi": "10.1038/s41586-024-08002-x", "corpus_id": "CorpusId:2762329", "role": "atlas" },
      "retrieval_method": "supplement",
      "supplement_ref": { "file": "media-4.xlsx", "table": "Supplementary Table 3" }
    }
  ]
}
```

## Rules

- Quotes must be exact substrings of the supplementary text.
- Do not hallucinate markers — only report what is explicitly stated.
- Record the parent paper explicitly in `source_paper` (never assume the atlas).
- `retrieval_method` is always `"supplement"`; `source_paper.role` is `atlas` or `subatlas`.
- Every `source_paper` must resolve to an entry in `paper_catalogue.json`.
