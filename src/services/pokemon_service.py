import random
from typing import Sequence

from src.exceptions.common import NotFoundError
from src.exceptions.error_codes import ErrorCode
from src.models.pokedex_item import PokedexItem
from src.models.pokemon import Pokemon
from src.models.user import User
from src.pokemons.evolution import evolution_line_cnts
from src.pokemons.pokemon_type import PokemonType
from src.pokemons.time import Time
from src.schemas.responses.pokemons import PokemonsResponse
from src.services.evolution_service import EvolutionService
from src.setting import settings
from src.utils import weighted_sample


class PokemonService:
    def __init__(self, *, evolution_service: EvolutionService) -> None:
        self._evolution_line_counts: dict[PokemonType, int] = {}
        self._evolution_service = evolution_service

    def give_pokemons_for_user(self, user: User, previous_commit_point: int, current_commit_point: int):
        new_count = self._calculate_new_pokemon_count(previous_commit_point, current_commit_point)
        canditates = list(self._get_new_pokemon_candidates(user.pokedex_items))
        new_pokemon_types = self._pick_pokemon_types_by_base_stat(canditates, new_count)
        user.update_pokedex(new_pokemon_types)

        new_pokemons = [Pokemon.create_random(pokemon_type) for pokemon_type in new_pokemon_types]
        user.pokemons.extend(new_pokemons)

    def _calculate_new_pokemon_count(self, updated_commit_point: int, current_commit_point: int) -> int:
        given_pokemon_count = updated_commit_point // settings.POKEMON_PER_COMMIT_POINT
        target_pokemon_count = current_commit_point // settings.POKEMON_PER_COMMIT_POINT
        return target_pokemon_count - given_pokemon_count

    def _get_new_pokemon_candidates(self, pokedex_items: Sequence[PokedexItem]) -> set[PokemonType]:
        candiates = set(evolution_line_cnts.keys())
        for pokedex_item in pokedex_items:
            if pokedex_item.type not in evolution_line_cnts:
                continue

            if evolution_line_cnts[pokedex_item.type] <= pokedex_item.obtain_count:
                candiates.remove(pokedex_item.type)

        return candiates

    def _pick_pokemon_types_by_base_stat(self, candidates: Sequence[PokemonType], count: int):
        weights = [1 / type.base_stat for type in candidates]
        return weighted_sample(candidates, weights, count)

    def level_up_pokemons_for_user(
        self, user: User, previous_commit_point: int, current_commit_point: int, time: Time
    ):
        add_level = self._calculate_add_level(previous_commit_point, current_commit_point)
        for pokemon in random.choices(user.pokemons, k=add_level):
            pokemon.level_up()
            rule = self._evolution_service.get_evolution_rule_for_pokemon(pokemon, user, time, None)
            if rule:
                self._evolution_service.evolve_pokemon(pokemon, user, rule)

    def _calculate_add_level(self, updated_commit_point: int, current_commit_point: int) -> int:
        given_pokemon_count = updated_commit_point // settings.LEVEL_UP_PER_COMMIT_POINT
        target_pokemon_count = current_commit_point // settings.LEVEL_UP_PER_COMMIT_POINT
        return target_pokemon_count - given_pokemon_count

    def get_pokemons_by_user(self, user: User) -> PokemonsResponse:
        return PokemonsResponse.of(user.pokemons)

    def find_pokemon_in_owner(self, pokemon_id: int, owner: User) -> Pokemon:
        for pokemon in owner.pokemons:
            if pokemon.id == pokemon_id:
                return pokemon

        raise NotFoundError(ErrorCode.POKEMON_NOT_FOUND)
