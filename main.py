def check_kdimut(operand):
    dict_kdimut = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, "~": 6, "!": 6}
    return dict_kdimut[str(operand)]


def convert_str_to_lst(expression: str):
    operators = {'+', '-', '*', '/', '(', ')', '^', '%', '@', '$', '&', '~', '!'}
    output = []
    temp_string = ''
    counter = -1
    while counter < len(expression)-1:
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


def calculator(operation: str):
    operands = {"+", "*", "/", "^", "%", "@", "$", "&", "~", "!", "-"}
    for operand in operands:
        operation_lst = operation

    return operation_lst


print(convert_str_to_lst("59+33*9"))
