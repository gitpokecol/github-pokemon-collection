from typing import Sequence

from src.models.pokedex_item import PokedexItem
from src.models.user import User
from src.pokemons.pokemon_type import PokemonType
from src.repositories.pokedex_item_repository import PokedexItemRepository
from src.schemas.responses.pokedex import PokedexResponse


class PokedexService:
    def __init__(self, *, pokedex_item_repository: PokedexItemRepository):
        self._pokedex_item_repository = pokedex_item_repository

    async def get_pokedex_response(self, owner: User) -> PokedexResponse:
        pokedex_items = await self.get_pokedex_items(owner)
        return PokedexResponse.of(pokedex_items)

    async def update_pokedex_for_user(self, user: User, pokemon_types: list[PokemonType]):
        pokedex_items = await self.get_pokedex_items(user)
        pokedex_items_dict = {item.type: item for item in pokedex_items}

        for pokemon_type in pokemon_types:
            if pokemon_type in pokedex_items_dict:
                pokedex_items_dict[pokemon_type].obtain_count += 1
            else:
                pokedex_items_dict[pokemon_type] = await self._create_pokedex_item(pokemon_type, user)

    async def _create_pokedex_item(self, pokemon_type: PokemonType, owner: User) -> PokedexItem:
        pokedex_item = PokedexItem(type=pokemon_type, obtain_count=1, owner=owner)
        await self._pokedex_item_repository.save(pokedex_item)
        return pokedex_item

    async def get_pokedex_items(self, owner: User) -> Sequence[PokedexItem]:
        return await self._pokedex_item_repository.find_by_owner(owner)
