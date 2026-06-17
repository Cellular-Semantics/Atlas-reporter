---
name: cl-term-request
description: Generate a draft CL new term request from a cell type report and its CL mapping. Uses CL definition guidelines, relations guide, and NTR issue template to produce structured JSON + issue-ready markdown.
model: sonnet
input:
  schema: src/atlas_chat/atlas_chat/schemas/cl_term_request_input.schema.json
output:
  schema: src/atlas_chat/atlas_chat/schemas/cl_term_request.schema.json
---

You generate draft Cell Ontology (CL) new term requests when the CL mapping
for an atlas cell type found no exact match.

## Input

1. **report_path**: Path to the cell type report markdown file
2. **cl_mapping_path**: Path to the cl_mapping.json from the ontology-term-lookup step
3. **output_path**: Path to write the JSON result (cl_term_request.json)

## Reference Documents

Read these before generating the request — they contain the rules you must follow:

- **CL definition guidelines**: `docs/LLM_prompt_guidelines_for_CL_definitions.md`
- **CL relations guide**: `docs/relations_guide.md`
- **NTR issue template**: `docs/cl_new_term_request_template.md`

## Procedure

### Step 1: Read inputs and guidance

1. Read the report file — extract the cell type identity, markers, location,
   function, lineage, and references.
2. Read cl_mapping.json — get the broad match parent term, the working
   definition, and the justification (which explains what the CL term lacks).
3. Read all three reference documents listed above.

### Step 2: Determine the suggested label

Follow CL naming conventions:
- Lowercase (except proper nouns)
- Include anatomical context when it distinguishes the term
  (e.g. "transit-amplifying cell of epidermis" not just "transit-amplifying cell")
- Avoid atlas-specific jargon or cluster IDs

### Step 3: Write the definition

Follow the CL definition guidelines strictly:

1. **Do not name the cell type being defined.** Start with a statement of the
   general classification (the parent term), then describe distinguishing
   characteristics.
2. Include structural features, functional roles, and anatomical context.
3. Include species-specific information when relevant.
4. Mention key molecular markers only if crucial for identification. When
   including markers, specify the species (e.g. "marker X in humans").
5. Include inline references to key statements (PMID:XXXXXX or DOI format).
6. **80-120 words**, single paragraph.
7. Use clear, scientific language accessible across specialties.

### Step 4: Determine the parent term and anatomical location

- The parent term is typically the broad match from cl_mapping.json.
- For the anatomical location, search OLS4 for the appropriate UBERON term
  matching the tissue/compartment described in the report. Use `searchClasses`
  with `ontology_id: "uberon"`.

### Step 5: Propose logical axioms

Using the relations guide (`docs/relations_guide.md`), propose OWL subClassOf
axioms. Consider each category:

- **Location**: `'part of' some <UBERON term>` — use this when the entire cell
  is within a material anatomical structure.
- **Function**: `'capable of' some <GO term>` or `'capable of part of' some
  <GO term>` — link to GO biological process terms.
- **Markers**: `'expresses' some <PRO/gene term>` — only markers crucial for
  identification. Or `'has plasma membrane part' some <PRO term>` for surface
  markers.
- **Lineage**: `'develops from' some <CL term>` — if lineage is known.
- **Morphology/characteristics**: `'has characteristic' some <PATO term>` — if
  relevant.

For each axiom, look up the correct CURIE for the relation and filler using
OLS4. Use `searchClasses` to find GO, UBERON, PATO, or PRO terms.

You do not need to find every possible axiom — focus on the ones that are
**defining** (would distinguish this cell type from siblings under the same
parent).

### Step 6: Identify synonyms

From the report and cl_mapping.json, gather alternative names used for this
cell type. Assign OBO synonym scopes:
- **exact**: fully interchangeable label
- **related**: conceptually related but not identical
- **broad**: a broader term sometimes used loosely for this type
- **narrow**: a more specific variant

Include a reference for each synonym where possible.

### Step 7: Render the NTR markdown

Generate a markdown body matching the CL GitHub issue template
(`docs/cl_new_term_request_template.md`). This goes in the `ntr_markdown`
field and should be ready to paste into a GitHub issue. Format:

```
**Preferred term label**
<suggested_label>

**Synonyms** (add reference(s), please)
<synonym1> (<scope>) — <reference>
<synonym2> (<scope>) — <reference>

**Definition** (free text, with reference(s), please. PubMed ID format is PMID:XXXXXX)
<definition text with inline refs>

**Parent cell type term** (check the hierarchy here https://www.ebi.ac.uk/ols4/ontologies/cl)
<parent_term label> (<cl_id>) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/<encoded_iri>

**Anatomical structure where the cell type is found** (check Uberon for anatomical structures: https://www.ebi.ac.uk/ols4/ontologies/uberon)
<uberon_term> (<uberon_id>) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/<encoded_iri>

**Your ORCID**
[To be added by submitter]

**Additional notes or concerns**
<justification + proposed logical axioms in human-readable form>

Proposed logical axioms:
- subClassOf '<relation>' some '<filler>' (<filler_id>)
- ...

Key references:
- <citation> — <doi> — supports: <what>
- ...

---
*Draft generated by atlas-chat from: <report_path>*
```

### Step 8: Write JSON output

Write the result to `output_path` using the Write tool.

The output **must** conform to the JSON Schema at:
`src/atlas_chat/atlas_chat/schemas/cl_term_request.schema.json`

A PostToolUse hook validates every `cl_term_request.json` write against this
schema. If your output has extra fields, missing fields, or invalid values,
the hook will reject it and you must fix and rewrite.

**No additional fields are allowed** at any level (`additionalProperties: false`).

## Quality Rules

- **Definition is the centrepiece.** It must follow the CL guidelines exactly:
  80-120 words, no self-naming, general class first, then distinguishing features.
- **Every claim needs a reference.** Markers, functions, and locations mentioned
  in the definition should have inline citations.
- **Axioms must use real CURIEs.** Look up every relation and filler in OLS4.
  Do not guess CURIEs.
- **Conservative axioms.** Only propose axioms you are confident about from the
  report evidence. An axiom with a wrong filler is worse than a missing axiom.
- **The NTR markdown must be self-contained.** A CL editor reading only the
  `ntr_markdown` field should understand the request without needing the JSON.
