from unittest.mock import AsyncMock

import pytest

from src.models.user import User
from src.services.pokedex_service import PokedexService
from src.services.pokemon_service import PokemonService
from src.setting import settings


@pytest.fixture()
def pokemon_service(
    mock_pokemon_repository: AsyncMock, mock_pokedex_service: PokedexService | AsyncMock
) -> PokemonService:
    return PokemonService(pokemon_repository=mock_pokemon_repository, pokedex_service=mock_pokedex_service)


@pytest.mark.parametrize(
    "current_commit_point,expected",
    [
        (settings.POKEMON_PER_COMMIT_POINT - 1, 0),
        (settings.POKEMON_PER_COMMIT_POINT, 1),
        (settings.POKEMON_PER_COMMIT_POINT * 3, 3),
    ],
)
async def test_give_pokemons_for_user__inputs_commit_point__add_new_pokemons(
    pokemon_service: PokemonService,
    mock_pokedex_service: PokedexService | AsyncMock,
    current_commit_point: int,
    expected: int,
):
    # given
    user = User(username="username")

    # when
    await pokemon_service.give_pokemons_for_user(user, 0, current_commit_point)

    # then
    assert len(user.pokemons) == expected
    args, _ = mock_pokedex_service.update_pokedex_for_user.call_args
    assert len(args[1]) == expected
