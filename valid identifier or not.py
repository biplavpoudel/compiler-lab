import re

def is_valid_identifier(identifier):
    # Check if the identifier matches the valid identifier pattern
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(pattern, identifier)

# Get input from the user
user_input = input("Enter an identifier: ")

# Check validity and display the result
if is_valid_identifier(user_input):
    print(f"{user_input} is a valid identifier.")
else:
    print(f"{user_input} is not a valid identifier.")
