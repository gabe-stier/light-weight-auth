# tests/test_auth.py
def test_successful_auth(auth_manager):
    token = auth_manager.authenticate("alice", "password123")
    assert token is not None
    user_info = auth_manager.verify_token(token)
    assert user_info["username"] == "alice"
    assert user_info["role"] == "user"

def test_failed_auth_wrong_password(auth_manager):
    token = auth_manager.authenticate("alice", "wrongpassword")
    assert token is None

def test_failed_auth_nonexistent_user(auth_manager):
    token = auth_manager.authenticate("eve", "nopass")
    assert token is None

def test_auth_multiple_backends(auth_manager):
    # Bob exists only in LDAP backend
    token = auth_manager.authenticate("bob", "ldapsecret")
    assert token is not None
    user_info = auth_manager.verify_token(token)
    assert user_info["username"] == "bob"
    assert user_info["role"] == "admin"
