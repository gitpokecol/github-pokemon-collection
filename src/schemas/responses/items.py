from pydantic import BaseModel

from src.models.bag_item import BagItem
from src.pokemons.item_type import ItemType


class DailyItemResponse(BaseModel):
    type: int

    @classmethod
    def of(cls, type: ItemType) -> "DailyItemResponse":
        return DailyItemResponse(type=type)


class Item(BaseModel):
    item_type: int
    count: int


class BagItemsResponse(BaseModel):
    items: list[Item]

    @classmethod
    def of(cls, bag_items: list[BagItem]) -> "BagItemsResponse":
        items = [Item(item_type=bag_item.item_type, count=bag_item.count) for bag_item in bag_items]
        return BagItemsResponse(items=items)
