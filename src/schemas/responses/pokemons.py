from pydantic import BaseModel

from src.models.pokemon import Pokemon


class PokemonReponse(BaseModel):
    level: int
    is_shiny: bool
    pokemon_type: int
    gender: str
    form: str | None

    @classmethod
    def of(cls, pokemon: Pokemon) -> "PokemonReponse":
        pokemon_type = pokemon.type
        return PokemonReponse(
            pokemon_type=pokemon_type,
            is_shiny=pokemon.is_shiny,
            gender=pokemon.gender,
            level=pokemon.level,
            form=pokemon.form,
        )


class PokemonsResponse(BaseModel):
    pokemons: list[PokemonReponse]

    @classmethod
    def of(cls, pokemons: list[Pokemon]) -> "PokemonsResponse":
        return PokemonsResponse(pokemons=[PokemonReponse.of(pokemon) for pokemon in pokemons])
