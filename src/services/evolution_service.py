import random

from src.models.pokemon import Pokemon
from src.models.user import User
from src.pokemons.evolution import EvolutionRule, evolution_rules
from src.pokemons.item_type import ItemType
from src.pokemons.pokemon_type import PokemonType
from src.pokemons.time import Time


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
            shedinja = Pokemon.create_random(PokemonType.Shedinja)
            owner.pokemons.append(shedinja)
            owner.update_pokedex([PokemonType.Shedinja])

        pokemon.type = rule.to

        if pokemon.form not in rule.to.available_forms:
            pokemon.form = None

        owner.update_pokedex([rule.to])
