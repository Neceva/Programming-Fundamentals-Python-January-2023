user_input = input().split()
count_shuffles = int(input())

left_part = 0
right_part = 0
count = 0

for i in range(count_shuffles):
    final_list = []
    left_part = user_input[:len(user_input)//2]
    right_part = user_input[len(user_input)//2:]

    for index in range(len(left_part)):
        final_list.append((left_part[index]))
        final_list.append((right_part[index]))
    user_input = final_list

print(user_input)

