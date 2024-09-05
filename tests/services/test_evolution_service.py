import pytest

from src.pokemons.evolution import EvolutionRule
from src.pokemons.form import BurmyWormadamForm
from src.pokemons.pokemon_type import PokemonType
from src.services.evolution_service import EvolutionService
from tests.utils.pokemon import create_pokemon
from tests.utils.user import create_user


@pytest.fixture
def evolution_service() -> EvolutionService:
    return EvolutionService()


def test_evolve_pokemon__remove_form_after_evolution(evolution_service: EvolutionService):
    # given
    burmy = create_pokemon(pokemon_type=PokemonType.Burmy, form=BurmyWormadamForm.SANDY, level=1)
    rule = EvolutionRule(to=PokemonType.Mothim, required_level=1)
    user = create_user(pokemons=[burmy])

    # when
    evolution_service.evolve_pokemon(burmy, user, rule)

    # then
    assert burmy.type == PokemonType.Mothim
    assert burmy.form is None


def test_evolve_pokemon__update_pokedex(evolution_service: EvolutionService):
    # given
    charmander = create_pokemon(pokemon_type=PokemonType.Charmander, level=1)
    user = create_user(pokemons=[charmander])
    rule = EvolutionRule(to=PokemonType.Charmeleon, required_level=1)

    # when
    evolution_service.evolve_pokemon(charmander, user, rule)

    # then
    pokedex = {pokedex_item.type: pokedex_item for pokedex_item in user.pokedex_items}
    assert PokemonType.Charmeleon in pokedex
    assert pokedex[PokemonType.Charmeleon].obtain_count == 1