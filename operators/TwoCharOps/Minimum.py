from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Min(TwoCharOps):
    def __init__(self, kdimut=5):
        super().__init__(kdimut)

    def operation(self, first_operand, second_operand):
        if first_operand < second_operand:
            return first_operand
        return second_operand
