from __future__ import annotations

import json
import os
from pathlib import Path

from pydantic import BaseModel

from github_app_posting.exceptions import CredentialError

_CONFIG_PATH = Path("~/.config/github_app_posting/config.json").expanduser()

_ENV_APP_ID = "GITHUB_APP_ID"
_ENV_KEY_PATH = "GITHUB_APP_PRIVATE_KEY_PATH"
_ENV_INSTALL_ID = "GITHUB_APP_INSTALLATION_ID"


class GitHubAppConfig(BaseModel):
    app_id: str
    private_key_path: Path
    installation_id: str

    model_config = {"arbitrary_types_allowed": True}


def load_config() -> GitHubAppConfig:
    """Discover GitHub App credentials.

    Priority:
    1. Environment variables GITHUB_APP_ID, GITHUB_APP_PRIVATE_KEY_PATH,
       GITHUB_APP_INSTALLATION_ID (all three must be set if any is set).
    2. ~/.config/github_app_posting/config.json with keys app_id,
       private_key_path, installation_id.

    Raises CredentialError if credentials cannot be resolved.
    """
    env_vals = {
        "app_id": os.environ.get(_ENV_APP_ID),
        "private_key_path": os.environ.get(_ENV_KEY_PATH),
        "installation_id": os.environ.get(_ENV_INSTALL_ID),
    }
    present = {k for k, v in env_vals.items() if v is not None}

    if present:
        missing = set(env_vals) - present
        if missing:
            names = {
                "app_id": _ENV_APP_ID,
                "private_key_path": _ENV_KEY_PATH,
                "installation_id": _ENV_INSTALL_ID,
            }
            missing_vars = ", ".join(names[k] for k in sorted(missing))
            raise CredentialError(
                f"Some GitHub App env vars are set but {missing_vars} is missing. "
                "Set all three or none."
            )
        return _build_config(env_vals)

    if _CONFIG_PATH.exists():
        try:
            raw = json.loads(_CONFIG_PATH.read_text())
        except json.JSONDecodeError as exc:
            raise CredentialError(f"Invalid JSON in {_CONFIG_PATH}: {exc}") from exc
        missing_keys = {"app_id", "private_key_path", "installation_id"} - set(raw)
        if missing_keys:
            raise CredentialError(
                f"Config file {_CONFIG_PATH} is missing required keys: "
                + ", ".join(sorted(missing_keys))
            )
        return _build_config(raw)

    raise CredentialError(
        "No GitHub App credentials found. Provide either:\n"
        f"  Env vars: {_ENV_APP_ID}, {_ENV_KEY_PATH}, {_ENV_INSTALL_ID}\n"
        f"  Config file: {_CONFIG_PATH} with keys app_id, private_key_path, installation_id"
    )


def _build_config(raw: dict[str, str | None]) -> GitHubAppConfig:
    path = Path(str(raw["private_key_path"])).expanduser()
    if not path.exists():
        raise CredentialError(f"Private key file not found: {path}")
    if not path.is_file():
        raise CredentialError(f"Private key path is not a file: {path}")
    return GitHubAppConfig(
        app_id=str(raw["app_id"]),
        private_key_path=path,
        installation_id=str(raw["installation_id"]),
    )
