from unittest.mock import AsyncMock

import pytest

from src.repositories.daily_item_abtain_repository import DailyItemAbtainRepository
from src.repositories.daily_item_repository import DailyItemRepository
from src.repositories.pokedex_item_repository import PokedexItemRepository
from src.repositories.pokemon_repository import PokemonRepository
from src.repositories.user_repository import UserRepository
from src.services.evolution_service import EvolutionService
from src.services.pokedex_service import PokedexService


@pytest.fixture()
def mock_pokedex_service() -> PokedexService | AsyncMock:
    return AsyncMock(spec=PokedexService)


@pytest.fixture()
def mock_pokemon_repository() -> PokemonRepository | AsyncMock:
    return AsyncMock(spec=PokemonRepository)


@pytest.fixture()
def mock_evolution_service() -> EvolutionService | AsyncMock:
    return AsyncMock(spec=EvolutionService)


@pytest.fixture()
def mock_daily_item_repository() -> DailyItemRepository | AsyncMock:
    return AsyncMock(spec=DailyItemRepository)


@pytest.fixture()
def mock_daily_item_abtain_repository() -> DailyItemAbtainRepository | AsyncMock:
    return AsyncMock(spec=DailyItemAbtainRepository)


@pytest.fixture()
def mock_user_repository() -> UserRepository | AsyncMock:
    return AsyncMock(spec=UserRepository)


@pytest.fixture()
def mock_pokedex_item_repository() -> PokedexItemRepository | AsyncMock:
    return AsyncMock(spec=PokedexItemRepository)
