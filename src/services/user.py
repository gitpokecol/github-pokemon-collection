from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.exceptions.user import UserNotFoundError
from src.models.user import User


class UserService:
    async def exists_by_username(self, *, session: AsyncSession, username: str) -> bool:
        user = await self._get_user(session, username)
        return user is not None

    async def create_new_user(self, *, session: AsyncSession, username: str, commit_point: int) -> User:
        user = User(username=username, commit_point=commit_point)
        session.add(user)
        await session.commit()
        await session.refresh(user)

        return user

    async def update_commit_point(self, *, session: AsyncSession, username: str, commit_point: int) -> User:
        user = await self._get_user(session, username)
        if user is None:
            raise UserNotFoundError

        user.commit_point = commit_point
        user.update_pokemons()
        await session.commit()
        await session.refresh(user)

        return user

    async def _get_user(self, session: AsyncSession, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        rs = await session.exec(stmt)
        return rs.first()
