from abc import ABC

from src.exceptions.error_codes import ErrorCode


class CommonException(ABC, Exception):
    def __init__(self, error_code: ErrorCode) -> None:
        super().__init__(error_code.detail)
        self._error_code = error_code

    @property
    def detail(self) -> str:
        return self._error_code.detail

    @property
    def error_code(self) -> ErrorCode:
        return self._error_code


class NotFoundError(CommonException):
    pass


class BadRequestError(CommonException):
    pass


class InternalServerError(CommonException):
    pass


class ServiceUnavailableError(CommonException):
    pass


class UnauthorizedError(CommonException):
    pass


class ForbiddenError(CommonException):
    pass
