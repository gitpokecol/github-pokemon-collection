from datetime import datetime, timezone

from sqlmodel.ext.asyncio.session import AsyncSession

from src.exceptions.external import GithubAPIRequestFailedError, GithubAPIUnavailableError
from src.external.github_api import GithubAPI
from src.renders.svg import SVGRenderer
from src.services.user import UserService


class PokemonsFacade:
    def __init__(self, *, user_service: UserService, github_api: GithubAPI, renderer: SVGRenderer) -> None:
        self._user_service = user_service
        self._github_api = github_api
        self._renderer = renderer

    async def render_pokemons(self, *, session: AsyncSession, username: str) -> str:
        if await self._user_service.exists_by_username(session=session, username=username):
            try:
                # TODO: updating commit point should be in background
                now_year = datetime.now(timezone.utc).year
                commit_point = await self._get_commit_point(username, now_year)
                user = await self._user_service.update_commit_point(
                    session=session, username=username, year=now_year, commit_point=commit_point
                )
            except GithubAPIRequestFailedError:
                pass  # ignore error
        else:
            try:
                commit_points = await self._get_commit_points(username)
                user = await self._user_service.create_new_user(
                    session=session, username=username, commit_points=commit_points
                )
            except GithubAPIRequestFailedError as e:
                raise GithubAPIUnavailableError from e

        return self._renderer.render_svg(
            pokemons=user.pokemon_types, commit_point=user.total_commit_point, username=username
        )

    async def _get_commit_points(self, username: str) -> dict[int, int]:
        return await self._github_api.get_user_total_contributions(username=username)

    async def _get_commit_point(self, username: str, year: int) -> int:
        return await self._github_api.get_user_contributions_by_year(username=username, year=year)
