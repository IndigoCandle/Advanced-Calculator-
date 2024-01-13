
from operators.singleCharOps.singleCharOps import SingleCharOps


class UnariMinus(SingleCharOps):
    def kdimut(self):
        return 2.5

    def operation(self, operand):
        return -1 * operand

    def position(self):
        return "Left"
