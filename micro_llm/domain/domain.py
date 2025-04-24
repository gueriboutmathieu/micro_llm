from micro_llm.domain.command_context import CommandContext
from micro_llm.domain.commands.query_llm_command import query_llm_command
from micro_llm.domain.commands.refresh_access_token_command import refresh_access_token_command
from micro_llm.domain.commands.signin_command import signin_command
from python_utils.domain import CommandContextCreator, Domain as BaseDomain




class Domain(BaseDomain[CommandContext]):
    def __init__(
        self,
        command_context_creator: CommandContextCreator[CommandContext],
    ) -> None:
        super().__init__(command_context_creator)

        self.query_llm = self._bind_command(query_llm_command)
        self.refresh_access_token = self._bind_command(refresh_access_token_command)
        self.signin = self._bind_command(signin_command)
