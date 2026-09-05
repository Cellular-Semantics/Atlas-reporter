"""CLI for the supplement content assessment.

Thin entry point so the assessment is usable without a Claude Code session:

.. code-block:: bash

    python -m atlas_chat.cli_supplement_assess --store S --doi D --cas cas.json

The implementation lives in :mod:`atlas_chat.services.supplement_assess`.
"""

from __future__ import annotations

from atlas_chat.services.supplement_assess import build_parser, main

__all__ = ["build_parser", "main"]

if __name__ == "__main__":
    raise SystemExit(main())
