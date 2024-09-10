from typing import Sequence

from sqlmodel import select

from src.models.pokemon import Pokemon
from src.models.user import User
from src.repositories.base_repository import BaseRepository


class PokemonRepository(BaseRepository):
    async def find_by_owner(self, owner: User) -> Sequence[Pokemon]:
        stmt = select(Pokemon).where(Pokemon.owner == owner)
        return (await self._session.exec(stmt)).unique().all()

    async def find_by_id(self, id: int) -> Pokemon | None:
        stmt = select(Pokemon).where(Pokemon.id == id)
        return (await self._session.exec(stmt)).first()
