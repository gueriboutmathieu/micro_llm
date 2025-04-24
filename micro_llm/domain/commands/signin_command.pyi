from micro_llm.domain.command_context import CommandContext as CommandContext
from micro_llm.domain.entities.user_tokens import UserTokens as UserTokens

def signin_command(command_context: CommandContext, public_key: str, username: str) -> UserTokens: ...
