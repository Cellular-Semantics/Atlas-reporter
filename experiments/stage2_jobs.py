#!/usr/bin/env python3
"""Generate Stage 2 batch job files.

Batching rule, which is the experiment's integrity constraint:

* `whole` condition — EVERY item legitimately gets the identical whole-paper context,
  so one reader answering many questions from it introduces no contamination. Batch freely.
* `*_b2k` conditions — contexts differ per item, so a reader that saw item X's slice
  while answering item Y could leak. Batched anyway for tractability, in small groups,
  and every answer's quote is checked against sibling contexts afterwards
  (stage2_leakcheck.py). Leakage is therefore detectable, not assumed absent.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).parent
S2 = HERE / "stage2"
JOBS = S2 / "jobs"
BATCH = {"whole": 9, "hybrid_b2k": 7, "document_b2k": 7}
MODELS = ("sonnet", "haiku")
CONDITIONS = ("hybrid_b2k", "document_b2k", "whole")


def main() -> int:
    manifest = json.loads((S2 / "manifest.json").read_text())
    JOBS.mkdir(exist_ok=True)
    for f in JOBS.glob("*.md"):
        f.unlink()

    planned = []
    for model in MODELS:
        for cond in CONDITIONS:
            todo = []
            for it in manifest:
                if cond not in it["conditions"]:
                    continue
                out = S2 / "answers" / f"{it['id']}__{cond}__{model}.json"
                if out.exists():
                    continue  # already run
                todo.append((it, out))
            for i in range(0, len(todo), BATCH[cond]):
                planned.append((model, cond, todo[i:i + BATCH[cond]]))

    for n, (model, cond, group) in enumerate(planned, 1):
        jid = f"J{n:03d}"
        lines = [
            f"# Stage 2 job {jid} — condition `{cond}`",
            "",
            "Follow `../READER_PROMPT.md` rules exactly. Read that file first.",
            "",
            "You have several questions below. For EACH one:",
            "",
            "1. Read ONLY its own CONTEXT file. Do not read any other context file, and do",
            "   not let one question's context inform another's answer.",
            "2. Answer ONLY from that context. If it does not contain the answer, set",
            "   `answerable` false — reporting absence is a correct outcome.",
            "3. `support_quote` must be copied VERBATIM and CONTIGUOUSLY from that context.",
            "   Do NOT join two separate passages into one quote. If the support spans",
            "   non-adjacent text, quote only the single most relevant passage.",
            "4. Write the JSON to its own OUTPUT path.",
            "",
            "Write every output file, then reply with just: DONE " + jid,
            "",
            "---",
            "",
        ]
        for it, out in group:
            ctx = HERE / it["conditions"][cond]["path"]
            lines += [
                f"## {it['id']}",
                f"CONTEXT: {ctx}",
                f"QUESTION: {it['question']}",
                f"OUTPUT:  {out}",
                "",
            ]
        (JOBS / f"{jid}.md").write_text("\n".join(lines))
        print(f"{jid}  {model:7} {cond:14} {len(group):2} items")

    (S2 / "jobs_index.json").write_text(json.dumps(
        [{"job": f"J{n:03d}", "model": m, "condition": c,
          "items": [i["id"] for i, _ in g]} for n, (m, c, g) in enumerate(planned, 1)], indent=1))
    print(f"\n{len(planned)} jobs covering {sum(len(g) for _, _, g in planned)} reads")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
