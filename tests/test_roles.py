# tests/test_roles.py
import pytest
from auth_module.roles import has_permission

def test_role_hierarchy():
    assert has_permission("admin", "user")
    assert has_permission("user", "guest")
    assert not has_permission("user", "admin")
    assert not has_permission("guest", "user")

def test_unknown_role_defaults():
    assert not has_permission("unknown", "guest")
    assert not has_permission("guest", "unknown")
