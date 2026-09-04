"""Build judge job files for the reads the deterministic scorer could not settle.

Only two questions reach a judge, and neither is answerable mechanically:

* **present items** — the quote is already verified verbatim, so grounding is
  not in question. What remains is whether the quote *supports* the reader's
  claim and whether the claim matches the intended answer. A grounded answer
  that is not the paper's claim is ``substituted``, not ``correct``.
* **absent items** — the reader found a quote and said something. Did it
  actually assert morphology, or did it hedge and effectively decline?

Declines never appear here (handoff rule 5): a judge asked to adjudicate a
decline will call it incorrect for having no answer.

The judge sees the intended answer and any hazard note. Hazards exist because
three items are mis-scorable without them — most sharply the DPYSL2+ marker
item, where the paper names AGR2 as new and BARX2/SOX9 as previously reported.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

CONTRACT = """\
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
"""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", type=Path, required=True)
    ap.add_argument("--batch", type=int, default=14)
    args = ap.parse_args()
    root = args.dir

    items = {i["id"]: i for i in json.loads((root / "manifest.json").read_text())["items"]}
    pending = json.loads((root / "judge_worklist.json").read_text())
    # Cases that already have a verdict from an earlier pass keep it -- only
    # unjudged cases get new job files.
    done: set[tuple[str, str]] = set()
    vdir = root / "verdicts"
    if vdir.exists():
        import re as _re
        for vp in vdir.glob("*.json"):
            raw = _re.sub(r"^```(?:json)?\s*|\s*```$", "", vp.read_text().strip())
            for v in json.loads(raw):
                done.add((v["arm"], v["id"]))
    pending = [r for r in pending if (r["arm"], r["id"]) not in done]

    jobs = root / "judge_jobs"
    jobs.mkdir(exist_ok=True)
    existing = len(list(jobs.glob("*.md")))

    batches = [pending[i : i + args.batch] for i in range(0, len(pending), args.batch)]
    for n, batch in enumerate(batches, existing + 1):
        parts = [CONTRACT, f"\n# Cases (batch {n})\n"]
        for row in batch:
            item = items[row["id"]]
            parts.append(f"\n## arm: {row['arm']} | id: {row['id']} | kind: {row['expect']}\n")
            parts.append(f"**Question:** {item['question']}\n")
            parts.append(f"**Intended answer:** {item['answer']}\n")
            if item.get("hazard"):
                parts.append(f"**Hazard:** {item['hazard'].strip()}\n")
            parts.append(f"**Reader's answer:** {row.get('reader_answer')}\n")
            for q in row.get("quotes") or []:
                parts.append(f"**Reader's quote:** “{q}”\n")
        (jobs / f"judge-{n:02d}.md").write_text("\n".join(parts))

    for path in sorted(jobs.glob("*.md")):
        print(f"  {path.name}  ~{len(path.read_text())//4} tokens")
    print(f"{len(batches)} judge jobs over {len(pending)} cases")


if __name__ == "__main__":
    main()
