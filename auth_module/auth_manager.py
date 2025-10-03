from backends.base_backend import AuthBackend


class AuthManager:
    def __init__(self) -> None:
        self.backends: dict[str, AuthBackend] = {}

    def register_backend(self, name: str, backend: AuthBackend):
        self.backends[name] = backend

    def authenticate(self, username: str, password: str) -> str | None:
        return None

    def verify_token(self, token: str) -> dict | None:
        return verify_token(token)
