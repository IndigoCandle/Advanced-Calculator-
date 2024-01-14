
from operators.singleCharOps.singleCharOps import SingleCharOps


class SignMinus(SingleCharOps):
    def kdimut(self):
        return 7

    def operation(self, operand):
        return -1 * operand

    def position(self):
        return "Left"
