from _typeshed import Incomplete
from micro_llm.domain.command_context import CommandContext as CommandContext
from micro_llm.domain.commands.query_llm_command import query_llm_command as query_llm_command
from micro_llm.domain.commands.refresh_access_token_command import refresh_access_token_command as refresh_access_token_command
from micro_llm.domain.commands.signin_command import signin_command as signin_command
from micro_llm.domain.commands.validate_user_command import validate_user_command as validate_user_command
from python_utils.domain import CommandContextCreator as CommandContextCreator, Domain as BaseDomain

class Domain(BaseDomain[CommandContext]):
    query_llm: Incomplete
    refresh_access_token: Incomplete
    signin: Incomplete
    validate_user: Incomplete
    def __init__(self, command_context_creator: CommandContextCreator[CommandContext]) -> None: ...
