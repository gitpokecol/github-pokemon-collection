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

    def update_pokedex_for_user(self, user: User, pokemon_types: list[PokemonType]):
        pokedex_items = {item.type: item for item in user.pokedex_items}

        for pokemon_type in pokemon_types:
            if pokemon_type in pokedex_items:
                pokedex_items[pokemon_type].obtain_count += 1
            else:
                pokedex_items[pokemon_type] = PokedexItem(type=pokemon_type, obtain_count=1)
                user.pokedex_items.append(pokedex_items[pokemon_type])

        self._pokedex_item_repository.save(*pokedex_items.values())
