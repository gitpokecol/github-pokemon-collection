from enum import Enum


class Time(str, Enum):
    DAY = "day"
    NIGHT = "night"

    def __str__(self) -> str:
        return self.value
