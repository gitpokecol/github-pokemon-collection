from sqlmodel import Field, Relationship, SQLModel

from .base import DatedAtMixin
from .pokemon import Pokemon
from .pokemon_type import PokemonType


class User(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "user"

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    commit_point: int
    pokemons: list[Pokemon] = Relationship(sa_relationship_kwargs={"lazy": "joined"})

    @property
    def pokemon_types(self) -> list[PokemonType]:
        return [pokemon.type for pokemon in self.pokemons]
