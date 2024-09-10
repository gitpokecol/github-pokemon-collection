import random

from src.exceptions.common import BadRequestError, ForbiddenError
from src.exceptions.error_codes import ErrorCode
from src.models.daily_item import DailyItem
from src.models.daily_item_abtain import DailyItemAbtain
from src.models.pokemon import Pokemon
from src.models.user import User
from src.pokemons.item_effect import EvolutionItemEffect, RareCandyEffect
from src.pokemons.item_type import ItemType
from src.pokemons.time import Time
from src.repositories.bag_item_repository import BagItemRepository
from src.repositories.daily_item_abtain_repository import DailyItemAbtainRepository
from src.repositories.daily_item_repository import DailyItemRepository
from src.schemas.responses.items import BagItemsResponse, DailyItemResponse, UseItemResponse
from src.services.evolution_service import EvolutionService

SUBSTITUTE_ITEM_TYPE = ItemType.RARE_CANDY


class ItemService:

    def __init__(
        self,
        *,
        evolution_service: EvolutionService,
        daily_item_repository: DailyItemRepository,
        daily_item_abtain_repository: DailyItemAbtainRepository,
        bag_item_repository: BagItemRepository,
    ) -> None:
        self._evolution_service = evolution_service
        self._daily_item_repo = daily_item_repository
        self._daily_item_abtain_repo = daily_item_abtain_repository
        self._bag_item_repo = bag_item_repository

    async def get_daily_item(self, user: User) -> DailyItemResponse:
        daily_item = await self._get_daily_item()
        is_given = await self._daily_item_abtain_repo.exist_by_user_and_daily_item(user, daily_item)

        return DailyItemResponse.of(type=daily_item.type, can_abtain=not is_given)

    async def give_daily_item_to_user(self, user: User, get_substitute: bool) -> None:
        daily_item = await self._get_daily_item()
        await self._validate_not_to_give_daily_item_to_user(user, daily_item)

        daily_item_abtain = DailyItemAbtain(user=user, daily_item=daily_item)
        await self._daily_item_abtain_repo.save(daily_item_abtain)

        if get_substitute:
            user.add_item(SUBSTITUTE_ITEM_TYPE)
        else:
            user.add_item(daily_item.type)

    async def _validate_not_to_give_daily_item_to_user(self, user: User, daily_item: DailyItem):
        is_given = await self._daily_item_abtain_repo.exist_by_user_and_daily_item(user, daily_item)

        if is_given:
            raise BadRequestError(ErrorCode.ALREADY_ABTAINED_DAILY_ITEM)

    async def _get_daily_item(self) -> DailyItem:
        daily_item = await self._daily_item_repo.find_for_today()

        if daily_item is None:
            daily_item = self._create_daily_item()
            await self._daily_item_repo.save(daily_item)

        return daily_item

    def _create_daily_item(self) -> DailyItem:
        item_type = random.choice(tuple(ItemType))
        daily_item = DailyItem(type=item_type)

        return daily_item

    async def get_bag_items(self, username: str) -> BagItemsResponse:
        bag_items = await self._bag_item_repo.find_containing_item_by_owner_name(username)
        return BagItemsResponse.of(bag_items)

    async def use_item_to_pokemon(
        self, pokemon: Pokemon, item_type: ItemType, user: User, time: Time
    ) -> UseItemResponse:
        self._validate_user_has_item(item_type, user)

        if item_type.effect is None:
            return UseItemResponse(is_used=False)

        item_type.effect.apply(pokemon)

        if isinstance(item_type.effect, EvolutionItemEffect):
            is_used = await self._use_evolution_item_to_pokemon(pokemon, item_type, user, time)
            if not is_used:
                return UseItemResponse(is_used=False)
        if isinstance(item_type.effect, RareCandyEffect):
            await self._use_evolution_item_to_pokemon(pokemon, item_type, user, time)

        user.remove_item(item_type)
        return UseItemResponse(is_used=True)

    async def _use_evolution_item_to_pokemon(
        self, pokemon: Pokemon, item_type: ItemType, user: User, time: Time
    ) -> bool:
        rule = self._evolution_service.get_evolution_rule_for_pokemon(pokemon, user, time, item_type)
        if rule is None:
            return False

        await self._evolution_service.evolve_pokemon(pokemon, user, rule)
        return True

    def _validate_user_has_item(self, item_type: ItemType, user: User):
        if not any([bag_item.item_type == item_type for bag_item in user.existed_bag_items]):
            raise ForbiddenError(ErrorCode.NOT_ENOUGH_ITEM)
