from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel

from src.models.base import DatedAtMixin
from src.models.pokemon_type import PokemonType


class PokedexItem(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "pokedex_item"
    __table_args__ = (UniqueConstraint("owner_id", "type"),)

    id: int | None = Field(default=None, primary_key=True)
    type: PokemonType
    obtain_count: int = Field(ge=0)
    owner_id: int = Field(default=None, foreign_key="owner.id")
