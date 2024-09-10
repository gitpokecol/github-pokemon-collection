from src.models.user import User
from src.renders.profile_renderer import ProfileRenderer
from src.schemas.backgrounds import Background
from src.schemas.pokemons import Facing
from src.services.pokemon_service import PokemonService


class ProfileService:
    def __init__(
        self,
        *,
        renderer: ProfileRenderer,
        pokemon_service: PokemonService,
    ) -> None:
        self._renderer = renderer
        self._pokemon_service = pokemon_service

    async def render_profile(
        self,
        *,
        user: User,
        facing: Facing,
        width: int,
        height: int,
        background: Background,
    ) -> str:
        pokemons = await self._pokemon_service.get_pokemons(user)

        return await self._renderer.render(
            pokemons=pokemons,
            commit_point=user.total_commit_point,
            username=user.username,
            facing=facing,
            width=width,
            height=height,
            background=background,
        )
