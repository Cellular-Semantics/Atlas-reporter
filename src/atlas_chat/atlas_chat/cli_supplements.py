"""CLI for the supplement store.

Thin entry point so the store is usable without a Claude Code session:

.. code-block:: bash

    python -m atlas_chat.cli_supplements inventory --jats paper.jats.xml
    python -m atlas_chat.cli_supplements adopt --store S --doi D --incoming DIR
    python -m atlas_chat.cli_supplements unpack --store S --doi D
    python -m atlas_chat.cli_supplements outline --file tables.xlsx
    python -m atlas_chat.cli_supplements slice --file tables.xlsx --locator "Table 12"

The implementation lives in :mod:`atlas_chat.services.supplement_store`.
"""

from __future__ import annotations

from atlas_chat.services.supplement_store import build_parser, main

__all__ = ["build_parser", "main"]

if __name__ == "__main__":
    raise SystemExit(main())
