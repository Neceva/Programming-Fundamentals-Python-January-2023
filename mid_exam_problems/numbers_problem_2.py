numbers_sequence = [int(number) for number in input().split()]

while True:
    commands = input().split()
    com = commands[0]
    if com == "Finish":
        print(" ".join(str(num) for num in numbers_sequence))
        break
    elif com == "Add":
        numbers_sequence.append(int(commands[1]))

    elif com == "Remove":
        if int(commands[1]) in numbers_sequence:
            numbers_sequence.remove(int(commands[1]))

    elif com == "Replace":
        if int(commands[1]) in numbers_sequence:
            index = numbers_sequence.index(int(commands[1]))
            numbers_sequence[index] = int(commands[2])

    elif com == "Collapse":
        numbers_sequence = [num for num in numbers_sequence if num >= int(commands[1])]