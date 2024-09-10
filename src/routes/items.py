from fastapi import Query
from fastapi.routing import APIRouter

from src.dependencies.auths import CurrentUserDep, TokenDep
from src.dependencies.services import ItemServiceDep
from src.schemas.responses.items import BagItemsResponse, DailyItemResponse

router = APIRouter()


@router.get("/api/item/daily")
async def get_daily_item(item_service: ItemServiceDep, current_user: CurrentUserDep) -> DailyItemResponse:
    return await item_service.get_daily_item(current_user)


@router.post("/api/item/daily/abtain")
async def abtain_item(
    item_service: ItemServiceDep,
    current_user: CurrentUserDep,
    get_substitute: bool = Query(False, alias="get-substitute"),
):
    await item_service.give_daily_item_to_user(current_user, get_substitute)


@router.get("/api/item/bag-items")
async def get_bag_items(item_service: ItemServiceDep, token: TokenDep) -> BagItemsResponse:
    return await item_service.get_bag_items(token.username)
