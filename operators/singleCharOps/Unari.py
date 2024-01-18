from operators.singleCharOps.singleCharOps import SingleCharOps


class UnariMinus(SingleCharOps):
    def __init__(self, kdimut=2.5, position="Left", can_dup=True):
        super().__init__(kdimut, position, can_dup)

    def operation(self, operand):
        return -1 * operand
