class InvalidUser(Exception):
    def __init__(self, ) -> None:
        self.message = {"msg": "Just the owner can update something"}
        super().__init__(self.message)