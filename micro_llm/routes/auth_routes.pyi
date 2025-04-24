from fastapi import FastAPI as FastAPI
from micro_llm.domain.domain import Domain as Domain
from micro_llm.domain.entities.user_tokens import UserTokens as UserTokens

def load_routes(fastapi_app: FastAPI, domain: Domain): ...
