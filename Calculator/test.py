import pytest

from Calculator.Exceptions import *
from Calculator.calculator import *


# Testing valid expressions
@pytest.mark.parametrize("expression, expected_result", [
    # simple expressions
    ("-2^2", -4),
    ("2---3!", -4),
    ("3+~-3", 6),
    ("3+3*3", 12),
    ("10 @ 20", 15),
    ("100 % 2", 0),
    ("20 & 10", 10),
    ("1/0", "division by zero"),
    ("2--3!", "Illegal operation"),
    ("-~3", "invalid expression"),
    ("(5-2)*3!", 18),
    ("120   -   (5)!+1", 1),
    ("6 3+2", "Caught"),
    ("2.3^2", 5.29),
    ("", "empty"),
    ("(-1)^0.5", "non real number"),
    ("(100^100)#", 1),
    ("8!!", "inf"),


    # complex expressions
    ("70 + 3.4@5 - 7 --3", 70.2),
    ("-7^2 + 5!--9%3+4@9", 77.5),
    ("100%3     -7*(-9^(2+1)!)-7", 3720081),
    ("4!--3+    2*(1.1)########", 31),
    ("~--(((-(-3-(45612^2.5)+4@6)---615#)$534%12)---803#+18!@12)", -3201186852863999.5),
    ("(83^3)&0@(52.7221%10)@2-(42^3!)&0@2-(87##!+30)", -749.319475),
    ("((((((((~-3!!^~-3!)#/5) ^ 100)#!#) + ~-(5&2$4)!#)%7 / 10 ) ^ 2 * 1000) % 3)! + ~-------((((((((~-3!!^~-3!)#/5) "
     "^ 100)#!#) + ~-(5&2$4)!#)%7 / 10 ) ^ 2 * 1000) %  3)!", 2),
    ("52!/83^(4@5+65)-12&(7-3--8.5)", -12),
    ("70 * 9 +(3%3)!!!!!!!!-70000 $94", -69369),
    ("20 - (5 * (3 + 2.5))", -7.5),
    ("(10!%9!--3*(70*(3-4.12)))^2", 55319.04),
    ("(50.232323+5%4) $ 70 ---9^2!+-4*(4@5)", -29),
    ("262.67851073127395*262.67851073127395 + 0.34035656401944897*1234", 69420),
    ("(420^69)#!#--3 $ (4 @ 9 & 84.78 + 2)", 72.5),
    ("3 ^ 2 ! - 5 * (4 $ 2)! * 2 + 7 @ 9 @ 11", -221.5),
    ("((12.5 + 34.7) / (56 - 45)) ^ 2 - 4 $ 5 $ 6", 12.4119008264),
    ("10000 % 1000 % 100 % 50 % 25 + 10!-7 ", 3628793),
    ("(20 - 3) * (2 ^ 3) + 1 + 5.5 @ 6.5", 143),
    ("(9^100)### & (-6040.7893- 9!) +30.39485--24572.43242 ", -344317.96203),
    ("((4 + 5) * (6 - 3) ^ 2 / 3) @ 5.5 @ 7.5", 11.875),
    ("3 ----- 4 + ~10 & 20 & ~30 - 2.5", -33.5),



])
def test_valid_expressions(expression, expected_result):
    try:
        assert (Calculator(expression)).result == expected_result
    except SyntaxError:
        print("invalid expression")
    except ZeroDivisionError:
        print("division by zero")
    except OverflowError:
        print("inf")
    except ArithmeticError:
        print("Illegal operation")
    except EmptyExpression:
        print("empty")
    except InvalidOutput:
        print("non real number")


