list_input = [int(num) for num in input().split(", ")]
positive_num = [num for num in list_input if num >= 0]
negative_num = [num for num in list_input if num < 0]
even_num = [num for num in list_input if num % 2 == 0]
odd_num = [num for num in list_input if num % 2 != 0]

print(f"Positive: {', '.join(str(num) for num in positive_num)}")
print(f"Negative: {', '.join(str(num) for num in negative_num)}")
print(f"Even: {', '.join(str(num) for num in even_num)}")
print(f"Odd: {', '.join(str(num) for num in odd_num)}")
