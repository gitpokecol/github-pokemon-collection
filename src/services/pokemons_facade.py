from datetime import datetime

from sqlmodel.ext.asyncio.session import AsyncSession

from src.external.github_api import GithubAPI
from src.renders.svg import SVGRenderer
from src.services.user import UserService


class PokemonsFacade:
    def __init__(self, *, user_service: UserService, github_api: GithubAPI, renderer: SVGRenderer) -> None:
        self._user_service = user_service
        self._github_api = github_api
        self._renderer = renderer

    async def render_pokemons(self, *, session: AsyncSession, username: str) -> str:
        commit_point = await self._get_commit_point(username)

        if await self._user_service.exists_by_username(session=session, username=username):
            # TODO: updating commit point should be in background
            user = await self._user_service.update_commit_point(
                session=session, username=username, commit_point=commit_point
            )
        else:
            user = await self._user_service.create_new_user(
                session=session, username=username, commit_point=commit_point
            )

        return self._renderer.render_svg(pokemons=user.pokemon_types, commit_point=commit_point, username=username)

    async def _get_commit_point(self, username: str) -> int:
        user_contribs = await self._github_api.get_user_total_contributions(username=username)
        current_year = datetime.utcnow().year
        return user_contribs.get(current_year, 0)
