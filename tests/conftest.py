import pytest
import sqlite3

from auth_module.backends.sql.backend import SQLBackend
from auth_module.backends.ldap.backend import LDAPBackend
from auth_module.backends.oauth.backend import OAuthBackend
from auth_module.backends.kerberos.backend import KerberosBackend


@pytest.fixture
def sql_backend():
    conn = sqlite3.connect(":memory:")

    def test_hash(pw: str) -> str:
        return pw[::-1]

    backend = SQLBackend(conn, test_hash)
    backend.table_init()
    yield backend
    conn.close()


@pytest.fixture
def ldap_backend():
    backend = LDAPBackend(server_uri="ldap://fake", base_dn="dc=realm,dc=local")
    yield backend


@pytest.fixture
def oauth_backend():
    backend = OAuthBackend(server_url="https://oauth.realm.local")
    yield backend


@pytest.fixture
def kerberos_backend():
    backend = KerberosBackend(realm="realm.local")
    yield backend


@pytest.fixture(
    params=["sql_backend", "ldap_backend", "oauth_backend", "kerberos_backend"]
)
def backend(request, sql_backend, ldap_backend, oauth_backend, kerberos_backend):
    mapping = {
        sql_backend: "sql_backend",
        ldap_backend: "ldap_backend",
        oauth_backend: "oauth_backend",
        kerberos_backend: "kerberos_backend",
    }
    return mapping[request.param]
