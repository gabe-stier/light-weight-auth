from backends.base_backend import AuthBackend
from commands import SQLCommands
from errors import InvalidRole
from typing import Callable, Any
import logging


class SQLBackend(AuthBackend):
    def __init__(
        self, db_connection: Any, hashing_function: Callable[[str], str] | None
    ) -> None:
        self.__conn = db_connection
        self.hash_func = hashing_function
        if self.hash_func == None:
            logging.warning("No hashing function set — storing passwords in plaintext!")

    def authenticate(self, username: str, password: str) -> bool:
        if self.hash_func != None:
            password_hash = self.hash_func(password)
        else:
            password_hash = password
        return False

    def get_user_info(self, username: str) -> dict:
        return_rsp = {}
        return return_rsp

    def register(self, username: str, password: str, role: str) -> bool:
        if role.lower() not in SQLCommands.ROLES:
            raise InvalidRole(
                f"'{role}' is not a valid role. Valid roles are: '{'\',\''.join(SQLCommands.ROLES)}'"
            )
        if self.hash_func != None:
            password_hash = self.hash_func(password)
        else:
            password_hash = password
        cursor = self.__conn.cursor()
        cursor.execute(SQLCommands.ADD_USER, (username, password_hash, role, False))
        return False

    def disable_user(self, username: str, status: bool) -> bool:
        return False
