import base64

from httpx import AsyncClient

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
        return {pokemon: await self._create_left_sprite_urls(pokemon.national_no) for pokemon in PokemonType}

    @file_cache("pokeball")
    async def get_pokeball(self) -> str:
        return await self._get_as_base64(POKEBALL_URL)

    async def _get_as_base64(self, url: str) -> str:
        res = await self._client.get(url)
        res.raise_for_status()
        return "data:" + res.headers["Content-Type"] + ";" + "base64," + base64.b64encode(res.content).decode("utf-8")

    async def _create_left_sprite_urls(self, national_no: int) -> tuple[str, str]:
        start_url = f"{SPRITE_BASE_URL}/o-l_hgss"
        poke_url = start_url + "/o-l_hs_" + str(national_no).zfill(3)

        if national_no in [3, 25]:
            frame_1 = poke_url + "_m-1.png"
            frame_2 = poke_url + "_m-2.png"
        else:
            frame_1 = poke_url + "_1.png"
            frame_2 = poke_url + "_2.png"

        return (await self._get_as_base64(frame_1), await self._get_as_base64(frame_2))
