from sqlmodel import select

from src.models.daily_item import DailyItem
from src.models.daily_item_abtain import DailyItemAbtain
from src.models.user import User
from src.repositories.base_repository import BaseRepository


class DailyItemAbtainRepository(BaseRepository):

    async def exist_by_user_and_daily_item(self, user: User, daily_item: DailyItem):
        stmt = select(DailyItemAbtain.id).where(DailyItemAbtain.user == user, DailyItemAbtain.daily_item == daily_item)
        result = await self._session.exec(stmt)
        return result.first() is not None
