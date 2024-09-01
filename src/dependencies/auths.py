from typing import Annotated

from fastapi import Cookie, Depends

from src.auths.jwt import JwtPayload, verify_token
from src.dependencies.db import SessionDep
from src.dependencies.services import UserServiceDep
from src.exceptions.common import UnauthorizedError
from src.exceptions.error_codes import ErrorCode
from src.models.user import User


async def get_token(token: str | None = Cookie(None, alias="Access-Token")) -> JwtPayload:
    if token:
        return verify_token(token)
    else:
        raise UnauthorizedError(ErrorCode.ACCESS_TOKEN_REQUIRED)


async def get_current_user(session: SessionDep, user_service: UserServiceDep, token: "TokenDep") -> User:
    user = await user_service.get_user(session, token.username)
    if not user:
        raise UnauthorizedError(ErrorCode.INVALID_ACCESS_TOKEN)

    return user


TokenDep = Annotated[JwtPayload, Depends(get_token)]
CurrentUserDep = Annotated[User, Depends(get_current_user)]
