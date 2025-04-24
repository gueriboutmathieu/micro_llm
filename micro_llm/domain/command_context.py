from typing import Protocol

from micro_llm.services.auth_service import AuthService
from micro_llm.services.llm_service import LlmService


class CommandContext(Protocol):
    @property
    def auth_service(self) -> AuthService:
        ...

    @property
    def llm_service(self) -> LlmService:
        ...

    def commit(self) -> None:
        ...

    def rollback(self) -> None:
        ...


def make_context(
    auth_service: AuthService,
    llm_service: LlmService,
) -> CommandContext:
    class CC:
        def __init__(self):
            self.auth_service = auth_service
            self.llm_service = llm_service

        def commit(self) -> None:
            ...

        def rollback(self) -> None:
            ...

    return CC()
