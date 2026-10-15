#!/usr/bin/env python3
"""Regenerate the test project's ``cas.json`` from where it is maintained.

``projects/test_projects/hca_reproductive/cas.json`` is a **copy**. The
original lives at ``projects/HCA_reproductive_atlas_v1/cas.json``, is built
there from the atlas ``obs`` plus the authors' supplementary tables, and is
enriched in place by ``scripts/subatlas_registry.py``. Keeping two
hand-maintained originals of a 5.4 MB file is how they silently diverge.

The copy is byte-for-byte, so drift is a hash comparison:

.. code-block:: bash

    python scripts/sync_test_project_cas.py --check   # exit 1 if they differ
    python scripts/sync_test_project_cas.py           # refresh the copy

Do not edit the copy. A rebuild of the source is an accession-minting event,
not a refresh — see the test project's README.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "projects" / "HCA_reproductive_atlas_v1" / "cas.json"
TARGET = REPO / "projects" / "test_projects" / "hca_reproductive" / "cas.json"


def digest(path: Path) -> str:
    """Return the SHA-1 of ``path``, read in chunks."""
    h = hashlib.sha1()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _short(path: Path) -> str:
    """Path relative to the repo when it is inside it, absolute otherwise."""
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def sync(source: Path, target: Path, *, check_only: bool = False) -> int:
    """Copy ``source`` over ``target``, or report whether they already match.

    Returns a process exit code: 0 when the two agree (or were made to), 1
    when they differ under ``check_only``, 2 when the source is missing.
    """
    if not source.exists():
        print(f"source missing: {source}", file=sys.stderr)
        return 2

    src = digest(source)
    tgt = digest(target) if target.exists() else None

    if src == tgt:
        print(f"up to date ({src[:8]})")
        return 0

    if check_only:
        where = "absent" if tgt is None else tgt[:8]
        print(f"DRIFT: source {src[:8]}, copy {where}", file=sys.stderr)
        print(f"  refresh with: python {Path(__file__).name}", file=sys.stderr)
        return 1

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    print(f"copied {_short(source)} -> {_short(target)} ({src[:8]})")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="report drift without writing; exit 1 if the copy is stale",
    )
    args = parser.parse_args()
    return sync(SOURCE, TARGET, check_only=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
