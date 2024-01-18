import math

from operators.TwoCharOps.TwoCharOps import TwoCharOps


class pow(TwoCharOps):
    def __init__(self, kdimut=3):
        super().__init__(kdimut)

    def operation(self, first_operand, second_operand):
        try:
            return math.pow(first_operand, second_operand)
        except ArithmeticError as e:
            raise ArithmeticError(f"Error ||  {e} - sorry, please try a smaller number :/")
