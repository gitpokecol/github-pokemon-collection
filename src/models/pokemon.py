from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel

from src.models.base import DatedAtMixin
from src.models.pokemon_type import PokemonType


class Pokemon(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "pokemon"
    __table_args__ = (UniqueConstraint("owner_id", "type"),)

    id: int | None = Field(default=None, primary_key=True)
    type: PokemonType
    is_shiny: bool = Field(default=False)
    owner_id: int = Field(default=None, foreign_key="user.id")
