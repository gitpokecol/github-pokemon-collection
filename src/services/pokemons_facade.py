from datetime import datetime, timezone

from fastapi import BackgroundTasks
from sqlmodel.ext.asyncio.session import AsyncSession

from src.exceptions.external import GithubAPIRequestFailedError, GithubAPIUnavailableError
from src.external.github_api import GithubAPI
from src.renders.svg import SVGRenderer
from src.schemas.pokemons import PokemonFace
from src.services.user import UserService
from src.setting import settings


class PokemonsFacade:
    def __init__(
        self,
        *,
        user_service: UserService,
        github_api: GithubAPI,
        renderer: SVGRenderer,
        background_tasks: BackgroundTasks
    ) -> None:
        self._user_service = user_service
        self._github_api = github_api
        self._renderer = renderer
        self._background_tasks = background_tasks

    async def render_pokemons(
        self, *, session: AsyncSession, username: str, face: PokemonFace, width: int, height: int
    ) -> str:
        user = await self._user_service.get_user(session=session, username=username)

        if user is not None:
            if (
                datetime.now(timezone.utc) - user.latest_commit_points_updated_at.replace(tzinfo=timezone.utc)
                >= settings.COMMIT_POINT_UPDATE_PERIOD
            ):
                self._background_tasks.add_task(self._update_commit_point_task, session=session, username=username)
        else:
            try:
                commit_points = await self._get_commit_points(username)
                user = await self._user_service.create_new_user(
                    session=session, username=username, commit_points=commit_points
                )
            except GithubAPIRequestFailedError as e:
                raise GithubAPIUnavailableError from e

        return self._renderer.render_svg(
            pokemons=user.pokemons,
            commit_point=user.total_commit_point,
            username=username,
            face=face,
            width=width,
            height=height,
        )

    async def _get_commit_points(self, username: str) -> dict[int, int]:
        return await self._github_api.get_user_total_contributions(username=username)

    async def _get_commit_point(self, username: str, year: int) -> int:
        return await self._github_api.get_user_contributions_by_year(username=username, year=year)

    async def _update_commit_point_task(self, *, session: AsyncSession, username: str):
        try:
            now_year = datetime.now(timezone.utc).year
            commit_point = await self._get_commit_point(username, now_year)
            await self._user_service.update_commit_point(
                session=session, username=username, year=now_year, commit_point=commit_point
            )
        except GithubAPIRequestFailedError:
            pass  # ignore error
