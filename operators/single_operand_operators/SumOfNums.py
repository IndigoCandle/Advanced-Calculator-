from operators.single_operand_operators.singleCharOps import SingleCharOps


class SumOfNum(SingleCharOps):
    def __init__(self, precedence=6, position="Right", can_dup=True):

        super().__init__(precedence, position, can_dup)
    def operation(self, operand: float) -> int:
        str_operand = str(operand)
        final_sum = 0
        for num in str_operand:
            if num != '.':
                final_sum += int(num)
        return final_sum
