from operators.singleCharOps.singleCharOps import SingleCharOps


class Factorial(SingleCharOps):
    def operation(self, operand):
        fact = 1
        for i in range(1, operand + 1):
            fact *= i
        return fact
