from fastapi import Depends, Query, Response
from fastapi.routing import APIRouter

from src.dependencies.db import SessionDep
from src.dependencies.facades import PokemonFacadeDep
from src.dependencies.users import get_username
from src.schemas.backgrounds import Background
from src.schemas.pokemons import Facing
from src.setting import settings

router = APIRouter()


@router.get("/pokemons/{username}")
async def get_pokemons_svg(
    session: SessionDep,
    pokemons_facade: PokemonFacadeDep,
    username: str = Depends(get_username),
    facing: Facing = Query(Facing.LEFT, alias="face"),
    width: int = Query(settings.SVG_WIDTH, ge=settings.SVG_MIN_WIDTH),
    height: int = Query(settings.SVG_HEIGHT, ge=settings.SVG_MIN_HEIGHT),
    background: Background = Query(Background.NONE),
):
    return Response(
        content=await pokemons_facade.render_pokemons(
            session=session, username=username, facing=facing, width=width, height=height, background=background
        ),
        headers={"content-type": "image/svg+xml", "Cache-Control": "max-age=3600"},
    )
