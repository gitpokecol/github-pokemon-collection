from src.models.pokedex_item import PokedexItem
from src.models.pokemon import Pokemon
from src.models.user import User


def create_user(
    *, username: str = "username", pokemons: list[Pokemon] = [], pokedex_items: list[PokedexItem] = []
) -> User:
    return User(username=username, pokemons=pokemons, pokedex_items=pokedex_items)
