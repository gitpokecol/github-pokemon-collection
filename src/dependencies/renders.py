from typing import Annotated

from fastapi import Depends

from ..renders.svg import SVGRenderer


async def get_svg_renderer() -> SVGRenderer:
    return SVGRenderer()


SVG_RENDERER_DEP = Annotated[SVGRenderer, Depends(get_svg_renderer)]
