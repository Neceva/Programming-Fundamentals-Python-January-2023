number_of_char = int(input())
sum_equals = 0
for i in range(number_of_char):
    char = input()
    sum_equals += ord(char)
print(f"The sum equals: {sum_equals}")