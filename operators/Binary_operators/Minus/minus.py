from operators.Binary_operators.TwoCharOps import TwoCharOps


class Minus(TwoCharOps):
    def __init__(self):
        super().__init__(1)

    def operation(self, first_operand, second_operand):
        """
        return first operand minus second operand
        """
        return first_operand - second_operand
