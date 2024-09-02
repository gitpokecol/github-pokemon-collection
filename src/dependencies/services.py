from typing import Annotated

from fastapi import Depends

from src.dependencies.external import IpAPIDep
from src.dependencies.repositories import DailyItemAbtainRepositoryDep, DailyItemRepositoryDep
from src.services.evolution_service import EvolutionService
from src.services.item_service import ItemService
from src.services.pokedex_service import PokedexService
from src.services.pokemon_service import PokemonService
from src.services.time_service import TimeService
from src.services.user_service import UserService


async def get_user_service() -> UserService:
    return UserService()


async def get_pokemon_service(
    evolution_service: "EvolutionServiceDep",
) -> PokemonService:
    return PokemonService(evolution_service=evolution_service)


async def get_item_service(
    evolution_service: "EvolutionServiceDep",
    daily_item_repository: DailyItemRepositoryDep,
    daily_item_abtain_repository: DailyItemAbtainRepositoryDep,
) -> ItemService:
    return ItemService(
        evolution_service=evolution_service,
        daily_item_repository=daily_item_repository,
        daily_item_abtain_repository=daily_item_abtain_repository,
    )


async def get_time_service(ip_api: IpAPIDep) -> TimeService:
    return TimeService(ip_api=ip_api)


async def get_evolution_service() -> EvolutionService:
    return EvolutionService()


async def get_pokedex_service() -> PokedexService:
    return PokedexService()


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
PokemonServiceDep = Annotated[PokemonService, Depends(get_pokemon_service)]
ItemServiceDep = Annotated[ItemService, Depends(get_item_service)]
TimeServiceDep = Annotated[TimeService, Depends(get_time_service)]
EvolutionServiceDep = Annotated[EvolutionService, Depends(get_evolution_service)]
PokedexServiceDep = Annotated[PokedexService, Depends(get_pokedex_service)]
