import random
import typing

from sqlalchemy import Integer, String, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from src.models.base import DatedAtMixin
from src.pokemons.form import ArceusForm, Form
from src.pokemons.gender import Gender
from src.pokemons.pokemon_type import PokemonType
from src.setting import settings

if typing.TYPE_CHECKING:
    from src.models.user import User


class Pokemon(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "pokemon"
    __table_args__ = (UniqueConstraint("owner_id", "type"),)

    id: int | None = Field(default=None, primary_key=True)
    type: PokemonType = Field(sa_type=Integer)
    is_shiny: bool = Field(default=False)
    level: int = Field(default=1, ge=1, le=100)
    friendship: int = Field(default=0, ge=0, le=255)
    gender: Gender = Field(sa_type=String)
    form: Form | None = Field(sa_type=String)

    owner_id: int = Field(default=None, foreign_key="user.id", ondelete="CASCADE", index=True)
    owner: "User" = Relationship(back_populates="pokemons")

    def level_up(self):
        self.level = min(self.level + 1, 100)

    @classmethod
    def create_random(cls, pokemon_type: PokemonType, owner: "User") -> "Pokemon":
        is_shiny = settings.SHINY_POKEMON_RATE > random.random()
        gender = random.choice(pokemon_type.available_genders)

        form = None
        if pokemon_type == PokemonType.Arceus:
            form = ArceusForm.DEFAULT
        elif pokemon_type.available_forms:
            form = random.choice(pokemon_type.available_forms)

        return Pokemon(type=pokemon_type, is_shiny=is_shiny, gender=gender, form=form, owner=owner)
