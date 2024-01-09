from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Div(TwoCharOps):
    def kdimut(self):
        return 2

    def operation(self, first_operand, second_operand):
        return first_operand / second_operand
