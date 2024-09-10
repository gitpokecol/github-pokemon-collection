from fastapi import Depends, Query, Response
from fastapi.routing import APIRouter

from src.dependencies.auths import CurrentUserDep
from src.dependencies.commons import ClientIpAddressDep
from src.dependencies.services import (
    ItemServiceDep,
    PokemonServiceDep,
    ProfileServiceDep,
    TimeServiceDep,
    UserServiceDep,
)
from src.dependencies.users import get_username
from src.pokemons.item_type import ItemType
from src.schemas.backgrounds import Background
from src.schemas.pokemons import Facing
from src.schemas.responses.items import UseItemResponse
from src.schemas.responses.pokemons import PokemonsResponse
from src.setting import settings

router = APIRouter()


@router.get("/pokemons/{username}")
async def get_pokemons_svg(
    profile_service: ProfileServiceDep,
    user_service: UserServiceDep,
    time_service: TimeServiceDep,
    client_ip_address: ClientIpAddressDep,
    username: str = Depends(get_username),
    facing: Facing = Query(Facing.LEFT, alias="face"),
    width: int = Query(settings.SVG_WIDTH, ge=settings.SVG_MIN_WIDTH),
    height: int = Query(settings.SVG_HEIGHT, ge=settings.SVG_MIN_HEIGHT),
    background: Background = Query(Background.NONE),
):
    time = await time_service.get_time_for_client(client_ip_address)
    user = await user_service.get_or_create_user(username)
    profile = await profile_service.render_profile(
        user=user,
        facing=facing,
        width=width,
        height=height,
        background=background,
        time=time,
    )
    return Response(
        content=profile,
        headers={"content-type": "image/svg+xml", "Cache-Control": "max-age=3600"},
    )


@router.get("/api/pokemons")
async def get_pokemons(pokemon_service: PokemonServiceDep, current_user: CurrentUserDep) -> PokemonsResponse:
    return pokemon_service.get_pokemons_by_user(current_user)


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
    pokemon = pokemon_service.find_pokemon_in_owner(pokemon_id, current_user)
    return await item_service.use_item_to_pokemon(pokemon, ItemType(item_type), current_user, time)
