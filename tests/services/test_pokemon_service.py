from unittest.mock import Mock

import pytest

from src.models.user import User
from src.services.pokemon_service import PokemonService
from src.setting import settings


@pytest.fixture()
def pokemon_serivce() -> PokemonService:
    return PokemonService()


@pytest.mark.parametrize(
    "current_commit_point,expected",
    [
        (settings.POKEMON_PER_COMMIT_POINT - 1, 0),
        (settings.POKEMON_PER_COMMIT_POINT, 1),
        (settings.POKEMON_PER_COMMIT_POINT * 3, 3),
    ],
)
async def test_give_pokemons_for_user__inputs_commit_point__add_new_pokemons(
    pokemon_serivce: PokemonService, mock_session: Mock, current_commit_point: int, expected: int
):
    # given
    user = User(username="username")

    # when
    pokemon_serivce.give_pokemons_for_user(user, 0, current_commit_point)

    # then
    assert len(user.pokemons) == expected
    assert len(user.pokedex_items) == expected


@pytest.mark.parametrize(
    "current_commit_point",
    [
        settings.POKEMON_PER_COMMIT_POINT - 1,
        settings.POKEMON_PER_COMMIT_POINT,
        settings.POKEMON_PER_COMMIT_POINT * 3,
    ],
)
async def test_give_pokemons_for_user__inputs_commit_point__update_pokedex_items(
    pokemon_serivce: PokemonService, mock_session: Mock, current_commit_point: int
):
    # given
    user = User(username="username")

    # when
    pokemon_serivce.give_pokemons_for_user(user, 0, current_commit_point)

    # then
    assert set(pokemon.type for pokemon in user.pokemons) == set(item.type for item in user.pokedex_items)
    for item in user.pokedex_items:
        assert item.obtain_count == 1
