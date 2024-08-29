from typing import Any, cast

import httpx
from httpx_oauth.clients.github import PROFILE_ENDPOINT, GitHubOAuth2


class GitHubOAuth2Client(GitHubOAuth2):
    async def get_username(self, token: str) -> str:

        async with httpx.AsyncClient(headers={**self.request_headers, "Authorization": f"token {token}"}) as client:
            response = await client.get(PROFILE_ENDPOINT)
            response.raise_for_status()

            data = cast(dict[str, Any], response.json())
            return data["name"]
