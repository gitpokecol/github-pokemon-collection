from datetime import datetime

from fastapi.routing import APIRouter

from src.dependencies.services import (
    CommitPointRewardServiceDep,
    TimeServiceDep,
    UserServiceDep,
)
from src.setting import settings

router = APIRouter()

@router.post("/internal/update-cp")
async def internal_update_commit_point_and_reward(
    *,
    commit_point_reward_service: CommitPointRewardServiceDep,
    time_service: TimeServiceDep,
    user_service: UserServiceDep,
):
    users = await user_service.get_users_within_last_seen_time(
        start_time=datetime.utcnow() - settings.COMMIT_POINT_UPDATE_PERIOD,
        end_time=datetime.utcnow(),
    )

    time = await time_service.get_time_for_client(None)
    for user in users:
        await commit_point_reward_service.update_commit_point_and_reward(user, time)