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


# Arm: blind — batch 2

## Context

No context is supplied for this batch.


# Questions


## G34-caparteriole-function

What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)


## G16-dc-function

What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)


## G30-hoxc5-function

What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)


## G07-macrophage-function

What function does the paper attribute to macrophage?


## G36-pear1-function

What function does the paper attribute to PEAR1+ fibroblast?


## G27-periderm-function

What function does the paper attribute to periderm?


## G13-tml-function

What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)


## G41-cuticle-location

Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)


## G24-fibroblast-location

Where in prenatal human skin is fibroblast found?


## G21-lyve1-location

Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)


## G18-matrix-location

Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)


## G26-periderm-location

Where in prenatal human skin is periderm found?


## G12-tml-location

Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)


## G39-arteriole-markers

Which genes mark arteriole?


## G31-dpysl2-markers

Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)


## G23-fibroblast-markers

Which genes mark fibroblast?


## G05-macrophage-markers

Which genes mark macrophage?


## G35-pear1-markers

Which genes mark PEAR1+ fibroblast?


## G11-tml-markers

Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)


## G54-arterioles-structure-absent

What does the paper say about the structure or morphology of arteriole?


## G55-cuticle-cortex-structure-absent

What does the paper say about the structure or morphology of cuticle/cortex? (cuticle/cortex is also referred to as: cuticle and cortex cells.)


## G45-dermal-condensate-structure-absent

What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)


## G49-hoxc5-plus-early-fibroblast-structure-absent

What does the paper say about the structure or morphology of HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)


## G42-macrophage-structure-absent

What does the paper say about the structure or morphology of macrophage?


## G52-pear1-plus-fibroblast-structure-absent

What does the paper say about the structure or morphology of PEAR1+ fibroblast?


## G28-periderm-structure

What does the paper say about the structure or morphology of periderm?


## G44-tml-macrophage-structure-absent

What does the paper say about the structure or morphology of TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)
