import logging
import random
from typing import Generator

from src.models.pokemon_type import PokemonType
from src.renders.images import ImageLoader
from src.template import svgs as svgs_templates


class SVGRenderer:
    pokeball: str
    pokemon_left_sprites: dict[PokemonType, tuple[str, str]]

    @classmethod
    async def prepare(cls, *, image_loader: ImageLoader):
        logging.info("Load images start")
        cls.pokeball = await image_loader.get_pokeball()
        cls.pokemon_left_sprites = await image_loader.get_pokemon_left_sprites()
        logging.info("Load images end")

    def render_svg(self, *, pokemons: list[PokemonType], commit_point: int, username: str) -> str:
        return svgs_templates.base.format(
            username=username,
            commit_point=commit_point,
            n_pokemons=len(pokemons),
            pokemons="\n".join(self._render_pokemons(pokemons)),
            poke_ball_url=self.pokeball,
        )

    def _render_pokemons(self, pokemons: list[PokemonType]) -> Generator[str, None, None]:
        for idx, pokemon in enumerate(pokemons):
            num = idx + 1
            duration = random.uniform(10, 15)
            offset = random.randint(-75, 80)
            delay = random.uniform(0, 10)

            frame_1, frame_2 = self.pokemon_left_sprites[pokemon]

            yield svgs_templates.pokemon.format(
                num=num, duration=duration, offset=offset, delay=delay, frame_1=frame_1, frame_2=frame_2
            )
