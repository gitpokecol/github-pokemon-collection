import asyncio
from typing import Coroutine, Literal

from src.pokemons.form import Form
from src.pokemons.gender import Gender
from src.pokemons.pokemon_type import PokemonType
from src.renders.utils import load_as_base64
from src.schemas.pokemons import Facing

GENDER_DIFFERENCE_POKEMON_NUMS = [3, 25, 154, 202, 208, 214, 415, 443, 444, 445, 449, 450]


class PokemonSprites:
    def __init__(self) -> None:
        self._cache_pokemon_sprite = {}

    async def prepare(self):
        coros: list[Coroutine] = []

        for pokemon_type in list(PokemonType):
            for facing in Facing:
                for is_shiny in (False, True):
                    for gender in pokemon_type.available_genders:
                        for frame in (1, 2):
                            if not pokemon_type.available_forms:
                                coros.append(
                                    self.get_sprite(pokemon_type.national_no, facing, is_shiny, gender, frame, None)
                                )
                            else:
                                for form in pokemon_type.available_forms:
                                    coros.append(
                                        self.get_sprite(
                                            pokemon_type.national_no, facing, is_shiny, gender, frame, form
                                        )
                                    )

        await asyncio.gather(*coros)

    async def get_sprite(
        self,
        national_no: int,
        facing: Facing,
        is_shiny: bool,
        gender: Gender,
        frame: Literal[1, 2],
        form: None | Form,
    ):
        if national_no not in GENDER_DIFFERENCE_POKEMON_NUMS:
            cache_key = (national_no, facing, is_shiny, None, frame, form)
        else:
            cache_key = (national_no, facing, is_shiny, gender, frame, form)

        if cache_key not in self._cache_pokemon_sprite:
            self._cache_pokemon_sprite[cache_key] = await load_as_base64(self._get_sprite_path(*cache_key))

        return self._cache_pokemon_sprite[cache_key]

    def _get_sprite_path(
        self,
        national_no: int,
        facing: Facing,
        is_shiny: bool,
        gender: None | Gender,
        frame: Literal[1, 2],
        form: None | Form,
    ) -> str:
        # imgs/pokemons/{id}_{facing}_shiny_{gender}_{form}_{frame}.png
        path = f"imgs/sprites/pokemon/{national_no}_{facing}_"

        if is_shiny:
            path += "shiny_"
        if gender and gender != Gender.GENDERLESS:
            path += f"{gender}_"
        if form and form != "":
            path += f"{form}_"

        return f"{path}{frame}.png"
