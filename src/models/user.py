import random
from datetime import datetime
from math import ceil

from sqlmodel import Field, Relationship, SQLModel

from src.models.base import DatedAtMixin
from src.models.commit_point import CommitPoint
from src.models.pokemon import Pokemon
from src.models.pokemon_type import PokemonType
from src.setting import settings


class User(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "user"

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    commit_points: list[CommitPoint] = Relationship(
        sa_relationship_kwargs={"lazy": "joined", "cascade": "all, delete"}
    )
    pokemons: list[Pokemon] = Relationship(sa_relationship_kwargs={"lazy": "joined", "cascade": "all, delete"})

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

        self._update_pokemons()

    def set_commit_point(self, year: int, commit_point: int):
        self._set_commit_point(year, commit_point)
        self._update_pokemons()

    def _update_pokemons(self):
        proper_n_pokemons = self._calc_proper_pokemon_cnt()
        self._add_new_pokemons(proper_n_pokemons - len(self.pokemons))

    def _add_new_pokemons(self, new_cnt: int):
        remain_types = set(PokemonType) - set(self.pokemon_types)
        pokemon_types = random.sample(list(remain_types), new_cnt)

        for pt in pokemon_types:
            is_shiny = settings.SHINY_POKEMON_RATE <= random.random()
            self.pokemons.append(Pokemon(type=pt, is_shiny=is_shiny))

    def _calc_proper_pokemon_cnt(self) -> int:
        return min(len(PokemonType), ceil(self.total_commit_point / settings.POKEMON_PER_COMMIT_POINT))

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
