from dataclasses import dataclass
from micro_llm.domain.entities.chat_role import ChatRole


@dataclass
class ChatMessage:
    role: ChatRole
    content: str
