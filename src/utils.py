from bisect import bisect_left
from datetime import _TzInfo, datetime
from itertools import accumulate
from random import random
from typing import Literal, Sequence, TypeVar

T = TypeVar("T")


def weighted_sample(population: Sequence[T], weights: Sequence[float], k: int = 1) -> list[T]:
    accum = list(accumulate(weights))
    total = accum[-1]
    sampl = {}
    while len(sampl) < k:
        index = bisect_left(accum, total * random())
        sampl[index] = population[index]
    return list(sampl.values())


def get_time_by_timezone(timezone: _TzInfo) -> Literal["day", "night"]:
    now = datetime.now(timezone)
    if 18 <= now.hour or now.hour < 6:
        return "night"
    else:
        return "day"
