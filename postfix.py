Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities of Operators


def infixToPostfix(expression_str: str):
    stack = []  # initialization of empty stack
    output = []
    temp_string = ''

    for i in range(len(expression_str)):
        temp_string = ''
        character = expression_str[i]
        while expression_str[i] not in Operators and i < len(expression_str):
            temp_string += expression_str[i]
            i += 1

        output.append(temp_string)

        character = expression_str[i]
        if character == '(':  # else Operators push onto stack

            stack.append('(')

        elif character == ')':

            while stack and stack[-1] != '(':
                output.append(stack.pop())

            stack.pop()

        else:

            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                output.append(stack.pop())

            stack.append(character)
        if i == len(expression_str):
            break

    while stack:
        output.append(stack.pop())

    return output


expression = input('Enter infix expression ')

print('infix notation: ', expression)

print('postfix notation: ', infixToPostfix(expression))
