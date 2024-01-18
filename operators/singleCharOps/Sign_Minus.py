from operators.singleCharOps.singleCharOps import SingleCharOps


class SignMinus(SingleCharOps):

    def __init__(self, kdimut=7, position="Left", can_dup=True):
        super().__init__(kdimut, position, can_dup)
    def operation(self, operand):
        return -1 * operand
