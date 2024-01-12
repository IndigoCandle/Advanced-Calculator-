from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Avg(TwoCharOps):
    def kdimut(self):
        return 5

    def operation(self, first_operand, second_operand):
        sum = first_operand + second_operand
        return sum / 2

