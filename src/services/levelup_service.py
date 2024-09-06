import random

from src.models.user import User
from src.pokemons.time import Time
from src.services.evolution_service import EvolutionService
from src.setting import settings


class LevelUpService:
    def __init__(self, *, evolution_service: EvolutionService) -> None:
        self._evolution_service = evolution_service

    async def level_up_pokemons_for_user(
        self, user: User, previous_commit_point: int, current_commit_point: int, time: Time
    ):
        add_level = self._calculate_add_level(previous_commit_point, current_commit_point)
        for pokemon in random.choices(user.pokemons, k=add_level):
            pokemon.level_up()
            rule = self._evolution_service.get_evolution_rule_for_pokemon(pokemon, user, time, None)
            if rule:
                await self._evolution_service.evolve_pokemon(pokemon, user, rule)

    def _calculate_add_level(self, updated_commit_point: int, current_commit_point: int) -> int:
        given_pokemon_count = updated_commit_point // settings.LEVEL_UP_PER_COMMIT_POINT
        target_pokemon_count = current_commit_point // settings.LEVEL_UP_PER_COMMIT_POINT
        return target_pokemon_count - given_pokemon_count
