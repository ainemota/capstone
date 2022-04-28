class InvalidKeys(Exception):
    def __init__(self, expectedKeys: list, receivedKeys: list) -> None:
        self.message = {"invalid_keys":{
            "expected_keys": expectedKeys,
            "received_keys": receivedKeys
        } }
        super().__init__(self.message)

