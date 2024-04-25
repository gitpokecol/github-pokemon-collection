from typing import Annotated

from fastapi import Depends

from src.dependencies.external import GITHUB_API_DEP
from src.dependencies.renders import SVG_RENDERER_DEP
from src.dependencies.services import USER_SERVICE_DEP
from src.services.pokemons_facade import PokemonsFacade


async def get_pokemons_facade(
    user_service: USER_SERVICE_DEP, github_api: GITHUB_API_DEP, renderer: SVG_RENDERER_DEP
) -> PokemonsFacade:
    return PokemonsFacade(user_service=user_service, github_api=github_api, renderer=renderer)


POKEMONS_FACADE_DEP = Annotated[PokemonsFacade, Depends(get_pokemons_facade)]
