import base64

import aiofiles


async def load_as_base64(path: str) -> str:
    async with aiofiles.open(path, "rb") as f:
        content = await f.read()
        return "data:image/png;base64," + base64.b64encode(content).decode("utf-8")
