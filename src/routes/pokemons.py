from fastapi import BackgroundTasks, Depends, Query, Response
from fastapi.routing import APIRouter

from src.dependencies.auths import CurrentUserDep
from src.dependencies.commons import ClientIpAddressDep
from src.dependencies.services import (
    CommitPointRewardServiceDep,
    ItemServiceDep,
    PokemonServiceDep,
    ProfileServiceDep,
    TimeServiceDep,
    UserServiceDep,
)
from src.dependencies.users import get_username
from src.models.user import User
from src.pokemons.item_type import ItemType
from src.schemas.backgrounds import Background
from src.schemas.pokemons import Facing
from src.schemas.responses.items import UseItemResponse
from src.schemas.responses.pokemons import PokemonsResponse
from src.services.time_service import TimeService
from src.setting import settings

router = APIRouter()


async def update_commit_point_and_reward_task(
    *,
    commit_point_reward_service: CommitPointRewardServiceDep,
    time_service: TimeService,
    client_ip_address: str | None,
    user: User
):
    time = await time_service.get_time_for_client(client_ip_address)
    await commit_point_reward_service.update_commit_point_and_reward(user, time)


@router.get("/pokemons/{username}")
async def get_pokemons_svg(
    profile_service: ProfileServiceDep,
    user_service: UserServiceDep,
    time_service: TimeServiceDep,
    commit_point_reward_service: CommitPointRewardServiceDep,
    client_ip_address: ClientIpAddressDep,
    background_tasks: BackgroundTasks,
    username: str = Depends(get_username),
    facing: Facing = Query(Facing.LEFT, alias="face"),
    width: int = Query(settings.SVG_WIDTH, ge=settings.SVG_MIN_WIDTH),
    height: int = Query(settings.SVG_HEIGHT, ge=settings.SVG_MIN_HEIGHT),
    background: Background = Query(Background.NONE),
):
    user = await user_service.get_or_create_user(username)
    if commit_point_reward_service.can_update_commit_point(user):
        background_tasks.add_task(
            update_commit_point_and_reward_task,
            commit_point_reward_service=commit_point_reward_service,
            time_service=time_service,
            client_ip_address=client_ip_address,
            user=user,
        )

    profile = await profile_service.render_profile(
        user=user,
        facing=facing,
        width=width,
        height=height,
        background=background,
    )

    return Response(
        content=profile,
        headers={
            "content-type": "image/svg+xml",
            "Cache-Control": "max-age=3600",
        },
    )


@router.get("/api/pokemons")
async def get_pokemons(
    pokemon_service: PokemonServiceDep,
    current_user: CurrentUserDep,
    time_service: TimeServiceDep,
    commit_point_reward_service: CommitPointRewardServiceDep,
    client_ip_address: ClientIpAddressDep,
    background_tasks: BackgroundTasks,
) -> PokemonsResponse:
    if commit_point_reward_service.can_update_commit_point(current_user):
        background_tasks.add_task(
            update_commit_point_and_reward_task,
            commit_point_reward_service=commit_point_reward_service,
            time_service=time_service,
            client_ip_address=client_ip_address,
            user=current_user,
        )

    return await pokemon_service.get_pokemons_response(current_user)


@router.post("/api/pokemon/{pokemon_id}/use-item")
async def use_item(
    pokemon_id: int,
    client_ip_address: ClientIpAddressDep,
    time_service: TimeServiceDep,
    item_service: ItemServiceDep,
    pokemon_service: PokemonServiceDep,
    current_user: CurrentUserDep,
    item_type: int = Query(alias="item-type"),
) -> UseItemResponse:
    time = await time_service.get_time_for_client(client_ip_address)
    pokemon = await pokemon_service.get_pokemon_by_id(pokemon_id)
    return await item_service.use_item_to_pokemon(pokemon, ItemType(item_type), current_user, time)
