class InvalidOutput(Exception):
    """
    output invalid exception
    """
    def __init__(self, message: str):
        self.message = message


class EmptyExpression(Exception):
    """
    expression empty exception
    """
    def __init__(self, message: str):
        self.message = message


