from fastapi import FastAPI as FastAPI
from micro_llm.domain.domain import Domain as Domain
from micro_llm.domain.entities.chat_message import ChatMessage as ChatMessage
from micro_llm.routes.utils.validate_user_wrapper import validate_user_wrapper as validate_user_wrapper

def load_routes(fastapi_app: FastAPI, domain: Domain): ...
