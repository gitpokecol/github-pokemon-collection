from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession


class BaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def save(self, *models: SQLModel):
        self._session.add_all(models)
        await self._session.flush(models)
        for model in models:
            await self._session.refresh(model)

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()
