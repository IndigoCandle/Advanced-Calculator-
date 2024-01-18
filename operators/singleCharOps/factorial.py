from operators.singleCharOps.singleCharOps import SingleCharOps


class Factorial(SingleCharOps):
    def __init__(self, kdimut=6, position="Right", can_dup=True):

        super().__init__(kdimut, position, can_dup)

    def kdimut(self):
        return 6

    def operation(self, operand):
        if operand - int(operand) == 0:
            operand = int(operand)
        if operand < 0:
            raise ValueError("! does not support operations on negative numbers")
        elif not isinstance(operand, int):
            raise ValueError("! does not support operations on float types")

        fact = 1
        for i in range(1, operand + 1):
            fact *= i
        return fact

    def position(self):
        return "Right"
