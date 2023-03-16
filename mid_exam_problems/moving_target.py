sequence_targets = [int(num) for num in input().split()]
command = input().split()
com = command[0]
while True:
    if com == "End":
        print("|".join(str(num) for num in sequence_targets))
        break
    elif com == "Shoot":
        if 0 <= int(command[1]) < len(sequence_targets):
            if sequence_targets[int(command[1])] > int(command[2]):
                sequence_targets[int(command[1])] -= int(command[2])
            else:
                del sequence_targets[int(command[1])]

    elif com == "Add":
        if 0 <= int(command[1]) < len(sequence_targets):
            sequence_targets.insert(int(command[1]), int(command[2]))
        else:
            print("Invalid placement!")

    elif com == "Strike":
        start = int(command[1]) - int(command[2])
        end = int(command[1]) + int(command[2])
        if start >= 0 and end < len(sequence_targets):
            del sequence_targets[start: end + 1]
        else:
            print("Strike missed!")
    command = input().split()
    com = command[0]