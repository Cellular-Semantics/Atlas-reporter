"""Pull the judge-decided reads out of both runs so a human can check them.

More than half of every arm's score is set by an LLM judge, not by string
matching. Aggregate numbers from those arms are only as good as the judge, so
this writes the underlying cases out in full and in a form that can be checked
without opening anything else:

* the question, the curator's intended answer, and the gold span;
* the gold span shown in situ, in the paragraph of context it came from;
* every quote each reader gave, verbatim;
* for each quote, whether it is genuinely in that item's own context, and
  exactly where -- file and paragraph number;
* whether the reader quoted the same paragraph the gold span is in, which is
  usually what separates a correct read from a substituted one;
* the judge's verdict and its stated reason.

Quote verification reuses ``score.py``'s ``normalise`` and ``in_context`` rather
than reimplementing them, so a quote marked verbatim here is verbatim by the
same test the scorer applied.

    uv run python experiments/stage3b/examples.py --out examples_for_review.md
    uv run python experiments/stage3b/examples.py --only-disagreements
"""

from __future__ import annotations

import argparse
import glob
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from score import in_context, load_answers, normalise  # noqa: E402

RUNS = {"Opus/Fable": ROOT / "runs/run1-mixed", "Sonnet": ROOT}
ARMS = ["whole", "local", "local-comb", "asta-sep", "asta-comb"]
WINDOW = 320  # characters of surrounding text shown either side of the gold span


def paragraphs(arm: str, item_id: str) -> list[str]:
    """The context as the reader saw it, split into the blocks it was built from."""
    path = context_path(arm, item_id)
    if not path.exists():
        return []
    return [normalise(p) for p in path.read_text().split("\n\n") if p.strip()]


def context_path(arm: str, item_id: str) -> Path:
    """Contexts live in one place. Both runs read identical context files -- that is
    what makes them comparable -- so ``runs/run1-mixed`` deliberately has no copy."""
    if arm == "whole":
        return ROOT / "contexts/whole/shared.txt"
    return ROOT / "contexts" / arm / f"{item_id}.txt"


def arm_contexts(arm: str, exclude: str) -> str:
    """Every other context file in this arm, concatenated.

    Used only to tell a leaked quote from an invented one. Scope is the whole arm
    rather than the reader's actual batch: wider than the truth, but it errs the
    safe way -- it can call a leak a leak, never an invention a leak. ``score.py``
    uses the same fallback when the batching record is missing.
    """
    d = ROOT / "contexts" / arm
    if arm == "whole" or not d.is_dir():
        return ""
    return normalise(" ".join(p.read_text() for p in sorted(d.glob("*.txt"))
                              if p.stem != exclude))


def locate(quote: str, paras: list[str]) -> int | None:
    """1-based index of the paragraph containing the quote, or None."""
    for n, p in enumerate(paras, 1):
        if in_context(quote, p):
            return n
    return None


def in_situ(span: str, paras: list[str]) -> tuple[int | None, str]:
    """The gold span with its surrounding text, so the reader can be judged in context."""
    n = locate(span, paras)
    if n is None:
        return None, ""
    para = paras[n - 1]
    i = para.find(span.rstrip(".,;: "))
    if i < 0:
        return n, para
    start, end = max(0, i - WINDOW), min(len(para), i + len(span) + WINDOW)
    text = ("… " if start else "") + para[start:end] + (" …" if end < len(para) else "")
    return n, text


def load_verdicts(run_dir: Path) -> dict[tuple[str, str], dict]:
    out = {}
    for path in glob.glob(str(run_dir / "verdicts" / "*.json")):
        for v in json.loads(Path(path).read_text()):
            out[(v["arm"], v["id"])] = v
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--arm", default=None, help="restrict to one context arm")
    ap.add_argument("--only-disagreements", action="store_true",
                    help="only cases where the two runs got different outcomes")
    args = ap.parse_args()
    out = args.out or ROOT / ("examples_disagreements.md" if args.only_disagreements
                              else "examples_for_review.md")

    manifest = json.loads((ROOT / "manifest.json").read_text())
    items = {i["id"]: i for i in manifest["items"]}
    paper = manifest["paper"]

    rows = {name: {(r["arm"], r["id"]): r for r in json.loads((d / "final.json").read_text())}
            for name, d in RUNS.items()}
    verdicts = {name: load_verdicts(d) for name, d in RUNS.items()}

    arms = [args.arm] if args.arm else ARMS
    lines = [
        "# Judged reads, for human review", "",
        f"Source paper: **{paper}** — every quote below is text from this paper and",
        "nothing else. The reader saw only the context block named under each case.", "",
        "Each case had its outcome set by an Opus judge rather than by string matching.",
        "The readers' quotes were machine-verified as verbatim before the judge saw them,",
        "so the judge was ruling only on whether the answer *meant* the right thing.",
        "In run 1 the judge was Opus grading Opus's own answers; that is the main reason",
        "to check these by hand.", "",
        "`verbatim` on a quote means it is an exact substring of that item's own context,",
        "by the same test the scorer used. `leaked` means it is real text from the paper",
        "that reached the reader through a different question batched with this one —",
        "a flaw in how the batch was built, not a fabrication by the reader.", "",
        "---", "",
    ]
    n = 0
    for arm in arms:
        block: list[str] = []
        answers = {name: load_answers(d, arm) for name, d in RUNS.items()}
        for iid, item in items.items():
            got = {m: rows[m].get((arm, iid)) for m in RUNS}
            if not all(got.values()):
                continue
            if not any(g["needs_judge"] for g in got.values()):
                continue
            if args.only_disagreements and len({g["outcome"] for g in got.values()}) == 1:
                continue
            n += 1
            paras = paragraphs(arm, iid)
            others = arm_contexts(arm, iid)
            block.append(f"### {iid} — {item['axis']}, expect {item['expect']}\n")
            block.append(f"**Question** {item['question']}\n")

            gold_para = None
            if item["expect"] == "present":
                block.append(f"**Intended answer** {item['answer']}\n")
                gold_para, shown = in_situ(normalise(item["span"]), paras)
                where = (f"paragraph {gold_para} of {len(paras)}" if gold_para
                         else "**not in this context** — the retriever never supplied it")
                block.append(f"**Gold span** ({where})\n")
                block.append(f"> {item['span']}\n")
                if shown:
                    block.append("**The gold span in its paragraph**\n")
                    block.append(f"> {shown}\n")
            else:
                block.append("**Intended answer** decline — the paper says nothing about "
                             "this cell type's structure or morphology.\n")
            if item.get("hazard"):
                block.append(f"**Hazard note given to the judge** {item['hazard']}\n")

            for m in RUNS:
                g, v = got[m], verdicts[m].get((arm, iid))
                why = f" — judge: *{v['why']}*" if v else ""
                block.append(f"**{m}** → `{g['outcome']}`{why}\n")
                block.append(f"> {g['reader_answer']}\n")
                quotes = (answers[m].get(iid) or {}).get("quotes") or []
                if not quotes:
                    block.append("*No quotes given.*\n")
                for q in quotes:
                    nq = normalise(q)
                    where = locate(nq, paras)
                    if where:
                        tag = f"verbatim, paragraph {where}"
                        if gold_para and where != gold_para:
                            tag += f" — **not the gold span's paragraph ({gold_para})**"
                        elif gold_para:
                            tag += " — same paragraph as the gold span"
                    elif others and in_context(nq, others):
                        tag = "**leaked** — from another question's context"
                    else:
                        tag = "**not found in the context supplied**"
                    block.append(f"- *{tag}*\n")
                    block.append(f"  > {q}\n")
            block.append(f"*Context both readers saw: `{context_path(arm, iid)}`*\n")
            block.append("---\n")
        if block:
            lines.append(f"## Context: {arm}\n")
            lines.extend(block)

    out.write_text("\n".join(lines))
    print(f"wrote {out} — {n} judged cases")


if __name__ == "__main__":
    main()
