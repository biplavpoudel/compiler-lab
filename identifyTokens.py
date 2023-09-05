# keywords = {"auto","break","case","char","const","continue","default","do",
# "double","else","enum","extern","float","for","goto",
# "if","int","long","register","return","short","signed",
# "sizeof","static","struct","switch","typedef","union",
# "unsigned","void","volatile","while", "main", "#include"}
#
# operators = {"+","-","*","/","<",">","=","<=",">=","==","!=","++","--","%"}
#
# delimiters = {'(',')','{','}','[',']','"',"'",';','#',',',''}
#
# def detect_keywords(text):
# 	arr = []
# 	for word in text:
# 		if word in keywords:
# 			arr.append(word)
# 	return list(set(arr))    #set doesn't allow duplicates
#
# def detect_operators(text):
# 	arr = []
# 	for word in text:
# 		if word in operators:
# 			arr.append(word)
# 	return list(set(arr))
#
# def detect_delimiters(text):
# 	arr = []
# 	for word in text:
# 		if word in delimiters:
# 			arr.append(word)
# 	return list(set(arr))
#
# def detect_num(text):
# 	arr = []
# 	for word in text:
# 		# try:
# 		# 	a = int(word)
# 		# 	arr.append(word)
# 		# except:
# 		# 	pass
# 		if word.isdigit():
# 			arr.append(word)
# 	return list(set(arr))
#
# def detect_identifiers(text):
# 	k = detect_keywords(text)
# 	o = detect_operators(text)
# 	d = detect_delimiters(text)
# 	n = detect_num(text)
# 	not_ident = k + o + d + n
# 	arr = []
# 	for word in text:
# 		if word not in not_ident:
# 			arr.append(word)
# 	return arr
#
# with open('lab1-example.txt') as t:
# 	text = t.read().split()
#
# print("Keywords: ",detect_keywords(text))
# print("Operators: ",detect_operators(text))
# print("Delimiters: ",detect_delimiters(text))
# print("Identifiers: ",detect_identifiers(text))
# print("Numbers: ",detect_num(text))

keywords = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto",
    "if", "int", "long", "register", "return", "short", "signed",
    "sizeof", "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while", "main", "#include"
}

operators = {"+", "-", "*", "/", "<", ">", "=", "<=", ">=", "==", "!=", "++", "--", "%"}

delimiters = {'(', ')', '{', '}', '[', ']', '"', "'", ';', '#', ',', ''}

def remove_comments(lines):
    filtered_lines = []
    in_comment_block = False

    for line in lines:
        if not in_comment_block:
            # Check for the start of a multi-line comment
            if '/*' in line:
                in_comment_block = True
                if '*/' in line:
                    in_comment_block = False
                continue

            # Check for single-line comments
            if '//' in line:
                line = line.split('//')[0]

            filtered_lines.append(line)
        else:
            # Check for the end of a multi-line comment
            if '*/' in line:
                in_comment_block = False

    return filtered_lines

def detect_keywords(text):
    arr = []
    for word in text:
        if word in keywords:
            arr.append(word)
    return list(set(arr))  # set doesn't allow duplicates

def detect_operators(text):
    arr = []
    for word in text:
        if word in operators:
            arr.append(word)
    return list(set(arr))

def detect_delimiters(text):
    arr = []
    for word in text:
        if word in delimiters:
            arr.append(word)
    return list(set(arr))

def detect_num(text):
    arr = []
    for word in text:
        if word.isdigit():
            arr.append(word)
    return list(set(arr))

def detect_identifiers(text):
    k = detect_keywords(text)
    o = detect_operators(text)
    d = detect_delimiters(text)
    n = detect_num(text)
    not_ident = k + o + d + n
    arr = []
    for word in text:
        if word not in not_ident:
            arr.append(word)
    return list(set(arr))

with open('lab1-example.txt') as t:
    lines = t.readlines()

# Remove comments from the code
lines = remove_comments(lines)

# Concatenate the lines to form a single string
code_text = ''.join(lines)

# Split the code text into individual words
text = code_text.split()

print("Keywords: ", detect_keywords(text))
print("Operators: ", detect_operators(text))
print("Delimiters: ", detect_delimiters(text))
print("Identifiers: ", detect_identifiers(text))
print("Numbers: ", detect_num(text))
