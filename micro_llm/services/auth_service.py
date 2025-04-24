from fastapi import HTTPException
from jwt import decode  # pyright: ignore

from python_utils.auth import Auth, AuthException


class AuthService(Auth):
    def __init__(self, secret_key: str, public_key: str):
        token_data_keys = ["user_id", "username"]
        super().__init__(secret_key, public_key, token_data_keys)

    def get_token_data(self, token: str) -> dict[str, str]:
        try:
            self.validate_token(token)
        except AuthException as e:
            raise HTTPException(status_code=401, detail=str(e))

        payload = decode(token, self.secret_key, algorithms=[self.algorithm])
        if not all(key in payload for key in self.token_data_keys):
            raise HTTPException(status_code=401, detail="Missing required data in token")

        return {"user_id": payload["user_id"], "username": payload["username"]}

    def validate_user(self, token: str) -> None:
        try:
            self.validate_token(token)
        except AuthException as e:
            raise HTTPException(status_code=401, detail=str(e))
        payload = decode(token, self.secret_key, algorithms=[self.algorithm])
        if not all(key in payload for key in self.token_data_keys):
            raise HTTPException(status_code=401, detail="Missing required data in token")
