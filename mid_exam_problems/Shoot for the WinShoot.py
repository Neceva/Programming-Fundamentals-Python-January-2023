target_sequence = [int(num) for num in input().split()]
shot_number = 0
counter_shots = 0
command = input()
while command != "End":
    index_of_shot = int(command)
    if index_of_shot <= (len(target_sequence) - 1):
        shot_number = int(target_sequence[index_of_shot])
        target_sequence[index_of_shot] = -1
        counter_shots += 1
        for index in range(len(target_sequence)):
            if target_sequence[index] != -1:
                if target_sequence[index] > shot_number:
                    target_sequence[index] -= shot_number
                else:
                    target_sequence[index] += shot_number
    command = input()

if command == "End":
    print(f"Shot targets: {counter_shots} -> {' '.join(str(num) for num in target_sequence)}")
