from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class Envrionment(Enum):
    TEST = "TEST"
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"


class Setting(BaseSettings):
    TITLE: str = "Github pokemon collection api"
    VERSION: str = "0.0.1"

    ENVIRONMENT: Envrionment = Envrionment.PRODUCTION

    DATABASE_URL: str
    GITHUB_API_TOKEN: str

    POKEMON_PER_COMMIT_POINT: int = 100

    model_config = SettingsConfigDict(env_file=".env")


settings = Setting()  # type: ignore
