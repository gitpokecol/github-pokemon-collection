from enum import Enum


class ErrorCode(Enum):
    detail: str

    # 400
    ALREADY_ABTAINED_DAILY_ITEM = "You already abtained the daily item."

    # 401
    INVALID_GITHUB_OAUTH_TOKEN = "Github oauth token is invalid"
    INVALID_ACCESS_TOKEN = "Access token is invalid"
    ACCESS_TOKEN_REQUIRED = "Access token is required"

    # 403
    NOT_ENOUGH_ITEM = "The item is not enough."

    # 404
    USER_NOT_FOUND = "The user is not found."
    POKEMON_NOT_FOUND = "The pokemon is not found"

    # 500
    INTERNAL_SERVER_ERROR = "Internal server has a problem."

    # 503
    GITHUB_API_SERVICE_UNAVAILABLE = "Github api is unavailable."

    def __init__(self, detail: str) -> None:
        self._value_ = self.name
        self.detail = detail
