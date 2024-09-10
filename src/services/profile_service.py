from src.models.user import User
from src.pokemons.time import Time
from src.renders.profile_renderer import ProfileRenderer
from src.schemas.backgrounds import Background
from src.schemas.pokemons import Facing
from src.services.commit_point_reward_service import CommitPointRewardService


class ProfileService:
    def __init__(
        self,
        *,
        commit_point_reward_service: CommitPointRewardService,
        renderer: ProfileRenderer,
    ) -> None:
        self._commit_point_reward_service = commit_point_reward_service
        self._renderer = renderer

    async def render_profile(
        self,
        *,
        user: User,
        facing: Facing,
        width: int,
        height: int,
        background: Background,
        time: Time,
    ) -> str:
        if self._commit_point_reward_service.can_update_commit_point(user):
            await self._commit_point_reward_service.update_commit_point_and_reward(user, time)
        return await self._renderer.render(
            pokemons=user.pokemons,
            commit_point=user.total_commit_point,
            username=user.username,
            facing=facing,
            width=width,
            height=height,
            background=background,
        )
