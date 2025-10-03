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

    def table_init(self) -> None:
        cursor = self.__conn
        cursor.execute(SQLCommands.USER_TABLE_CREATION)
        cursor.exectue(SQLCommands.TOKEN_TABLE_CREATION)
        self.__commit_and_close(cursor)

    def authenticate(self, username: str, password: str) -> bool:
        user_authenticated = False
        if self.hash_func != None:
            password_hash = self.hash_func(password)
        else:
            password_hash = password
        cursor = self.__conn.cursor()
        cursor.execute(SQLCommands.VALIDATE_USER, (username, password_hash))
        user = cursor.fetchone()
        if user is not None:
            user_authenticated = True
        self.__commit_and_close(cursor)
        return user_authenticated

    def get_user(self, username: str) -> dict | None:
        cursor = self.__conn.cursor()
        cursor.execute(SQLCommands.DESCRIBE_USER, (username,))
        user = cursor.fetchone()
        self.__commit_and_close(cursor)
        return user

    def register(self, username: str, password: str, role: str) -> bool:
        user_registered = False
        if role.lower() not in SQLCommands.ROLES:
            raise InvalidRole(
                f"'{role}' is not a valid role. Valid roles are: '{'\',\''.join(SQLCommands.ROLES)}'"
            )
        if self.hash_func != None:
            password_hash = self.hash_func(password)
        else:
            password_hash = password
        cursor = self.__conn.cursor()
        try:
            cursor.execute(SQLCommands.ADD_USER, (username, password_hash, role, False))
            user_registered = True
        except Exception as e:
            print(e)
        finally:
            self.__commit_and_close(cursor)
        return user_registered

    def modify_user_status(self, username: str, status: bool) -> bool:
        updated_status = False
        match (status):
            case True:
                command = SQLCommands.DISABLE_USER
            case False:
                command = SQLCommands.ENABLE_USER
        cursor = self.__conn.cursor()
        try:
            cursor.execute(command, (username,))
            updated_status = True
        except Exception as e:
            print(e)
        finally:
            self.__commit_and_close(cursor)
        return updated_status

    def __commit_and_close(self, cursor):
        try:
            cursor.commit()
        except:
            pass
        cursor.close()
