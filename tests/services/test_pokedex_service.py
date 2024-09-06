from unittest.mock import AsyncMock

import pytest

from src.pokemons.pokemon_type import PokemonType
from src.repositories.pokedex_item_repository import PokedexItemRepository
from src.services.pokedex_service import PokedexService
from tests.utils.pokedex import create_pokedex_item
from tests.utils.user import create_user


@pytest.fixture
def pokedex_service(mock_pokedex_item_repository: PokedexItemRepository | AsyncMock) -> PokedexService:
    return PokedexService(pokedex_item_repository=mock_pokedex_item_repository)


async def test_update_pokedex_for_user__add_new_pokemon_type(
    pokedex_service: PokedexService, mock_pokedex_item_repository: PokedexItemRepository | AsyncMock
):
    # given
    pokemon_type = PokemonType.Charmander
    user = create_user()

    # when
    await pokedex_service.update_pokedex_for_user(user, [pokemon_type])

    # then
    pokedex = {pokedex_item.type: pokedex_item for pokedex_item in user.pokedex_items}
    assert pokemon_type in pokedex
    assert pokedex[pokemon_type].obtain_count == 1
    mock_pokedex_item_repository.save.assert_called_once()


async def test_update_pokedex_for_user__add_existed_pokemon_type(pokedex_service: PokedexService):
    # given
    pokemon_type = PokemonType.Charmander
    user = create_user(pokedex_items=[create_pokedex_item(type=pokemon_type)])

    # when
    await pokedex_service.update_pokedex_for_user(user, [pokemon_type])

    # then
    pokedex = {pokedex_item.type: pokedex_item for pokedex_item in user.pokedex_items}
    assert pokemon_type in pokedex
    assert pokedex[pokemon_type].obtain_count == 2
