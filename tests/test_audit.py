# tests/test_audit.py
import pytest

class AuditLogger:
    def __init__(self):
        self.entries = []

    def log(self, action, username, success):
        self.entries.append({"action": action, "username": username, "success": success})

@pytest.fixture
def audit_logger():
    return AuditLogger()

def test_audit_logging_success(audit_logger):
    audit_logger.log("login", "alice", True)
    assert audit_logger.entries[-1]["success"] is True
    assert audit_logger.entries[-1]["username"] == "alice"

def test_audit_logging_failure(audit_logger):
    audit_logger.log("login", "bob", False)
    assert audit_logger.entries[-1]["success"] is False
