from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.exceptions.common import NotFoundError
from src.exceptions.error_codes import ErrorCode
from src.models.user import User


class UserService:
    async def create_new_user(self, *, session: AsyncSession, username: str, commit_points: dict[int, int]) -> User:
        user = User(username=username)
        user.set_commit_points(commit_points)

        session.add(user)
        await session.commit()
        await session.refresh(user)

        return user

    async def update_commit_point(self, *, session: AsyncSession, username: str, year: int, commit_point: int) -> User:
        user = await self.get_user(session, username)
        if user is None:
            raise NotFoundError(ErrorCode.USER_NOT_FOUND)

        user.set_commit_point(year, commit_point)

        await session.commit()
        await session.refresh(user)

        return user

    async def get_user(self, session: AsyncSession, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        rs = await session.exec(stmt)
        return rs.first()
