from typing import Annotated

from fastapi import Depends

from src.external.github_api import GithubAPI


async def get_github_api() -> GithubAPI:
    return GithubAPI()


GITHUB_API_DEP = Annotated[GithubAPI, Depends(get_github_api)]
