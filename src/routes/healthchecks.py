from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}