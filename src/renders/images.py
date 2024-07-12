import base64
from functools import lru_cache
from typing import Literal

import aiofiles
from httpx import AsyncClient

from src.models.pokemon_type import PokemonType

POKEBALL_IMAGE_PATH = "imgs/ui/pokeball.png"


class ImageLoader:
    def __init__(self) -> None:
        self._client = AsyncClient(http2=True)

    @lru_cache
    async def get_pokemon_left_sprites(self) -> dict[PokemonType, tuple[str, str]]:
        return {
            pokemon_type: (
                await self._load_as_base64(self._get_pokemon_sprite_path(pokemon_type, "left", False, 1)),
                await self._load_as_base64(self._get_pokemon_sprite_path(pokemon_type, "left", False, 2)),
            )
            for pokemon_type in PokemonType
        }

    @lru_cache
    async def get_pokemon_right_sprites(self) -> dict[PokemonType, tuple[str, str]]:
        return {
            pokemon_type: (
                await self._load_as_base64(self._get_pokemon_sprite_path(pokemon_type, "right", False, 1)),
                await self._load_as_base64(self._get_pokemon_sprite_path(pokemon_type, "right", False, 2)),
            )
            for pokemon_type in PokemonType
        }

    @lru_cache
    async def get_pokemon_shiny_left_sprites(self) -> dict[PokemonType, tuple[str, str]]:
        return {
            pokemon_type: (
                await self._load_as_base64(self._get_pokemon_sprite_path(pokemon_type, "left", True, 1)),
                await self._load_as_base64(self._get_pokemon_sprite_path(pokemon_type, "left", True, 2)),
            )
            for pokemon_type in PokemonType
        }

    @lru_cache
    async def get_pokemon_shiny_right_sprites(self) -> dict[PokemonType, tuple[str, str]]:
        return {
            pokemon_type: (
                await self._load_as_base64(self._get_pokemon_sprite_path(pokemon_type, "right", True, 1)),
                await self._load_as_base64(self._get_pokemon_sprite_path(pokemon_type, "right", True, 2)),
            )
            for pokemon_type in PokemonType
        }

    @lru_cache
    async def get_pokeball(self) -> str:
        return await self._load_as_base64(POKEBALL_IMAGE_PATH)

    async def _load_as_base64(self, path: str) -> str:
        async with aiofiles.open(path, "rb") as f:
            content = await f.read()
            return "data:image/png;base64," + base64.b64encode(content).decode("utf-8")

    def _get_pokemon_sprite_path(
        self,
        pokemon_type: PokemonType,
        face: Literal["right"] | Literal["left"],
        is_shiny: bool,
        frame: Literal[1] | Literal[2],
    ) -> str:
        if is_shiny:
            return f"imgs/pokemons/{pokemon_type.national_no}_{face}_{frame}.png"
        else:
            return f"imgs/pokemons/{pokemon_type.national_no}_{face}_shiny_{frame}.png"
