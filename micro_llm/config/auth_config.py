from python_utils.env_vars import EnvVar


def to_list_of_strings(value: str) -> list[str]:
    return [item.strip() for item in value.split(",")]


class AuthConfig:
    def __init__(self) -> None:
        self.secret_key = EnvVar[str]("AUTH_SECRET_KEY", cast_fct=str).value
        self.public_key = EnvVar[str]("AUTH_PUBLIC_KEY", cast_fct=str).value
        self.allowed_origins = EnvVar[list[str]]("AUTH_ALLOWED_ORIGINS", cast_fct=to_list_of_strings).value
