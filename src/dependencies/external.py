from typing import Annotated

from fastapi import Depends

from src.external.github_api import GithubAPI
from src.external.ip_api import IpAPI


async def get_github_api() -> GithubAPI:
    return GithubAPI()


async def get_ip_api() -> IpAPI:
    return IpAPI()


GithubAPIDep = Annotated[GithubAPI, Depends(get_github_api)]
IpAPIDep = Annotated[IpAPI, Depends(get_ip_api)]
