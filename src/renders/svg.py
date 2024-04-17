import random
from typing import Generator

from models.pokemon_type import PokemonType

sprite_base_url = "https://www.pokencyclopedia.info/sprites/overworlds"
poke_ball_url = "https://www.pokencyclopedia.info/sprites/items/items_old/i_old_poke-ball.png"


class SVGRenderer:

    def render_svg(self, *, pokemons: list[PokemonType], commit_point: int, username: str) -> str:

        def pets() -> Generator[str, str, None]:
            for idx, pokemon in enumerate(pokemons):
                num = idx + 1
                frame_1, frame_2 = self._create_left_sprite_urls(pokemon.national_no)

                yield (
                    f'<g class="pet" id="pet-{num}">'
                    f'<g class="left">'
                    f'<image class="frame-2" xmlns="http://www.w3.org/2000/svg" width="32" height="32" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="{frame_1}"/>'  # noqa: E501
                    f'<image class="frame-1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="{frame_2}"/>'  # noqa: E501
                    "</g>"
                    "</g>"
                )

        n_pets = len(pokemons)
        style_element = self._create_style(n_pets)
        pets_elements = "\n".join(pets())

        return (
            '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="250">'
            f"{style_element}"
            '<rect xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="white"/>'
            '<rect xmlns="http://www.w3.org/2000/svg" x="0.01" y="0.01" rx="4.5" width="99.99%" height="99.99%" stroke="#e4e2e2"  fill="#ffffff" stroke-opacity="1"/>'  # noqa: E501
            '<g transform="translate(20, 30)">'
            f'<text  x="0" y="0" class="header">{username}\'s Pokemons</text>'
            "</g>"
            '<g transform="translate(20, 230)">'
            f'<text x="25" y="0" class="bottom">({n_pets}/151)</text>'
            f'<image x="-7" y="-22" xmlns="http://www.w3.org/2000/svg" width="30" height="30" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="{poke_ball_url}"/>'  # noqa: E501
            f"</g>"
            '<g transform="translate(180, 230)">'
            f'<text x="25" y="0" class="bottom">CP {commit_point}</text>'
            "</g>"
            '<g id="pets" transform="translate(0,40)">'
            f"{pets_elements}"
            "</g></svg>"
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

    def _create_style(self, n_pets: int) -> str:
        def pets() -> Generator[str, None, None]:
            for num in range(1, n_pets + 1):
                duration = random.uniform(10, 15)
                offset = random.randint(-80, 80)
                delay = random.uniform(0, 10)

                yield (
                    f"#pet-{num}" + " {"
                    f"--pet-move-duration: {duration}s;"
                    f"--pet-x-offsets: {offset+60}px;"
                    f"--pet-y-offsets: {offset}px;"
                    f"--pet-move-delay: {delay}s"
                    "}"
                )

        pets_style = "\n".join(pets())

        return (
            '<style xmlns="http://www.w3.org/2000/svg">'
            '@import url("https://fonts.cdnfonts.com/css/public-pixel")'
            ":root {"
            "--pet-x-offsets: 20px;"
            "--pet-y-offsets: 20px;"
            "--pet-move-duration: 10s;"
            "--pet-move-delay: 0s;"
            "}"
            ".frame-1 { animation: 0.5s linear infinite move-frame-1; }"
            ".frame-2 { animation: 0.5s linear infinite move-frame-2; }"
            "@keyframes move-frame-1 { 0% {opacity: 0;} 49% {opacity: 0;} 50% {opacity: 1;} 100% {opacity: 1;} }"
            "@keyframes move-frame-2 { 0% {opacity: 1;} 49% {opacity: 1;} 50% {opacity: 0;} 100% {opacity: 0;} }"
            ".pet {"
            "opacity: 0;"
            "animation-name: move-pet;"
            "animation-duration: var(--pet-move-duration);"
            "animation-delay: var(--pet-move-delay);"
            "animation-iteration-count: infinite;"
            "animation-timing-function: linear;"
            "}"
            "@keyframes move-pet {"
            "0% {opacity: 1; transform: translate(120%, calc(64px + var(--pet-y-offsets)));}"
            "100% {opacity: 1; transform: translate(-120%, calc(64px + var(--pet-y-offsets)));}"
            "}"
            'text { font-family: "Public Pixel", sans-serif; }'
            ".header { font-weight: 0; font-size: 12px; }"
            ".bottom { font-weight: 0; font-size: 10px; }"
            f"{pets_style}"
            "</style>"
        )
