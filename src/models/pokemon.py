from sqlalchemy import Integer, UniqueConstraint
from sqlmodel import Field, SQLModel

from src.models.base import DatedAtMixin
from src.pokemons.form import Form
from src.pokemons.gender import Gender
from src.pokemons.pokemon_type import PokemonType


class Pokemon(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "pokemon"
    __table_args__ = (UniqueConstraint("owner_id", "type"),)

    id: int | None = Field(default=None, primary_key=True)
    type: PokemonType = Field(sa_type=Integer)
    is_shiny: bool = Field(default=False)
    level: int = Field(default=1, ge=1, le=100)
    friendship: int = Field(default=0, ge=0, le=255)
    gender: Gender
    form: Form | None
    owner_id: int = Field(default=None, foreign_key="user.id")

    def level_up(self):
        self.level = min(self.level + 1, 100)
