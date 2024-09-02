from fastapi import status
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.user import User
from src.pokemons.pokemon_type import PokemonType


async def test_get_pokedex__valid_request__responses_pokedex(
    client: AsyncClient, session: AsyncSession, user: User, use_token
):
    # given
    user.update_pokedex([PokemonType.Abomasnow, PokemonType.Cacnea])
    await session.commit()

    # when
    response = await client.get("/api/pokedex")

    # then
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "items": [{"pokemon_type": int(PokemonType.Cacnea)}, {"pokemon_type": int(PokemonType.Abomasnow)}]
    }
