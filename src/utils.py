from bisect import bisect_left
from datetime import date, datetime, timezone
from itertools import accumulate
from random import random
from typing import Sequence, TypeVar

T = TypeVar("T")


def weighted_sample(population: Sequence[T], weights: Sequence[float], k: int = 1) -> list[T]:
    accum = list(accumulate(weights))
    total = accum[-1]
    sampl = {}
    while len(sampl) < k:
        index = bisect_left(accum, total * random())
        sampl[index] = population[index]
    return list(sampl.values())


def utc_now_date() -> date:
    return datetime.now(timezone.utc).date()
