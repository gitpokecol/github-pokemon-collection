from typing import Sequence

from src.exceptions.common import NotFoundError
from src.exceptions.error_codes import ErrorCode
from src.models.pokedex_item import PokedexItem
from src.models.pokemon import Pokemon
from src.models.user import User
from src.pokemons.evolution import evolution_line_cnts
from src.pokemons.pokemon_type import PokemonType
from src.repositories.pokemon_repository import PokemonRepository
from src.schemas.responses.pokemons import PokemonsResponse
from src.services.pokedex_service import PokedexService
from src.utils import weighted_sample


class PokemonService:
    def __init__(self, *, pokemon_repository: PokemonRepository, pokedex_service: PokedexService) -> None:
        self._evolution_line_counts: dict[PokemonType, int] = {}
        self._pokemon_repository = pokemon_repository
        self._pokedex_service = pokedex_service

    async def give_pokemons_for_user(self, user: User, new_count: int):
        pokedex_items = await self._pokedex_service.get_pokedex_items(user)
        canditates = list(self._get_new_pokemon_candidates(pokedex_items))
        new_pokemon_types = self._pick_pokemon_types_by_base_stat(canditates, min(len(canditates), new_count))
        await self._pokedex_service.update_pokedex_for_user(user, new_pokemon_types)

        new_pokemons = [Pokemon.create_random(pokemon_type, user) for pokemon_type in new_pokemon_types]
        await self._pokemon_repository.save(*new_pokemons)

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

    async def get_pokemons_response(self, owner: User) -> PokemonsResponse:
        pokemons = await self.get_pokemons(owner)
        sorted_pokemons = sorted(pokemons, key=lambda p: p.created_at)
        return PokemonsResponse.of(sorted_pokemons)

    async def get_pokemon_by_id(self, pokemon_id: int) -> Pokemon:
        pokemon = await self._pokemon_repository.find_by_id(pokemon_id)

        if not pokemon:
            raise NotFoundError(ErrorCode.POKEMON_NOT_FOUND)

        return pokemon

    async def get_pokemons(self, owner: User) -> Sequence[Pokemon]:
        return await self._pokemon_repository.find_by_owner(owner)
