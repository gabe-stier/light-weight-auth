class BaseError(Exception):
    def __init__(self, message: str, *args: object) -> None:
        self.message = message
