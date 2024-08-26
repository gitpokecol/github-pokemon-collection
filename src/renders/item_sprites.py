from src.renders.utils import load_as_base64

POKEBALL_IMAGE_PATH = "imgs/ui/pokeball.png"


class ItemSprites:
    def __init__(self) -> None:
        self._cache_sprites = {}

    async def prepare(self):
        self._cache_sprites["pokeball"] = await self.get_pokeball_sprite()

    async def get_pokeball_sprite(self):
        if "pokeball" not in self._cache_sprites:
            self._cache_sprites["pokeball"] = await load_as_base64(POKEBALL_IMAGE_PATH)

        return self._cache_sprites["pokeball"]
