from operators.singleCharOps.singleCharOps import SingleCharOps
from operators.operatorFactory import OperatorCreator

factory = OperatorCreator()


class Duplicate(SingleCharOps):

    duplicate_operators = {'-': ['_', '---', '+'],
                           '/': ['/', '=', '*']}


def convert_str_to_lst(expression: str):
    if not expression:
        raise SyntaxError("expression can't be empty")
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
                if expression[counter] != ' ' and expression[counter] != '.' and expression[counter] != '   ':
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
                    if float(character) != output[-1]:
                        output.append(float(character))
                break
    return output


def run_for_element(expression: list, element: str, index: int):
    duplicate_counter = 0
    while expression[index] == element:
        expression.pop(index)
        duplicate_counter += 1
    return duplicate_counter


def handle_minus(expression_array: list):
    if not expression_array:
        raise SyntaxError("input must contain an expression")
    counter = 0
    temp_expression_array = expression_array
    cur_element = expression_array[counter]
    if cur_element in Duplicate.duplicate_operators:
        duplicate_counter = run_for_element(temp_expression_array, cur_element, counter)
        if duplicate_counter > 0:
            if duplicate_counter % 2 == 0:
                counter -= 1
            else:
                temp_expression_array.insert(0, Duplicate.duplicate_operators.get(cur_element)[0])

    while counter < len(temp_expression_array) - 1:
        duplicate_counter = 0
        if temp_expression_array[counter] in Duplicate.duplicate_operators:
            cur_element = temp_expression_array[counter]
            duplicate_counter = run_for_element(temp_expression_array, cur_element, counter)
            if duplicate_counter > 0:
                if duplicate_counter % 2 == 0:
                    if temp_expression_array[counter - 1] != '(':
                        if temp_expression_array[counter - 1] not in factory.operators:
                            temp_expression_array.insert(counter, Duplicate.duplicate_operators.get(cur_element)[1])
                            temp_expression_array.insert(counter, cur_element)
                        else:
                            temp_expression_array.insert(counter, Duplicate.duplicate_operators.get(cur_element)[2])

                else:

                    if (temp_expression_array[counter - 1] in factory.operators and
                            OperatorCreator.operator_factory(factory,
                                                             temp_expression_array[counter - 1]).position() != "Right"):
                        try:
                            temp_expression_array.insert(counter, Duplicate.duplicate_operators.get(cur_element)[1])
                        except ArithmeticError as e:
                            raise SyntaxError(f"incorrect operator format: {e}")
                    elif temp_expression_array[counter - 1] == '(':
                        temp_expression_array.insert(counter, Duplicate.duplicate_operators.get(cur_element)[0])
                    else:
                        temp_expression_array.insert(counter, cur_element)
        counter += 1
    return temp_expression_array


data = "2+(///3!)"
data = convert_str_to_lst(data)
print(data)
data = handle_minus(data)
print(data)
