from typing import Sequence

from sqlmodel import select

from src.models.bag_item import BagItem
from src.repositories.base_repository import BaseRepository


class BagItemRepository(BaseRepository):
    async def find_containing_item_by_owner_id(self, owner_id: int) -> Sequence[BagItem]:
        stmt = select(BagItem).where(BagItem.owner_id == owner_id, BagItem.count > 0)
        return (await self._session.exec(stmt)).unique().all()
