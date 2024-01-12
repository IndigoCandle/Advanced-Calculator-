from operators import operatorFactory
from operators.operatorFactory import OperatorCreator

factory = OperatorCreator()


def check_kdimut(operand):
    dict_kdimut = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, "~": 6, "!": 6}
    return dict_kdimut[str(operand)]


def convert_str_to_lst(expression: str):
    operators = {'+', '-', '*', '/', '(', ')', '^', '%', '@', '$', '&', '~', '!'}
    output = []
    temp_string = ''
    counter = -1
    while counter < len(expression) - 1:
        temp_string = ''
        if counter >= len(expression) - 1:
            break
        counter += 1
        character = expression[counter]
        if counter == len(expression) - 1:
            output.append(float(character))
            break
        while counter < len(expression) and expression[counter] not in operators:
            temp_string += expression[counter]
            counter += 1

        if temp_string != '':
            output.append(float(temp_string))
        if counter < len(expression):
            character = expression[counter]
            output.append(character)

    return output


def handle_minus(expression_array: list):
    counter = 0
    temp_expression_array = expression_array
    while counter < len(temp_expression_array) - 1:
        minus_counter = 0
        while temp_expression_array[counter] == '-':
            temp_expression_array.pop(counter)
            minus_counter += 1
        if minus_counter > 0:
            if minus_counter % 2 == 0:
                temp_expression_array.insert(counter, '+')
            else:
                temp_expression_array.insert(counter, '-')
        counter += 1
    return temp_expression_array


def handle_operators(expression):
    pos = 0
    operators = {'+', '-', '*', '/', '(', ')', '^', '%', '@', '$', '&', '~', '!'}
    while pos < len(expression) - 1:
        if expression[pos] in operators:
            if expression[pos + 1] == '-':
                expression[pos + 2] *= -1
                expression.pop(pos + 1)
            elif expression[pos + 1] == '+':
                expression.pop(pos + 1)
        pos += 1


def calculate(expression_lst: list):
    sub_expression = ''
    send_temp_expression = []
    result_expression = []
    pos = 0
    found_bracket = False
    stack = []
    while pos < len(expression_lst):
        if expression_lst[pos] == '(':
            while expression_lst[pos] != ')':
                stack.append(expression_lst[pos])
                pos += 1
                if pos == len(expression_lst) and not stack:
                    raise SyntaxError("too many (, not enough )")
            while len(stack) >= 1 and pos < len(expression_lst):
                while not found_bracket and stack:
                    item_to_insert = stack.pop(-1)
                    if item_to_insert == '(':
                        found_bracket = True
                    else:
                        send_temp_expression.insert(0, item_to_insert)
                if not found_bracket:
                    raise SyntaxError("too many ), not enough (")
                stack.append((calculator2(send_temp_expression)).pop())
                found_bracket = False
                send_temp_expression = []
        if expression_lst[pos] != ')':
            result_expression.append(expression_lst[pos])
        pos += 1

    result_expression.append(stack.pop())
    return result_expression


def calculator2(revised_list: list):
    operator_list_for_kdimut = factory.operator_list()
    curr_operator_list = []
    for element in revised_list:
        if element in operator_list_for_kdimut:
            if element not in curr_operator_list:
                curr_operator_list.append(element)
    i = 0
    while i < len(operator_list_for_kdimut):
        if operator_list_for_kdimut[i] not in curr_operator_list:
            operator_list_for_kdimut.remove(operator_list_for_kdimut[i])
            i -= 1
        i += 1

    for i in range(len(operator_list_for_kdimut)):
        pos = 0
        kdimut = OperatorCreator.operator_factory(factory, operator_list_for_kdimut[-1]).kdimut()

        while pos < len(revised_list):
            if revised_list[pos] in operator_list_for_kdimut:
                try:
                    operator = OperatorCreator.operator_factory(factory, revised_list[pos])
                except ValueError as e:
                    raise SyntaxError(f"expression is illegal: {e}")
                curr_kdimut = operator.kdimut()
                if curr_kdimut == kdimut:
                    if operator.position() == "Center":
                        result = operator.operation(revised_list[pos - 1], revised_list[pos + 1])
                        for j in range(3):
                            revised_list.pop(pos - 1)

                    elif operator.position() == "Right":
                        result = operator.operation(revised_list[pos - 1])
                        for j in range(2):
                            revised_list.pop(pos - 1)
                    elif operator.position() == "Left":
                        find_next_operand = pos + 1
                        while isinstance(revised_list[find_next_operand], float):
                            find_next_operand += 1
                        result = operator.operation(revised_list[find_next_operand])
                        revised_list.insert(pos, result)
                    else:
                        raise SyntaxError("Operator doesn't have a position")
                    revised_list.append(result)
            pos += 1
        operator_list_for_kdimut.pop(-1)
    return revised_list


def calculator(revised_list: list):
    dict_kdimut = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, "~": 6, "!": 6}
    operands = {"+", "*", "/", "^", "%", "@", "$", "&", "~", "!", "-"}
    kdimut = 6

    for i in range(6):

        for z in range(3):
            pos = 0
            while pos < len(revised_list):
                if revised_list[pos] in operands:
                    try:
                        operator = OperatorCreator.operator_factory(factory, revised_list[pos])
                    except ValueError as e:
                        raise SyntaxError(f"expression is illegal: {e}")
                    if operator.kdimut == kdimut:
                        result = all_operations(revised_list[pos - 1], revised_list[pos], revised_list[pos + 1])
                        for j in range(3):
                            revised_list.pop(pos - 1)

                        revised_list.insert(pos - 1, result)
                pos += 1
        kdimut -= 1
    final_result = revised_list[0]
    if final_result - int(final_result) == 0:
        final_result = int(final_result)
    return final_result


def all_operations(first_obj, operator, second_obj):
    match operator:
        case '+':
            return first_obj + second_obj
        case '-':
            return first_obj - second_obj
        case '*':
            return first_obj * second_obj
        case '/':
            return first_obj / second_obj
        case '@':
            return (first_obj + second_obj) / 2
        case '^':
            return first_obj ** second_obj
        case '$':
            return max(first_obj, second_obj)
        case '&':
            return min(first_obj, second_obj)
        case '%':
            return first_obj % second_obj
        case _:
            raise TypeError(f"{operator} is and invalid operand")


print(calculate([2, '*', '(', '(', 5, '+', 5, ')', '-', 5, ')']))
calculator2([2, '*', 3, '-', 5, '!'])

data = convert_str_to_lst("4 / 2 + 1")
print(data)
data = handle_minus(data)
print(data)
handle_operators(data)
print(data)
print(calculator(data))
