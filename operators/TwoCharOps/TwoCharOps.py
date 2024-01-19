from operators.operators import Operators


class TwoCharOps(Operators):
    def __init__(self, precedence):
        super().__init__(precedence, "Center")

    def operation(self, first_operand, second_operand):
        pass

