from unittest.mock import Mock

import pytest

from src.services.user import UserService
from tests.utils.common import mock_coroutine


@pytest.fixture()
def user_service() -> UserService:
    return UserService()


@pytest.fixture()
def session():
    session = Mock()
    session.commit = mock_coroutine
    session.close = mock_coroutine
    return session


async def test_create_new_user__inputs_upper_lower_mixed_username__returns_lowercase_username_user(
    user_service: UserService, session
):
    # given
    username = "User NaMe"
    commit_points = dict()

    # when
    created = await user_service.create_new_user(session=session, username=username, commit_points=commit_points)

    # then
    assert created.username == "user name"
