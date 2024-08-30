import pytest

from src.models.pokemon_type import PokemonType
from src.models.user import User
from src.pokemons.time import Time
from src.services.pokemon_service import PokemonService
from src.setting import settings
from tests.utils.pokemon import create_pokemon
from tests.utils.user import create_user


@pytest.fixture()
def pokemon_service() -> PokemonService:
    return PokemonService()


@pytest.mark.parametrize(
    "current_commit_point,expected",
    [
        (settings.POKEMON_PER_COMMIT_POINT - 1, 0),
        (settings.POKEMON_PER_COMMIT_POINT, 1),
        (settings.POKEMON_PER_COMMIT_POINT * 3, 3),
    ],
)
def test_give_pokemons_for_user__inputs_commit_point__add_new_pokemons(
    pokemon_service: PokemonService, current_commit_point: int, expected: int
):
    # given
    user = User(username="username")

    # when
    pokemon_service.give_pokemons_for_user(user, 0, current_commit_point)

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
def test_give_pokemons_for_user__inputs_commit_point__update_pokedex_items(
    pokemon_service: PokemonService, current_commit_point: int
):
    # given
    user = User(username="username")

    # when
    pokemon_service.give_pokemons_for_user(user, 0, current_commit_point)

    # then
    assert set(pokemon.type for pokemon in user.pokemons) == set(item.type for item in user.pokedex_items)
    for item in user.pokedex_items:
        assert item.obtain_count == 1


def test_level_up_pokemons_for_user__inputs_user_with_eligible_pokemon__level_up_and_evolve_pokemon(
    pokemon_service: PokemonService,
):
    # given
    init_level = 16
    charmander = create_pokemon(pokemon_type=PokemonType.Charmander, level=init_level)
    user = create_user(pokemons=[charmander])

    # when
    pokemon_service.level_up_pokemons_for_user(user, 0, 10, Time.DAY)

    # then: level up and evolve to Charmeleon
    assert charmander.level == init_level + (10 // settings.LEVEL_UP_PER_COMMIT_POINT)
    assert charmander.type == PokemonType.Charmeleon
