from typing import Any

from httpx import AsyncClient, HTTPStatusError

from src.exceptions.external import GithubAPIRequestFailedError
from src.setting import settings
from src.template import github_api as github_api_templates


class GithubAPI:

    def __init__(self) -> None:
        self.client = AsyncClient(headers={"Authorization": f"Bearer {settings.GITHUB_API_TOKEN}"})

    async def get_user_total_contributions(self, *, username: str) -> dict[int, int]:
        years = await self._get_user_contribution_years(username=username)
        return {year: await self.get_user_contributions_by_year(username=username, year=year) for year in years}

    async def get_user_contributions_by_year(self, *, username: str, year: int) -> int:
        query = github_api_templates.contribution.format(username=username, start_year=year, end_year=year)
        data = await self._query_graphql(query)
        return data["user"]["contributionsCollection"]["totalCommitContributions"]

    async def _get_user_contribution_years(self, *, username: str) -> list[int]:
        query = github_api_templates.contribution_years.format(username=username)
        data = await self._query_graphql(query)
        return data["user"]["contributionsCollection"]["contributionYears"]

    async def _query_graphql(self, *queries: str) -> dict[str, Any]:
        query = "{" + "\n".join(queries) + "}"
        res = await self.client.post("https://api.github.com/graphql", json={"query": query})

        try:
            res.raise_for_status()
        except HTTPStatusError as e:
            raise GithubAPIRequestFailedError from e

        res_json = res.json()
        if "data" not in res_json:
            raise GithubAPIRequestFailedError

        return res_json["data"]
