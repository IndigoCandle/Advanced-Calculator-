from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Avg(TwoCharOps):
    def __init__(self, precedence=5):
        super().__init__(precedence)

    def operation(self, first_operand, second_operand):
        sum = first_operand + second_operand
        return sum / 2

