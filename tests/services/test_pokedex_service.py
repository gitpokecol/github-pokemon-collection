from unittest.mock import AsyncMock

import pytest

from src.models.pokedex_item import PokedexItem
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
    pokemon_types = [PokemonType.Charmander, PokemonType.Abra]
    user = create_user()

    # when
    await pokedex_service.update_pokedex_for_user(user, pokemon_types)

    # then
    calls = mock_pokedex_item_repository.save.call_args_list
    for pokemon_type, call in zip(pokemon_types, calls):
        args, _ = call
        pokedex_item: PokedexItem = args[0]
        assert pokedex_item.type == pokemon_type
        assert pokedex_item.obtain_count == 1


async def test_update_pokedex_for_user__add_existed_pokemon_type(
    pokedex_service: PokedexService, mock_pokedex_item_repository: PokedexItemRepository | AsyncMock
):
    # given
    pokemon_type = PokemonType.Charmander
    pokedex_item = create_pokedex_item(type=pokemon_type)
    user = create_user()
    mock_pokedex_item_repository.find_by_owner.return_value = [pokedex_item]

    # when
    await pokedex_service.update_pokedex_for_user(user, [pokemon_type])

    # then
    assert pokedex_item.obtain_count == 2
