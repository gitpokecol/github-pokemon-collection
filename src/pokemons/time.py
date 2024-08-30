from datetime import datetime, tzinfo
from enum import Enum


class Time(str, Enum):
    DAY = "day"
    NIGHT = "night"

    def __str__(self) -> str:
        return self.value


def get_time_by_timezone(timezone: tzinfo) -> Time:
    now = datetime.now(timezone)
    if 18 <= now.hour or now.hour < 6:
        return Time.NIGHT
    else:
        return Time.DAY
