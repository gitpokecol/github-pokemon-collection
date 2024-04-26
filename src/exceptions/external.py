from fastapi import status

from src.exceptions.base import BaseException


class GithubAPIRequestFailedError(Exception):
    def __init__(self, *args) -> None:
        super().__init__("Github API request has failed", *args)


class GithubAPIUnavailableError(BaseException):
    detail = "Github API Unavailable Error"
    http_status = status.HTTP_503_SERVICE_UNAVAILABLE
