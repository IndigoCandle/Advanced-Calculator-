import math

from Calculator.Exceptions import InvalidOutput
from operators.Binary_operators.TwoCharOps import TwoCharOps


class pow(TwoCharOps):
    def __init__(self, precedence=3):
        super().__init__(precedence)

    def operation(self, first_operand, second_operand):
        """
        raises a first_operand by the power of second_operand.

        :raises InvalidOutput: number is too big or imaginary.
        """
        try:
            return math.pow(first_operand, second_operand)
        except ArithmeticError:
            raise InvalidOutput(f"inf")
        except ValueError:
            raise InvalidOutput(f"This calculator doesnt support imaginary numbers 😅")
