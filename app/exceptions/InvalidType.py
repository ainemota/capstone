class InvalidType(Exception):
    def __init__(self, key, validType) -> None:
        self.message = {"error": f"The {key} must be {validType} type!"}
        super().__init__(self.message)