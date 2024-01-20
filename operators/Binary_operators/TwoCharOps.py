from operators.operators import Operators


class TwoCharOps(Operators):
    def __init__(self, precedence):
        """
        Base Class constructor of all Binary_operators. Sets the position to center by default.

        :param precedence: holds the precedence of each operator.
        """
        super().__init__(precedence, "Center")

    def operation(self, first_operand, second_operand):
        """
        abstract method for performing all the operator operations. accepts two numbers in order.

        :param first_operand: first number
        :param second_operand: second number
        """
        pass

