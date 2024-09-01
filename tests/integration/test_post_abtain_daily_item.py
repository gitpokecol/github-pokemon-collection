from fastapi import status
from httpx import AsyncClient


async def test_post_abtain_daily_item__without_token__response_unauthorized(client: AsyncClient):
    # when
    response = await client.post("/api/item/daily/abtain")

    # then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_post_abtain_daily_item__valids_request__response_ok(client: AsyncClient, use_token):
    # when
    response = await client.post("/api/item/daily/abtain")

    # then
    assert response.status_code == status.HTTP_200_OK
