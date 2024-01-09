from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Minus(TwoCharOps):
    def kdimut(self):
        return 1

    def operation(self, first_operand, second_operand):
        return first_operand - second_operand
