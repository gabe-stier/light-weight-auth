from typing import Protocol


class LDAPBackend(Protocol):
    def authenticate(self, username: str, password: str) -> bool:
        pass

    def get_user(self, username: str) -> dict | None:
        pass
