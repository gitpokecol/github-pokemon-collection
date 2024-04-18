from typing import Annotated

from fastapi import Depends

from ..services.pokemons_facade import PokemonsFacade
from .externals import GITHUB_API_DEP
from .renders import SVG_RENDERER_DEP
from .services import USER_SERVICE_DEP


async def get_pokemons_facade(
    user_service: USER_SERVICE_DEP, github_api: GITHUB_API_DEP, renderer: SVG_RENDERER_DEP
) -> PokemonsFacade:
    return PokemonsFacade(user_service=user_service, github_api=github_api, renderer=renderer)


POKEMONS_FACADE_DEP = Annotated[PokemonsFacade, Depends(get_pokemons_facade)]
