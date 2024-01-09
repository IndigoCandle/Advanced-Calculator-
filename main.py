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
    prethesis_handler = []
    pos = 0

    while pos < len(expression_lst):
        if expression_lst[pos] == '(':
            prethesis_handler.append(expression_lst[pos])


def calculator(revised_list: list):
    dict_kdimut = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, "~": 6, "!": 6}
    operands = {"+", "*", "/", "^", "%", "@", "$", "&", "~", "!", "-"}
    kdimut = 6

    for i in range(6):

        for z in range(3):
            pos = 0
            while pos < len(revised_list):
                if revised_list[pos] in operands:
                    if dict_kdimut[revised_list[pos]] == kdimut:
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


data = convert_str_to_lst("2.3*----------------------------3*5+0.5")
print(data)
data = handle_minus(data)
print(data)
handle_operators(data)
print(data)
print(calculator(data))
