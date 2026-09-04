"""Batch the items into reader job files, one file per subagent call.

Items sharing an identical context may be batched freely (handoff rule 6). The
``blind`` and ``whole`` arms share one context each, so their batch size is set
only by output length. The ``local`` arm has a context per item, so its batches
are small and the run must be leak-checked afterwards.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

BATCH = {"blind": 28, "whole": 14, "local": 7, "asta-sep": 7, "asta-comb": 7, "local-comb": 7}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", type=Path, required=True)
    ap.add_argument("--arms", nargs="+", default=None)
    args = ap.parse_args()

    root = args.dir
    manifest = json.loads((root / "manifest.json").read_text())["items"]
    contract = (root / "READER_PROMPT.md").read_text()
    whole = (root / "contexts" / "whole" / "shared.txt").read_text()

    jobs_dir = root / "jobs"
    jobs_dir.mkdir(exist_ok=True)
    for old in jobs_dir.glob("*.md"):
        if args.arms is None or any(old.name.startswith(a) for a in args.arms):
            old.unlink()

    written = []
    for arm in ("blind", "whole", "local", "asta-sep", "asta-comb", "local-comb"):
        if args.arms and arm not in args.arms:
            continue
        size = BATCH[arm]
        # Deal items round-robin by label rather than slicing consecutively.
        # Items are authored label-major, so a consecutive slice puts an item
        # next to its own label's other axes -- and the local arm's per-item
        # contexts then overlap heavily, which is how two reads quoted a
        # sibling's context in the first run.
        n_batches = (len(manifest) + size - 1) // size
        dealt: list[list[dict]] = [[] for _ in range(n_batches)]
        for k, item in enumerate(sorted(manifest, key=lambda m: (m["axis"], m["label"]))):
            dealt[k % n_batches].append(item)
        batches = [b for b in dealt if b]
        for n, batch in enumerate(batches, 1):
            parts = [contract, f"\n# Arm: {arm} — batch {n}\n"]
            if arm == "whole":
                parts.append(f"## Context (shared by every question below)\n\n{whole}\n")
            elif arm == "blind":
                parts.append("## Context\n\nNo context is supplied for this batch.\n")
            parts.append("\n# Questions\n")
            for item in batch:
                parts.append(f"\n## {item['id']}\n\n{item['question']}\n")
                if arm not in ("blind", "whole"):
                    ctx = (root / "contexts" / arm / f"{item['id']}.txt").read_text()
                    parts.append(f"\n### Context for {item['id']}\n\n{ctx}\n")
            path = jobs_dir / f"{arm}-{n:02d}.md"
            path.write_text("\n".join(parts))
            written.append((path.name, len(batch), len(path.read_text()) // 4))

    for name, n, tok in written:
        print(f"  {name:<14} {n:>3} items  ~{tok:>6} tokens")
    print(f"{len(written)} job files, {sum(n for _, n, _ in written)} reads total")


if __name__ == "__main__":
    main()
