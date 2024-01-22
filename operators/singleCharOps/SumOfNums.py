from operators.singleCharOps.singleCharOps import SingleCharOps


class SumOfNum(SingleCharOps):

    def kdimut(self):
        return 6

    def operation(self, operand: float) -> int:
        str_operand = str(operand)
        final_sum = 0
        for num in str_operand:
            if num != '.':
                final_sum += int(num)
        return final_sum

    def position(self):
        return "Right"