from fastapi import status
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.user import User
from src.pokemons.form import ArceusForm
from src.pokemons.gender import Gender
from src.pokemons.pokemon_type import PokemonType
from tests.utils.pokemon import create_pokemon


async def test_get_pokemons__valid_request__response_pokemons(
    client: AsyncClient, session: AsyncSession, user: User, use_token
):
    # given
    pikachu = create_pokemon(pokemon_type=PokemonType.Pikachu, level=32, gender=Gender.FEMALE, is_shiny=True)
    arceus = create_pokemon(pokemon_type=PokemonType.Arceus, level=42, gender=Gender.GENDERLESS, form=ArceusForm.DARK)
    user.pokemons.append(pikachu)
    user.pokemons.append(arceus)
    await session.commit()

    # when
    res = await client.get("/api/pokemons")

    # then
    assert res.status_code == status.HTTP_200_OK
    assert res.json() == {
        "pokemons": [
            {
                "id": pikachu.id,
                "pokemon_type": pikachu.type,
                "level": pikachu.level,
                "gender": pikachu.gender,
                "is_shiny": pikachu.is_shiny,
                "form": pikachu.form,
            },
            {
                "id": arceus.id,
                "pokemon_type": arceus.type,
                "level": arceus.level,
                "gender": arceus.gender,
                "is_shiny": arceus.is_shiny,
                "form": arceus.form,
            },
        ]
    }
