from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel

from .base import DatedAtMixin
from .pokemon_type import PokemonType


class Pokemon(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "pokemon"
    __table_args__ = (UniqueConstraint("owner_id", "type"),)

    id: int | None = Field(default=None, primary_key=True)
    type: PokemonType
    owner_id: int = Field(foreign_key="user.id")
