from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.user import User


async def get_user(session: AsyncSession, *, username: str):
    stmt = select(User).where(User.username == username)
    rs = await session.exec(stmt)
    return rs.first()
