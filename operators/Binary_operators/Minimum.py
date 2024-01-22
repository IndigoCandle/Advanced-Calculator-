from operators.Binary_operators.TwoCharOps import TwoCharOps


class Min(TwoCharOps):
    def __init__(self, precedence=5):
        super().__init__(precedence)

    def operation(self, first_operand, second_operand):
        """
            return the smaller operand out of first operand, second operand
        """
        if first_operand < second_operand:
            return first_operand
        return second_operand
