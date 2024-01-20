from operators.single_operand_operators.singleCharOps import SingleCharOps


class UnariMinus(SingleCharOps):
    def __init__(self, precedence=2.5, position="Left", can_dup=True):
        """
        Constructor for "Unari_Minus". represents the unari type of the "Minus" operator.
        """
        super().__init__(precedence, position, can_dup)

    def operation(self, operand):
        """
        reverses the sign of an operand sign(negative/positive)
        """
        return -1 * operand
