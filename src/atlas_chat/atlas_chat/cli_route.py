"""CLI for the subatlas routing table.

Thin entry point so the table is inspectable without a Claude Code session:

.. code-block:: bash

    python -m atlas_chat.cli_route --cas cas.json --label "Ligament fibroblast"

The implementation lives in :mod:`atlas_chat.services.subatlas_routing`.
"""

from __future__ import annotations

from atlas_chat.services.subatlas_routing import build_parser, main

__all__ = ["build_parser", "main"]

if __name__ == "__main__":
    raise SystemExit(main())
