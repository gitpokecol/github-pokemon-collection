from sqlalchemy import Integer
from sqlmodel import Field, SQLModel

from src.models.base import DatedAtMixin
from src.pokemons.item_type import ItemType


class Item(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "item"

    id: int | None = Field(default=None, primary_key=True)
    type: ItemType = Field(sa_type=Integer)
    owner_id: int = Field(default=None, foreign_key="user.id")
