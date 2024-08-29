from typing import Literal

from pydantic import BaseModel


class IpApiResponse(BaseModel):
    status: Literal["success", "fail"]
    timezone: str | None
