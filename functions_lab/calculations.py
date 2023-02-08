def calculation(first, second, operator):
    result = 0
    if operator == "multiply":
        result = first * second
    if operator == "divide":
        result = first / second
    if operator == "add":
        result = first + second
    if operator == "subtract":
        result = first - second
    return int(result)


input_operator = input()
first_number = int(input())
second_number = int(input())
print(calculation(first_number, second_number, input_operator))
