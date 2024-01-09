from operators.TwoCharOps.TwoCharOps import TwoCharOps


class Max(TwoCharOps):
    def kdimut(self):
        return 5

    def operation(self, first_operand, second_operand):
        if first_operand > second_operand:
            return first_operand
        return second_operand
