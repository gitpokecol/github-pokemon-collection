from fastapi import Query, Response
from fastapi.routing import APIRouter

from src.dependencies.db import SessionDep
from src.dependencies.facades import PokemonsFacadeDep
from src.schemas.backgrounds import Background
from src.schemas.pokemons import PokemonFace
from src.setting import settings

router = APIRouter()


@router.get("/pokemons/{username}")
async def get_pokemons_svg(
    username: str,
    session: SessionDep,
    pokemons_facade: PokemonsFacadeDep,
    face: PokemonFace = Query(PokemonFace.LEFT),
    width: int = Query(settings.SVG_WIDTH, ge=settings.SVG_MIN_WIDTH),
    height: int = Query(settings.SVG_HEIGHT, ge=settings.SVG_MIN_HEIGHT),
    background: Background = Query(Background.NONE),
):
    return Response(
        content=await pokemons_facade.render_pokemons(
            session=session, username=username, face=face, width=width, height=height, background=background
        ),
        headers={"content-type": "image/svg+xml", "Cache-Control": "max-age=3600"},
    )
