from operators.Binary_operators.TwoCharOps import TwoCharOps


class Mul(TwoCharOps):
    def __init__(self, precedence=2):
        super().__init__(precedence)

    def operation(self, first_operand, second_operand):
        """
            return first operand times second operand
        """
        return first_operand * second_operand
