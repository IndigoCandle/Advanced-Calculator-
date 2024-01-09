from operators.TwoCharOps.TwoCharOps import TwoCharOps


class pow(TwoCharOps):
    def kdimut(self):
        return 3

    def operation(self, first_operand, second_operand):
        return first_operand ** second_operand
