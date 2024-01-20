from operators.single_operand_operators.Minus.Unari import UnariMinus
from operators.single_operand_operators.singleCharOps import SingleCharOps


class SignMinus(UnariMinus):

    def __init__(self, precedence=7):
        super().__init__(precedence)


