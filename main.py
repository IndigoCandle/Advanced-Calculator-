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
            output.append(character)
            break
        while counter < len(expression) and expression[counter] not in operators:
            temp_string += expression[counter]
            counter += 1

        if temp_string != '':
            output.append(temp_string)
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


def calculator(revised_list: list):
    dict_kdimut = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, "~": 6, "!": 6}
    operands = {"+", "*", "/", "^", "%", "@", "$", "&", "~", "!", "-"}
    output = []

    for operand in revised_list:
        operation_lst = operation

    return operation_lst


data = convert_str_to_lst("59+33-----97")
print(data)
print(handle_minus(data))
