from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Minus(TwoCharOps):
    def __init__(self):
        super().__init__(1)

    def operation(self, first_operand, second_operand):
        return first_operand - second_operand
