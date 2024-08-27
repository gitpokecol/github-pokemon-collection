from typing import Annotated

from fastapi import BackgroundTasks, Depends

from src.dependencies.external import GithubAPIDep
from src.dependencies.renders import ProfileRendererDep
from src.dependencies.services import PokemonSerivceDep, UserServiceDep
from src.services.pokemon_facade import PokemonFacade


async def get_pokemon_facade(
    pokemon_service: PokemonSerivceDep,
    user_service: UserServiceDep,
    github_api: GithubAPIDep,
    renderer: ProfileRendererDep,
    background_tasks: BackgroundTasks,
) -> PokemonFacade:
    return PokemonFacade(
        user_service=user_service,
        pokemon_service=pokemon_service,
        github_api=github_api,
        renderer=renderer,
        background_tasks=background_tasks,
    )


PokemonFacadeDep = Annotated[PokemonFacade, Depends(get_pokemon_facade)]
