import random
from typing import Sequence

from src.models.pokemon import Pokemon
from src.models.user import User
from src.pokemons.time import Time
from src.services.evolution_service import EvolutionService


class LevelUpService:
    def __init__(self, *, evolution_service: EvolutionService) -> None:
        self._evolution_service = evolution_service

    async def level_up_pokemons(self, user: User, pokemons: Sequence[Pokemon], add_level: int, time: Time):
        for pokemon in random.choices(pokemons, k=add_level):
            pokemon.level_up()
            rule = self._evolution_service.get_evolution_rule_for_pokemon(pokemon, user, time, None)
            if rule:
                await self._evolution_service.evolve_pokemon(pokemon, user, rule)
