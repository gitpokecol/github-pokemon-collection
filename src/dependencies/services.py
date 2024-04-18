from typing import Annotated

from fastapi import Depends

from ..services.user import UserService


async def get_user_service() -> UserService:
    return UserService()


USER_SERVICE_DEP = Annotated[UserService, Depends(get_user_service)]
