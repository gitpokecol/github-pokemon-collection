from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel

from .pokemon_type import PokemonType


class Pokemon(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("owner_id", "type"),)

    id: int | None = Field(default=None, primary_key=True)
    type: PokemonType = Field(nullable=False)
    owner_id: int = Field(nullable=False)
