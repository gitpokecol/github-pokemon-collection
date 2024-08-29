from typing import Annotated

from fastapi import Cookie, Depends

from src.auths.jwt import JwtPayload, verify_token
from src.exceptions.common import UnauthorizedError
from src.exceptions.error_codes import ErrorCode


async def get_token(token: str = Cookie("Access-Token")) -> JwtPayload:
    if token:
        return verify_token(token)
    else:
        raise UnauthorizedError(ErrorCode.ACCESS_TOKEN_REQUIRED)


TokenDep = Annotated[str, Depends(get_token)]
