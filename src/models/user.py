from datetime import datetime
from typing import Sequence

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel

from src.models.base import DatedAtMixin
from src.models.commit_point import CommitPoint
from src.models.pokedex_item import PokedexItem
from src.models.pokemon import Pokemon
from src.models.pokemon_type import PokemonType


class UserBase(SQLModel, DatedAtMixin):
    username: str = Field(unique=True)

    @field_validator("username", mode="before")
    @classmethod
    def username_to_lowercase(cls, username: str) -> str:
        return username.lower()


class User(UserBase, table=True):
    __tablename__: str = "user"

    id: int | None = Field(default=None, primary_key=True)
    commit_points: list[CommitPoint] = Relationship(
        sa_relationship_kwargs={"lazy": "joined", "cascade": "all, delete"}
    )
    pokemons: list[Pokemon] = Relationship(sa_relationship_kwargs={"lazy": "joined", "cascade": "all, delete"})
    pokedex_items: list[PokedexItem] = Relationship(
        sa_relationship_kwargs={"lazy": "joined", "cascade": "all, delete"}
    )

    @property
    def pokemon_types(self) -> list[PokemonType]:
        return [pokemon.type for pokemon in self.pokemons]

    @property
    def total_commit_point(self) -> int:
        return sum(cp.commit_point for cp in self.commit_points)

    @property
    def latest_commit_points_updated_at(self) -> datetime:
        return max(cp.updated_at for cp in self.commit_points)

    def set_commit_points(self, commit_points: dict[int, int]):
        for year, cp in commit_points.items():
            self._set_commit_point(year, cp)

    def set_commit_point(self, year: int, commit_point: int):
        self._set_commit_point(year, commit_point)

    def update_pokedex(self, pokemon_types: Sequence[PokemonType]):
        pokedex_items = {item.type: item for item in self.pokedex_items}

        for pokemon_type in pokemon_types:
            if pokemon_type in pokedex_items:
                pokedex_items[pokemon_type].obtain_count += 1
            else:
                pokedex_items[pokemon_type] = PokedexItem(type=pokemon_type, obtain_count=1)
                self.pokedex_items.append(pokedex_items[pokemon_type])

    def _set_commit_point(self, year: int, commit_point: int):
        model = self._get_commit_point(year)
        if model is None:
            self.commit_points.append(CommitPoint(year=year, commit_point=commit_point))
        else:
            model.commit_point = commit_point

    def _get_commit_point(self, year: int) -> CommitPoint | None:
        for model in self.commit_points:
            if model.year == year:
                return model

        return None
