import os
import pathlib
import sys
from typing import Literal, TypeAlias

from httpx import Client
from tqdm import tqdm

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
from src.models.pokemon_type import PokemonType  # noqa: E402

ORIGIN_SPRITE_BASE_URL = "https://www.pokencyclopedia.info/sprites/overworlds"

Face: TypeAlias = Literal["right"] | Literal["left"]
Frame: TypeAlias = Literal[1] | Literal[2]

client = Client(http2=True)


def get_origin_sprite_path(pokemon_type: PokemonType, face: Face, is_shiny: bool, frame: Frame) -> str:
    match (face):
        case "left":
            if is_shiny:
                face_part = "o-l_hgss_shiny/o-l_hs-S_"
            else:
                face_part = "o-l_hgss/o-l_hs_"
        case "right":
            if is_shiny:
                face_part = "o-r_hgss_shiny/o-r_hs-S_"
            else:
                face_part = "o-r_hgss/o-r_hs_"

    number_part = str(pokemon_type.national_no).zfill(3)
    if pokemon_type.national_no in [3, 25]:
        number_part += "_m-"
    else:
        number_part += "_"

    return f"{ORIGIN_SPRITE_BASE_URL}/{face_part}{number_part}{frame}.png"


def get_local_sprite_path(pokemon_type: PokemonType, face: Face, is_shiny: bool, frame: Frame):
    if is_shiny:
        return f"imgs/pokemons/{pokemon_type.national_no}_{face}_{frame}.png"
    else:
        return f"imgs/pokemons/{pokemon_type.national_no}_{face}_shiny_{frame}.png"


def load_sprite(pokemon_type: PokemonType, face: Face, is_shiny: bool, frame: Frame) -> bytes:
    origin_sprite_path = get_origin_sprite_path(pokemon_type, face, is_shiny, frame)

    res = client.get(origin_sprite_path)
    res.raise_for_status()
    return res.content


def save_sprite(content: bytes, pokemon_type: PokemonType, face: Face, is_shiny: bool, frame: Frame):
    local_sprite_path = get_local_sprite_path(pokemon_type, face, is_shiny, frame)
    with open(local_sprite_path, "wb") as f:
        f.write(content)


def fetch_sprite(pokemon_type: PokemonType, face: Face, is_shiny: bool, frame: Frame):
    local_sprite_path = get_local_sprite_path(pokemon_type, face, is_shiny, frame)
    if not os.path.exists(local_sprite_path):
        content = load_sprite(pokemon_type, face, is_shiny, frame)
        save_sprite(content, pokemon_type, face, is_shiny, frame)


def main():
    os.makedirs("imgs/pokemons", exist_ok=True)

    for pokemon_type in tqdm(PokemonType):
        fetch_sprite(pokemon_type, "left", False, 1)
        fetch_sprite(pokemon_type, "left", False, 2)

        fetch_sprite(pokemon_type, "right", False, 1)
        fetch_sprite(pokemon_type, "right", False, 2)

        fetch_sprite(pokemon_type, "left", True, 1)
        fetch_sprite(pokemon_type, "left", True, 2)

        fetch_sprite(pokemon_type, "right", True, 1)
        fetch_sprite(pokemon_type, "right", True, 2)


main()
