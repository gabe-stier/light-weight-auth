from backends.base_backend import AuthBackend


class SQLBackend(AuthBackend):
    def __init__(self, db_connection) -> None:
        self.__conn = db_connection

    def authenticate(self, username: str, password: str) -> bool:
        return

    def get_user_info(self, username: str) -> dict:

        return
