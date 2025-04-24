from fastapi import Depends, FastAPI

from micro_llm.domain.domain import Domain
from micro_llm.domain.entities.chat_message import ChatMessage
from micro_llm.routes.utils.validate_user_wrapper import validate_user_wrapper


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.post("/query")
    async def query_llm(  # pyright: ignore[reportUnusedFunction]
        chat_messages: list[ChatMessage],
        model: str = "gpt-4.1-nano",
        _: None = Depends(validate_user_wrapper(domain))
    ) -> ChatMessage:
        return domain.query_llm(chat_messages, model)
