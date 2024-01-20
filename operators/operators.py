class Operators:
    def __init__(self, precedence, position):
        """
        Base Class constructor of all operators.

        :param precedence: holds the precedence of each operator.
        :param position: holds the position of the operator in relation to the operand/s
        """
        self.precedence = precedence
        self.position = position

