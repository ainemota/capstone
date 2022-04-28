class InvalidId(Exception):
    def __init__(self, modelName) -> None:
        self.message = {"error": f"{modelName} id not found!"}
        super().__init__(self.message)