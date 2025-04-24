from micro_llm.domain.command_context import CommandContext


def validate_user_command(command_context: CommandContext, access_token: str) -> None:
    command_context.auth_service.validate_user(access_token)
