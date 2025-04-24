from micro_llm.domain.command_context import CommandContext as CommandContext
from micro_llm.domain.entities.chat_message import ChatMessage as ChatMessage

def query_llm_command(command_context: CommandContext, chat_messages: list[ChatMessage], model: str, temperature: int) -> ChatMessage: ...
