from typing import Sequence

from sqlmodel import select

from src.models.pokedex_item import PokedexItem
from src.models.user import User
from src.repositories.base_repository import BaseRepository


class PokedexItemRepository(BaseRepository):

    async def find_by_owner(self, owner: User) -> Sequence[PokedexItem]:
        stmt = select(PokedexItem).where(PokedexItem.owner == owner)
        return (await self._session.exec(stmt)).unique().all()
