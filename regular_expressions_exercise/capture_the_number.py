import re

pattern = r"(\d+)"

strings = input()
while strings:
    matches = re.findall(pattern, strings)
    if matches:
        print(" ".join(matches), end=" ")
    strings = input()
    