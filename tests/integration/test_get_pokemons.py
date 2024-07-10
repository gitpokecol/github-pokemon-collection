import asyncio

from fastapi import status
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.user import User


async def test_get_pokemons__valid_request__responses_svg(client: AsyncClient):
    # when
    response = await client.get("/pokemons/2jun0")
    content = response.content.decode()

    # then
    assert response.status_code == status.HTTP_200_OK
    assert "<svg" in content
    assert "</svg>" in content


async def test_get_pokemons__not_existed_username__responses_not_found(client: AsyncClient):
    # when
    response = await client.get("/pokemons/2")

    # then
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_get_pokemons__10_requests_at_same_time__responses_ok(client: AsyncClient, session: AsyncSession):
    # given
    username = "2jun0"
    user = User(username=username)
    user.set_commit_points(
        {
            2024: 100,
        }
    )
    session.add(user)
    await session.commit()

    # when
    responses = await asyncio.gather(
        client.get("/pokemons/2jun0"),
        client.get("/pokemons/2jun0"),
        client.get("/pokemons/2jun0"),
        client.get("/pokemons/2jun0"),
        client.get("/pokemons/2jun0"),
        client.get("/pokemons/2jun0"),
        client.get("/pokemons/2jun0"),
        client.get("/pokemons/2jun0"),
        client.get("/pokemons/2jun0"),
        client.get("/pokemons/2jun0"),
    )

    # then
    for response in responses:
        assert response.status_code == status.HTTP_200_OK
