from httpx import AsyncClient

from src.schemas.external.ip_api import IpApiResponse

IP_API_BASE_URL = "http://ip-api.com"


class IpAPI:

    def __init__(self) -> None:
        self.client = AsyncClient(base_url=IP_API_BASE_URL)

    async def get_timezone_by_ip_address(self, ip_address: str) -> None | IpApiResponse:
        res = await self.client.get(f"/json/{ip_address}??fields=status,timezone")

        if res.status_code >= 400:
            return None

        return IpApiResponse.model_validate(res.json())
