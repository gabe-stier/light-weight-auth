from abc import ABC, abstractmethod


class AuthBackend(ABC):
    @abstractmethod
    def authenticate(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def get_user_info(self, username: str) -> dict:
        pass
