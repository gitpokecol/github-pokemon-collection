from datetime import datetime, timezone

from fastapi import BackgroundTasks
from sqlmodel.ext.asyncio.session import AsyncSession

from src.external.github_api import GithubAPI
from src.models.user import User
from src.renders.profile_renderer import ProfileRenderer
from src.schemas.backgrounds import Background
from src.schemas.pokemons import Facing
from src.services.pokemon_service import PokemonService
from src.services.time_service import TimeService
from src.services.user_service import UserService
from src.setting import settings


class PokemonFacade:
    def __init__(
        self,
        *,
        user_service: UserService,
        pokemon_service: PokemonService,
        github_api: GithubAPI,
        time_service: TimeService,
        renderer: ProfileRenderer,
        background_tasks: BackgroundTasks
    ) -> None:
        self._user_service = user_service
        self._pokemon_service = pokemon_service
        self._github_api = github_api
        self._time_service = time_service
        self._renderer = renderer
        self._background_tasks = background_tasks

    async def render_pokemons(
        self,
        *,
        session: AsyncSession,
        username: str,
        facing: Facing,
        width: int,
        height: int,
        background: Background,
        viewer_ip_address: str | None
    ) -> str:
        user = await self._user_service.get_user(session=session, username=username)

        if user:
            if (
                datetime.now(timezone.utc) - user.latest_commit_points_updated_at.replace(tzinfo=timezone.utc)
                >= settings.COMMIT_POINT_UPDATE_PERIOD
            ):
                self._background_tasks.add_task(
                    self._update_commit_point_and_update_pokemons_task,
                    session=session,
                    user=user,
                    viewer_ip_address=viewer_ip_address,
                )
        else:
            commit_points = await self._get_commit_points(username)
            user = self._user_service.create_new_user(session=session, username=username, commit_points=commit_points)

            await self._update_pokemons(user, viewer_ip_address, 0, user.total_commit_point)
            await session.commit()

        return await self._renderer.render(
            pokemons=user.pokemons,
            commit_point=user.total_commit_point,
            username=username,
            facing=facing,
            width=width,
            height=height,
            background=background,
        )

    async def _get_commit_points(self, username: str) -> dict[int, int]:
        return await self._github_api.get_user_total_contributions(username=username)

    async def _get_commit_point(self, username: str, year: int) -> int:
        return await self._github_api.get_user_contributions_by_year(username=username, year=year)

    async def _update_commit_point_and_update_pokemons_task(
        self, *, session: AsyncSession, user: User, viewer_ip_address: str | None
    ):
        now_year = datetime.now(timezone.utc).year
        commit_point = await self._get_commit_point(user.username, now_year)

        previous_commit_point = user.total_commit_point
        user.set_commit_point(now_year, commit_point)
        await self._update_pokemons(user, viewer_ip_address, previous_commit_point, user.total_commit_point)
        await session.commit()

    async def _update_pokemons(
        self, user: User, ip_address: str | None, previous_commit_point: int, current_commit_point: int
    ):
        time = await self._time_service.get_time_for_client(ip_address)
        self._pokemon_service.give_pokemons_for_user(user, previous_commit_point, user.total_commit_point)
        self._pokemon_service.level_up_pokemons_for_user(user, previous_commit_point, user.total_commit_point, time)
