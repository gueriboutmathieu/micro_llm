from _typeshed import Incomplete
from micro_llm.domain.domain import Domain as Domain
from micro_llm.routes import auth_routes as auth_routes, llm_routes as llm_routes
from micro_llm.routes.utils import origins_middleware as origins_middleware

class FastapiApp:
    app: Incomplete
    def __init__(self, domain: Domain, allowed_origins: list[str]) -> None: ...
