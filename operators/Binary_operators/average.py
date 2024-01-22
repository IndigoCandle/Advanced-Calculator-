from operators.Binary_operators.TwoCharOps import TwoCharOps


class Avg(TwoCharOps):
    def __init__(self, precedence=5):
        super().__init__(precedence)

    def operation(self, first_operand, second_operand):
        """
        return average of two operands
        """
        sum_together = first_operand + second_operand
        return sum_together / 2

