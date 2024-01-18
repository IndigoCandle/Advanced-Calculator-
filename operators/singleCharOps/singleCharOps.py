from operators.operators import Operators


class SingleCharOps(Operators):
    def __init__(self, kdimut, position, can_dup):
        super().__init__(kdimut, position)
        self.can_dup = can_dup
    def operation(self, operand):
        pass
