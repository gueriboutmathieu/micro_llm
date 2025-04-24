from uuid6 import uuid7

from micro_llm.domain.command_context import CommandContext
from micro_llm.domain.entities.user_tokens import UserTokens


def signin_command(command_context: CommandContext, public_key: str, username: str) -> UserTokens:
    command_context.auth_service.validate_public_key(public_key)

    token_data = {"user_id": str(uuid7()), "username": username}

    access_token = command_context.auth_service.create_access_token(token_data)

    refresh_token = command_context.auth_service.create_refresh_token(token_data)

    return UserTokens(
        access_token=access_token,
        refresh_token=refresh_token,
    )
