import re

text = input()

pattern = r"\b(?P<Day>\d{2})(.|-|/)(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"

match = re.finditer(pattern, text)

for match in match:
    date = match.groupdict()
    print(f"Day: {date['Day']}, Month: {date['Month']}, Year: {date['Year']}")
