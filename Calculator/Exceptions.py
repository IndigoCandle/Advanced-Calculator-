class InvalidOutput(Exception):
    def __init__(self, message: str):
        self.message = message


class EmptyExpression(Exception):
    def __init__(self, message: str):
        self.message = message


