from operators.TwoCharOps.power import pow
from operators.TwoCharOps.Modulo import Mod
from operators.TwoCharOps.Maximum import Max
from operators.TwoCharOps.Minimum import Min
from operators.TwoCharOps.Minus.minus import Minus
from operators.TwoCharOps.average import Avg
from operators.TwoCharOps.divide import Div
from operators.TwoCharOps.multiply import Mul
from operators.TwoCharOps.plus import Plus
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
                 "_": UnariMinus,
                 "---": SignMinus}

    @staticmethod
    def operator_list():
        operators = ['+', '-', '*', '/', '_', '^', '%', '@', '$', '&', '~', '!', '#', '---']
        return operators

    def operator_factory(self, operator: str):
        operator_class = self.operators.get(operator)
        if operator_class:
            return operator_class()
        else:
            raise ValueError(f"Unknown operator type: {operator_class}")
