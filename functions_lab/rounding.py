def rounded_numbers(numbers):
    final_list_num = []
    for num in numbers:
        final_list_num.append(round(float(num)))
    return  final_list_num


numbers_input = input().split()
print(rounded_numbers(numbers_input))