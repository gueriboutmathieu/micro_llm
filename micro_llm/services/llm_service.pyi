from _typeshed import Incomplete
from micro_llm.domain.entities.chat_message import ChatMessage as ChatMessage

class LlmService:
    api_key: Incomplete
    client: Incomplete
    def __init__(self, api_key: str) -> None: ...
    def query(self, chat_messages: list[ChatMessage], model: str, temperature: int) -> ChatMessage: ...
