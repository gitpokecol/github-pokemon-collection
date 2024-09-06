from typing import Annotated

from fastapi import Depends, Header

from src.auths.jwt import JwtPayload, verify_token
from src.dependencies.services import UserServiceDep
from src.exceptions.common import UnauthorizedError
from src.exceptions.error_codes import ErrorCode
from src.models.user import User


async def get_token(authorization: str | None = Header(None, alias="Authorization")) -> JwtPayload:
    if authorization:
        return verify_token(authorization)
    else:
        raise UnauthorizedError(ErrorCode.ACCESS_TOKEN_REQUIRED)


async def get_current_user(user_service: UserServiceDep, token: "TokenDep") -> User:
    user = await user_service.get_user(token.username)
    if not user:
        raise UnauthorizedError(ErrorCode.INVALID_ACCESS_TOKEN)

    return user


TokenDep = Annotated[JwtPayload, Depends(get_token)]
CurrentUserDep = Annotated[User, Depends(get_current_user)]
