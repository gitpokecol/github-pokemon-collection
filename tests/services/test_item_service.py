from unittest.mock import AsyncMock

import pytest

from src.models.daily_item import DailyItem
from src.models.daily_item_abtain import DailyItemAbtain
from src.repositories.daily_item_abtain_repository import DailyItemAbtainRepository
from src.repositories.daily_item_repository import DailyItemRepository
from src.services.item_service import ItemService
from tests.utils.item import create_daily_item
from tests.utils.user import create_user


@pytest.fixture()
def mock_daily_item_repository() -> DailyItemRepository | AsyncMock:
    return AsyncMock(spec=DailyItemRepository)


@pytest.fixture()
def mock_daily_item_abtain_repository() -> DailyItemAbtainRepository | AsyncMock:
    return AsyncMock(spec=DailyItemAbtainRepository)


@pytest.fixture
def item_service(mock_daily_item_repository: AsyncMock, mock_daily_item_abtain_repository: AsyncMock) -> ItemService:
    return ItemService(
        daily_item_repository=mock_daily_item_repository,
        daily_item_abtain_repository=mock_daily_item_abtain_repository,
    )


async def test_get_daily_item__existed__return_DailyItemResponse(
    item_service: ItemService, mock_daily_item_repository: DailyItemRepository | AsyncMock
):
    # given
    daily_item = create_daily_item()
    mock_daily_item_repository.find_daily_item_for_today.return_value = daily_item

    # when
    result = await item_service.get_daily_item()

    # then
    assert result.type == daily_item.type


async def test_get_daily_item__non_existed__create_DailyItem(
    item_service: ItemService, mock_daily_item_repository: DailyItemRepository | AsyncMock
):
    # given
    mock_daily_item_repository.find_daily_item_for_today.return_value = None

    # when
    result = await item_service.get_daily_item()

    # then
    args, _ = mock_daily_item_repository.save.call_args
    created: DailyItem = args[0]
    assert created.type == result.type


async def test_give_daily_item_to_user__non_existed_DailyItem__create_DailyItem(
    item_service: ItemService,
    mock_daily_item_repository: DailyItemRepository | AsyncMock,
):
    # given
    user = create_user()
    mock_daily_item_repository.find_daily_item_for_today.return_value = None

    # when
    await item_service.give_daily_item_to_user(user)

    # then
    mock_daily_item_repository.save.assert_called_once()


async def test_give_daily_item_to_user__existed_DailyItem__create_DailyItemAbtain(
    item_service: ItemService,
    mock_daily_item_repository: DailyItemRepository | AsyncMock,
    mock_daily_item_abtain_repository: DailyItemAbtainRepository | AsyncMock,
):
    # given
    user = create_user()
    daily_item = create_daily_item()
    mock_daily_item_repository.find_daily_item_for_today.return_value = daily_item

    # when
    await item_service.give_daily_item_to_user(user)

    # then
    args, _ = mock_daily_item_abtain_repository.save.call_args
    created: DailyItemAbtain = args[0]
    assert created.daily_item == daily_item
    assert created.user == user


# async def test_give_daily_item_to_user__existed_DailyItemAbtain__raise_BadRequestError(
#     item_service: ItemService,
#     mock_daily_item_repository: DailyItemRepository | AsyncMock,
#     mock_daily_item_abtain_repository: DailyItemAbtainRepository | AsyncMock,
# ):
#     # given
#     user = create_user()
#     daily_item = create_daily_item()
#     mock_daily_item_repository.find_daily_item_for_today.return_value = daily_item

#     # when
#     await item_service.give_daily_item_to_user(user)

#     # then
