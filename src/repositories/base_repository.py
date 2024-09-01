from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession


class BaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def save(self, model: SQLModel):
        self._session.add(model)

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()
