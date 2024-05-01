import logging
import random
from typing import Generator

from src.exceptions.base import InternalError
from src.models.pokemon import Pokemon
from src.models.pokemon_type import PokemonType
from src.renders.images import ImageLoader
from src.schemas.pokemons import PokemonFace
from src.template import svgs as svgs_templates

pokemon_templates = {PokemonFace.LEFT: svgs_templates.pokemon_left, PokemonFace.RIGHT: svgs_templates.pokemon_right}


class SVGRenderer:
    pokeball: str
    pokemon_left_sprites: dict[PokemonType, tuple[str, str]]

    @classmethod
    async def prepare(cls, *, image_loader: ImageLoader):
        logging.info("Load images start")
        cls.pokeball = await image_loader.get_pokeball()
        cls.pokemon_left_sprites = await image_loader.get_pokemon_left_sprites()
        cls.pokemon_right_sprites = await image_loader.get_pokemon_right_sprites()
        cls.pokemon_shiny_left_sprites = await image_loader.get_pokemon_shiny_left_sprites()
        cls.pokemon_shiny_right_sprites = await image_loader.get_pokemon_shiny_right_sprites()
        logging.info("Load images end")

    def render_svg(self, *, pokemons: list[Pokemon], commit_point: int, username: str, face: PokemonFace) -> str:
        return svgs_templates.base.format(
            username=username,
            commit_point=commit_point,
            n_pokemons=len(pokemons),
            pokemons="\n".join(self._render_pokemons(pokemons, face)),
            poke_ball_url=self.pokeball,
        )

    def _render_pokemons(self, pokemons: list[Pokemon], face: PokemonFace) -> Generator[str, None, None]:
        for idx, pokemon in enumerate(pokemons):
            num = idx + 1
            duration = random.uniform(10, 15)
            offset = random.randint(-75, 80)
            delay = random.uniform(0, 10)

            if face is PokemonFace.LEFT:
                if pokemon.is_shiny:
                    frame_1, frame_2 = self.pokemon_shiny_left_sprites[pokemon.type]
                else:
                    frame_1, frame_2 = self.pokemon_left_sprites[pokemon.type]
            elif face is PokemonFace.RIGHT:
                if pokemon.is_shiny:
                    frame_1, frame_2 = self.pokemon_shiny_right_sprites[pokemon.type]
                else:
                    frame_1, frame_2 = self.pokemon_right_sprites[pokemon.type]
            else:
                raise InternalError

            yield pokemon_templates[face].format(
                num=num, duration=duration, offset=offset, delay=delay, frame_1=frame_1, frame_2=frame_2
            )
