from src.models.pokedex_item import PokedexItem
from src.models.user import User
from src.pokemons.pokemon_type import PokemonType
from tests.utils.user import create_user


def create_pokedex_item(
    *, obtain_count: int = 1, type: PokemonType = PokemonType.Bulbasaur, owner: None | User = None
) -> PokedexItem:
    if owner is None:
        owner = create_user()

    return PokedexItem(obtain_count=obtain_count, type=type, owner=owner)
