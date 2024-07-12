from typing import Annotated

from fastapi import Depends

from src.renders.images import ImageLoader
from src.renders.svg import SVGRenderer

image_loader = ImageLoader()


async def get_svg_renderer() -> SVGRenderer:
    return SVGRenderer(image_loader)


SVGRendererDep = Annotated[SVGRenderer, Depends(get_svg_renderer)]
