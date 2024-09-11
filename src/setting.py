from datetime import timedelta
from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class Envrionment(str, Enum):
    TEST = "TEST"
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"


class Setting(BaseSettings):
    TITLE: str = "Github pokemon collection api"
    VERSION: str = "4"

    # env
    ENVIRONMENT: Envrionment = Envrionment.PRODUCTION

    # database
    DATABASE_URL: str

    # github
    GITHUB_API_TOKEN: str
    GITHUB_OAUTH_CLIENT_ID: str
    GITHUB_OAUTH_CLIENT_SECRET: str
    GITHUB_OAUTH_CALLBACK_URL: str

    # auth
    JWT_SECRET: str

    # render
    SVG_WIDTH: int = 300
    SVG_MIN_WIDTH: int = 250
    SVG_HEIGHT: int = 250
    SVG_MIN_HEIGHT: int = 200

    # pokemon strategy
    POKEMON_PER_COMMIT_POINT: int = 50
    LEVEL_UP_PER_COMMIT_POINT: int = 2
    SHINY_POKEMON_RATE: float = 0.1
    COMMIT_POINT_UPDATE_PERIOD: timedelta = timedelta(hours=1)

    # cors
    CROSS_ORIGINS: list[str]

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Setting()  # type: ignore
