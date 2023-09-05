def count_operators(input_string):
    operators = ['+', '-', '*', '/', '%', '=', '>', '<', '!', '&', '|', '^', '~', ',']
    operator_count = 0

    for char in input_string:
        if char in operators:
            operator_count += 1

    return operator_count


# Get input from the user
input_string = input("Enter a string: ")

# Count operators in the input string
num_operators = count_operators(input_string)
print(f"Number of operators in the input string: {num_operators}")
