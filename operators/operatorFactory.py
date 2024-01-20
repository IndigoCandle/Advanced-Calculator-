from operators.Binary_operators.power import pow
from operators.Binary_operators.Modulo import Mod
from operators.Binary_operators.Maximum import Max
from operators.Binary_operators.Minimum import Min
from operators.Binary_operators.Minus.minus import Minus
from operators.Binary_operators.average import Avg
from operators.Binary_operators.divide import Div
from operators.Binary_operators.multiply import Mul
from operators.Binary_operators.plus import Plus
from operators.single_operand_operators.SumOfNums import SumOfNum
from operators.single_operand_operators.Minus.Unari import UnariMinus
from operators.single_operand_operators.Tilda import Tilda
from operators.single_operand_operators.factorial import Factorial
from operators.single_operand_operators.Minus.Sign_Minus import SignMinus


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
    operator_classes = {}

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
            if operator in self.operator_classes:
                return self.operator_classes.get(operator)
            curr_op_class = operator_class()
            self.operator_classes[operator] = curr_op_class
            return curr_op_class
        else:
            raise ValueError(f"Unknown operator type: {operator_class}")
