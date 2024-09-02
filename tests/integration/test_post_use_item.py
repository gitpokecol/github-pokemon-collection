from fastapi import status
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.bag_item import BagItem
from src.models.user import User
from src.pokemons.item_type import ItemType
from src.pokemons.pokemon_type import PokemonType
from tests.utils.pokemon import create_pokemon


async def test_post_use_item__valid_request__responses_ok(
    client: AsyncClient, session: AsyncSession, user: User, use_token
):
    # given
    sun_stone = ItemType.SUN_STONE
    pokemon = create_pokemon(pokemon_type=PokemonType.Sunkern)
    user.bag_items.append(BagItem(item_type=sun_stone, count=1))
    user.pokemons.append(pokemon)
    await session.commit()
    await session.refresh(pokemon)

    # when
    response = await client.post(f"/api/pokemon/{pokemon.id}/use-item", params={"item-type": int(sun_stone)})

    # then
    assert response.status_code == status.HTTP_200_OK
    res_json = response.json()
    assert res_json == {"is_used": True}
