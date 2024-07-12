import asyncio
import base64
from typing import Coroutine, Literal

import aiofiles
from httpx import AsyncClient

from src.models.pokemon_type import PokemonType
from src.schemas.backgrounds import Background
from src.schemas.pokemons import PokemonFace

POKEBALL_IMAGE_PATH = "imgs/ui/pokeball.png"


class ImageLoader:
    def __init__(self) -> None:
        self._client = AsyncClient(http2=True)
        self._cache_get_pokemon_sprite = {}
        self._cache_get_pokeball = None
        self._cache_background = {}

    async def prepare(self):
        coros: list[Coroutine] = []

        for pokemon_type in PokemonType:
            for face in PokemonFace:
                for is_shiny in [False, True]:
                    coros.append(self.get_pokemon_sprite(pokemon_type, face, is_shiny, 1))
                    coros.append(self.get_pokemon_sprite(pokemon_type, face, is_shiny, 2))

        coros.append(self.get_pokeball())
        await asyncio.gather(*coros)

    async def get_pokemon_sprite(
        self, pokemon_type: PokemonType, face: PokemonFace, is_shiny: bool, frame: Literal[1] | Literal[2]
    ):
        cache_key = (pokemon_type, face, is_shiny, frame)
        if cache_key not in self._cache_get_pokemon_sprite:
            self._cache_get_pokemon_sprite[cache_key] = await self._load_as_base64(
                self._get_pokemon_sprite_path(pokemon_type, face, is_shiny, frame)
            )

        return self._cache_get_pokemon_sprite[cache_key]

    async def get_pokeball(self) -> str:
        if self._cache_get_pokeball is None:
            self._cache_get_pokeball = await self._load_as_base64(POKEBALL_IMAGE_PATH)

        return self._cache_get_pokeball

    async def get_background(self, background: Background) -> str:
        if background not in self._cache_background:
            self._cache_background[background] = await self._load_as_base64(self._get_background_path(background))

        return self._cache_background[background]

    async def _load_as_base64(self, path: str) -> str:
        async with aiofiles.open(path, "rb") as f:
            content = await f.read()
            return "data:image/png;base64," + base64.b64encode(content).decode("utf-8")

    def _get_pokemon_sprite_path(
        self,
        pokemon_type: PokemonType,
        face: PokemonFace,
        is_shiny: bool,
        frame: Literal[1] | Literal[2],
    ) -> str:
        if is_shiny:
            return f"imgs/pokemons/{pokemon_type.national_no}_{face.value}_{frame}.png"
        else:
            return f"imgs/pokemons/{pokemon_type.national_no}_{face.value}_shiny_{frame}.png"

    def _get_background_path(self, background: Background):
        return f"imgs/backgrounds/{background.value}.png"
