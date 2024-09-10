from unittest.mock import AsyncMock

import pytest

from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService


@pytest.fixture()
def user_service(mock_user_repository: UserRepository | AsyncMock) -> UserService:
    return UserService(user_repository=mock_user_repository)


async def test_get_or_create_user__inputs_upper_lower_mixed_username__returns_lowercase_username_user(
    user_service: UserService, mock_user_repository: UserRepository | AsyncMock
):
    # given
    username = "User NaMe"
    mock_user_repository.find_by_username.return_value = None

    # when
    created = await user_service.get_or_create_user(username=username)
    # then
    assert created.username == "user name"
