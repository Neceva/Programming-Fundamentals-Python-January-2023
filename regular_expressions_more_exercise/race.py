import re
from unicodedata import digit

participants_list = input().split(", ")
name_char = []
distance_num = []
players = {}
current_name = ""
current_distance = 0
pattern = r"[A-Za-z0-9]"
info = input()

while info != "end of race":
    match = re.findall(pattern, info)
    for char in match:
        if char.isdigit():
            distance_num.append(int(char))
        else:
            name_char.append(char)

    current_name = "".join(name_char)
    current_distance = sum(distance_num)
    for name in participants_list:
        if current_name == name:
            if current_name in players.keys():
                players[current_name] += current_distance
            else:
                players[current_name] = current_distance

    name_char.clear()
    distance_num.clear()
    info = input()
players = sorted(players.items(), key=lambda x: x[1], reverse=True)

print(f"1st place: {players[0][0]}")
print(f"2nd place: {players[1][0]}")
print(f"3rd place: {players[2][0]}")
