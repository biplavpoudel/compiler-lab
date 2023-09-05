def translate_arithmetic_expression(expression):
    assignments = expression.split('\n')
    intermediate_code = []

    temp_counter = 1  # To generate unique temporary variable names

    for assignment in assignments:
        tokens = assignment.split(' = ')
        result_variable = tokens[0]
        arithmetic_expression = tokens[1]

        terms = arithmetic_expression.split()
        result = f"temp{temp_counter}"
        temp_counter += 1

        intermediate_result = terms[0]
        for i in range(2, len(terms), 2):
            operator = terms[i - 1]
            operand = terms[i]

            if operator == '+':
                opcode = "ADD"
            elif operator == '-':
                opcode = "SUB"
            elif operator == '*':
                opcode = "MUL"
            elif operator == '/':
                opcode = "DIV"
            else:
                raise ValueError(f"Unsupported operator: {operator}")

            intermediate_code.append(f"{opcode} {result}, {intermediate_result}, {operand}")
            intermediate_result = result

            result = f"temp{temp_counter}"
            temp_counter += 1

        intermediate_code.append(f"STORE {intermediate_result}, {result_variable}")

    assembly_code = "\n".join(intermediate_code)
    return assembly_code

# Example usage
expression = "a = a + b\n" \
             "c = a * d - b\n" \
             "f = a + c\n" \
             "g = f / d"

assembly_code = translate_arithmetic_expression(expression)
print(assembly_code)
