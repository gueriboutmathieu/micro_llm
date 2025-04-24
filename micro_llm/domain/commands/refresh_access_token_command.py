from micro_llm.domain.command_context import CommandContext


def refresh_access_token_command(command_context: CommandContext, refresh_token: str) -> str:
    command_context.auth_service.validate_token(refresh_token)

    token_data = command_context.auth_service.get_token_data(refresh_token)

    return command_context.auth_service.create_access_token(token_data)
