from datetime import datetime

from sqlmodel import select

from src.models.user import User
from src.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    async def find_by_username(self, username: str):
        stmt = select(User).where(User.username == username)
        return (await self._session.exec(stmt)).first()

    async def find_all_within_last_seen_time(self, start_time: datetime, end_time: datetime) -> list[User]:
        stmt = select(User).where(User.last_seen_at >= start_time, User.last_seen_at <= end_time)
        return (await self._session.exec(stmt)).unique().all()
