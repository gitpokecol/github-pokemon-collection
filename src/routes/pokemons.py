from fastapi import Response
from fastapi.routing import APIRouter

from src.dependencies.db import SessionDep
from src.dependencies.facades import PokemonsFacadeDep

router = APIRouter()


@router.get("/pokemons/{username}")
async def get_pokemons_svg(
    username: str,
    session: SessionDep,
    pokemons_facade: PokemonsFacadeDep,
):
    return Response(
        content=await pokemons_facade.render_pokemons(session=session, username=username),
        headers={"content-type": "image/svg+xml", "Cache-Control": "max-age=3600"},
    )
