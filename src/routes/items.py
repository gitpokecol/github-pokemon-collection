from fastapi.routing import APIRouter

from src.dependencies.db import SessionDep
from src.dependencies.services import ItemServiceDep

router = APIRouter()


@router.get("/api/item/daily")
async def get_daily_item(session: SessionDep, item_service: ItemServiceDep):
    return await item_service.get_daily_item(session)
