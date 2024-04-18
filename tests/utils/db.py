from sqlalchemy.util.concurrency import greenlet_spawn
from sqlmodel import SQLModel

from tests.db import engine


async def drop_tables():
    await greenlet_spawn(SQLModel.metadata.drop_all, engine.sync_engine)


async def create_all_table():
    await greenlet_spawn(SQLModel.metadata.create_all, engine.sync_engine)
