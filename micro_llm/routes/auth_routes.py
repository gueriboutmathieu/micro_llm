from fastapi import FastAPI, HTTPException

from micro_llm.domain.domain import Domain
from micro_llm.domain.entities.user_tokens import UserTokens
from python_utils.auth import AuthException


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.post("/auth/signin")
    async def signin(public_key: str, username: str) -> UserTokens:  # pyright: ignore[reportUnusedFunction]
        try:
            user_tokens = domain.signin(public_key, username)
        except AuthException as e:
            raise HTTPException(status_code=401, detail=str(e)) from e
        return user_tokens

    @fastapi_app.post("/auth/refresh-access-token")
    async def refresh_access_token(refresh_token: str) -> str:  # pyright: ignore[reportUnusedFunction]
        try:
            access_token = domain.refresh_access_token(refresh_token)
        except AuthException as e:
            raise HTTPException(status_code=401, detail=str(e)) from e
        return access_token
