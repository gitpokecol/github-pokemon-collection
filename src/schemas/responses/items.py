from pydantic import BaseModel

from src.pokemons.item_type import ItemType


class DailyItemResponse(BaseModel):
    type: int

    @classmethod
    def of(cls, type: ItemType):
        return DailyItemResponse(type=type)
