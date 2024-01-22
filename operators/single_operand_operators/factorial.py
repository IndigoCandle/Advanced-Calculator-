from operators.single_operand_operators.singleCharOps import SingleCharOps


class Factorial(SingleCharOps):
    def __init__(self, precedence=6, position="Right", can_dup=True):

        super().__init__(precedence, position, can_dup)

    def operation(self, operand):
        """
        returns the factorial of operand
        :raises ValueError: ! does not support operations on negative numbers
        :raises ValueError: ! does not support operations on float types
        """
        operand = round(operand, 10)
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
