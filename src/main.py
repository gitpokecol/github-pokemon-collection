from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.staticfiles import StaticFiles

from src.dependencies.renders import image_loader
from src.exceptions.handler import install_exception_handlers
from src.routes.pokemons import router as pokemon_router
from src.setting import Envrionment, settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await image_loader.prepare()
    yield


if settings.ENVIRONMENT is Envrionment.PRODUCTION:
    app = FastAPI(lifespan=lifespan, title=settings.TITLE, version=settings.VERSION, docs_url=None, redoc_url=None)
else:
    app = FastAPI(lifespan=lifespan, title=settings.TITLE, version=settings.VERSION)


app.include_router(pokemon_router)
install_exception_handlers(app)

app.mount("/static", StaticFiles(directory="static"), name="static")
