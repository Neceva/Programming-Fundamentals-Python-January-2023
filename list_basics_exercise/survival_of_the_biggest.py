list_of_str_num = input().split()
count_to_remove = int(input())
list_of_int = []
numbers = 0

for num in list_of_str_num:
    list_of_int.append(int(num))
for i in range(count_to_remove):
    current_min_el = min(list_of_int)
    list_of_str_num.remove((str(current_min_el)))
    list_of_int.remove(current_min_el)

print(", ".join(list_of_str_num))