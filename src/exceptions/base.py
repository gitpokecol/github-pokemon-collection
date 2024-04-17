class BaseException(Exception):
    detail: str

    def __new__(cls):
        if cls is BaseException:
            raise NotImplementedError

        return super().__new__(cls)


class NotFoundError(BaseException):
    detail = "Not Found Error"


class BadRequestError(BaseException):
    detail = "Bad Request Error"


class InternalError(BaseException):
    detail = "Internal Server Error"
