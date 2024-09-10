from src.models.user import User
from src.renders.profile_renderer import ProfileRenderer
from src.schemas.backgrounds import Background
from src.schemas.pokemons import Facing


class ProfileService:
    def __init__(
        self,
        *,
        renderer: ProfileRenderer,
    ) -> None:
        self._renderer = renderer

    async def render_profile(
        self,
        *,
        user: User,
        facing: Facing,
        width: int,
        height: int,
        background: Background,
    ) -> str:
        return await self._renderer.render(
            pokemons=user.pokemons,
            commit_point=user.total_commit_point,
            username=user.username,
            facing=facing,
            width=width,
            height=height,
            background=background,
        )
