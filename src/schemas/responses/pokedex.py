from pydantic import BaseModel

from src.models.pokedex_item import PokedexItem


class PokedexItemResponse(BaseModel):
    pokemon_type: int


class PokedexResponse(BaseModel):
    items: list[PokedexItemResponse]

    @classmethod
    def of(cls, pokedex_items: list[PokedexItem]) -> "PokedexResponse":
        items = [PokedexItemResponse(pokemon_type=pokedex_item.type) for pokedex_item in pokedex_items]
        return PokedexResponse(items=items)
