from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.user import User, UserBase


class UserService:

    def create_new_user(self, *, session: AsyncSession, username: str, commit_points: dict[int, int]) -> User:
        user = User.model_validate(UserBase(username=username))
        user.set_commit_points(commit_points)

        session.add(user)
        return user

    async def update_commit_point(self, *, user: User, year: int, commit_point: int) -> None:
        user.set_commit_point(year, commit_point)

    async def get_user(self, session: AsyncSession, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        rs = await session.exec(stmt)

        await session.close()
        return rs.first()
