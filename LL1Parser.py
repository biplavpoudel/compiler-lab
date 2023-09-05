# Import functions and data from LL1ParserGenerator.py
import first, follow
from recursionRemoval import result
from first import firsts
from follow import follows

# Get the list of terminals from the result
terminals = set()
for productions in result.values():
    for production in productions:
        for symbol in production:
            if symbol not in result:
                terminals.add(symbol)

# Get the list of non-terminals from the result
non_terminals = list(result.keys())

# Initialize the parse table
parse_table = {}
for non_terminal in non_terminals:
    parse_table[non_terminal] = {}
    for terminal in terminals:
        parse_table[non_terminal][terminal] = []

# Populate the parse table
for non_terminal in non_terminals:
    for production in result[non_terminal]:
        first_symbol = None
        for symbol in production:
            if symbol in result:
                first_symbol = symbol
                break
        first_symbols = firsts[first_symbol]
        for terminal in first_symbols:
            if terminal != 'e':
                parse_table[non_terminal][terminal].append(production)

        if 'e' in first_symbols:
            follow_symbols = follows[non_terminal]
            for terminal in follow_symbols:
                parse_table[non_terminal][terminal].append(production)

# Print the LL(1) parse table
print("LL(1) Parse Table:")
# Print the header row with non-terminals as columns
header = "\t\t".join(non_terminals)
print("\t\t", header)
for terminal in terminals:
    row = []
    for non_terminal in non_terminals:
        productions = parse_table[non_terminal][terminal]
        if len(productions) > 0:
            row.append(" | ".join([" ".join(production) for production in productions]))
        else:
            row.append("-")
    row_str = "\t\t".join(row)
    print(terminal, "\t\t", row_str)


