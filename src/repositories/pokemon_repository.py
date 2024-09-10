from typing import Sequence

from sqlmodel import col, select

from src.models.pokemon import Pokemon
from src.models.user import User
from src.pokemons.pokemon_type import PokemonType
from src.repositories.base_repository import BaseRepository


class PokemonRepository(BaseRepository):
    async def find_by_owner(self, owner: User) -> Sequence[Pokemon]:
        stmt = select(Pokemon).where(Pokemon.owner == owner)
        return (await self._session.exec(stmt)).unique().all()

    async def find_by_id(self, id: int) -> Pokemon | None:
        stmt = select(Pokemon).where(Pokemon.id == id)
        return (await self._session.exec(stmt)).first()

    async def exist_by_types_and_owner(self, owner: User, types: Sequence[PokemonType]) -> bool:
        stmt = select(Pokemon.id).where(Pokemon.owner == owner, col(Pokemon.type).in_(types))
        return (await self._session.exec(stmt)).first() is not None
