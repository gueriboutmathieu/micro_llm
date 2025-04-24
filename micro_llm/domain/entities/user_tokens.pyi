from dataclasses import dataclass

@dataclass
class UserTokens:
    access_token: str
    refresh_token: str
    def __init__(self, access_token, refresh_token) -> None: ...
