import uvicorn

from micro_llm.config.auth_config import AuthConfig
from micro_llm.config.openai_config import OpenaiConfig
from micro_llm.domain.domain import Domain
from micro_llm.routes.fastapi_app import FastapiApp
from micro_llm.services.auth_service import AuthService
from micro_llm.services.llm_service import LlmService
from python_utils.loggers import get_logger


# Logger
logger = get_logger(__name__)


# Configs
auth_config = AuthConfig()
openai_config = OpenaiConfig()


# Services
auth_service = AuthService(auth_config.secret_key, auth_config.public_key)
llm_service = LlmService(openai_config.api_key)


class CommandContext:
    def __init__(self):
        self.auth_service = auth_service
        self.llm_service = llm_service

    def commit(self):
        pass

    def rollback(self):
        pass



bound_domain = Domain(CommandContext)
fastapi_app = FastapiApp(bound_domain)


def run_server():
    uvicorn.run(fastapi_app.app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    run_server()
