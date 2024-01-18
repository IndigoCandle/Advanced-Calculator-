from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Div(TwoCharOps):
    def __init__(self, kdimut=2):
        super().__init__(kdimut)

    def operation(self, first_operand, second_operand):
        if second_operand == 0:
            raise ZeroDivisionError(f"division by zero {first_operand}/{second_operand}")
        return first_operand / second_operand
