import random

from src.models.pokemon import Pokemon
from src.models.user import User
from src.pokemons.evolution import EvolutionRule, evolution_rules
from src.pokemons.item_type import ItemType
from src.pokemons.pokemon_type import PokemonType
from src.pokemons.time import Time
from src.repositories.pokemon_repository import PokemonRepository
from src.services.pokedex_service import PokedexService


class EvolutionService:

    def __init__(self, *, pokedex_service: PokedexService, pokemon_repository: PokemonRepository) -> None:
        self._pokedex_service = pokedex_service
        self._pokemon_repository = pokemon_repository

    async def get_evolution_rule_for_pokemon(
        self, pokemon: Pokemon, owner: User, time: Time, item: ItemType | None
    ) -> EvolutionRule | None:
        if pokemon.type not in evolution_rules:
            return None

        rules = evolution_rules[pokemon.type]

        if pokemon.type in (PokemonType.Wurmple, PokemonType.Tyrogue):
            return random.choice(rules)

        if pokemon.type == PokemonType.Mantyke:
            if not await self._pokemon_repository.exist_by_types_and_owner(
                owner, (PokemonType.Remoraid, PokemonType.Octillery)
            ):
                return None

        for rule in rules:
            if rule.can_evolve(pokemon, item, time):
                return rule

        return None

    async def evolve_pokemon(self, pokemon: Pokemon, owner: User, rule: EvolutionRule):
        if pokemon.type == PokemonType.Nincada:
            shedinja = Pokemon.create_random(PokemonType.Shedinja, owner)
            await self._pokemon_repository.save(shedinja)
            await self._pokedex_service.update_pokedex_for_user(owner, [PokemonType.Shedinja])

        pokemon.type = rule.to

        if pokemon.form not in rule.to.available_forms:
            pokemon.form = None

        await self._pokedex_service.update_pokedex_for_user(owner, [rule.to])

    async def get_pokemons(self, user: User):
        return await self._pokemon_repository.find_by_owner(user)
