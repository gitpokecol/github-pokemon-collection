from fastapi import FastAPI

from .routers.pokemon import router as pokemon_router
from .setting import Envrionment, settings

if settings.ENVIRONMENT is Envrionment.PRODUCTION:
    app = FastAPI(title=settings.TITLE, version=settings.VERSION)
else:
    app = FastAPI(title=settings.TITLE, version=settings.VERSION, docs_url=None, redoc_url=None)

app.include_router(pokemon_router)
