def smallest_number(first, second, third):
    min_number = min(first, second, third)
    return min_number


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = smallest_number(first_number, second_number, third_number)
print(result)

