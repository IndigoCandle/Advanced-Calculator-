from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Plus(TwoCharOps):
    def __init__(self, kdimut=1):
        super().__init__(kdimut)

    def operation(self, first_operand, second_operand):
        return first_operand + second_operand
