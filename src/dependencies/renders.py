from typing import Annotated

from fastapi import Depends

from src.renders.svg import SVGRenderer


async def get_svg_renderer() -> SVGRenderer:
    return SVGRenderer()


SVGRendererDep = Annotated[SVGRenderer, Depends(get_svg_renderer)]
