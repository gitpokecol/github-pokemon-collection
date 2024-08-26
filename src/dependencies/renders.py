from typing import Annotated

from fastapi import Depends

from src.renders.backgrounds import BackgroundImages
from src.renders.item_sprites import ItemSprites
from src.renders.pokemon_sprites import PokemonSprites
from src.renders.profile_renderer import ProfileRenderer

pokemon_sprites = PokemonSprites()
background_images = BackgroundImages()
item_sprites = ItemSprites()


async def get_profile_renderer() -> ProfileRenderer:
    return ProfileRenderer(pokemon_sprites, item_sprites, background_images)


ProfileRendererDep = Annotated[ProfileRenderer, Depends(get_profile_renderer)]
