from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Mul(TwoCharOps):
    def kdimut(self):
        return 2

    def operation(self, first_operand, second_operand):
        return first_operand * second_operand
