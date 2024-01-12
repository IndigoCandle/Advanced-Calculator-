operators = {'+', '-', '*', '/', '(', ')', '^', '%', '@', '$', '&', '~', '!', '#'}


def convert_str_to_lst(expression: str):
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
    while pos < len(expression) - 1:
        if expression[pos] in operators:
            if expression[pos + 1] == '-':
                expression[pos + 1] = '_'
            elif expression[pos + 1] == '+':
                expression.pop(pos + 1)
        pos += 1
"""
def calculate(expression_list: list) -> float:
    operand_stack = []
    operator_stack = []
    for element in expression_list:
        if isinstance(element, float):
            operand_stack.append(element)
        elif element in operators: """

data = convert_str_to_lst("4/---------------2!")
print(data)
data = handle_minus(data)
print(data)
handle_operators(data)
print(data)
