from datetime import datetime, timezone, tzinfo

import pytz

from src.external.ip_api import IpAPI
from src.pokemons.time import Time


class TimeService:
    def __init__(self, *, ip_api: IpAPI):
        self._ip_api = ip_api

    async def get_time_for_client(self, ip_address: str | None) -> Time:
        client_timezone = await self._get_timezone_by_ip_address(ip_address)

        if client_timezone:
            return self._get_time_by_timezone(client_timezone)
        else:
            return self._get_time_by_timezone(timezone.utc)

    async def _get_timezone_by_ip_address(self, ip_address: str | None) -> tzinfo | None:
        if not ip_address:
            return None

        ip_api_res = await self._ip_api.get_timezone_by_ip_address(ip_address)

        if ip_api_res and ip_api_res.status == "success" and ip_api_res.timezone:
            return pytz.timezone(ip_api_res.timezone)

        return None

    def _get_time_by_timezone(self, timezone: tzinfo) -> Time:
        now = datetime.now(timezone)
        if 18 <= now.hour or now.hour < 6:
            return Time.NIGHT
        else:
            return Time.DAY
