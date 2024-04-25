from fastapi import FastAPI, HTTPException, Request
from fastapi.exception_handlers import http_exception_handler

from src.exceptions.base import BaseException


def install_exception_handlers(app: FastAPI):
    @app.exception_handler(BaseException)
    async def custom_exception_handler(request: Request, err: BaseException):
        http_exc = HTTPException(status_code=err.http_status, detail=err.detail)
        return await http_exception_handler(request, http_exc)
