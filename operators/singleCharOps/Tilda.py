from operators.singleCharOps.singleCharOps import SingleCharOps


class Tilda(SingleCharOps):
    def __init__(self, kdimut=6, position="Left", can_dup=False):
        super().__init__(kdimut, position, can_dup)
    def operation(self, operand):
        return -1 * operand

