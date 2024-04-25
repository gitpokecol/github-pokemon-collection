from fastapi import Response
from fastapi.routing import APIRouter

from src.dependencies.db import SESSION_DEP
from src.dependencies.facades import POKEMONS_FACADE_DEP

router = APIRouter()


@router.get("/pokemons/{username}")
async def get_pokemons_svg(username: str, session: SESSION_DEP, pokemons_facade: POKEMONS_FACADE_DEP):
    return Response(
        content=await pokemons_facade.render_pokemons(session=session, username=username),
        headers={"content-type": "image/svg+xml", "Cache-Control": "max-age=3600"},
    )
