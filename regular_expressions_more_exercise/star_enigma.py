import re

numbers_of_messages = int(input())
letter_list = ['s', 't', 'a', 'r', 'S', 'T', 'A', 'R']
decrypted_list = []
decrypted_message = ""
attacked_planets = []
destroyed_planets = []
code = 0
pattern = r"[^@\-\!\:\>]*@([A-Za-z]+)[^@\-\!\:\>]*:(\d+)[^@\-\!\:\>]*" \
          r"\!([AD])[^@\-\!\:\>]*\![^@\-\!\:\>]*->(\d+)[^@\-\!\:\>]*"

for i in range(numbers_of_messages):
    encrypted_message = input()
    pattern1 = r'[starSTAR]'
    code = len(re.findall(pattern1, encrypted_message))

    for char in encrypted_message:
        decrypted_list.append(chr(ord(char) - code))
    decrypted_message = "".join(decrypted_list)
    match = re.search(pattern, decrypted_message)
    if match:
        planet_name, population, attack_type, soldier_count = match.groups()
        if attack_type == "A":
            attacked_planets.append(planet_name)
        elif attack_type == "D":
            destroyed_planets.append(planet_name)
    decrypted_list.clear()
    decrypted_message = ""
    code = 0

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
