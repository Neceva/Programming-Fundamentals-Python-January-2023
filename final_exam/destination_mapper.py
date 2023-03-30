import re

places = input()
destinations = []
travel_points = 0
pattern = r'(=|\/)([A-Z][A-Za-z][A-Za-z]+)\1'

matches = re.findall(pattern, places)

for match in matches:
    destinations.append(match[1])
    travel_points += len(match[1])

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {travel_points}')
