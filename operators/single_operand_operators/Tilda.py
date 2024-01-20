from operators.single_operand_operators.singleCharOps import SingleCharOps


class Tilda(SingleCharOps):
    def __init__(self, precedence=6, position="Left", can_dup=False):
        super().__init__(precedence, position, can_dup)

    def operation(self, operand):
        return -1 * operand
