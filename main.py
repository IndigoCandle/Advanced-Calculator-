from operators.operatorFactory import OperatorCreator

factory = OperatorCreator()


def convert_str_to_lst(expression: str):
    operators = factory.operator_list()
    output = []
    counter = -1
    while counter < len(expression) - 1:
        temp_string = ''
        if counter < len(expression) - 1:
            counter += 1
            character = expression[counter]

            while (counter < len(expression) and expression[counter] not in operators
                   and expression[counter] != ')' and expression[counter] != '('):
                if expression[counter] != ' ' and expression[counter] != '.':
                    try:
                        check = float(expression[counter])
                    except ValueError:

                        raise SyntaxError(f"could not convert {expression[counter]} to float - Illegal operator")
                temp_string += expression[counter]
                counter += 1

            if temp_string != '' and temp_string != ' ':
                try:
                    output.append(float(temp_string))
                except ValueError as e:
                    raise SyntaxError(f"too many dots: {e}")
            if counter < len(expression):
                character = expression[counter]
                output.append(character)
            else:
                if character != '' and character != ' ' and character != temp_string:
                    output.append(float(character))
                break
    return output


def handle_minus(expression_array: list):
    counter = 0
    temp_expression_array = expression_array
    if expression_array[counter] == '-':
        minus_counter = 0
        while temp_expression_array[counter] == '-':
            temp_expression_array.pop(counter)
            minus_counter += 1
        if minus_counter > 0:
            if minus_counter % 2 == 0:
                counter -= 1
            else:
                temp_expression_array.insert(0, '_')

    while counter < len(temp_expression_array) - 1:
        minus_counter = 0
        while temp_expression_array[counter] == '-':
            temp_expression_array.pop(counter)
            minus_counter += 1
        if minus_counter > 0:
            if minus_counter % 2 == 0:
                if temp_expression_array[counter - 1] not in factory.operators and minus_counter != 2:
                    temp_expression_array.insert(counter, '+')
                elif not temp_expression_array[counter - 1] in factory.operators:
                    temp_expression_array.insert(counter, '---')

            else:

                if (temp_expression_array[counter - 1] in factory.operators and
                        OperatorCreator.operator_factory(factory,
                                                         temp_expression_array[counter - 1]).position() != "Right"):
                    try:
                        temp_expression_array.insert(counter, '---')
                    except ArithmeticError as e:
                        raise SyntaxError(f"incorrect operator format: {e}")
                else:
                    temp_expression_array.insert(counter, '-')
        counter += 1
    return temp_expression_array


def bracket_handler(expression_lst: list) -> list:
    send_temp_expression = []
    result_expression = []
    pos = 0
    found_bracket = False
    stack = []
    while pos < len(expression_lst):
        if expression_lst[pos] == '(':
            while pos < len(expression_lst) - 1:
                if expression_lst[pos] != ')':
                    stack.append(expression_lst[pos])
                pos += 1
                if pos == len(expression_lst) and not stack:
                    raise SyntaxError("too many (, not enough )")
                if expression_lst[pos] == ')':
                    while not found_bracket and stack:
                        item_to_insert = stack.pop(-1)
                        if item_to_insert == '(':
                            found_bracket = True
                        else:
                            send_temp_expression.insert(0, item_to_insert)
                    if not found_bracket:
                        raise SyntaxError("too many ), not enough (")
                    try:
                        stack.append((calculator2(send_temp_expression)).pop())
                    except IndexError:
                        raise SyntaxError(f"Brackets can't be empty: {expression_lst}")
                    found_bracket = False
                    send_temp_expression = []
                    if '(' not in stack:
                        result_expression.append(stack.pop())
                        break
        #        if expression_lst[pos] == ')' and not found_bracket: SyntaxError("too many ), not enough (")
        if expression_lst[pos] != ')':
            result_expression.append(expression_lst[pos])
        pos += 1
    if stack:
        raise SyntaxError("too many (, not enough )")
    return result_expression


def calculator2(revised_list: list) -> list:
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
                        try:
                            result = operator.operation(revised_list[pos - 1], revised_list[pos + 1])
                        except ArithmeticError as e:
                            raise ArithmeticError(e)
                        except IndexError:
                            raise SyntaxError(f"insufficient operands {revised_list}")
                        for j in range(3):
                            revised_list.pop(pos - 1)
                        revised_list.insert(pos - 1, result)
                    elif operator.position() == "Right":
                        try:
                            result = operator.operation(revised_list[pos - 1])
                        except ValueError as e:
                            raise SyntaxError(f"Error - {e}")
                        for j in range(2):
                            revised_list.pop(pos - 1)
                        revised_list.insert(pos - 1, result)
                    elif operator.position() == "Left":
                        find_next_operand = pos + 1
                        while (not isinstance(revised_list[find_next_operand], float) and not
                        isinstance(revised_list[find_next_operand], int) and
                               find_next_operand < len(revised_list)):
                            find_next_operand += 1
                        result = operator.operation(revised_list[find_next_operand])
                        revised_list.pop(pos)
                        revised_list.pop(pos)
                        revised_list.insert(pos, result)
                    else:
                        raise SyntaxError("Operator doesn't have a position")

                    pos -= 1
            pos += 1
        operator_list_for_kdimut.pop(-1)
    return revised_list

try:
    data = "3!-4"
    print(data)
    data = convert_str_to_lst(data)
    print(data)
    data = handle_minus(data)
    print(data)
    data = bracket_handler(data)
    print(data)
    print(calculator2(data).pop(0))
except Exception as e:
    print(e)
