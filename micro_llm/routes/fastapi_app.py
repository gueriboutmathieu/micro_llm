import importlib.metadata
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from flare.domain.domain import Domain
from flare.routes import auth_routes, user_routes, video_routes
from python_utils import fastapi_generic_routes as generic_routes
from python_utils import fastapi_middleware as catch_exceptions_middleware



class FastapiApp:
    def __init__(self, domain: Domain) -> None:
        package_name = "flare"
        version = importlib.metadata.version(package_name)
        self.app = FastAPI(version=version)

        catch_exceptions_middleware.add_middleware(self.app)
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        auth_routes.load_routes(self.app, domain)
        generic_routes.load_routes(self.app, package_name, version)
        user_routes.load_routes(self.app, domain)
        video_routes.load_routes(self.app, domain)
