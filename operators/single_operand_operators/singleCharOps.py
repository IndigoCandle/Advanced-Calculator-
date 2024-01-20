from operators.operators import Operators


class SingleCharOps(Operators):
    def __init__(self, precedence, position, can_dup):
        """
        Base Class constructor of all operators operating on one operand.

        :param can_dup: boolean holding whether an operator can have multiple occurrences in a row.
        """
        super().__init__(precedence, position)
        self.can_dup = can_dup

    def operation(self, operand):
        """abstract method for performing all the operator operations. accepts one number.

        :param operand: number for the operation to be performed on.
        """
        pass
