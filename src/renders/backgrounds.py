from src.renders.utils import load_as_base64
from src.schemas.backgrounds import Background


class BackgroundImages:
    def __init__(self) -> None:
        self._cache_background = {}

    async def prepare(self):
        for background in Background:
            if background is Background.NONE:
                continue

            self._cache_background[background] = await self.get_image(background)

    async def get_image(self, background: Background) -> str:
        if background not in self._cache_background:
            self._cache_background[background] = await load_as_base64(self._get_background_path(background))

        return self._cache_background[background]

    def _get_background_path(self, background: Background) -> str:
        return f"imgs/backgrounds/{background.value}.png"
