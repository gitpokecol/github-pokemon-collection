from pydantic import BaseModel


class AuthCallbackResponse(BaseModel):
    access_token: str
