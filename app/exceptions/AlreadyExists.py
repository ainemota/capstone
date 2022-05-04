class AlreadyExists(Exception):
    def __init__(self, key) -> None:
        self.message = {"error": f"This {key} already exists!"}
        super().__init__(self.message)