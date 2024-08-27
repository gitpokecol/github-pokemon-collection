from typing import Annotated

from fastapi import Depends

from src.services.pokemon_service import PokemonService
from src.services.user_service import UserService


async def get_user_service() -> UserService:
    return UserService()


async def get_pokemon_service() -> PokemonService:
    return PokemonService()


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
PokemonSerivceDep = Annotated[PokemonService, Depends(get_pokemon_service)]
