from src.models.pokedex_item import PokedexItem
from src.pokemons.pokemon_type import PokemonType


def create_pokedex_item(*, obtain_count: int = 1, type: PokemonType = PokemonType.Bulbasaur) -> PokedexItem:
    return PokedexItem(obtain_count=obtain_count, type=type)
