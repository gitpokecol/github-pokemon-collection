import random
from typing import AsyncGenerator, NamedTuple

from src.models.pokemon import Pokemon
from src.renders.images import ImageLoader
from src.schemas.backgrounds import Background
from src.schemas.pokemons import PokemonFace
from src.template import svgs as svgs_templates

pokemon_templates = {PokemonFace.LEFT: svgs_templates.pokemon_left, PokemonFace.RIGHT: svgs_templates.pokemon_right}


class SVGRenderer:

    def __init__(self, image_loader: ImageLoader):
        self._image_loader = image_loader

    async def render_svg(
        self,
        *,
        pokemons: list[Pokemon],
        commit_point: int,
        username: str,
        face: PokemonFace,
        width: int,
        height: int,
        background: Background
    ) -> str:
        return svgs_templates.base.format(
            width=width,
            height=height,
            username=username,
            commit_point=commit_point,
            n_pokemons=len(pokemons),
            pokemons="\n".join([pokemon async for pokemon in self._render_pokemons(pokemons, face, height)]),
            poke_ball_url=await self._image_loader.get_pokeball(),
            background=await self._render_background(background),
        )

    async def _render_pokemons(
        self, pokemons: list[Pokemon], face: PokemonFace, height: int
    ) -> AsyncGenerator[str, None]:

        rendering_pokemons = [
            rendering_pokemon async for rendering_pokemon in self._rendering_pokmemons(pokemons, face, height)
        ]
        rendering_pokemons.sort(key=lambda r: r.offset)

        for idx, rendering_pokemon in enumerate(rendering_pokemons):
            num = idx + 1
            yield pokemon_templates[face].format(
                num=num,
                duration=rendering_pokemon.duration,
                offset=rendering_pokemon.offset,
                delay=rendering_pokemon.delay,
                frame_1=rendering_pokemon.frames[0],
                frame_2=rendering_pokemon.frames[1],
            )

    async def _rendering_pokmemons(
        self, pokemons: list[Pokemon], face: PokemonFace, height: int
    ) -> AsyncGenerator["_RenderingPokemon", None]:
        for pokemon in pokemons:
            duration = random.uniform(10, 15)
            offset = random.randint(0, height - 95)
            delay = random.uniform(0, 10)

            sprite_frame_1 = await self._image_loader.get_pokemon_sprite(pokemon.type, face, pokemon.is_shiny, 1)
            sprite_frame_2 = await self._image_loader.get_pokemon_sprite(pokemon.type, face, pokemon.is_shiny, 1)

            yield _RenderingPokemon(
                duration=duration, offset=offset, delay=delay, frames=(sprite_frame_1, sprite_frame_2)
            )

    async def _render_background(self, background: Background) -> str:
        if background is Background.NONE:
            return ""
        else:
            background_image = await self._image_loader.get_background(background)
            return svgs_templates.background.format(background=background_image)


class _RenderingPokemon(NamedTuple):
    duration: float
    offset: int
    delay: float
    frames: tuple[str, str]
