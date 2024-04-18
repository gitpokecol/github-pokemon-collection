from .base import NotFoundError


class UserNotFoundError(NotFoundError):
    detail = "User Not Found Error"
