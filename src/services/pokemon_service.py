import random
from typing import Sequence

from src.models.pokedex_item import PokedexItem
from src.models.pokemon import Pokemon
from src.models.user import User
from src.pokemons.evolution import EvolutionRule, evolution_line_cnts, evolution_rules
from src.pokemons.item_type import ItemType
from src.pokemons.pokemon_type import PokemonType
from src.pokemons.time import Time
from src.setting import settings
from src.utils import weighted_sample


class PokemonService:
    def __init__(self) -> None:
        self._evolution_line_counts: dict[PokemonType, int] = {}

    def give_pokemons_for_user(self, user: User, previous_commit_point: int, current_commit_point: int):
        new_count = self._calculate_new_pokemon_count(previous_commit_point, current_commit_point)
        canditates = list(self._get_new_pokemon_candidates(user.pokedex_items))
        new_pokemon_types = self._pick_pokemon_types_by_base_stat(canditates, new_count)
        user.update_pokedex(new_pokemon_types)

        new_pokemons = [self._create_pokemon(pokemon_type) for pokemon_type in new_pokemon_types]
        user.pokemons.extend(new_pokemons)

    def _calculate_new_pokemon_count(self, updated_commit_point: int, current_commit_point: int) -> int:
        given_pokemon_count = updated_commit_point // settings.POKEMON_PER_COMMIT_POINT
        target_pokemon_count = current_commit_point // settings.POKEMON_PER_COMMIT_POINT
        return target_pokemon_count - given_pokemon_count

    def _get_new_pokemon_candidates(self, pokedex_items: Sequence[PokedexItem]) -> set[PokemonType]:
        candiates = set(evolution_line_cnts.keys())
        for pokedex_item in pokedex_items:
            if pokedex_item.type not in evolution_line_cnts:
                continue

            if evolution_line_cnts[pokedex_item.type] <= pokedex_item.obtain_count:
                candiates.remove(pokedex_item.type)

        return candiates

    def _pick_pokemon_types_by_base_stat(self, candidates: Sequence[PokemonType], count: int):
        weights = [1 / type.base_stat for type in candidates]
        return weighted_sample(candidates, weights, count)

    def _create_pokemon(self, pokemon_type: PokemonType):
        is_shiny = settings.SHINY_POKEMON_RATE > random.random()
        gender = random.choice(pokemon_type.available_genders)

        form = None
        if pokemon_type.available_forms:
            form = random.choice(pokemon_type.available_forms)

        return Pokemon(type=pokemon_type, is_shiny=is_shiny, gender=gender, form=form)

    def level_up_pokemons_for_user(
        self, user: User, previous_commit_point: int, current_commit_point: int, time: Time
    ):
        add_level = self._calculate_add_level(previous_commit_point, current_commit_point)
        for pokemon in random.choices(user.pokemons, k=add_level):
            pokemon.level_up()

            rule = self._get_evolution_rule_for_pokemon(
                pokemon,
                user,
                time,
                None,
            )

            if rule:
                self._evolve_pokemon(pokemon, user, rule)

    def _calculate_add_level(self, updated_commit_point: int, current_commit_point: int) -> int:
        given_pokemon_count = updated_commit_point // settings.LEVEL_UP_PER_COMMIT_POINT
        target_pokemon_count = current_commit_point // settings.LEVEL_UP_PER_COMMIT_POINT
        return target_pokemon_count - given_pokemon_count

    def _evolve_pokemon(self, pokemon: Pokemon, owner: User, rule: EvolutionRule):
        if pokemon.type == PokemonType.Nincada:
            shedinja = self._create_pokemon(PokemonType.Shedinja)
            owner.pokemons.append(shedinja)

        pokemon.type = rule.to

    def _get_evolution_rule_for_pokemon(
        self, pokemon: Pokemon, owner: User, time: Time, item: ItemType | None
    ) -> EvolutionRule | None:
        if pokemon.type not in evolution_rules:
            return None

        rules = evolution_rules[pokemon.type]

        if pokemon.type in (PokemonType.Wurmple, PokemonType.Tyrogue):
            return random.choice(rules)

        for rule in rules:
            if rule.can_evolve(pokemon, owner, item, time):
                return rule

        return None
