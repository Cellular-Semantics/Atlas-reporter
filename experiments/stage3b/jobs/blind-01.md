You are answering questions about cell types from a single research paper.

## The rule that matters

**Every assertion must be backed by a supporting quote copied verbatim from the
context supplied to you.** An answer without a quote is worthless here, however
correct it may be. If you cannot find text that supports a claim, do not make
the claim.

## Rules

1. Answer **only** from the context block given with each question. Do not use
   what you already know about the cell type, the paper, or the field. Your own
   knowledge is not evidence.
2. Copy quotes **character for character** from the context. Do not paraphrase,
   reword, correct, or tidy them.
3. **Never splice.** A quote must be one continuous run of text. Do not join two
   passages that are not adjacent in the context, and do not insert an ellipsis
   to bridge them. If two separate passages are needed, give two quotes.
4. If the context does not answer the question, set `"found": false`, say so in
   `answer`, and leave `quotes` empty. **This is a correct and expected
   outcome** — several questions are about things this paper does not discuss.
   Declining is not failing. Guessing is.
5. If the context is empty or absent, `"found": false` is the only correct
   response.
6. Answer each question independently. Do not let one question's context inform
   another's answer.

## Output

Return a JSON array, one object per question, nothing else:

```json
[
  {
    "id": "G01-placode-structure",
    "found": true,
    "answer": "One or two sentences, in your own words.",
    "quotes": ["exact continuous run of text from the context"]
  },
  {
    "id": "G17-matrix-markers",
    "found": false,
    "answer": "The supplied context does not say.",
    "quotes": []
  }
]
```


# Arm: blind — batch 1

## Context

No context is supplied for this batch.


# Questions


## G40-arteriole-function

What function does the paper attribute to arteriole?


## G32-dpysl2-function

What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)


## G25-fibroblast-function

What function does the paper attribute to fibroblast?


## G22-lyve1-function

What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)


## G19-matrix-function

What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)


## G38-postn-function

What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)


## G03-placode-function

What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)


## G10-wnt2fib-function

What function does the paper attribute to WNT2+ fibroblast?


## G15-dc-location

Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)


## G29-hoxc5-location

Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)


## G06-macrophage-location

Where in prenatal human skin is macrophage found?


## G37-postn-location

Where in prenatal human skin is POSTN+ basal cell found? (POSTN+ basal cell is also referred to as: POSTN+ basal.)


## G02-placode-location

Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)


## G09-wnt2fib-location

Where in prenatal human skin is WNT2+ fibroblast found?


## G33-caparteriole-markers

Which genes mark capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)


## G14-dc-markers

Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)


## G20-lyve1-markers

Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)


## G17-matrix-markers

Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)


## G04-placode-markers

Which genes mark hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)


## G08-wnt2fib-markers

Which genes mark WNT2+ fibroblast?


## G51-capillary-arterioles-structure-absent

What does the paper say about the structure or morphology of capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)


## G50-dpysl2-plus-basal-structure-absent

What does the paper say about the structure or morphology of DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)


## G48-fibroblast-structure-absent

What does the paper say about the structure or morphology of fibroblast?


## G47-lyve1-plus-plus-macrophage-structure-absent

What does the paper say about the structure or morphology of LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)


## G46-matrix-structure-absent

What does the paper say about the structure or morphology of hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)


## G53-postn-plus-basal-structure-absent

What does the paper say about the structure or morphology of POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)


## G01-placode-structure

What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)


## G43-wnt2-plus-fibroblast-structure-absent

What does the paper say about the structure or morphology of WNT2+ fibroblast?
