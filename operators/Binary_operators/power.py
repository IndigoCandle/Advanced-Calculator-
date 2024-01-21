import math

from Calculator.Exceptions import InvalidOutput
from operators.Binary_operators.TwoCharOps import TwoCharOps


class pow(TwoCharOps):
    def __init__(self, precedence=3):
        super().__init__(precedence)

    def operation(self, first_operand, second_operand):
        try:
            return math.pow(first_operand, second_operand)
        except ArithmeticError as e:
            raise InvalidOutput(f"Error ||  {e} - sorry, please try a smaller number :/")
        except ValueError:
            raise InvalidOutput(f"This calculator doesnt support imaginary numbers 😅")
