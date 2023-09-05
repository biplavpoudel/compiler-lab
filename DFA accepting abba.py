def dfa_accept(input_string):
    transitions = {
        0: {'a': 1},
        1: {'b': 2},
        2: {'b': 3},
        3: {'a': 4}
    }

    current_state = 0

    for char in input_string:
        if current_state in transitions and char in transitions[current_state]:
            current_state = transitions[current_state][char]
        else:
            return False

    return current_state == 4


def dfa():
    accepted_string = "abba"
    user_input = input("Enter the string: ")

    if dfa_accept(user_input):
        print("Input accepted!")
    else:
        print("Input rejected!")

dfa()