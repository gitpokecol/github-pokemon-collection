from src.models.daily_item import DailyItem
from src.models.daily_item_abtain import DailyItemAbtain
from src.models.user import User
from src.pokemons.item_type import ItemType


def create_daily_item(*, type: ItemType = ItemType.METAL_COAT) -> DailyItem:
    return DailyItem(type=type)


def create_daily_item_abtain(*, daily_item: DailyItem, user: User):
    return DailyItemAbtain(daily_item=daily_item, user=user)
