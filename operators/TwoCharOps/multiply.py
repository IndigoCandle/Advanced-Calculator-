from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Mul(TwoCharOps):
    def __init__(self, kdimut=2):
        super().__init__(kdimut)

    def kdimut(self):
        return 2

    def operation(self, first_operand, second_operand):
        return first_operand * second_operand
