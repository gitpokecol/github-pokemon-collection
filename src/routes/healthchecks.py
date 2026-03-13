from fastapi.routing import APIRouter

router = APIRouter()

@router.post("/healthcheck")
async def healthcheck():
    return {"status": "ok"}