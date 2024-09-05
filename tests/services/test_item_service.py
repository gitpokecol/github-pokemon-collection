from unittest.mock import AsyncMock

import pytest

from src.exceptions.common import BadRequestError
from src.models.daily_item import DailyItem
from src.models.daily_item_abtain import DailyItemAbtain
from src.pokemons.item_type import ItemType
from src.repositories.daily_item_abtain_repository import DailyItemAbtainRepository
from src.repositories.daily_item_repository import DailyItemRepository
from src.services.evolution_service import EvolutionService
from src.services.item_service import SUBSTITUTE_ITEM_TYPE, ItemService
from tests.utils.item import create_daily_item
from tests.utils.user import create_user


@pytest.fixture()
def mock_evolution_service() -> EvolutionService | AsyncMock:
    return AsyncMock(spec=EvolutionService)


@pytest.fixture()
def mock_daily_item_repository() -> DailyItemRepository | AsyncMock:
    return AsyncMock(spec=DailyItemRepository)


@pytest.fixture()
def mock_daily_item_abtain_repository() -> DailyItemAbtainRepository | AsyncMock:
    return AsyncMock(spec=DailyItemAbtainRepository)


@pytest.fixture
def item_service(
    mock_evolution_service: AsyncMock,
    mock_daily_item_repository: AsyncMock,
    mock_daily_item_abtain_repository: AsyncMock,
) -> ItemService:
    return ItemService(
        evolution_service=mock_evolution_service,
        daily_item_repository=mock_daily_item_repository,
        daily_item_abtain_repository=mock_daily_item_abtain_repository,
    )


async def test_get_daily_item__existed__return_DailyItemResponse(
    item_service: ItemService,
    mock_daily_item_repository: DailyItemRepository | AsyncMock,
    mock_daily_item_abtain_repository: DailyItemAbtainRepository | AsyncMock,
):
    # given
    user = create_user()
    daily_item = create_daily_item()
    mock_daily_item_repository.find_for_today.return_value = daily_item
    mock_daily_item_abtain_repository.exist_by_user_and_daily_item.return_value = False

    # when
    result = await item_service.get_daily_item(user)

    # then
    assert result.type == daily_item.type
    assert result.can_abtain is True


async def test_get_daily_item__non_existed__create_DailyItem(
    item_service: ItemService,
    mock_daily_item_repository: DailyItemRepository | AsyncMock,
    mock_daily_item_abtain_repository: DailyItemAbtainRepository | AsyncMock,
):
    # given
    user = create_user()
    mock_daily_item_repository.find_for_today.return_value = None
    mock_daily_item_abtain_repository.exist_by_user_and_daily_item.return_value = False

    # when
    result = await item_service.get_daily_item(user)

    # then
    args, _ = mock_daily_item_repository.save.call_args
    created: DailyItem = args[0]
    assert created.type == result.type
    assert result.can_abtain is True


async def test_get_daily_item__existed_DailyItemAbtain(
    item_service: ItemService,
    mock_daily_item_repository: DailyItemRepository | AsyncMock,
    mock_daily_item_abtain_repository: DailyItemAbtainRepository | AsyncMock,
):
    # given
    user = create_user()
    daily_item = create_daily_item()
    mock_daily_item_repository.find_for_today.return_value = daily_item
    mock_daily_item_abtain_repository.exist_by_user_and_daily_item.return_value = True

    # when
    result = await item_service.get_daily_item(user)

    # then
    assert result.type == daily_item.type
    assert result.can_abtain is False


async def test_give_daily_item_to_user__non_existed_DailyItem__create_DailyItem(
    item_service: ItemService,
    mock_daily_item_repository: DailyItemRepository | AsyncMock,
    mock_daily_item_abtain_repository: DailyItemAbtainRepository | AsyncMock,
):
    # given
    user = create_user()
    mock_daily_item_repository.find_for_today.return_value = None
    mock_daily_item_abtain_repository.exist_by_user_and_daily_item.return_value = False

    # when
    await item_service.give_daily_item_to_user(user, False)

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
    mock_daily_item_repository.find_for_today.return_value = daily_item
    mock_daily_item_abtain_repository.exist_by_user_and_daily_item.return_value = False

    # when
    await item_service.give_daily_item_to_user(user, False)

    # then
    args, _ = mock_daily_item_abtain_repository.save.call_args
    created: DailyItemAbtain = args[0]
    assert created.daily_item == daily_item
    assert created.user == user


async def test_give_daily_item_to_user__existed_DailyItemAbtain__raise_BadRequestError(
    item_service: ItemService,
    mock_daily_item_repository: DailyItemRepository | AsyncMock,
    mock_daily_item_abtain_repository: DailyItemAbtainRepository | AsyncMock,
):
    # given
    user = create_user()
    daily_item = create_daily_item()
    mock_daily_item_repository.find_for_today.return_value = daily_item
    mock_daily_item_abtain_repository.exist_by_user_and_daily_item.return_value = True

    # when & then
    with pytest.raises(BadRequestError):
        await item_service.give_daily_item_to_user(user, False)


async def test_give_daily_item_to_user__valid_inputs__give_daily_item_to_user(
    item_service: ItemService,
    mock_daily_item_repository: DailyItemRepository | AsyncMock,
    mock_daily_item_abtain_repository: DailyItemAbtainRepository | AsyncMock,
):
    # given
    user = create_user()
    daily_item = create_daily_item()
    mock_daily_item_repository.find_for_today.return_value = daily_item
    mock_daily_item_abtain_repository.exist_by_user_and_daily_item.return_value = False

    # when
    await item_service.give_daily_item_to_user(user, False)

    # then
    assert user.bag_items[0].item_type == daily_item.type


async def test_give_daily_item_to_user__get_substitute_is_True__give_substitute_item_to_user(
    item_service: ItemService,
    mock_daily_item_repository: DailyItemRepository | AsyncMock,
    mock_daily_item_abtain_repository: DailyItemAbtainRepository | AsyncMock,
):
    # given
    user = create_user()
    daily_item = create_daily_item(type=ItemType.BLANK_PLATE)
    mock_daily_item_repository.find_for_today.return_value = daily_item
    mock_daily_item_abtain_repository.exist_by_user_and_daily_item.return_value = False

    # when
    await item_service.give_daily_item_to_user(user, True)

    # then
    assert user.bag_items[0].item_type == SUBSTITUTE_ITEM_TYPE


# async def test_use_item_to_pokemon__input_rare_candy__level_up_and_try_evolve_pokemon(
#     item_service: ItemService, mock_evolution_service: EvolutionService | AsyncMock
# ):
#     # given
#     user = create_user()
#     pokemon = create_pokemon(pokemon)
#     user.pokemons.append(pokemon)
#     mock_evolution_service.get_evolution_rule_for_pokemon.return_value = EvolutionRule(to=)

#     # when
#     is_used = item_service.use_item_to_pokemon(pokemon, ItemType.RARE_CANDY, user, Time.DAY)

#     # then
#     assert user.bag_items[0].item_type == SUBSTITUTE_ITEM_TYPE
