from src.models.pokemon import Pokemon
from src.models.user import User
from src.pokemons.form import Form
from src.pokemons.gender import Gender
from src.pokemons.pokemon_type import PokemonType
from tests.utils.user import create_user


def create_pokemon(
    *,
    owner: None | User = None,
    pokemon_type: PokemonType = PokemonType.Bulbasaur,
    is_shiny: bool = False,
    gender: Gender = Gender.FEMALE,
    form: None | Form = None,
    level: int = 0,
    friendship: int = 0
) -> Pokemon:
    if owner is None:
        owner = create_user()

    return Pokemon(
        type=pokemon_type, is_shiny=is_shiny, level=level, friendship=friendship, gender=gender, form=form, owner=owner
    )
