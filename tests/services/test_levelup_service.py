from unittest.mock import AsyncMock

import pytest

from src.pokemons.evolution import evolution_rules
from src.pokemons.pokemon_type import PokemonType
from src.pokemons.time import Time
from src.services.evolution_service import EvolutionService
from src.services.levelup_service import LevelUpService
from src.setting import settings
from tests.utils.pokemon import create_pokemon
from tests.utils.user import create_user


@pytest.fixture
def levelup_service(mock_evolution_service: EvolutionService | AsyncMock) -> LevelUpService:
    return LevelUpService(evolution_service=mock_evolution_service)


async def test_level_up_pokemons_for_user__inputs_user_with_eligible_pokemon__level_up_and_evolve_pokemon(
    levelup_service: LevelUpService, mock_evolution_service: EvolutionService | AsyncMock
):
    # given
    init_level = 16
    charmander = create_pokemon(pokemon_type=PokemonType.Charmander, level=init_level)
    user = create_user(pokemons=[charmander])
    mock_evolution_service.get_evolution_rule_for_pokemon.return_value = evolution_rules[PokemonType.Charmander]

    # when
    await levelup_service.level_up_pokemons_for_user(user, 0, 10, Time.DAY)

    # then: level up and try evolve
    assert charmander.level == init_level + (10 // settings.LEVEL_UP_PER_COMMIT_POINT)
    mock_evolution_service.evolve_pokemon.assert_called()
