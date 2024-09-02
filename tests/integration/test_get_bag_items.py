from fastapi import status
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.bag_item import BagItem
from src.models.user import User
from src.pokemons.item_type import ItemType


async def test_get_bag_items__valid_request__responses_bag_items(
    client: AsyncClient, session: AsyncSession, user: User, use_token
):
    # given
    user.bag_items.append(BagItem(item_type=ItemType.FIRE_STONE, count=2))
    user.bag_items.append(BagItem(item_type=ItemType.ICE_STONE, count=1))
    await session.commit()

    # when
    response = await client.get("/api/item/bag-items")

    # then
    assert response.status_code == status.HTTP_200_OK
    res_json = response.json()
    assert res_json == {
        "items": [{"item_type": ItemType.FIRE_STONE, "count": 2}, {"item_type": ItemType.ICE_STONE, "count": 1}]
    }
