from fastapi import APIRouter

from src.dependencies.auths import CurrentUserDep
from src.dependencies.services import PokedexServiceDep
from src.schemas.responses.pokedex import PokedexResponse

router = APIRouter()


@router.get("/api/pokedex")
async def get_pokedex(pokedex_service: PokedexServiceDep, current_user: CurrentUserDep) -> PokedexResponse:
    return pokedex_service.get_pokedex(current_user)
