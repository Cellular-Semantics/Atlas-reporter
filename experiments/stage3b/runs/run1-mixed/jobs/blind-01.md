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


## G01-placode-structure

What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)


## G02-placode-location

Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)


## G03-placode-function

What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)


## G04-placode-markers

Which genes mark hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)


## G05-macrophage-markers

Which genes mark macrophage?


## G06-macrophage-location

Where in prenatal human skin is macrophage found?


## G07-macrophage-function

What function does the paper attribute to macrophage?


## G08-wnt2fib-markers

Which genes mark WNT2+ fibroblast?


## G09-wnt2fib-location

Where in prenatal human skin is WNT2+ fibroblast found?


## G10-wnt2fib-function

What function does the paper attribute to WNT2+ fibroblast?


## G11-tml-markers

Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)


## G12-tml-location

Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)


## G13-tml-function

What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)


## G14-dc-markers

Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)


## G15-dc-location

Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)


## G16-dc-function

What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)


## G17-matrix-markers

Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)


## G18-matrix-location

Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)


## G19-matrix-function

What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)


## G20-lyve1-markers

Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)


## G21-lyve1-location

Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)


## G22-lyve1-function

What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)


## G23-fibroblast-markers

Which genes mark fibroblast?


## G24-fibroblast-location

Where in prenatal human skin is fibroblast found?


## G25-fibroblast-function

What function does the paper attribute to fibroblast?


## G26-periderm-location

Where in prenatal human skin is periderm found?


## G27-periderm-function

What function does the paper attribute to periderm?


## G28-periderm-structure

What does the paper say about the structure or morphology of periderm?
