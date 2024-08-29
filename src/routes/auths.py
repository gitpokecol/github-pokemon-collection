from fastapi import Depends, Response
from fastapi.routing import APIRouter
from httpx_oauth.integrations.fastapi import OAuth2AuthorizeCallback
from httpx_oauth.oauth2 import OAuth2Token

from src.auths.jwt import encode_token
from src.auths.oauth_client import GitHubOAuth2Client
from src.exceptions.common import UnauthorizedError
from src.exceptions.error_codes import ErrorCode
from src.setting import settings

client = GitHubOAuth2Client(
    settings.GITHUB_OAUTH_CLIENT_ID,
    settings.GITHUB_OAUTH_CLIENT_SECRET,
)

router = APIRouter()


@router.get("/api/oauth/callback-github", name="oauth.github.callback")
async def callback_github_oauth(
    response: Response,
    access_token_state: tuple[OAuth2Token, str | None] = Depends(
        OAuth2AuthorizeCallback(client, "oauth.github.callback")
    ),
):
    github_token, state = access_token_state

    if "error" in github_token:
        raise UnauthorizedError(ErrorCode.GITHUB_API_SERVICE_UNAVAILABLE)

    username = await client.get_username(github_token["access_token"])

    access_token = encode_token(username)
    response.set_cookie("Access-Token", access_token)


@router.get("/api/oauth/authorize-github", name="oauth.github.authorize")
async def authorize_github_oauth():
    return await client.get_authorization_url(
        settings.GITHUB_OAUTH_CALLBACK_URL,
        scope=["user"],
    )
