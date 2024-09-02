import asyncio
import pathlib
import sys

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))

from src.models.user import User  # noqa: E402
from src.pokemons.item_type import ItemType  # noqa: E402
from src.setting import settings  # noqa: E402


async def main():
    engine = create_async_engine(settings.DATABASE_URL)
    async with AsyncSession(engine) as session:
        stmt = select(User)
        users = list((await session.exec(stmt)).unique().all())

        for user in users:
            for _ in range(20):
                user.add_item(ItemType.RARE_CANDY)

        await session.commit()


asyncio.run(main())
