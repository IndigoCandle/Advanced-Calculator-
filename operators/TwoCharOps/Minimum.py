from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Min(TwoCharOps):
    def __init__(self, precedence=5):
        super().__init__(precedence)

    def operation(self, first_operand, second_operand):
        if first_operand < second_operand:
            return first_operand
        return second_operand
