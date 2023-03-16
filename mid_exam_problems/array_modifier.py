array_input = [int(number) for number in input().split()]
while True:
    command = input().split()
    com = command[0]
    if com == "end":
        break
    if com == "swap":
        array_input[int(command[1])], array_input[int(command[2])] \
            = array_input[int(command[2])], array_input[int(command[1])]
    elif com == "multiply":
        array_input[int(command[1])] = int(array_input[int(command[1])]) * int(array_input[int(command[2])])

    if com == "decrease":
        for index in range(len(array_input)):
            array_input[index] -= 1

print(", ".join(str(number) for number in array_input))
