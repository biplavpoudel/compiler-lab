import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')  # Download the necessary resources if not already downloaded

def generate_tokens(input_text):
    tokens = word_tokenize(input_text)
    return tokens

input_text = input("Enter a sentence: ")
tokens = generate_tokens(input_text)
print("Tokens:", tokens)



