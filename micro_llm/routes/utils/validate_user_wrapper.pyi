from fastapi import Depends as Depends
from micro_llm.domain.domain import Domain as Domain
from python_utils.auth import oauth2_scheme as oauth2_scheme

def validate_user_wrapper(domain: Domain): ...
