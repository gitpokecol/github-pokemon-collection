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
    pokemons: list[Pokemon] = Relationship(sa_relationship_kwargs={"lazy": "joined"})

    def __post_init__(self):
        n_pokemon = ceil(self.commit_point / settings.POKEMON_PER_COMMIT_POINT)
        pokemon_types = random.sample(list(PokemonType), n_pokemon)

        for pt in pokemon_types:
            self.pokemons.append(Pokemon(type=pt))

    @property
    def pokemon_types(self) -> list[PokemonType]:
        return [pokemon.type for pokemon in self.pokemons]
