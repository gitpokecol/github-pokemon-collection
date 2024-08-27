import functools
import inspect
import pickle
from bisect import bisect_left
from itertools import accumulate
from os import path
from pathlib import Path
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


def file_cache(filename: str):
    cache_dir = Path("__cache__")
    cache_file = cache_dir.joinpath(filename + ".pickle")

    def _file_cache(func):
        if inspect.iscoroutinefunction(func):

            @functools.wraps(func)
            async def async_inner_file_cache(*args, **kwargs):
                if path.exists(cache_file):
                    with open(cache_file, "rb") as f:
                        rs = pickle.load(f)
                else:
                    rs = await func(*args, **kwargs)
                    cache_file.parent.mkdir(exist_ok=True)
                    with open(cache_file, "wb") as f:
                        pickle.dump(rs, f)

                return rs

            return async_inner_file_cache
        else:

            @functools.wraps(func)
            def inner_file_cache(*args, **kwargs):
                if path.exists(cache_file):
                    with open(cache_file, "rb") as f:
                        rs = pickle.load(f)
                else:
                    rs = func(*args, **kwargs)
                    cache_file.parent.mkdir(exist_ok=True)
                    with open(cache_file, "wb") as f:
                        pickle.dump(rs, f)

                return rs

        return inner_file_cache

    return _file_cache
