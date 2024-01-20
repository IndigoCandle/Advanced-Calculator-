from operators.Binary_operators.TwoCharOps import TwoCharOps


class Div(TwoCharOps):
    def __init__(self, precedence=2):
        super().__init__(precedence)

    def operation(self, first_operand, second_operand):
        if second_operand == 0:
            raise ZeroDivisionError(f"division by zero {first_operand}/{second_operand}")
        return first_operand / second_operand
