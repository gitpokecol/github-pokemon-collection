from typing import Sequence

from sqlmodel import select

from src.models.pokemon import Pokemon
from src.repositories.base_repository import BaseRepository


class PokemonRepository(BaseRepository):
    async def find_by_owner_id(self, owner_id: int) -> Sequence[Pokemon]:
        stmt = select(Pokemon).where(Pokemon.owner_id == owner_id).distinct()
        return (await self._session.exec(stmt)).all()
