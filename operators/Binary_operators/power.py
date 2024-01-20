import math

from operators.Binary_operators.TwoCharOps import TwoCharOps


class pow(TwoCharOps):
    def __init__(self, precedence=3):
        super().__init__(precedence)

    def operation(self, first_operand, second_operand):
        try:
            return math.pow(first_operand, second_operand)
        except ArithmeticError as e:
            raise ArithmeticError(f"Error ||  {e} - sorry, please try a smaller number :/")
