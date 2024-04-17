from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exception_handlers import http_exception_handler

from exceptions.base import BadRequestError, InternalError, NotFoundError


def install_exception_handlers(app: FastAPI):
    @app.exception_handler(NotFoundError)
    async def not_found_error_handler(request: Request, err: NotFoundError):
        http_exc = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.detail)
        return await http_exception_handler(request, http_exc)

    @app.exception_handler(InternalError)
    async def internal_server_error_handler(request: Request, err: InternalError):
        http_exc = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=err.detail)
        return await http_exception_handler(request, http_exc)

    @app.exception_handler(BadRequestError)
    async def bad_request_error_handler(request: Request, err: BadRequestError):
        http_exc = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=err.detail)
        return await http_exception_handler(request, http_exc)

    @app.exception_handler(Exception)
    async def exception_handler(request: Request, err: Exception):
        return await internal_server_error_handler(request, InternalError())
