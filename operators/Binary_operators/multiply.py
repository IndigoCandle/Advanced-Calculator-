from operators.Binary_operators.TwoCharOps import TwoCharOps


class Mul(TwoCharOps):
    def __init__(self, precedence=2):
        super().__init__(precedence)

    def kdimut(self):
        return 2

    def operation(self, first_operand, second_operand):
        return first_operand * second_operand
