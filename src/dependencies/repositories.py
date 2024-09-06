from typing import Annotated

from fastapi import Depends

from src.dependencies.db import SessionDep
from src.repositories.daily_item_abtain_repository import DailyItemAbtainRepository
from src.repositories.daily_item_repository import DailyItemRepository
from src.repositories.pokedex_item_repository import PokedexItemRepository


async def get_daily_item_repository(session: SessionDep) -> DailyItemRepository:
    return DailyItemRepository(session)


async def get_daily_item_abtain_repository(session: SessionDep) -> DailyItemAbtainRepository:
    return DailyItemAbtainRepository(session)


async def get_pokedex_item_repository(session: SessionDep) -> PokedexItemRepository:
    return PokedexItemRepository(session)


DailyItemRepositoryDep = Annotated[DailyItemRepository, Depends(get_daily_item_repository)]
DailyItemAbtainRepositoryDep = Annotated[DailyItemAbtainRepository, Depends(get_daily_item_abtain_repository)]
PokedexItemRepositoryDep = Annotated[PokedexItemRepository, Depends(get_pokedex_item_repository)]
