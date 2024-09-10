from typing import Sequence

from pydantic import BaseModel

from src.models.bag_item import BagItem
from src.pokemons.item_type import ItemType


class DailyItemResponse(BaseModel):
    type: int
    can_abtain: bool

    @classmethod
    def of(cls, type: ItemType, can_abtain: bool) -> "DailyItemResponse":
        return DailyItemResponse(type=type, can_abtain=can_abtain)


class Item(BaseModel):
    item_type: int
    count: int


class BagItemsResponse(BaseModel):
    items: list[Item]

    @classmethod
    def of(cls, bag_items: Sequence[BagItem]) -> "BagItemsResponse":
        items = [Item(item_type=bag_item.item_type, count=bag_item.count) for bag_item in bag_items]
        return BagItemsResponse(items=items)


class UseItemResponse(BaseModel):
    is_used: bool
