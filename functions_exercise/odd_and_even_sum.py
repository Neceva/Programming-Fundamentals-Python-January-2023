def even_odd_numbers(number):
    sum_of_odd_numbers = 0
    sum_of_even_numbers = 0

    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even_numbers += int(digit)
        else:
            sum_of_odd_numbers += int(digit)
    return sum_of_odd_numbers, sum_of_even_numbers


user_input_num = input()
sum_of_odd_digits, sum_of_even_digits = even_odd_numbers(user_input_num)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
