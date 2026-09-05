---
name: pdf-text
description: Turn a PDF into plain text on disk — a paper that reaches neither JATS nor ASTA, a supplementary PDF whose tables cannot be read, a legends document that is prose. Writes the text plus a sidecar saying what came out and what did not, so you can decide afterwards whether to read it. Needs the [text-access] extra (pymupdf4llm).
output:
  schema: src/atlas_chat/atlas_chat/schemas/pdf_text_extract.schema.json
---

# pdf-text

Extraction and reading are separate decisions. This skill runs the extraction and
then tells you what you have: how much text, from how many pages, in what sections,
with what missing. Loading a forty-page PDF's text into your context is a choice you
make *after* seeing those numbers, not a side effect of extracting it.

## When this is the right tool

- A paper reaches neither EuropePMC JATS nor ASTA, and a text dump beats nothing.
- A supplementary PDF came back shapeless from `index-supplements` — no readable
  columns. Two of the twenty-one supplementary PDFs in the corpus carried real
  cluster-to-name evidence (including `mCL2` → Sertoli cells) and both were prose,
  not tables. A shapeless PDF is not an empty one.
- You need to settle whether a file contains cell-type content at all.

## When it is not

- Building a searchable index — that is `local-paper-index`, which chunks and embeds.
- Reading supplementary *spreadsheets* — that is `index-supplements`.
- Citation edges and in-text anchors — a different deliverable (#13).
- Scanned PDFs. There is no OCR here; you get a recorded gap.

## Running it

Everything that touches bytes is in `atlas_chat.services.pdf_text`, behind a CLI.
Output paths are yours to choose — the service derives nothing.

```bash
uv sync --extra text-access        # once: pymupdf4llm + curl-cffi

uv run python -m atlas_chat.cli_pdf_text --pdf path/to/paper.pdf --out path/to/textdir
```

It writes three files into `--out`:

| file | what is in it |
|---|---|
| `<stem>.text.txt` | body paragraphs, blank-line separated, no markup |
| `<stem>.figure_text.txt` | text found *inside* figures — axis labels, panel tags, gene strips |
| `<stem>.extract.json` | the sidecar: page count, character counts, per-paragraph section tags and offsets, gaps |

Exit codes: `0` text extracted, `2` none came out (read the gaps), `1` error.

Useful flags: `--stem` to name the outputs, `--no-figure-text` to drop figure text
entirely, `--quiet` to print only the sidecar path.

## Read the sidecar before the text

The sidecar is small; read it first, always. `outputs.n_chars` against
`source.n_pages` tells you whether the extraction is worth anything, and `segments`
gives you section labels with character offsets, so you can read one section with
`sed`/slicing instead of loading the file.

```bash
# What did we get?
uv run python -c "
import json,sys; d=json.load(open(sys.argv[1]))
print(d['outputs']['n_chars'], 'chars,', d['source']['n_pages'], 'pages')
print(sorted({s['section'] for s in d['segments']}))
[print('GAP', g['kind'], g['detail']) for g in d.get('gaps', [])]
" path/to/textdir/paper.extract.json
```

If `gaps` contains `no_text_extracted`, the paper is **unread**, not empty. Say so
downstream — an image-only PDF that produced nothing must never be reported as a
paper with no relevant content.

## Two hazards, both real

**Reading order is not reliable.** pymupdf4llm reassembles columns paragraph by
paragraph, and on heavily-floated layouts (three-column Science articles are the
worst) it can shuffle them. Two half-sentences from different columns can end up
adjacent — and a quote spliced across that join will *pass* a plain substring check.
The sidecar records `retrieval_method: "pdf_text"` for exactly this reason. Do not
treat PDF-derived text as equivalent to JATS when grounding a quote; prefer JATS
whenever a paper has it.

**Figure text is not prose.** It is kept in its own file so it can be searched for
recall — a gene name that appears only in a figure axis is still a finding — without
ever being quoted as a sentence. Do not blockquote from `figure_text.txt`.

## Calling it from Python

```python
from atlas_chat.services.pdf_text import extract_pdf_text

result = extract_pdf_text("paper.pdf", "textdir")
if not result.has_body_text:
    ...   # record result.gaps; do not conclude the paper is empty
text = result.text_path.read_text()
```
