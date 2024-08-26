from typing import Annotated

from fastapi import BackgroundTasks, Depends

from src.dependencies.external import GithubAPIDep
from src.dependencies.renders import ProfileRendererDep
from src.dependencies.services import UserServiceDep
from src.services.pokemons_facade import PokemonsFacade


async def get_pokemons_facade(
    user_service: UserServiceDep,
    github_api: GithubAPIDep,
    renderer: ProfileRendererDep,
    background_tasks: BackgroundTasks,
) -> PokemonsFacade:
    return PokemonsFacade(
        user_service=user_service, github_api=github_api, renderer=renderer, background_tasks=background_tasks
    )


PokemonsFacadeDep = Annotated[PokemonsFacade, Depends(get_pokemons_facade)]
