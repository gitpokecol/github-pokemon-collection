from enum import Enum


class ErrorCode(Enum):
    detail: str

    # 400

    # 402
    INVALID_GITHUB_OAUTH_TOKEN = "Github oauth token is invalid"
    INVALID_ACCESS_TOKEN = "Access token is invalid"
    ACCESS_TOKEN_REQUIRED = "Access token is required"

    # 404
    USER_NOT_FOUND = "The user is not found."

    # 500
    INTERNAL_SERVER_ERROR = "Internal server has a problem."

    # 503
    GITHUB_API_SERVICE_UNAVAILABLE = "Github api is unavailable."

    def __init__(self, detail: str) -> None:
        self._value_ = self.name
        self.detail = detail
