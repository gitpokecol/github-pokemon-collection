import pytest

from src.models.pokemon_type import PokemonType
from src.pokemons.evolution import EvolutionRule, evolution_rules
from src.pokemons.gender import Gender
from src.pokemons.item import Item
from src.pokemons.time import Time
from tests.utils.pokemon import create_pokemon
from tests.utils.user import create_user

rule_required_level = evolution_rules[PokemonType.Bulbasaur]


@pytest.mark.parametrize(
    "required_level,required_item,required_time,required_friendship",
    [
        (10, None, None, 0),
        (0, Item.PROTECTOR, None, 0),
        (10, None, Time.DAY, 0),
        (0, None, None, 225),
        (50, Item.FIRE_STONE, Time.NIGHT, 225),
    ],
)
def test_can_evolve__inputs_required_level_item_time_friendship__return_true(
    required_level: int,
    required_item: Item | None,
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
    owner = create_user()

    # when
    result = rule.can_evolve(pokemon, owner, item, time)

    # then
    assert result is True


@pytest.mark.parametrize(
    "level,item,time,friendship",
    [
        (9, Item.PROTECTOR, Time.NIGHT, 225),  # not met level
        (10, None, Time.NIGHT, 225),  # not met item
        (10, Item.DRACO_PLATE, Time.NIGHT, 225),  # not met item
        (10, Item.PROTECTOR, Time.DAY, 225),  # not met time
        (10, Item.PROTECTOR, Time.NIGHT, 224),  # not met friendship
    ],
)
def test_can_evolve__inputs_not_met_level_item_time_friendship__return_false(
    level: int, item: None | Item, time: Time, friendship: int
):
    # given
    required_level = 10
    required_item = Item.PROTECTOR
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
    owner = create_user()

    # when
    result = rule.can_evolve(pokemon, owner, item, time)

    # then
    assert result is False


def test_can_evolve__input_not_met_gender___return_false():
    # given
    level = 10

    only_female_rule = EvolutionRule(to=PokemonType.Wormadam, required_level=level)
    only_male_rule = EvolutionRule(to=PokemonType.Mothim, required_level=level)
    female_pokemon = create_pokemon(pokemon_type=PokemonType.Burmy, level=level, gender=Gender.FEMALE)
    male_pokemon = create_pokemon(pokemon_type=PokemonType.Burmy, level=level, gender=Gender.MALE)
    owner = create_user()

    # when
    result1 = only_female_rule.can_evolve(male_pokemon, owner, None, Time.DAY)
    result2 = only_male_rule.can_evolve(female_pokemon, owner, None, Time.DAY)

    # then
    assert (result1, result2) == (False, False)


def test_can_evolve__input_mantyke_but_owner_not_have_required_pokemon___return_false():
    # given
    level = 10

    rule = EvolutionRule(to=PokemonType.Mantine, required_level=level)
    mantyke_pokemon = create_pokemon(pokemon_type=PokemonType.Mantyke, level=level)
    owner = create_user()

    # when
    result = rule.can_evolve(mantyke_pokemon, owner, None, Time.DAY)

    # then
    assert result is False


def test_can_evolve__input_mantyke_and_owner_have_required_pokemon___return_true():
    # given
    level = 10

    rule = EvolutionRule(to=PokemonType.Mantine, required_level=level)
    mantyke_pokemon = create_pokemon(pokemon_type=PokemonType.Mantyke, level=level)
    remoraid_pokemon = create_pokemon(pokemon_type=PokemonType.Remoraid, level=level)
    octillery_pokemon = create_pokemon(pokemon_type=PokemonType.Octillery, level=level)
    remoraid_owner = create_user(pokemons=[remoraid_pokemon])
    octillery_owner = create_user(pokemons=[octillery_pokemon])

    # when
    result1 = rule.can_evolve(mantyke_pokemon, remoraid_owner, None, Time.DAY)
    result2 = rule.can_evolve(mantyke_pokemon, octillery_owner, None, Time.DAY)

    # then
    assert all([result1, result2]) is True
