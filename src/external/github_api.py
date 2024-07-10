from typing import Any, TypedDict

from httpx import AsyncClient, HTTPStatusError

from src.exceptions.common import NotFoundError, ServiceUnavailableError
from src.exceptions.error_codes import ErrorCode
from src.schemas.external.github import UserContributionsByYear, UserContributionYears
from src.setting import settings
from src.template import github_apis as github_api_templates


class GraphQLResponseJson(TypedDict):
    data: dict[str, Any]


class GithubAPI:

    def __init__(self) -> None:
        self.client = AsyncClient(headers={"Authorization": f"Bearer {settings.GITHUB_API_TOKEN}"})

    async def get_user_total_contributions(self, *, username: str) -> dict[int, int]:
        years = await self._get_user_contribution_years(username=username)
        return {year: await self.get_user_contributions_by_year(username=username, year=year) for year in years}

    async def get_user_contributions_by_year(self, *, username: str, year: int) -> int:
        query = github_api_templates.contribution_by_year.format(username=username, year=year)
        res = await self._query_graphql(query)

        data = UserContributionsByYear.model_validate(res["data"])

        if data.user is None:
            raise NotFoundError(ErrorCode.USER_NOT_FOUND)

        return data.user.contributionsCollection.totalCommitContributions

    async def _get_user_contribution_years(self, *, username: str) -> list[int]:
        query = github_api_templates.contribution_years.format(username=username)
        res = await self._query_graphql(query)

        data = UserContributionYears.model_validate(res["data"])

        if data.user is None:
            raise NotFoundError(ErrorCode.USER_NOT_FOUND)

        return data.user.contributionsCollection.contributionYears

    async def _query_graphql(self, *queries: str) -> GraphQLResponseJson:
        query = "{" + "\n".join(queries) + "}"
        res = await self.client.post("https://api.github.com/graphql", json={"query": query})

        try:
            res.raise_for_status()
        except HTTPStatusError as e:
            raise ServiceUnavailableError(ErrorCode.GITHUB_API_SERVICE_UNAVAILABLE) from e

        return res.json()
