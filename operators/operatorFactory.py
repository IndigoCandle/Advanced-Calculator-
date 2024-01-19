from operators.TwoCharOps.power import pow
from operators.TwoCharOps.Modulo import Mod
from operators.TwoCharOps.Maximum import Max
from operators.TwoCharOps.Minimum import Min
from operators.TwoCharOps.Minus.minus import Minus
from operators.TwoCharOps.average import Avg
from operators.TwoCharOps.divide import Div
from operators.TwoCharOps.multiply import Mul
from operators.TwoCharOps.plus import Plus
from operators.singleCharOps.SumOfNums import SumOfNum
from operators.singleCharOps.Unari import UnariMinus
from operators.singleCharOps.Tilda import Tilda
from operators.singleCharOps.factorial import Factorial
from operators.singleCharOps.Sign_Minus import SignMinus


class OperatorCreator:
    operators = {"+": Plus,
                 "*": Mul,
                 "/": Div,
                 "^": pow,
                 "%": Mod,
                 "@": Avg,
                 "$": Max,
                 "&": Min,
                 "~": Tilda,
                 "!": Factorial,
                 "-": Minus,
                 "#": SumOfNum,
                 "UNARY_MINUS": UnariMinus,
                 "SIGN_MINUS": SignMinus}

    @staticmethod
    def operator_list():
        operators = ['+', '-', '*', '/', 'UNARY_MINUS', '^', '%', '@', '$', '&', '~', '!', '#', 'SIGN_MINUS']
        return operators

    @staticmethod
    def dup_operators():
        """
        returns a dictionary of each duplicatable operator - allows to add more duplicatable and unary operators.
        special operators must be implemented!
        duplicate_operators:
            key - the operator
            list value:
                [0] - unary version
                [1] - sign version
        :return:
            dictionary of duplicate list
        """
        duplicate_operators = {'-': ['UNARY_MINUS', 'SIGN_MINUS']}
        return duplicate_operators

    def operator_factory(self, operator: str):
        """
        finds and creates a class matching "operator"
        :param operator: a string of an operator
        :return: instance of class operator
        """
        operator_class = self.operators.get(operator)
        if operator_class:
            return operator_class()
        else:
            raise ValueError(f"Unknown operator type: {operator_class}")
