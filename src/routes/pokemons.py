from fastapi import Query, Response
from fastapi.routing import APIRouter

from src.dependencies.db import SessionDep
from src.dependencies.facades import PokemonsFacadeDep
from src.schemas.pokemons import PokemonFace

router = APIRouter()


@router.get("/pokemons/{username}")
async def get_pokemons_svg(
    username: str, session: SessionDep, pokemons_facade: PokemonsFacadeDep, face: PokemonFace = Query(PokemonFace.LEFT)
):
    return Response(
        content=await pokemons_facade.render_pokemons(session=session, username=username, face=face),
        headers={"content-type": "image/svg+xml", "Cache-Control": "max-age=3600"},
    )
