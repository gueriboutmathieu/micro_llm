from fastapi import FastAPI, HTTPException, Request, Response
from typing import Awaitable, Callable


def add_middleware(fastapi_app: FastAPI, allowed_origins: list[str]) -> None:
    @fastapi_app.middleware("http")
    async def verify_origins(  # pyright: ignore[reportUnusedFunction]
        request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ):
        origin = request.headers.get("origin")
        if origin is None or origin not in allowed_origins:
            raise HTTPException(status_code=403, detail="Origin not allowed")

        return await call_next(request)
