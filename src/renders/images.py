import base64

from httpx import AsyncClient
from pydantic import BaseModel

from src.models.pokemon_type import PokemonType
from src.utils import file_cache

SPRITE_BASE_URL = "https://www.pokencyclopedia.info/sprites/overworlds"
POKEBALL_URL = "https://www.pokencyclopedia.info/sprites/items/items_old/i_old_poke-ball.png"

pokemon_left_sprites: dict[PokemonType, tuple[str, str]] = {}
pokeball: str = ""


class ImageLoader:
    def __init__(self) -> None:
        self._client = AsyncClient(http2=True)

    @file_cache("pokemon_left_sprites")
    async def get_pokemon_left_sprites(self) -> dict[PokemonType, tuple[str, str]]:
        return {pokemon: await self._create_left_sprite_urls(pokemon) for pokemon in PokemonType}

    @file_cache("pokemon_right_sprites")
    async def get_pokemon_right_sprites(self) -> dict[PokemonType, tuple[str, str]]:
        return {pokemon: await self._create_right_sprite_urls(pokemon) for pokemon in PokemonType}

    @file_cache("pokemon_shiny_left_sprites")
    async def get_pokemon_shiny_left_sprites(self) -> dict[PokemonType, tuple[str, str]]:
        return {pokemon: await self._create_shiny_left_sprite_urls(pokemon) for pokemon in PokemonType}

    @file_cache("pokemon_shiny_right_sprites")
    async def get_pokemon_shiny_right_sprites(self) -> dict[PokemonType, tuple[str, str]]:
        return {pokemon: await self._create_shiny_right_sprite_urls(pokemon) for pokemon in PokemonType}

    @file_cache("pokeball")
    async def get_pokeball(self) -> str:
        return await self._get_as_base64(POKEBALL_URL)

    async def _get_as_base64(self, url: str) -> str:
        res = await self._client.get(url)
        res.raise_for_status()
        return "data:" + res.headers["Content-Type"] + ";" + "base64," + base64.b64encode(res.content).decode("utf-8")

    async def _create_left_sprite_urls(self, type: PokemonType) -> tuple[str, str]:
        frame_1, frame_2 = SpriteUrl(SPRITE_BASE_URL).left().type(type).frames()
        return (await self._get_as_base64(frame_1), await self._get_as_base64(frame_2))

    async def _create_right_sprite_urls(self, type: PokemonType) -> tuple[str, str]:
        frame_1, frame_2 = SpriteUrl(SPRITE_BASE_URL).right().type(type).frames()
        return (await self._get_as_base64(frame_1), await self._get_as_base64(frame_2))

    async def _create_shiny_left_sprite_urls(self, type: PokemonType) -> tuple[str, str]:
        frame_1, frame_2 = SpriteUrl(SPRITE_BASE_URL).left_shiny().type(type).frames()
        return (await self._get_as_base64(frame_1), await self._get_as_base64(frame_2))

    async def _create_shiny_right_sprite_urls(self, type: PokemonType) -> tuple[str, str]:
        frame_1, frame_2 = SpriteUrl(SPRITE_BASE_URL).right_shiny().type(type).frames()
        return (await self._get_as_base64(frame_1), await self._get_as_base64(frame_2))


class SpriteUrl(BaseModel):
    def __init__(self, base: str) -> None:
        """Will set `{base}/{face}/{type}{frame}.png`"""

        self._base = base
        self._face = None
        self._type = None

    def right(self):
        self._face = "o-r_hgss/o-r_hs_"
        return self

    def left(self):
        self._face = "/o-l_hgss/o-l_hs_"
        return self

    def right_shiny(self):
        self._face = "/o-r_hgss_shiny/o-r_hs-S_"
        return self

    def left_shiny(self):
        self._face = "/o-l_hgss_shiny/o-l_hs-S_"
        return self

    def type(self, poke_type: PokemonType):
        self._type = str(poke_type.national_no).zfill(3)
        if poke_type.national_no in [3, 25]:
            self._type += "_m-"
        else:
            self._type += "_"

        return self

    def frames(self) -> tuple[str, str]:
        return self._url("1"), self._url("2")

    def _url(self, frame: str) -> str:
        return f"{self._base}/{self._face}/{self._type}.png"
