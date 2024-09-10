from src.models.user import User, UserBase
from src.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, *, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    async def get_user(self, username: str) -> User | None:
        return await self._user_repository.find_by_username(username)

    async def get_or_create_user(self, username: str) -> User:
        user = await self.get_user(username)

        if user:
            return user

        return await self._create_new_user(username)

    async def _create_new_user(self, username: str) -> User:
        user = User.model_validate(UserBase(username=username))

        await self._user_repository.save(user)
        return user
