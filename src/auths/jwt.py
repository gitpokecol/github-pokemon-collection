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
    encoded = jwt.encode(payload.model_dump(), settings.JWT_SECRET)
    return f"Bearer {encoded}"


def verify_token(token: str) -> JwtPayload:
    if not token.startswith("Bearer "):
        raise UnauthorizedError(ErrorCode.INVALID_ACCESS_TOKEN)

    try:
        return JwtPayload.model_validate(jwt.decode(token[7:], settings.JWT_SECRET))
    except (jwt.InvalidTokenError, ValidationError):
        raise UnauthorizedError(ErrorCode.INVALID_ACCESS_TOKEN)
