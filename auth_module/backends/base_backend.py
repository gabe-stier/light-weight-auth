from abc import ABC, abstractmethod


class AuthBackend(ABC):
    @abstractmethod
    def authenticate(self, username: str, password: str) -> bool: ...

    @abstractmethod
    def get_user(self, username: str) -> dict | None: ...
