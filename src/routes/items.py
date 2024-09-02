from fastapi import Query
from fastapi.routing import APIRouter

from src.dependencies.auths import CurrentUserDep
from src.dependencies.services import ItemServiceDep

router = APIRouter()


@router.get("/api/item/daily")
async def get_daily_item(item_service: ItemServiceDep):
    return await item_service.get_daily_item()


@router.post("/api/item/daily/abtain")
async def abtain_item(item_service: ItemServiceDep, current_user: CurrentUserDep, get_substitute: bool = Query(False)):
    await item_service.give_daily_item_to_user(current_user, get_substitute)
