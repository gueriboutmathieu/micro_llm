from _typeshed import Incomplete
from micro_llm.config.auth_config import AuthConfig as AuthConfig
from micro_llm.config.openai_config import OpenaiConfig as OpenaiConfig
from micro_llm.domain.domain import Domain as Domain
from micro_llm.routes.fastapi_app import FastapiApp as FastapiApp
from micro_llm.services.auth_service import AuthService as AuthService
from micro_llm.services.llm_service import LlmService as LlmService

logger: Incomplete
auth_config: Incomplete
openai_config: Incomplete
auth_service: Incomplete
llm_service: Incomplete

class CommandContext:
    auth_service: Incomplete
    llm_service: Incomplete
    def __init__(self) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...

bound_domain: Incomplete
fastapi_app: Incomplete

def run_server() -> None: ...
