from fastapi import status
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession


async def test_get_pokemons(client: AsyncClient, session: AsyncSession):
    username = "2jun0"

    res = await client.get(f"/pokemons/{username}")
    assert res.status_code == status.HTTP_200_OK
