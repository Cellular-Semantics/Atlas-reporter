#!/usr/bin/env python3
"""PreToolUse hook: curation-mode write guard.

Two-tier write policy:

**Non-trusted users (default)**
  Only paths under ``projects/`` and ``planning/`` may be written.
  Everything else is blocked (allowlist mode).

**Trusted users** (git user.email in ``TRUSTED_USERS``)
  May write anywhere *except* the explicit denylist: ``src/``, ``.claude/``,
  and ``tests/``. These are considered infrastructure — they must go through
  a dev-mode session started from ``CLAUDE_dev.md``.

Exit codes:
  0 — allow the edit
  2 — block the edit (Claude sees the stderr message)
https://docs.anthropic.com/en/docs/claude-code/hooks#exit-code-2-behavior
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

# Trusted users use the denylist path instead of the allowlist.
TRUSTED_USERS = {"ubyndr@gmail.com", "ub2@sanger.ac.uk"}

# Non-trusted: only these top-level zones are writable.
_ALLOWLIST_ZONES = ("projects", "planning")

# Trusted: these top-level zones are always blocked, even in dev sessions.
_DENYLIST_ZONES = ("src", ".claude", "tests")

_PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _get_current_user_email() -> str | None:
    """Return current git user.email, or None if unavailable.

    Overridable via ATLAS_CHAT_HOOK_USER env var for tests:
      - unset      → fall through to ``git config user.email``
      - empty str  → treat as untrusted (simulates no configured user)
      - any value  → use as-is
    """
    override = os.environ.get("ATLAS_CHAT_HOOK_USER")
    if override is not None:
        return override or None
    try:
        result = subprocess.run(
            ["git", "config", "user.email"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        if result.returncode == 0:
            return result.stdout.strip() or None
    except (subprocess.SubprocessError, FileNotFoundError, OSError):
        pass
    return None


def _top_level_zone(file_path: Path) -> str | None:
    """Return the first path component relative to the project root, or None."""
    try:
        rel = file_path.resolve().relative_to(_PROJECT_ROOT)
    except (ValueError, OSError):
        return None
    parts = rel.parts
    return parts[0] if parts else None


def _emit_rejection(file_path: Path, user: str | None, *, trusted: bool) -> None:
    print("\n" + "=" * 64, file=sys.stderr)
    print("BLOCKING EDIT: curation mode — write out of scope", file=sys.stderr)
    print("=" * 64, file=sys.stderr)
    print(f"Target: {file_path}", file=sys.stderr)
    print(f"User:   {user or '(no git user.email set)'}", file=sys.stderr)
    print("", file=sys.stderr)
    if trusted:
        print("Infrastructure paths are blocked even in dev sessions.", file=sys.stderr)
        print("Blocked zones:", file=sys.stderr)
        for zone in _DENYLIST_ZONES:
            print(f"  - {zone}/", file=sys.stderr)
        print("", file=sys.stderr)
        print("To change infrastructure, open a separate CLAUDE_dev.md session", file=sys.stderr)
        print("and make the change through normal code review.", file=sys.stderr)
    else:
        print("In curation mode you may only write under:", file=sys.stderr)
        for zone in _ALLOWLIST_ZONES:
            print(f"  - {zone}/", file=sys.stderr)
        print("", file=sys.stderr)
        print("Edits to src/, .claude/, tests/, docs/, and root files are out of", file=sys.stderr)
        print("scope. Options:", file=sys.stderr)
        print("  - Capture the request as a note under planning/ and stop.", file=sys.stderr)
        print("  - If you are authorised for dev work, start a CLAUDE_dev.md", file=sys.stderr)
        print("    session instead.", file=sys.stderr)
    print("=" * 64 + "\n", file=sys.stderr)


def main() -> None:
    data = json.load(sys.stdin)
    tool_name = data.get("tool_name", "")
    if tool_name not in ("Write", "Edit", "MultiEdit"):
        sys.exit(0)

    file_path_str = data.get("tool_input", {}).get("file_path", "")
    if not file_path_str:
        sys.exit(0)
    file_path = Path(file_path_str)
    zone = _top_level_zone(file_path)
    user = _get_current_user_email()

    if user in TRUSTED_USERS:
        # Trusted path: denylist — block infrastructure zones only.
        if zone in _DENYLIST_ZONES:
            _emit_rejection(file_path, user, trusted=True)
            sys.exit(2)
        sys.exit(0)
    else:
        # Untrusted path: allowlist — only content zones permitted.
        if zone not in _ALLOWLIST_ZONES:
            _emit_rejection(file_path, user, trusted=False)
            sys.exit(2)
        sys.exit(0)


if __name__ == "__main__":
    main()
