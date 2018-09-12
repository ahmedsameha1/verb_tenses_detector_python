import re

sentence = input("Enter a sentence: ")
pattern = re.compile(r"\.\s[a-zA-Z].+\.")
matches = pattern.finditer(sentence)
for match in matches:
    print(match)
