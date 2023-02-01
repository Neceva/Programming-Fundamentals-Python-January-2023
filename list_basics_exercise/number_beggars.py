list_input = input().split(", ")
beggars_count = int(input())
sum_current_beggar = 0
first_index = 0
list_input_int = []
final_list = []

for num in list_input:
    list_input_int.append(int(num))
while first_index < beggars_count:
    sum_current_beggar = 0
    for index in range(first_index, len(list_input_int), beggars_count):
        sum_current_beggar += list_input_int[index]
    final_list.append(sum_current_beggar)
    first_index += 1

print(final_list)

