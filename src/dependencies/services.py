from typing import Annotated

from fastapi import Depends

from src.services.user import UserService


async def get_user_service() -> UserService:
    return UserService()


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
