current_input = input().split()
symbols = "".join(current_input)
letters = {}

for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1
for char, occurrences in letters.items():
    print(f"{char} -> {occurrences}")
