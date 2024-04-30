from unittest.mock import Mock

from fastapi import status
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession

from src.dependencies.external import get_github_api
from src.main import app
from tests.utils.user import get_user


class GithubAPIFake:
    def __init__(self, contributions: dict[int, int]) -> None:
        self.contribs = contributions

    async def get_user_total_contributions(self, *args, **kwargs) -> dict[int, int]:
        return self.contribs

    async def get_user_contributions_by_year(self, *args, year: int, **kwargs) -> int:
        return self.contribs[year]


async def test_get_pokemons_should_create_user(client: AsyncClient, session: AsyncSession):
    contribs = {
        2021: 50,
        2022: 200,
        2023: 0,
        2024: 100,
    }
    app.dependency_overrides[get_github_api] = lambda: Mock(wraps=GithubAPIFake(contribs))

    res = await client.get("/pokemons/2jun0")
    assert res.status_code == status.HTTP_200_OK

    user = await get_user(session, username="2jun0")
    assert user is not None
    for cp in user.commit_points:
        assert cp.year in contribs
        assert contribs[cp.year] == cp.commit_point
