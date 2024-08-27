from typing import Annotated

from fastapi import Depends

from src.services.pokemon_service import PokemonSerivce
from src.services.user_service import UserService


async def get_user_service() -> UserService:
    return UserService()


async def get_pokemon_service() -> PokemonSerivce:
    return PokemonSerivce()


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
PokemonSerivceDep = Annotated[PokemonSerivce, Depends(get_pokemon_service)]
