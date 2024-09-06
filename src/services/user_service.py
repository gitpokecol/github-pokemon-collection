from src.models.user import User, UserBase
from src.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, *, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    async def create_new_user(self, *, username: str, commit_points: dict[int, int]) -> User:
        user = User.model_validate(UserBase(username=username))
        user.set_commit_points(commit_points)

        await self._user_repository.save(user)
        return user

    async def get_user(self, username: str) -> User | None:
        return await self._user_repository.find_by_username(username)
