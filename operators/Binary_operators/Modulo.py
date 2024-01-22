from operators.Binary_operators.TwoCharOps import TwoCharOps


class Mod(TwoCharOps):
    def __init__(self, precedence=4):
        super().__init__(precedence)

    def operation(self, first_operand, second_operand):
        """
            return first operand modulo second operand
        """
        return first_operand % second_operand
