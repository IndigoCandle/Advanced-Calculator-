from operators.operators import Operators


class TwoCharOps(Operators):
    def __init__(self, kdimut):
        super().__init__(kdimut, "Center")

    def operation(self, first_operand, second_operand):
        pass

