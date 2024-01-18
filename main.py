from operators.operatorFactory import OperatorCreator


class Calculator:
    def __init__(self, expression: str):
        self.expression = expression
        self.factory = OperatorCreator()
        self.operator_list = self.factory.operator_list()
        self.duplicate_operators = self.factory.dup_operators()
        self.result = self.solve()

    @staticmethod
    def is_digit(num_string):
        num_string = num_string.replace(' ', '')
        num_string = num_string.replace('\t', '')
        return num_string.replace('.', '').isdigit()

    def convert(self) -> list:
        duplicates = self.factory.dup_operators()
        bracket_counter = 0
        output = []
        curr_num = ''
        for char in self.expression:
            if char in self.operator_list or (char in ['(', ')']):
                if self.is_digit(curr_num):
                    try:
                        output.append(float(curr_num))
                    except ValueError:
                        raise SyntaxError("Error |  there can't be a space between two digits")
                curr_num = ''
                if (output and char not in duplicates and char in self.operator_list and char == output[-1] and
                        self.factory.operator_factory(char).position() != "Right"):
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
            if self.is_digit(curr_num):
                output.append(float(curr_num))
        return output

    def run_for_element(self, expression: list, element: str, index: int):
        duplicate_counter = 0
        while expression[index] == element:
            expression.pop(index)
            duplicate_counter += 1
        if expression[index] in self.operator_list and duplicate_counter > 1:
            raise SyntaxError(
                f"there can't be multiple recurrences of {element} before another operator: {expression[index]}")
        return duplicate_counter

    def handle_minus(self, expression_array: list):
        if not expression_array:
            raise SyntaxError("input must contain an expression")
        duplicate_operators = self.duplicate_operators
        counter = 0
        temp_expression_array = expression_array
        cur_element = expression_array[counter]
        if cur_element in duplicate_operators:
            duplicate_counter = self.run_for_element(temp_expression_array, cur_element, counter)
            if duplicate_counter > 0:
                if temp_expression_array[counter] in self.operator_list:
                    raise SyntaxError(
                        f"{temp_expression_array[counter]} cant be after an Unari operator: {cur_element}")
                if duplicate_counter % 2 == 0:
                    counter -= 1
                else:
                    temp_expression_array.insert(0, duplicate_operators.get(cur_element)[0])

        while counter < len(temp_expression_array) - 1:
            duplicate_counter = 0
            if temp_expression_array[counter] in duplicate_operators:
                cur_element = temp_expression_array[counter]
                duplicate_counter = self.run_for_element(temp_expression_array, cur_element, counter)
                if duplicate_counter > 0:
                    if duplicate_counter % 2 == 0:
                        if temp_expression_array[counter - 1] != '(':
                            if temp_expression_array[counter - 1] not in self.operator_list:
                                temp_expression_array.insert(counter, duplicate_operators.get(cur_element)[1])
                                temp_expression_array.insert(counter, cur_element)
                    else:

                        if (temp_expression_array[counter - 1] in self.operator_list and
                                self.factory.operator_factory(
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

    def bracket_handler(self, expression_lst: list) -> list:
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
                            stack.append((self.calculate(send_temp_expression)))
                        except IndexError:
                            raise SyntaxError(f"Brackets can't be empty-> index {pos - 1} to {pos}")
                        found_bracket = False
                        send_temp_expression = []
                        if '(' not in stack:
                            result_expression.append(stack.pop())
                            break
            if expression_lst[pos] != ')':
                result_expression.append(expression_lst[pos])
            pos += 1
        return result_expression

    def calculate(self, revised_list: list) -> float:
        curr_operator_list = [oper for oper in self.operator_list if oper in revised_list]
        operator_list_for_kdimut = [oper for oper in self.operator_list if oper in curr_operator_list]

        for i in range(len(operator_list_for_kdimut)):
            pos = 0
            kdimut = self.factory.operator_factory(operator_list_for_kdimut[-1]).kdimut()

            while pos < len(revised_list):
                if revised_list[pos] in operator_list_for_kdimut:
                    try:
                        operator = self.factory.operator_factory(revised_list[pos])
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
                                del revised_list[pos - 1:pos + 2]
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
                            del revised_list[pos - 1:pos + 1]
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
                            del revised_list[pos:pos + 2]
                            revised_list.insert(pos, result)
                        else:
                            raise SyntaxError("Operator doesn't have a position")

                        pos -= 1
                pos += 1
            operator_list_for_kdimut.pop(-1)
        if len(revised_list) > 1:
            raise SyntaxError(f"Error | {revised_list[1]} out of place")
        return revised_list.pop(0)

    def solve(self):
        data_list = self.convert()
        data_list = self.handle_minus(data_list)
        data_list = self.bracket_handler(data_list)
        return self.calculate(data_list)


print((Calculator("(100 $ 50 $ 25) - (10 & 5 & 3) + ~20")).result)

"""
def main():
    while True:
        try:
            e = "   5"
            print(is_digit(e))
            expression = input("Enter and expression:")
        except EOFError:
            print("\n Please dont press ctrl+d :)")
            break
        except KeyboardInterrupt:
            print("\n Please dont interrupt the process :(")
            break
        try:
            expression = convert(expression)
            expression = handle_minus(expression)
            expression = bracket_handler(expression)
            # print(f"Result: {calculate(expression)}")
            hi = calculate(expression)
            print(hi == hi)
            if input("Do another calculation? (yes/no): ").lower() != 'yes':
                break
        except (KeyboardInterrupt) as e:
            print(f"Error | {e}")
            break


if __name__ == "__main__":
    main()"""
