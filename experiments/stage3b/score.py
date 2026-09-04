"""Score the Stage 3b run.

Everything decidable without a model is decided here; only genuinely
interpretive calls are handed to a judge, and items resolved here can never
reach it. That containment is deliberate — in Stage 2 ten already-judged-correct
answers were reported wrong because judge-scored items fell through into an
entity branch.

The five rules this encodes, each of which cost a correction cycle before:

1. No key is derived from prose. Present items carry an authored ``answer``;
   whether a reader matched it is a judgement, so it goes to the judge.
2. ``expect`` is tested explicitly, never by truthiness. ``absent`` means the
   paper has nothing to say, which is different from a passage being withheld.
3. A decline is right or wrong depending on the group. For ``expect: absent`` it
   is the correct answer. For ``expect: present`` it is a miss — but an *honest*
   one when the gold span never reached the context, which is a retrieval
   failure and not the reader's.
4. Grounded is not correct. ``fabricated`` (quote not in context) and
   ``substituted`` (quote real, claim not supported by it) stay separate from
   ``correct``.
5. A decline is never sent to a judge. It will be called incorrect for having
   no answer.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ARMS = ("blind", "whole", "local", "asta-sep", "asta-comb", "local-comb")


def normalise(text: str) -> str:
    text = re.sub(r"[‘’]", "'", text)
    text = re.sub(r"[“”]", '"', text)
    text = text.replace("–", "-").replace("—", "-").replace("−", "-")
    return re.sub(r"\s+", " ", text).strip()


def in_context(quote: str, context: str) -> bool:
    """Is the quote present, allowing only added sentence-final punctuation?

    A reader that copies a clause and closes it with a full stop has not
    invented anything -- the claim is still checkable against the source, which
    is what grounding means. Splices and inventions are unaffected: neither
    becomes a substring by dropping a trailing period.
    """
    if quote in context:
        return True
    trimmed = quote.rstrip(".,;: ")
    return bool(trimmed) and trimmed in context


def context_for(root: Path, arm: str, item_id: str) -> str:
    if arm == "blind":
        return ""
    if arm == "whole":
        return normalise((root / "contexts" / "whole" / "shared.txt").read_text())
    return normalise((root / "contexts" / arm / f"{item_id}.txt").read_text())


def load_answers(root: Path, arm: str) -> dict[str, dict]:
    """Answers for one arm. ``localfix-*`` files are singleton re-reads and are
    loaded last so they override the batched read they replace."""
    out: dict[str, dict] = {}
    paths = sorted(p for p in (root / "answers").glob(f"{arm}-*.json")
                   if arm != "local" or not p.name.startswith("local-comb"))
    if arm == "local":
        paths += sorted((root / "answers").glob("localfix-*.json"))
    for path in paths:
        raw = path.read_text().strip()
        # Readers sometimes wrap the array in a fenced block.
        raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw)
        for obj in json.loads(raw):
            out[obj["id"]] = obj
    return out


def classify(item: dict, answer: dict | None, context: str, siblings: str = "") -> dict:
    """One item, one arm -> an outcome, decided without a model where possible.

    ``siblings`` is the concatenated context of the other items batched with
    this one. A quote absent from the item's own context but present in a
    sibling's is **leaked**, not fabricated: the reader quoted real paper text
    that it should not have been able to see. That is a flaw in how the batch
    was built, and scoring it as fabrication would blame the reader for the
    harness's mistake.
    """
    if answer is None:
        return {"outcome": "no_answer", "needs_judge": False}

    found = bool(answer.get("found"))
    quotes = [normalise(q) for q in (answer.get("quotes") or []) if q and q.strip()]
    verbatim = [q for q in quotes if q and in_context(q, context)]
    off_context = [q for q in quotes if not in_context(q, context)]
    leaked = [q for q in off_context if siblings and in_context(q, siblings)]
    bogus = [q for q in off_context if q not in leaked]

    # Rule 2 / rule 3: test `expect` explicitly, and let the group decide.
    if item["expect"] == "absent":
        if not found:
            return {"outcome": "correct_decline", "needs_judge": False}
        if bogus or not quotes:
            return {"outcome": "fabricated", "needs_judge": False, "bad_quotes": bogus}
        if leaked:
            return {"outcome": "leaked", "needs_judge": False, "leaked_quotes": leaked}
        # Quote is real; whether the answer actually asserts morphology is a
        # judgement, so it goes to the judge rather than being assumed wrong.
        return {"outcome": "pending", "needs_judge": True, "quotes": verbatim}

    # expect == "present"
    if not found:
        # Rule 5: never judge a decline. Rule 3: distinguish the reader's failure
        # from the retriever's.
        honest = not item.get("span_in_context", True)
        return {"outcome": "honest_miss" if honest else "miss", "needs_judge": False}

    if not quotes:
        return {"outcome": "unsupported", "needs_judge": False}
    if bogus:
        # Rule 4, and the splicing check: a spliced quote is not a substring.
        return {"outcome": "fabricated", "needs_judge": False, "bad_quotes": bogus}
    if leaked:
        return {"outcome": "leaked", "needs_judge": False, "leaked_quotes": leaked}
    return {"outcome": "pending", "needs_judge": True, "quotes": verbatim}


def batch_siblings(root: Path, arm: str) -> dict[str, str]:
    """item id -> concatenated context of every other item the same reader saw.

    Scope is the **reader agent**, not the job file. Agents were given several
    job files to process in sequence, so a context supplied for job file 1 is
    still in the agent's window when it answers job file 3. Scoping the leak
    check to one job file therefore misses real cross-contamination and
    reports it as fabrication instead -- blaming the reader for the harness's
    packing decision. `agent_job_groups.json` records what each agent actually
    read; without it we fall back to arm-wide scope, which is wider but errs in
    the same safe direction.
    """
    if arm in ("blind", "whole"):
        return {}

    contexts = {p.stem: normalise(p.read_text()) for p in (root / "contexts" / arm).glob("*.txt")}

    # job file -> the items in it
    job_items: dict[str, list[str]] = {}
    for job in (root / "jobs").glob(f"{arm}-*.md"):
        job_items[job.stem] = re.findall(r"^## (G\d+-\S+)$", job.read_text(), re.M)

    groups_path = root / "agent_job_groups.json"
    if groups_path.exists():
        groups = [g for g in json.loads(groups_path.read_text())]
    else:
        groups = [list(job_items)]

    # item -> every item any co-reading agent also saw
    seen_with: dict[str, set[str]] = {}
    for group in groups:
        items: list[str] = []
        for job in group:
            items.extend(job_items.get(job, []))
        for iid in items:
            seen_with.setdefault(iid, set()).update(i for i in items if i != iid)

    return {
        iid: normalise(" ".join(contexts.get(o, "") for o in sorted(others)))
        for iid, others in seen_with.items()
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", type=Path, required=True)
    args = ap.parse_args()
    root = args.dir

    items = {i["id"]: i for i in json.loads((root / "manifest.json").read_text())["items"]}

    results: list[dict] = []
    for arm in ARMS:
        if not list((root / "answers").glob(f"{arm}-*.json")):
            continue
        answers = load_answers(root, arm)
        siblings = batch_siblings(root, arm)
        for iid, item in items.items():
            ctx = context_for(root, arm, iid)
            row = dict(item)
            row["span_in_context"] = bool(item.get("span") and normalise(item["span"]) in ctx)
            verdict = classify(row, answers.get(iid), ctx, siblings.get(iid, ""))
            results.append(
                {
                    "arm": arm,
                    "id": iid,
                    "axis": item["axis"],
                    "expect": item["expect"],
                    "span_in_context": row["span_in_context"],
                    "reader_answer": (answers.get(iid) or {}).get("answer"),
                    **verdict,
                }
            )

    (root / "scores.json").write_text(json.dumps(results, indent=1))

    print(f"{root}/scores.json: {len(results)} scored reads\n")
    for arm in ARMS:
        rows = [r for r in results if r["arm"] == arm]
        if not rows:
            continue
        c = Counter(r["outcome"] for r in rows)
        print(f"  {arm:<7} n={len(rows):<4} " + "  ".join(f"{k}={v}" for k, v in c.most_common()))
    pending = [r for r in results if r["needs_judge"]]
    print(f"\n  awaiting judge: {len(pending)}")
    (root / "judge_worklist.json").write_text(json.dumps(pending, indent=1))


if __name__ == "__main__":
    main()
