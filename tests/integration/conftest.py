import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession

from src.main import app
from tests.db import engine
from tests.utils.db import create_all_table, drop_tables

lock = asyncio.Lock()


@pytest.fixture(autouse=True)
async def database():
    async with lock:
        await drop_tables()
        await create_all_table()
        yield
        await drop_tables()


@pytest.fixture()
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client


@pytest.fixture()
async def session(database) -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
