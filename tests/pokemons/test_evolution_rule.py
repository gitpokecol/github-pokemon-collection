import pytest

from src.pokemons.evolution import EvolutionRule, evolution_rules
from src.pokemons.gender import Gender
from src.pokemons.item_type import ItemType
from src.pokemons.pokemon_type import PokemonType
from src.pokemons.time import Time
from tests.utils.pokemon import create_pokemon

rule_required_level = evolution_rules[PokemonType.Bulbasaur]


@pytest.mark.parametrize(
    "required_level,required_item,required_time,required_friendship",
    [
        (10, None, None, 0),
        (0, ItemType.PROTECTOR, None, 0),
        (10, None, Time.DAY, 0),
        (0, None, None, 225),
        (50, ItemType.FIRE_STONE, Time.NIGHT, 225),
    ],
)
def test_can_evolve__inputs_required_level_item_time_friendship__return_true(
    required_level: int,
    required_item: ItemType | None,
    required_time: Time | None,
    required_friendship: int,
):
    # given
    rule = EvolutionRule(
        to=PokemonType.Ivysaur,
        required_level=required_level,
        required_time=required_time,
        required_item=required_item,
        required_friendship=required_friendship,
    )

    level = max(1, required_level)
    time = required_time if required_time else Time.DAY
    friendship = required_friendship
    item = required_item

    pokemon = create_pokemon(pokemon_type=PokemonType.Bulbasaur, level=level, friendship=friendship)

    # when
    result = rule.can_evolve(pokemon, item, time)

    # then
    assert result is True


@pytest.mark.parametrize(
    "level,item,time,friendship",
    [
        (9, ItemType.PROTECTOR, Time.NIGHT, 225),  # not met level
        (10, None, Time.NIGHT, 225),  # not met item
        (10, ItemType.DRACO_PLATE, Time.NIGHT, 225),  # not met item
        (10, ItemType.PROTECTOR, Time.DAY, 225),  # not met time
        (10, ItemType.PROTECTOR, Time.NIGHT, 224),  # not met friendship
    ],
)
def test_can_evolve__inputs_not_met_level_item_time_friendship__return_false(
    level: int, item: None | ItemType, time: Time, friendship: int
):
    # given
    required_level = 10
    required_item = ItemType.PROTECTOR
    required_time = Time.NIGHT
    required_friendship = 225

    rule = EvolutionRule(
        to=PokemonType.Ivysaur,
        required_level=required_level,
        required_time=required_time,
        required_item=required_item,
        required_friendship=required_friendship,
    )

    pokemon = create_pokemon(pokemon_type=PokemonType.Bulbasaur, level=level, friendship=friendship)

    # when
    result = rule.can_evolve(pokemon, item, time)

    # then
    assert result is False


def test_can_evolve__input_not_met_gender___return_false():
    # given
    level = 10

    only_female_rule = EvolutionRule(to=PokemonType.Wormadam, required_level=level)
    only_male_rule = EvolutionRule(to=PokemonType.Mothim, required_level=level)
    female_pokemon = create_pokemon(pokemon_type=PokemonType.Burmy, level=level, gender=Gender.FEMALE)
    male_pokemon = create_pokemon(pokemon_type=PokemonType.Burmy, level=level, gender=Gender.MALE)

    # when
    result1 = only_female_rule.can_evolve(male_pokemon, None, Time.DAY)
    result2 = only_male_rule.can_evolve(female_pokemon, None, Time.DAY)

    # then
    assert (result1, result2) == (False, False)
