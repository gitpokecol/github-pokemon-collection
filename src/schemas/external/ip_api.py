from typing import Literal

from pydantic import BaseModel, Field


class IpApiResponse(BaseModel):
    status: Literal["success", "fail"]
    timezone: str | None = Field(None)
