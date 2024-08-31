from fastapi import status
from httpx import AsyncClient


async def test_get_daily_item__valid_request__responses_daily_item(client: AsyncClient):
    # when
    response = await client.get("/api/item/daily")

    # then
    assert response.status_code == status.HTTP_200_OK
    res_json = response.json()
    assert "type" in res_json
