import re

pattern = r'%([A-Z][a-z]+)%\w*[^\|\%\$\.]*<(\w+)>\w*[^\|\%\$\.]*\|(\d+)\|[A-Za-z]*(d?\d+\.?\d*)\$'
total = 0
line = input()

while line != "end of shift":

    match = re.search(pattern, line)

    if match:
        customer, product, count, price = match.groups()
        print(f"{customer}: {product} - {(int(count) * float(price)):.2f}")
        total += int(count) * float(price)
    line = input()

print(f"Total income: {total:.2f}")