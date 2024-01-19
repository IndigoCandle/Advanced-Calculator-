from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Plus(TwoCharOps):
    def __init__(self, precedence=1):
        super().__init__(precedence)

    def operation(self, first_operand, second_operand):
        return first_operand + second_operand
