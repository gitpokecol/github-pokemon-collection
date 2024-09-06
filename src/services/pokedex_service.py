from src.models.pokedex_item import PokedexItem
from src.models.user import User
from src.pokemons.pokemon_type import PokemonType
from src.repositories.pokedex_item_repository import PokedexItemRepository
from src.schemas.responses.pokedex import PokedexResponse


class PokedexService:
    def __init__(self, *, pokedex_item_repository: PokedexItemRepository):
        self._pokedex_item_repository = pokedex_item_repository

    def get_pokedex(self, user: User) -> PokedexResponse:
        return PokedexResponse.of(user.pokedex_items)

    async def update_pokedex_for_user(self, user: User, pokemon_types: list[PokemonType]):
        pokedex_items = {item.type: item for item in user.pokedex_items}

        for pokemon_type in pokemon_types:
            if pokemon_type in pokedex_items:
                pokedex_items[pokemon_type].obtain_count += 1
            else:
                pokedex_items[pokemon_type] = await self._create_pokedex_item(pokemon_type, user)
                user.pokedex_items.append(pokedex_items[pokemon_type])

    async def _create_pokedex_item(self, pokemon_type: PokemonType, owner: User) -> PokedexItem:
        pokedex_item = PokedexItem(type=pokemon_type, obtain_count=1, owner=owner)
        await self._pokedex_item_repository.save(pokedex_item)
        return pokedex_item
