from unittest.mock import Mock

import pytest

from src.services.user_service import UserService


@pytest.fixture()
def user_service() -> UserService:
    return UserService()


async def test_create_new_user__inputs_upper_lower_mixed_username__returns_lowercase_username_user(
    user_service: UserService, mock_session: Mock
):
    # given
    username = "User NaMe"
    commit_points = dict()

    # when
    created = user_service.create_new_user(session=mock_session, username=username, commit_points=commit_points)

    # then
    assert created.username == "user name"
