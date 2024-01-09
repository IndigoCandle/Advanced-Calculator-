from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Mod(TwoCharOps):
    def kdimut(self):
        return 4

    def operation(self, first_operand, second_operand):
        return first_operand % second_operand
