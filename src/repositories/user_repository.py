from sqlmodel import select

from src.models.user import User
from src.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    async def find_by_username(self, username: str):
        stmt = select(User).where(User.username == username)
        return (await self._session.exec(stmt)).first()
