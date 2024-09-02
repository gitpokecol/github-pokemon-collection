import random

from src.models.pokemon import Pokemon
from src.models.user import User
from src.pokemons.evolution import EvolutionRule, evolution_rules
from src.pokemons.item_type import ItemType
from src.pokemons.pokemon_type import PokemonType
from src.pokemons.time import Time
from src.setting import settings


class EvolutionService:

    def get_evolution_rule_for_pokemon(
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

    def evolve_pokemon(self, pokemon: Pokemon, owner: User, rule: EvolutionRule):
        if pokemon.type == PokemonType.Nincada:
            shedinja = self._create_pokemon(PokemonType.Shedinja)
            owner.pokemons.append(shedinja)

        pokemon.type = rule.to

    def _create_pokemon(self, pokemon_type: PokemonType):
        is_shiny = settings.SHINY_POKEMON_RATE > random.random()
        gender = random.choice(pokemon_type.available_genders)

        form = None
        if pokemon_type.available_forms:
            form = random.choice(pokemon_type.available_forms)

        return Pokemon(type=pokemon_type, is_shiny=is_shiny, gender=gender, form=form)
