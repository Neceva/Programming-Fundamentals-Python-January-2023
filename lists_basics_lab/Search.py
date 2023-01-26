num = int(input())
keyword = input()
input_str_list = []
filtered_list = []

for i in range(num):
    current_input = input()
    input_str_list.append(current_input)
    if keyword in current_input:
        filtered_list.append(current_input)

print(input_str_list)
print(filtered_list)
