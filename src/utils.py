import functools
import inspect
import pickle
from os import path
from pathlib import Path


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
