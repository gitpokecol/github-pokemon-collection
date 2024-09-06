import typing

from sqlalchemy import Integer, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from src.models.base import DatedAtMixin
from src.pokemons.item_type import ItemType

if typing.TYPE_CHECKING:
    from src.models.user import User


class BagItem(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "bag_item"
    __table_args__ = (UniqueConstraint("owner_id", "item_type"),)

    id: int | None = Field(default=None, primary_key=True)
    item_type: ItemType = Field(sa_type=Integer)
    count: int = Field(ge=0)

    owner_id: int = Field(default=None, foreign_key="user.id", ondelete="CASCADE")
    owner: "User" = Relationship(back_populates="bag_items")
