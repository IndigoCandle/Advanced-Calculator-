from operators.operatorFactory import OperatorCreator

factory = OperatorCreator()


def convert(expression: str) -> list:
    if not expression:
        raise SyntaxError("expression can't be empty")
    duplicates = factory.dup_operators()
    bracket_counter = 0
    index = 0
    output = []
    curr_num = ''
    while index < len(expression) and expression[index] in ['\t', ' ']:
        index += 1
    if index == len(expression):
        raise SyntaxError("expression can't be empty")
    updated_expression = expression[index:len(expression)]
    for char in updated_expression:
        if char in factory.operators or (char in ['(', ')']):
            if curr_num not in ['\t', ' ', '']:
                output.append(float(curr_num))
                curr_num = ''
            if (output and char not in duplicates and char == output[-1] and
                    factory.operator_factory(char).position() != "Right"):
                raise SyntaxError(f"operator {char} is illegal in this sequence")
            output.append(char)
        else:
            curr_num += char
        if char == '(':
            bracket_counter += 1
        elif char == ')':
            bracket_counter -= 1
    if bracket_counter > 0:
        raise SyntaxError("Error - too many (")
    elif bracket_counter < 0:
        raise SyntaxError("Error - too many )")
    if curr_num != '':
        try:
            output.append(float(curr_num))
        except ValueError:
            return output
    return output


def run_for_element(expression: list, element: str, index: int):
    duplicate_counter = 0
    while expression[index] == element:
        expression.pop(index)
        duplicate_counter += 1
    if expression[index] in factory.operators and duplicate_counter > 1:
        raise SyntaxError(
            f"there can't be multiple recurrences of {element} before another operator: {expression[index]}")
    return duplicate_counter


def handle_minus(expression_array: list):
    if not expression_array:
        raise SyntaxError("input must contain an expression")
    duplicate_operators = factory.dup_operators()
    counter = 0
    temp_expression_array = expression_array
    cur_element = expression_array[counter]
    if cur_element in duplicate_operators:
        duplicate_counter = run_for_element(temp_expression_array, cur_element, counter)

        if duplicate_counter > 0:
            if duplicate_counter % 2 == 0:
                counter -= 1
            else:
                temp_expression_array.insert(0, duplicate_operators.get(cur_element)[0])

    while counter < len(temp_expression_array) - 1:
        duplicate_counter = 0
        if temp_expression_array[counter] in duplicate_operators:
            cur_element = temp_expression_array[counter]
            duplicate_counter = run_for_element(temp_expression_array, cur_element, counter)
            if duplicate_counter > 0:
                if duplicate_counter % 2 == 0:
                    if temp_expression_array[counter - 1] != '(':
                        if temp_expression_array[counter - 1] not in factory.operators:
                            temp_expression_array.insert(counter, duplicate_operators.get(cur_element)[1])
                            temp_expression_array.insert(counter, cur_element)
                else:

                    if (temp_expression_array[counter - 1] in factory.operators and
                            OperatorCreator.operator_factory(factory,
                                                             temp_expression_array[counter - 1]).position() != "Right"):
                        try:
                            temp_expression_array.insert(counter, duplicate_operators.get(cur_element)[1])
                        except ArithmeticError as e:
                            raise SyntaxError(f"incorrect operator format: {e}")
                    elif temp_expression_array[counter - 1] == '(':
                        temp_expression_array.insert(counter, duplicate_operators.get(cur_element)[0])
                    else:
                        temp_expression_array.insert(counter, cur_element)
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

                if expression_lst[pos] == ')':
                    while not found_bracket and stack:
                        item_to_insert = stack.pop(-1)
                        if item_to_insert == '(':
                            found_bracket = True
                        else:
                            send_temp_expression.insert(0, item_to_insert)
                    try:
                        stack.append((calculate(send_temp_expression)).pop())
                    except IndexError:
                        raise SyntaxError(f"Brackets can't be empty-> index {pos - 1} to {pos}")
                    found_bracket = False
                    send_temp_expression = []
                    if '(' not in stack:
                        result_expression.append(stack.pop())
                        break
        #        if expression_lst[pos] == ')' and not found_bracket: SyntaxError("too many ), not enough (")
        if expression_lst[pos] != ')':
            result_expression.append(expression_lst[pos])
        pos += 1
    return result_expression


def calculate(revised_list: list) -> list:
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
                        if pos == 0:
                            raise SyntaxError(f"Syntax Error: {revised_list[pos]} can't be at index {pos}")
                        try:
                            result = operator.operation(revised_list[pos - 1], revised_list[pos + 1])
                        except (ArithmeticError, TypeError) as e:
                            raise ArithmeticError(e)
                        except IndexError:
                            raise SyntaxError(f"insufficient operands {revised_list}")
                        try:
                            for j in range(3):
                                revised_list.pop(pos - 1)
                        except IndexError:
                            raise SyntaxError(f"insufficient operands {revised_list}")
                        revised_list.insert(pos - 1, result)
                    elif operator.position() == "Right":
                        if pos - 1 < 0:
                            raise SyntaxError(f"Operator {revised_list[pos]} is misplaced")
                        try:
                            result = operator.operation(revised_list[pos - 1])
                        except ValueError as e:
                            raise SyntaxError(f"Error - {e}")
                        for j in range(2):
                            revised_list.pop(pos - 1)
                        revised_list.insert(pos - 1, result)
                    elif operator.position() == "Left":
                        if pos + 1 >= len(revised_list):
                            raise SyntaxError(f"{revised_list[pos]} is misplaced")
                        find_next_operand = pos + 1
                        while (not isinstance(revised_list[find_next_operand], float) and not
                        isinstance(revised_list[find_next_operand], int) and
                               find_next_operand < len(revised_list) - 1):
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
    if len(revised_list) > 1:
        raise SyntaxError(f"{revised_list[1]} out of place")
    return revised_list


def main():
    while True:
        try:
            expression = input("Enter and expression:")
        except EOFError:
            print("Please dont press ctrl+d :)")
            break
        except KeyboardInterrupt:
            print("Please dont interrupt the process :(")
            break
        try:
            expression = convert(expression)
            expression = handle_minus(expression)
            expression = bracket_handler(expression)
            print(f"Result: {calculate(expression).pop(0)}")
            if input("Do another calculation? (yes/no): ").lower() != 'yes':
                break
        except (SyntaxError, ValueError, IndexError, ArithmeticError, EOFError, KeyboardInterrupt) as e:
            print(e)
            break


if __name__ == "__main__":
    main()
