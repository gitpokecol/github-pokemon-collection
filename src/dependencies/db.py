from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from ..db import engine


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session


SESSION_DEP = Annotated[AsyncSession, Depends(get_session)]
