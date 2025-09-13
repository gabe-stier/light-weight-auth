# tests/test_token.py
import time
from auth_module.token import create_token, verify_token

def test_token_creation_and_verification():
    user_info = {"username": "alice", "role": "user"}
    token = create_token(user_info, expires_in=10)
    assert verify_token(token)["username"] == "alice"

def test_token_expiration():
    user_info = {"username": "alice", "role": "user"}
    token = create_token(user_info, expires_in=1)  # expires in 1 sec
    time.sleep(2)
    assert verify_token(token) is None
