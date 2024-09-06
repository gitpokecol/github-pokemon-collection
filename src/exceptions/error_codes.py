from enum import Enum


class ErrorCode(str, Enum):
    detail: str

    # 400
    ALREADY_ABTAINED_DAILY_ITEM = "You already abtained the daily item."

    # 401
    INVALUD_GITHUB_AUTHORIZATION = "Github authorization is invalid"
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

    def __new__(cls, detail: str) -> "ErrorCode":
        instance = str.__new__(cls, detail)
        instance._value_ = detail
        instance.detail = detail

        return instance
