from datetime import datetime, timezone

from src.external.github_api import GithubAPI
from src.models.user import User
from src.pokemons.time import Time
from src.repositories.user_repository import UserRepository
from src.services.levelup_service import LevelUpService
from src.services.pokemon_service import PokemonService
from src.setting import settings


class CommitPointRewardService:
    def __init__(
        self,
        *,
        github_api: GithubAPI,
        pokemon_service: PokemonService,
        levelup_service: LevelUpService,
        user_repository: UserRepository,
    ) -> None:
        self._github_api = github_api
        self._pokemon_service = pokemon_service
        self._levelup_service = levelup_service
        self._user_repo = user_repository

    def can_update_commit_point(self, user: User) -> bool:
        return (
            len(user.commit_points) == 0
            or datetime.now(timezone.utc) - user.latest_commit_points_updated_at.replace(tzinfo=timezone.utc)
            >= settings.COMMIT_POINT_UPDATE_PERIOD
        )

    async def update_commit_point_and_reward(self, user: User, time: Time):
        previous_commit_point = user.total_commit_point

        if len(user.commit_points) == 0:
            user.set_commit_points(await self._get_commit_points(user.username))
        else:
            this_year = datetime.now(timezone.utc).year
            commit_point = await self._get_commit_point(user.username, this_year)
            user.set_commit_point(this_year, commit_point)

        await self._user_repo.save(user)

        await self._reward_for_user(user, time, previous_commit_point, user.total_commit_point)

    async def _reward_for_user(self, user: User, time: Time, previous_commit_point: int, current_commit_point: int):
        new_pokemon_count = self._calculate_new_pokemon_count(previous_commit_point, current_commit_point)
        await self._pokemon_service.give_pokemons_for_user(user, new_pokemon_count)

        pokemons = await self._pokemon_service.get_pokemons(user)
        add_level = self._calculate_add_level(previous_commit_point, current_commit_point)
        await self._levelup_service.level_up_pokemons(user, pokemons, add_level, time)

    async def _get_commit_points(self, username: str) -> dict[int, int]:
        return await self._github_api.get_user_total_contributions(username=username)

    async def _get_commit_point(self, username: str, year: int) -> int:
        return await self._github_api.get_user_contributions_by_year(username=username, year=year)

    def _calculate_new_pokemon_count(self, updated_commit_point: int, current_commit_point: int) -> int:
        given_pokemon_count = updated_commit_point // settings.POKEMON_PER_COMMIT_POINT
        target_pokemon_count = current_commit_point // settings.POKEMON_PER_COMMIT_POINT
        return target_pokemon_count - given_pokemon_count

    def _calculate_add_level(self, updated_commit_point: int, current_commit_point: int) -> int:
        given_pokemon_count = updated_commit_point // settings.LEVEL_UP_PER_COMMIT_POINT
        target_pokemon_count = current_commit_point // settings.LEVEL_UP_PER_COMMIT_POINT
        return target_pokemon_count - given_pokemon_count
