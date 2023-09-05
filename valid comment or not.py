def is_valid_c_comment(line):
    line = line.strip()
    if (line.startswith("/*") and line.endswith("*/")) or (line.startswith("//")):
        return True

# Get input from the user
user_input = input("Enter a line of text: ")

# Check if it's a valid C/C++ comment
if is_valid_c_comment(user_input):
    print("Valid C/C++ comment.")
else:
    print("Not a valid comment.")
