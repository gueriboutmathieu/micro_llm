from dataclasses import dataclass
from micro_llm.domain.entities.chat_role import ChatRole as ChatRole

@dataclass
class ChatMessage:
    role: ChatRole
    content: str
    def __init__(self, role, content) -> None: ...
