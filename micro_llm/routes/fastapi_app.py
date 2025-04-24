import importlib.metadata
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from micro_llm.domain.domain import Domain
from micro_llm.routes import auth_routes, llm_routes
from micro_llm.routes.utils import origins_middleware
from python_utils import fastapi_generic_routes as generic_routes
from python_utils import fastapi_middleware as catch_exceptions_middleware


class FastapiApp:
    def __init__(self, domain: Domain, allowed_origins: list[str]) -> None:
        package_name = "micro_llm"
        version = importlib.metadata.version(package_name)
        self.app = FastAPI(version=version)

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        catch_exceptions_middleware.add_middleware(self.app)
        origins_middleware.add_middleware(self.app, allowed_origins)

        auth_routes.load_routes(self.app, domain)
        generic_routes.load_routes(self.app, package_name, version)
        llm_routes.load_routes(self.app, domain)
