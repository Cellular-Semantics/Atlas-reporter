from __future__ import annotations

import time
from datetime import UTC, datetime, timedelta

import httpx
import jwt

from github_app_posting.config import GitHubAppConfig
from github_app_posting.exceptions import CredentialError, GitHubAPIError

_GITHUB_API = "https://api.github.com"
_HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
_REFRESH_BUFFER_SECONDS = 60
_JWT_LIFETIME_SECONDS = 540  # 9 min; GitHub max is 10 min


class GitHubAppAuth:
    """Manages GitHub App JWT minting and installation token exchange with caching."""

    def __init__(self, config: GitHubAppConfig) -> None:
        self._config = config
        self._private_key = self._load_key()
        self._cached_token: str | None = None
        self._token_expires_at: datetime | None = None

    def _load_key(self) -> str:
        try:
            return self._config.private_key_path.read_text()
        except OSError as exc:
            raise CredentialError(
                f"Cannot read private key {self._config.private_key_path}: {exc}"
            ) from exc

    def _make_jwt(self) -> str:
        now = int(time.time())
        payload = {
            "iat": now - 60,  # issued 60s in the past — clock skew guard
            "exp": now + _JWT_LIFETIME_SECONDS,
            "iss": self._config.app_id,
        }
        return jwt.encode(payload, self._private_key, algorithm="RS256")

    def _fetch_installation_token(self) -> tuple[str, datetime]:
        app_jwt = self._make_jwt()
        url = f"{_GITHUB_API}/app/installations/{self._config.installation_id}/access_tokens"
        with httpx.Client(timeout=30) as client:
            resp = client.post(
                url,
                headers={**_HEADERS, "Authorization": f"Bearer {app_jwt}"},
            )
        if not resp.is_success:
            raise GitHubAPIError(resp.status_code, resp.text)
        data = resp.json()
        token = data["token"]
        expires_at = datetime.fromisoformat(data["expires_at"].replace("Z", "+00:00"))
        return token, expires_at

    def get_token(self) -> str:
        """Return a valid installation token, refreshing if near expiry."""
        needs_refresh = (
            self._cached_token is None
            or self._token_expires_at is None
            or datetime.now(UTC)
            >= self._token_expires_at - timedelta(seconds=_REFRESH_BUFFER_SECONDS)  # noqa: E501
        )
        if needs_refresh:
            self._cached_token, self._token_expires_at = self._fetch_installation_token()
        return self._cached_token  # type: ignore[return-value]
