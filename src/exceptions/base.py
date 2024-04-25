from fastapi import status


class BaseException(Exception):
    detail: str
    http_status: int

    def __new__(cls):
        if cls is BaseException:
            raise NotImplementedError

        return super().__new__(cls)


class NotFoundError(BaseException):
    detail = "Not Found Error"
    http_status = status.HTTP_404_NOT_FOUND


class BadRequestError(BaseException):
    detail = "Bad Request Error"
    http_status = status.HTTP_400_BAD_REQUEST


class InternalError(BaseException):
    detail = "Internal Server Error"
    http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
