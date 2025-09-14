# tests/conftest.py
import pytest
from auth_module.auth_manager import AuthManager
from auth_module.backends.base_backend import AuthBackend


# Fake backend for testing
class FakeBackend(AuthBackend):
    def __init__(self, name, users, role="user"):
        self.name = name
        self.users = users  # dict: username -> password
        self.role = role

    def authenticate(self, username, password):
        return self.users.get(username) == password

    def get_user_info(self, username):
        if username in self.users:
            return {"username": username, "role": self.role}
        return {}


# Fixture for AuthManager with multiple fake backends
@pytest.fixture
def auth_manager():
    manager = AuthManager()
    manager.register_backend(
        "sql", FakeBackend("sql", {"alice": "password123"}, role="user")
    )
    manager.register_backend(
        "ldap", FakeBackend("ldap", {"bob": "ldapsecret"}, role="admin")
    )
    manager.register_backend(
        "oauth", FakeBackend("oauth", {"carol": "oauthpass"}, role="user")
    )
    manager.register_backend(
        "kerberos", FakeBackend("kerberos", {"dan": "kerbpass"}, role="user")
    )
    return manager
