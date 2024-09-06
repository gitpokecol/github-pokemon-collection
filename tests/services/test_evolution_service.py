from unittest.mock import AsyncMock

import pytest

from src.pokemons.evolution import EvolutionRule
from src.pokemons.form import BurmyWormadamForm
from src.pokemons.pokemon_type import PokemonType
from src.repositories.pokemon_repository import PokemonRepository
from src.services.evolution_service import EvolutionService
from src.services.pokedex_service import PokedexService
from tests.utils.pokemon import create_pokemon
from tests.utils.user import create_user


@pytest.fixture
def evolution_service(
    mock_pokedex_service: PokedexService | AsyncMock, mock_pokemon_repository: PokemonRepository | AsyncMock
) -> EvolutionService:
    return EvolutionService(pokedex_service=mock_pokedex_service, pokemon_repository=mock_pokemon_repository)


async def test_evolve_pokemon__remove_form_after_evolution(evolution_service: EvolutionService):
    # given
    burmy = create_pokemon(pokemon_type=PokemonType.Burmy, form=BurmyWormadamForm.SANDY, level=1)
    rule = EvolutionRule(to=PokemonType.Mothim, required_level=1)
    user = create_user(pokemons=[burmy])

    # when
    await evolution_service.evolve_pokemon(burmy, user, rule)

    # then
    assert burmy.type == PokemonType.Mothim
    assert burmy.form is None
