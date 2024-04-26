from fastapi import FastAPI

from src.exceptions.handler import install_exception_handlers
from src.routes.pokemons import router as pokemon_router
from src.setting import Envrionment, settings

if settings.ENVIRONMENT is Envrionment.PRODUCTION:
    app = FastAPI(title=settings.TITLE, version=settings.VERSION)
else:
    app = FastAPI(title=settings.TITLE, version=settings.VERSION, docs_url=None, redoc_url=None)

app.include_router(pokemon_router)
install_exception_handlers(app)
