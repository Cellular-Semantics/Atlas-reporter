# Plan: Curation-guard dev/content mode separation

Date: 2026-06-23 · Author: do12 (dev-mode planning)
Standalone task — independent of `plan_project_initialization_v2_2026-06-23.md`
(but a prerequisite for comfortably doing that infra work).

## Context

`.claude/hooks/curation_guard.py` gates writes by **git identity**, not by
**session intent**:

- Untrusted users → allowlist (`projects/`, `planning/` only).
- Trusted users (`TRUSTED_USERS`) → denylist: blocked from `src/`, `.claude/`,
  `tests/` *in every session*.

Two problems this causes:

1. **Infra work is impossible without hand-editing the hook.** Even a trusted
   developer can't write `src/` or `.claude/` because the denylist blocks those
   for everyone. Today the only way in is to manually empty `_DENYLIST_ZONES` or
   disable the PreToolUse hook — fragile and easy to leave in a bad state.
2. **No separation of dev vs content.** Adding `projects/` to the denylist (to
   stop dev sessions touching content) would *also* block the same trusted user
   from legitimate curation, because identity can't distinguish the two session
   types.

The fix is a **per-session mode signal**, decoupled from identity.

## Goal

One env-driven switch so a session is explicitly either **dev** (infra,
no content) or **curation** (content, no infra), with no hand-editing of the
hook or settings per task.

## Design

Add `ATLAS_CHAT_MODE` (default `curation`) to `curation_guard.py`. Replace the
identity-only branch with mode-first logic:

```python
MODE = os.environ.get("ATLAS_CHAT_MODE", "curation")
CONTENT_ZONES = ("projects",)          # curation-only
SHARED_ZONES  = ("planning",)          # writable in both modes

if MODE == "dev":
    if user not in TRUSTED_USERS:
        block("dev mode requires a trusted git user.email")
    if zone in CONTENT_ZONES:
        block("dev sessions must not edit content (projects/)")
    allow                               # src/ .claude/ tests/ docs/ root/ planning/
else:  # curation (default)
    if zone not in (CONTENT_ZONES + SHARED_ZONES):
        block                           # infra blocked; content + plans only
    allow
```

Resulting matrix:

| Zone | curation (default) | dev (`ATLAS_CHAT_MODE=dev`, trusted) |
|---|---|---|
| `projects/` | ✅ | ❌ |
| `planning/` | ✅ | ✅ |
| `src/ .claude/ tests/ docs/ root` | ❌ | ✅ |
| outside repo | ❌ (untrusted) / ✅ (trusted)* | ✅ |

\* Decide explicitly: keep current behaviour where trusted users can write
outside the repo, or tighten. Lean toward allowing it in dev mode only.

**Usage:** dev sessions launched with `ATLAS_CHAT_MODE=dev claude`; everything
else stays curation. The existing `ATLAS_CHAT_HOOK_USER` test override is kept.

## Files

- `.claude/hooks/curation_guard.py` — mode logic above; update module docstring
  and the rejection messages (mention the mode + how to enter dev).
- `tests/unit/test_curation_guard.py` — extend (drive via subprocess with
  `ATLAS_CHAT_HOOK_USER` + `ATLAS_CHAT_MODE` env): cover
  curation-blocks-infra, curation-allows-projects, dev-allows-infra,
  dev-blocks-projects, dev-requires-trusted, default-mode-is-curation.
- `CLAUDE_dev.md` / `CLAUDE.md` — document the `ATLAS_CHAT_MODE=dev` launch and
  the new matrix (replace the current "trusted denylist" description).
- `README.md` (Development section) — note `ATLAS_CHAT_MODE=dev claude`.

## Rollout (avoid self-lockout)

The hook reads the script per call and the env at launch. Saving the new guard
makes it live immediately as `curation`, which would block further infra edits
in a session that wasn't launched with `ATLAS_CHAT_MODE=dev`. Therefore:

1. Make this change in a session launched with `ATLAS_CHAT_MODE=dev` set, **or**
2. Do it under a temporary manual unblock (`_DENYLIST_ZONES = ()`), save the
   rewritten guard **last**, then restart with `ATLAS_CHAT_MODE=dev claude`.

User intends to **restart the session** after these hook/permission changes to
pick them up cleanly.

## Verification

- `uv run pytest -m unit tests/unit/test_curation_guard.py` green.
- Manual: in a `curation` session, a `src/` write is blocked and a `projects/`
  write succeeds; in an `ATLAS_CHAT_MODE=dev` session (trusted), the reverse.
- Untrusted user in dev mode is blocked with the "requires trusted user"
  message.
