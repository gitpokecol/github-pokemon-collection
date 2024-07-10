import asyncio

from fastapi import status
from httpx import AsyncClient


async def test_get_pokemons__valid_request__responses_svg(client: AsyncClient):
    # when
    response = await client.get("/pokemons/2jun0")
    response_json = response.json()

    # then
    assert response.status_code == status.HTTP_200_OK
    assert response_json


async def test_get_pokemons__not_existed_username__responses_not_found(client: AsyncClient):
    # when
    response = await client.get("/pokemons/2")

    # then
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_get_pokemons__10_requests_at_same_time__responses_ok(client: AsyncClient):
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
