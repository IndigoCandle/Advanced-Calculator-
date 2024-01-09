def infix_postfix(exp_list:list) ->list:
    postfix_list = []
    operator_stack = []

    for num in exp_list:
        if isinstance(num, float or int):
            postfix_list.append(num)
            counter += 1
        elif num == '(':
            operator_stack.append(num)
        elif num == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix_list.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while operator_stack and (num.kdimut < operator_stack[-1].kdimut) or
                             (num.kdimut == operator_stack[-1].kdimut) and num.associativity == 'L')):
                postfix_list.append(operator_stack.pop())
            operator_stack.append(num)
    while operator_stack:
        postfix_list.append(operator_stack.pop())
    return postfix_list
