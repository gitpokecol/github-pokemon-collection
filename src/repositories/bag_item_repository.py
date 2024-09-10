from sqlmodel import select

from src.models.bag_item import BagItem
from src.models.user import User
from src.repositories.base_repository import BaseRepository


class BagItemRepository(BaseRepository):
    async def find_containing_item_by_owner_name(self, owner_name: str):
        stmt = select(BagItem).join(User).where(User.username == owner_name).distinct()
        return (await self._session.exec(stmt)).all()
