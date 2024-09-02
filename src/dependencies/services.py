from typing import Annotated

from fastapi import Depends

from src.dependencies.external import IpAPIDep
from src.dependencies.repositories import DailyItemAbtainRepositoryDep, DailyItemRepositoryDep
from src.services.item_service import ItemService
from src.services.pokemon_service import PokemonService
from src.services.time_service import TimeService
from src.services.user_service import UserService


async def get_user_service() -> UserService:
    return UserService()


async def get_pokemon_service() -> PokemonService:
    return PokemonService()


async def get_item_service(
    daily_item_repository: DailyItemRepositoryDep, daily_item_abtain_repository: DailyItemAbtainRepositoryDep
) -> ItemService:
    return ItemService(
        daily_item_repository=daily_item_repository, daily_item_abtain_repository=daily_item_abtain_repository
    )

async def get_time_service(ip_api: IpAPIDep) -> TimeService:
    return TimeService(ip_api=ip_api)




UserServiceDep = Annotated[UserService, Depends(get_user_service)]
PokemonServiceDep = Annotated[PokemonService, Depends(get_pokemon_service)]
ItemServiceDep = Annotated[ItemService, Depends(get_item_service)]
TimeServiceDep = Annotated[TimeService, Depends(get_time_service)]
