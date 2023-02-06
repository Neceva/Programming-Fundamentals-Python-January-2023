def sum_numbers(first, second):
    sum_num = first + second
    return sum_num


def subtract(sum, third):
    subtract_num = sum - third
    return subtract_num


def add_and_subtract(first, second, third):
    sum_first_second_num = sum_numbers(first, second)
    result = subtract(sum_first_second_num, third)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
