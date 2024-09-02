from typing import Protocol

from src.models.pokemon import Pokemon
from src.pokemons.form import ArceusForm


class ItemEffect(Protocol):
    def apply(self, pokemon: Pokemon):
        pass


class PlateEffect(ItemEffect):
    def __init__(self, form: ArceusForm) -> None:
        self._form = form

    def apply(self, pokemon: Pokemon):
        pokemon.form = self._form


class RareCandyEffect(ItemEffect):
    def apply(self, pokemon: Pokemon):
        pokemon.level_up()


class EvolutionItemEffect(ItemEffect):
    pass
