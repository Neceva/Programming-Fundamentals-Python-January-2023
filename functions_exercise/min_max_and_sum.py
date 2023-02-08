def min_max_sum_value(list_input):
    list_numbers_int = []
    for num in list_input:
        list_numbers_int.append(int(num))

    min_num = min(list_numbers_int)
    max_num = max(list_numbers_int)
    sum_num = sum(list_numbers_int)
    return min_num, max_num, sum_num


list_numbers = input().split()
minimum_number, maximum_number, sum_all_numbers = min_max_sum_value(list_numbers)
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_all_numbers}")
