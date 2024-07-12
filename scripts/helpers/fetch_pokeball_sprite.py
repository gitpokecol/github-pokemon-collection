import os
import pathlib
import sys

from httpx import Client

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
ORIGIN_POKEBALL_URL = "https://www.pokencyclopedia.info/sprites/items/items_old/i_old_poke-ball.png"
LOCAL_POKEBALL_URL = "imgs/ui/pokeball.png"

client = Client(http2=True)


def main():
    os.makedirs("imgs/ui", exist_ok=True)

    res = client.get(ORIGIN_POKEBALL_URL)
    res.raise_for_status()

    with open(LOCAL_POKEBALL_URL, "wb") as f:
        f.write(res.content)


main()
