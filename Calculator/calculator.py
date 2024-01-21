from Calculator.Exceptions import EmptyExpression
from operators.operatorFactory import OperatorCreator
from operators.single_operand_operators.singleCharOps import SingleCharOps


class Calculator:
    """
    Class Calculator - the main function for solving the equation.
    Accepts a string representing a mathematical expression. converts, breaks down and calculates the expression.
    The result is kept within the result variable.
    """

    def __init__(self, expression: str):
        """
        Constructor Class of Calculator

        :param expression:  string representing a mathematical expression
        factory: am instance of OperatorCreator class. represents the class for creating an instance of each
                operator class. also contains the list and dictionary of all the operators.
        operator_list: a list of all the operators in sorted order.
        duplicate_operators: a dictionary of duplicatable operators and their forms
        result: final result of the operation.
        """
        expression = str(expression)
        self.expression = expression
        self.factory = OperatorCreator()
        self.operator_list = self.factory.operator_list()
        self.duplicate_operators = self.factory.dup_operators()
        self.result = self.solve()

    @staticmethod
    def is_digit(num_string: str) -> bool:
        """
        accepts a String - removes dots, tabs and spaces and checks if it qualifies as a digit.

        :param num_string: string to check.
        :return: True if num_string can be turned into a number, false otherwise.
        """
        num_string = num_string.replace(' ', '')
        num_string = num_string.replace('\t', '')
        return num_string.replace('.', '').isdigit()

    def check_output_index(self, list_to_check: list, index: int) -> bool:
        """
        checks if an
        :param list_to_check:
        :param index:
        :return:
        """
        return list_to_check[index] in self.operator_list

    def check_output_char(self, element):
        return element in self.operator_list

    def convert(self) -> list:
        """
        converts a string(expression) to a list. counts brackets and performs several syntax checks.
        :return: a list representing the expression
        """
        bracket_counter = 0
        output = []
        curr_num = ''

        def in_range(index):
            try:
                output[index]
            except IndexError:
                return False
            return True

        for char in self.expression:
            if self.check_output_char(char) or (char in ['(', ')']):
                if self.is_digit(curr_num):
                    try:
                        output.append(float(curr_num))
                    except ValueError:
                        raise SyntaxError(f"Error |  there can't be a space between two digits 🙈 {curr_num}")
                curr_num = ''
                # checks if the operators are in a legal order. Takes duplicatable and right oriented operators into
                # consideration.
                if output and char not in self.duplicate_operators and self.check_output_char(char):
                    curr_op_class = self.factory.operator_factory(char)
                    if ((isinstance(curr_op_class, SingleCharOps) and not curr_op_class.can_dup and char == output[-1])
                            or (output[-1] in self.operator_list and char != output[-1] and not in_range(-2) or
                                (self.check_output_index(output, -1) and self.check_output_index(output, -2) and not
                                self.factory.operator_factory(output[-2]).position == "Right"))):
                        raise SyntaxError(f"operator {char} is illegal in this sequence 😉")

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
                try:
                    output.append(float(curr_num))
                except ValueError:
                    raise SyntaxError(f"Error |  there can't be a space between two digits 🙈 {curr_num}")
        return output

    def run_for_element(self, expression: list, element: str, index: int):
        """
        gets a list, an element and an index.
        runs, whilst the expression at index is equal to element and count them(index doesn't increase
        rather the elements get deleted).

        :param expression: a list to run on
        :param element: element to operate on
        :param index: the index of expression to start from
        :return: duplicate_counter - the amount of elements in a row in expression from index
        """
        duplicate_counter = 0
        while expression[index] == element:
            expression.pop(index)
            duplicate_counter += 1
        if self.check_output_index(expression, index) and duplicate_counter > 1:
            raise SyntaxError(
                f"there can't be multiple recurrences of {element} before another operator: {expression[index]}")
        return duplicate_counter

    def handle_duplicates(self, expression_array: list):
        """
        handles all the duplicate types from dup_operators. finds all the duplicates instances,
        deletes them and replaces them accordingly.
        :param expression_array: the mathematical expression as a list
        :return: A list with all the duplicates handled, deleted and replaced.
        """
        if not expression_array:
            raise EmptyExpression("input must contain an expression")
        duplicate_operators = self.duplicate_operators
        i = 0
        temp_expression_array = expression_array
        cur_element = expression_array[i]
        if cur_element in duplicate_operators:
            duplicate_counter = self.run_for_element(temp_expression_array, cur_element, i)
            if duplicate_counter > 0:
                if self.check_output_index(temp_expression_array, i):
                    raise SyntaxError(
                        f"{temp_expression_array[i]} cant be after an Unari operator: {cur_element} 😉")
                if duplicate_counter % 2 == 0:
                    i -= 1
                else:
                    temp_expression_array.insert(0, duplicate_operators.get(cur_element)[0])

        while i < len(temp_expression_array) - 1:
            if temp_expression_array[i] in duplicate_operators:
                cur_element = temp_expression_array[i]
                duplicate_counter = self.run_for_element(temp_expression_array, cur_element, i)
                if duplicate_counter > 0:
                    if duplicate_counter % 2 == 0:
                        if temp_expression_array[i - 1] != '(':
                            if ((self.check_output_index(temp_expression_array, i - 1) and
                                 self.factory.operator_factory(temp_expression_array[i - 1]).position == "Right") or
                                    not self.check_output_index(temp_expression_array, i - 1)):
                                temp_expression_array.insert(i, duplicate_operators.get(cur_element)[1])
                                temp_expression_array.insert(i, cur_element)
                    else:

                        if (self.check_output_index(temp_expression_array, i - 1) and
                                self.factory.operator_factory(
                                    temp_expression_array[i - 1]).position != "Right"):
                            try:
                                temp_expression_array.insert(i, duplicate_operators.get(cur_element)[1])
                            except ArithmeticError as e:
                                raise SyntaxError(f"incorrect operator format: {e}")
                        elif temp_expression_array[i - 1] == '(':
                            temp_expression_array.insert(i, duplicate_operators.get(cur_element)[0])
                        else:
                            temp_expression_array.insert(i, cur_element)
            i += 1
        return temp_expression_array

    def bracket_handler(self, expression_lst: list) -> list:
        """
        Accepts a mathematical expression in the form of a list. uses a stack to calculate and send the expressions
        in the most inner bracket and out to the calculate function. The expressions within the brackets
        are replaced with the result resulted from calculate().

        :param expression_lst: a mathematical expression in the form of a list
        :return: An expression list without any brackets.
        """
        send_temp_expression = []
        result_expression = []
        j = 0
        found_bracket = False
        stack = []
        while j < len(expression_lst):
            result_returned = False
            if expression_lst[j] == '(':
                while j < len(expression_lst) - 1 and not result_returned:
                    if expression_lst[j] != ')':
                        stack.append(expression_lst[j])
                    j += 1

                    if expression_lst[j] == ')':
                        while not found_bracket and stack:
                            item_to_insert = stack.pop()
                            if item_to_insert == '(':
                                found_bracket = True
                            else:
                                # insert into the temporary list to send to calculate in the right order
                                send_temp_expression.insert(0, item_to_insert)
                        try:
                            stack.append((self.calculate(send_temp_expression)))
                        except IndexError:
                            raise SyntaxError(f"Brackets can't be empty-> index {j - 1} to {j}")
                        found_bracket = False
                        send_temp_expression = []
                        if '(' not in stack:
                            result_expression.append(stack.pop())
                            result_returned = True
            if expression_lst[j] != ')':
                result_expression.append(expression_lst[j])
            j += 1
        return result_expression

    def calculate(self, expression_list: list) -> float:
        """
        Accepts an expression without any brackets. Finds all the operators, inserts them sorted according to their
        precedence. loops for each precedence from the end, removes the current operation and inserts the result.
        :param expression_list: Mathematical expression without any brackets
        :return: result(int/float)
        """
        curr_kdimut_operator_list = []
        for element in expression_list:
            if (self.check_output_char(element) and self.factory.operator_factory(element) not in
                    curr_kdimut_operator_list):
                curr_kdimut_operator_list.append(self.factory.operator_factory(element).precedence)
        curr_kdimut_operator_list.sort()

        for i in range(len(curr_kdimut_operator_list)):
            j = 0
            kdimut = curr_kdimut_operator_list[-1]

            while j < len(expression_list):
                if self.check_output_index(expression_list, j):
                    try:
                        operator = self.factory.operator_factory(expression_list[j])
                    except ValueError as e:
                        raise SyntaxError(f"expression is illegal: {e}")
                    curr_kdimut = operator.precedence
                    if curr_kdimut == kdimut:
                        if operator.position == "Center":
                            if j == 0:
                                raise SyntaxError(f"Syntax Error: {expression_list[j]} can't be at index {j}")
                            try:
                                result = operator.operation(expression_list[j - 1], expression_list[j + 1])
                            except ZeroDivisionError as e:
                                raise ZeroDivisionError(f"{e} at index {j - 1}")
                            except (ArithmeticError, TypeError):
                                raise SyntaxError(f"{expression_list[j]} is illegal in this position 🧐")
                            except IndexError:
                                raise SyntaxError(f"insufficient operands {expression_list}")
                            try:
                                del expression_list[j - 1:j + 2]
                            except IndexError:
                                raise SyntaxError(f"insufficient operands {expression_list}")
                            expression_list.insert(j - 1, result)
                        elif operator.position == "Right":
                            if j - 1 < 0:
                                raise SyntaxError(f"Operator {expression_list[j]} is misplaced 😡")
                            try:
                                result = operator.operation(expression_list[j - 1])
                            except ValueError as e:
                                raise SyntaxError(f"Error - {e}")
                            del expression_list[j - 1:j + 1]
                            expression_list.insert(j - 1, result)
                        elif operator.position == "Left":
                            if j + 1 >= len(expression_list):
                                raise SyntaxError(f"{expression_list[j]} is misplaced 😡")
                            find_next_operand = j + 1
                            while (not isinstance(expression_list[find_next_operand], float) and not
                            isinstance(expression_list[find_next_operand], int) and
                                   find_next_operand < len(expression_list) - 1):
                                find_next_operand += 1
                            result = operator.operation(expression_list[find_next_operand])
                            expression_list.pop(j)
                            expression_list.pop(find_next_operand - 1)
                            expression_list.insert(find_next_operand - 1, result)
                        else:
                            raise SyntaxError("Operator doesn't have a position 👨‍🦯")

                        j -= 1
                j += 1
            curr_kdimut_operator_list.pop()
        if len(expression_list) > 1:
            raise SyntaxError(f"Error | {expression_list[1]} out of place 😡")
        result = expression_list.pop()
        try:
            if result == int(result):
                result = int(result)
        except OverflowError:
            return result
        return round(result, 10)

    def solve(self):
        data_list = self.convert()
        data_list = self.handle_duplicates(data_list)
        data_list = self.bracket_handler(data_list)
        return round(self.calculate(data_list), 10)
