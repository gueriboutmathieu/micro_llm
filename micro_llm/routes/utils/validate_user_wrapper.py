from fastapi import Depends
from typing import Annotated

from micro_llm.domain.domain import Domain
from python_utils.auth import oauth2_scheme


def validate_user_wrapper(domain: Domain):
    async def validate_user(token: Annotated[str, Depends(oauth2_scheme)]) -> None:
        return domain.validate_user(token)
    return validate_user
