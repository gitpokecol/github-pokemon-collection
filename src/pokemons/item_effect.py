from typing import Protocol

from src.models.pokemon import Pokemon
from src.pokemons.form import ArceusForm
from src.pokemons.pokemon_type import PokemonType


class ItemEffect(Protocol):
    def apply(self, pokemon: Pokemon):
        pass


class PlateEffect(ItemEffect):
    def __init__(self, form: ArceusForm) -> None:
        self._form = form

    def apply(self, pokemon: Pokemon):
        if pokemon.type == PokemonType.Arceus:
            pokemon.form = self._form


class RareCandyEffect(ItemEffect):
    def apply(self, pokemon: Pokemon):
        pokemon.level_up()


class EvolutionItemEffect(ItemEffect):
    pass
