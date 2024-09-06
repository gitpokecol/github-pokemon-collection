from datetime import datetime
from typing import Sequence

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel

from src.models.bag_item import BagItem
from src.models.base import DatedAtMixin
from src.models.commit_point import CommitPoint
from src.models.pokedex_item import PokedexItem
from src.models.pokemon import Pokemon
from src.pokemons.item_type import ItemType
from src.pokemons.pokemon_type import PokemonType


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
    bag_items: list[BagItem] = Relationship(sa_relationship_kwargs={"lazy": "joined", "cascade": "all, delete"})

    @property
    def pokemon_types(self) -> list[PokemonType]:
        return [pokemon.type for pokemon in self.pokemons]

    @property
    def total_commit_point(self) -> int:
        return sum(cp.commit_point for cp in self.commit_points)

    @property
    def latest_commit_points_updated_at(self) -> datetime:
        return max(cp.updated_at for cp in self.commit_points)

    @property
    def existed_bag_items(self) -> list[BagItem]:
        return [bag_item for bag_item in self.bag_items if bag_item.count > 0]

    def set_commit_points(self, commit_points: dict[int, int]):
        for year, cp in commit_points.items():
            self._set_commit_point(year, cp)

    def set_commit_point(self, year: int, commit_point: int):
        self._set_commit_point(year, commit_point)

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

    def add_item(self, item_type: ItemType):
        bag_item = self._get_item_bag_by_item_type(item_type)

        if bag_item is not None:
            bag_item.count += 1
        else:
            new_bag_item = BagItem(item_type=item_type, count=1)
            self.bag_items.append(new_bag_item)

    def remove_item(self, item_type: ItemType):
        bag_item = self._get_item_bag_by_item_type(item_type)
        assert bag_item is not None

        bag_item.count -= 1

        if bag_item.count == 0:
            self.bag_items.remove(bag_item)

    def _get_item_bag_by_item_type(self, item_type: ItemType) -> BagItem | None:
        for bag_item in self.bag_items:
            if bag_item.item_type == item_type:
                return bag_item

        return None
