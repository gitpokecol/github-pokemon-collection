from datetime import datetime

from src.models.user import User, UserBase
from src.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, *, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    async def get_user(self, username: str) -> User | None:
        return await self._user_repository.find_by_username(username)
    
    async def create_user(self, username: str) -> User:
        return await self._create_new_user(username)

    async def get_or_create_user(self, username: str) -> User:
        user = await self.get_user(username)

        if user:
            return user

        return await self._create_new_user(username)
    
    async def update_user_seen_time(self, user: User) -> None:
        user.last_seen_at = datetime.utcnow()
        await self._user_repository.save(user)

    async def get_users_within_last_seen_time(self, start_time: datetime, end_time: datetime) -> list[User]:
        return await self._user_repository.find_all_within_last_seen_time(start_time, end_time)

    async def _create_new_user(self, username: str) -> User:
        user = User.model_validate(UserBase(username=username))

        await self._user_repository.save(user)
        return user
