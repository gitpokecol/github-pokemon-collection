from datetime import datetime, timedelta, timezone

import jwt
from pydantic import BaseModel, ValidationError

from src.exceptions.common import UnauthorizedError
from src.exceptions.error_codes import ErrorCode
from src.setting import settings


class JwtPayload(BaseModel):
    username: str
    exp: datetime


def encode_token(username: str) -> str:
    payload = JwtPayload(username=username, exp=datetime.now(tz=timezone.utc) + timedelta(hours=3))
    return jwt.encode(payload.model_dump(), settings.JWT_SECRET)


def verify_token(token: str) -> JwtPayload:
    try:
        return JwtPayload.model_validate(jwt.decode(token, settings.JWT_SECRET))
    except jwt.InvalidTokenError | ValidationError:
        raise UnauthorizedError(ErrorCode.INVALID_ACCESS_TOKEN)
