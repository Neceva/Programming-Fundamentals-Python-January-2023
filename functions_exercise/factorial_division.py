def factorial_number(some_number):
    for num in range(1, some_number):
        some_number *= num
    return some_number


first_number = int(input())
second_number = int(input())
factorial_first_number = factorial_number(first_number)
factorial_second_number = factorial_number(second_number)
final_result = factorial_first_number / factorial_second_number
print(f"{final_result:.2f}")