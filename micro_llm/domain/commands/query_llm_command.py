from micro_llm.domain.command_context import CommandContext
from micro_llm.domain.entities.chat_message import ChatMessage


def query_llm_command(
    command_context: CommandContext,
    chat_messages: list[ChatMessage],
    model: str,
    temperature: int
) -> ChatMessage:
    return command_context.llm_service.query(chat_messages, model, temperature)
