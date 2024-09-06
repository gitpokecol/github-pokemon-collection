from unittest.mock import AsyncMock

import pytest

from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService


@pytest.fixture()
def user_service(mock_user_repository: UserRepository | AsyncMock) -> UserService:
    return UserService(user_repository=mock_user_repository)


async def test_create_new_user__inputs_upper_lower_mixed_username__returns_lowercase_username_user(
    user_service: UserService,
):
    # given
    username = "User NaMe"
    commit_points = dict()

    # when
    created = await user_service.create_new_user(username=username, commit_points=commit_points)

    # then
    assert created.username == "user name"
