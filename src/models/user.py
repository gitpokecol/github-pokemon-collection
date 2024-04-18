import random
from math import ceil

from sqlmodel import Field, Relationship, SQLModel

from ..setting import settings
from .base import DatedAtMixin
from .pokemon import Pokemon
from .pokemon_type import PokemonType


class User(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "user"

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    commit_point: int
    pokemons: list[Pokemon] = Relationship(sa_relationship_kwargs={"lazy": "joined", "cascade": "all, delete"})

    @property
    def pokemon_types(self) -> list[PokemonType]:
        return [pokemon.type for pokemon in self.pokemons]

    def __post_init__(self):
        self._init_pokemons()

    def _init_pokemons(self):
        n_pokemons = self._calc_proper_pokemon_cnt()
        pokemon_types = random.sample(list(PokemonType), n_pokemons)

        for pt in pokemon_types:
            self.pokemons.append(Pokemon(type=pt))

    def update_pokemons(self):
        proper_n_pokemons = self._calc_proper_pokemon_cnt()

        if len(self.pokemons) > proper_n_pokemons:
            self._reset_pokemons()
        elif len(self.pokemons) < proper_n_pokemons:
            self._add_new_pokemons(proper_n_pokemons - len(self.pokemons))

    def _reset_pokemons(self):
        self.pokemons.clear()
        self._init_pokemons()

    def _add_new_pokemons(self, new_cnt: int):
        remain_types = set(PokemonType) - set(self.pokemon_types)
        pokemon_types = random.sample(list(remain_types), new_cnt)

        for pt in pokemon_types:
            self.pokemons.append(Pokemon(type=pt))

    def _calc_proper_pokemon_cnt(self) -> int:
        return min(len(PokemonType), ceil(self.commit_point / settings.POKEMON_PER_COMMIT_POINT))
