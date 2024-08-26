import random
from typing import AsyncGenerator, NamedTuple

from src.models.pokemon import Pokemon
from src.renders.backgrounds import BackgroundImages
from src.renders.item_sprites import ItemSprites
from src.renders.pokemon_sprites import PokemonSprites
from src.schemas.backgrounds import Background
from src.schemas.pokemons import Facing
from src.template import svgs as svgs_templates

pokemon_templates = {
    Facing.LEFT: svgs_templates.pokemon_left,
    Facing.RIGHT: svgs_templates.pokemon_right,
}


class ProfileRenderer:

    def __init__(
        self, pokemon_sprites: PokemonSprites, item_sprites: ItemSprites, background_images: BackgroundImages
    ):
        self._pokemon_sprites = pokemon_sprites
        self._item_sprites = item_sprites
        self._background_images = background_images

    async def render(
        self,
        *,
        pokemons: list[Pokemon],
        commit_point: int,
        username: str,
        facing: Facing,
        width: int,
        height: int,
        background: Background
    ) -> str:
        if background is Background.ABYSS:
            text_color = "white"
        else:
            text_color = "black"

        return svgs_templates.base.format(
            width=width,
            height=height,
            username=username,
            commit_point=commit_point,
            n_pokemons=len(pokemons),
            pokemons="\n".join([pokemon async for pokemon in self._render_pokemons(pokemons, facing, height)]),
            poke_ball_url=await self._item_sprites.get_pokeball_sprite(),
            background=await self._render_background(background),
            text_color=text_color,
        )

    async def _render_pokemons(
        self, pokemons: list[Pokemon], facing: Facing, height: int
    ) -> AsyncGenerator[str, None]:

        rendering_pokemons = [
            rendering_pokemon async for rendering_pokemon in self._rendering_pokmemons(pokemons, facing, height)
        ]
        rendering_pokemons.sort(key=lambda r: r.offset)

        for idx, rendering_pokemon in enumerate(rendering_pokemons):
            num = idx + 1
            yield pokemon_templates[facing].format(
                num=num,
                duration=rendering_pokemon.duration,
                offset=rendering_pokemon.offset,
                delay=rendering_pokemon.delay,
                frame_1=rendering_pokemon.frames[0],
                frame_2=rendering_pokemon.frames[1],
            )

    async def _rendering_pokmemons(
        self, pokemons: list[Pokemon], facing: Facing, height: int
    ) -> AsyncGenerator["_RenderingPokemon", None]:
        for pokemon in pokemons:
            duration = random.uniform(10, 15)
            offset = random.randint(0, height - 95)
            delay = random.uniform(0, 10)

            sprite_frame_1 = await self._pokemon_sprites.get_sprite(
                pokemon.type, facing, pokemon.is_shiny, pokemon.gender, 1, pokemon.form
            )
            sprite_frame_2 = await self._pokemon_sprites.get_sprite(
                pokemon.type, facing, pokemon.is_shiny, pokemon.gender, 2, pokemon.form
            )

            yield _RenderingPokemon(
                duration=duration, offset=offset, delay=delay, frames=(sprite_frame_1, sprite_frame_2)
            )

    async def _render_background(self, background: Background) -> str:
        if background is Background.NONE:
            return svgs_templates.background_none
        else:
            background_image = await self._background_images.get_image(background)
            return svgs_templates.background.format(background=background_image)


class _RenderingPokemon(NamedTuple):
    duration: float
    offset: int
    delay: float
    frames: tuple[str, str]
