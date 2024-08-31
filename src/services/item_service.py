import random

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.daily_item import DailyItem
from src.pokemons.item_type import ItemType
from src.utils import utc_now_date


class ItemService:
    def __init__(self):
        pass

    async def get_daily_item(self, session: AsyncSession):
        daily_item = await self._find_daily_item(session)

        if daily_item:
            return daily_item

        daily_item = self._create_daily_item(session)
        await session.commit()
        return daily_item

    async def _find_daily_item(self, session: AsyncSession):
        current_date = utc_now_date()
        stmt = select(DailyItem).where(DailyItem.created_date == current_date)
        result = await session.exec(stmt)

        return result.first()

    def _create_daily_item(self, session: AsyncSession):
        item_type = random.choice(tuple(ItemType))
        daily_item = DailyItem(type=item_type)
        session.add(daily_item)

        return daily_item
