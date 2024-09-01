import random

from src.models.daily_item import DailyItem
from src.models.daily_item_abtain import DailyItemAbtain
from src.models.user import User
from src.pokemons.item_type import ItemType
from src.repositories.daily_item_abtain_repository import DailyItemAbtainRepository
from src.repositories.daily_item_repository import DailyItemRepository
from src.schemas.responses.items import DailyItemResponse


class ItemService:

    def __init__(
        self, *, daily_item_repository: DailyItemRepository, daily_item_abtain_repository: DailyItemAbtainRepository
    ) -> None:
        self._daily_item_repo = daily_item_repository
        self._daily_item_abtain_repo = daily_item_abtain_repository

    async def get_daily_item(self) -> DailyItemResponse:
        daily_item = await self._get_daily_item()
        return DailyItemResponse.of(type=daily_item.type)

    async def give_daily_item_to_user(self, user: User) -> None:
        daily_item = await self._get_daily_item()

        daily_item_abtain = DailyItemAbtain(user=user, daily_item=daily_item)
        self._daily_item_abtain_repo.save(daily_item_abtain)

    async def _get_daily_item(self) -> DailyItem:
        daily_item = await self._daily_item_repo.find_for_today()

        if daily_item is None:
            daily_item = self._create_daily_item()
            self._daily_item_repo.save(daily_item)

        return daily_item

    def _create_daily_item(self) -> DailyItem:
        item_type = random.choice(tuple(ItemType))
        daily_item = DailyItem(type=item_type)

        return daily_item
