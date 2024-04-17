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

    model_config = SettingsConfigDict(env_file=".env")


settings = Setting()
