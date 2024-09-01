from sqlmodel import select

from src.models.daily_item import DailyItem
from src.repositories.base_repository import BaseRepository
from src.utils import utc_now_date


class DailyItemRepository(BaseRepository):

    async def find_daily_item_for_today(self) -> DailyItem | None:
        current_date = utc_now_date()
        stmt = select(DailyItem).where(DailyItem.created_date == current_date)
        result = await self._session.exec(stmt)

        return result.first()
