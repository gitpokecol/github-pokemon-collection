import random
from typing import Generator

from src.models.pokemon_type import PokemonType
from src.renders import templates

sprite_base_url = "https://www.pokencyclopedia.info/sprites/overworlds"
poke_ball_url = "https://www.pokencyclopedia.info/sprites/items/items_old/i_old_poke-ball.png"


class SVGRenderer:

    def render_svg(self, *, pokemons: list[PokemonType], commit_point: int, username: str) -> str:
        return templates.base_svg.format(
            username=username,
            commit_point=commit_point,
            n_pokemons=len(pokemons),
            pokemons="\n".join(self._render_pokemons(pokemons)),
            poke_ball_url=poke_ball_url,
        )

    def _create_left_sprite_urls(self, national_no: int) -> tuple[str, str]:
        start_url = f"{sprite_base_url}/o-l_hgss"
        poke_url = start_url + "/o-l_hs_" + str(national_no).zfill(3)

        if national_no in [3, 25]:
            frame_1 = poke_url + "_m-1.png"
            frame_2 = poke_url + "_m-2.png"
        else:
            frame_1 = poke_url + "_1.png"
            frame_2 = poke_url + "_2.png"

        return frame_1, frame_2

    def _render_pokemons(self, pokemons: list[PokemonType]) -> Generator[str, None, None]:
        for idx, pokemon in enumerate(pokemons):
            num = idx + 1
            duration = random.uniform(10, 15)
            offset = random.randint(-80, 80)
            delay = random.uniform(0, 10)

            frame_1, frame_2 = self._create_left_sprite_urls(pokemon.national_no)

            yield templates.pokemon_svg.format(
                num=num, duration=duration, offset=offset, delay=delay, frame_1=frame_1, frame_2=frame_2
            )
