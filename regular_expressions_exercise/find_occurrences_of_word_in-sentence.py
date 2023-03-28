import re

text = input()
word = input()

pattern = fr"\b({word})\b"

match = re.findall(pattern, text, re.IGNORECASE)
print(len(match))
