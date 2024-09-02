from src.models.user import User
from src.schemas.responses.pokedex import PokedexResponse


class PokedexService:
    def get_pokedex(self, user: User) -> PokedexResponse:
        return PokedexResponse.of(user.pokedex_items)
