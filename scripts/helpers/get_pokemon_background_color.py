import pathlib
import sys
from typing import Any

from PIL import Image

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
print(str(pathlib.Path(__file__).resolve().parents[2]))
BLOCK_SIZE = 1
DEFAULT_COLOR = "#FFFFFF"


def get_background_color_of_sprite(image_path):
    image = Image.open(image_path)

    # Convert the image to RGBA if it's not already in that format
    image = image.convert("RGBA")
    width, height = image.size

    pixels: Any = image.getdata()

    rgb = {"r": 0, "g": 0, "b": 0}
    count = 0

    for i in range(0, len(pixels), BLOCK_SIZE):
        r, g, b, a = pixels[i]
        if a == 0:  # Ignore fully transparent pixels
            continue

        count += 1
        rgb["r"] += r
        rgb["g"] += g
        rgb["b"] += b

    if count == 0:
        return DEFAULT_COLOR

    rgb["r"] = min(255, int((rgb["r"] / count) * 1.5))
    rgb["g"] = min(255, int((rgb["g"] / count) * 1.5))
    rgb["b"] = min(255, int((rgb["b"] / count) * 1.5))

    # Convert RGB values to hexadecimal and format as #RRGGBB
    hex_color = f"#{rgb['r']:02x}{rgb['g']:02x}{rgb['b']:02x}"

    return hex_color


def main():
    base_path = pathlib.Path("./imgs/sprites/pokemon")
    colors = {}

    for sprite_path in base_path.iterdir():
        if not ("front" in sprite_path.name and sprite_path.name.endswith("1.png")):
            continue

        id = int(sprite_path.name.split("_")[0])
        if id in colors:
            continue

        colors[id] = get_background_color_of_sprite(str(sprite_path.absolute()))

    for id in sorted(colors.keys()):
        print(f'{id}: "{colors[id]}"')


main()
