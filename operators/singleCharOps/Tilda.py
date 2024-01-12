from operators.singleCharOps.singleCharOps import SingleCharOps


class Tilda(SingleCharOps):
    def kdimut(self):
        return 6

    def operation(self, operand):
        return -1 * operand

    def position(self):
        return "Left"
