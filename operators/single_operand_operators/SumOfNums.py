from Calculator.Exceptions import InvalidOutput
from operators.single_operand_operators.singleCharOps import SingleCharOps


class SumOfNum(SingleCharOps):
    def __init__(self, precedence=6, position="Right", can_dup=True):

        super().__init__(precedence, position, can_dup)

    def operation(self, operand: float) -> int:
        """
        operator # only operates until the letter e. calculates the sum of all digits.

        :param operand: number to operate on.
        :raises InvalidOutput: # can't operate on negative numbers
        :return:sum of all digits
        """
        if operand < 0:
            raise InvalidOutput("# can't operate on negative numbers")
        operand_str = str(operand)
        final_sum = 0
        e_found = False
        for num in operand_str:
            if not e_found:
                if num == 'e':
                    e_found = True
                else:
                    if num != '.':
                        final_sum += int(num)
        return final_sum
