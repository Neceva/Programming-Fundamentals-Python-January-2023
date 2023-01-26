number_N = int(input())
positive_num = []
negative_num = []
even_num = []
odd_num = []

for i in range(number_N):
    current_number = int(input())
    if current_number >= 0:
        positive_num.append(current_number)
    else:
        negative_num.append(current_number)
    if current_number % 2 == 0:
        even_num.append(current_number)
    else:
        odd_num.append(current_number)

command = input()
if command == "positive":
    print(positive_num)
elif command == "negative":
    print(negative_num)
elif command == "even":
    print(even_num)
else:
    print(odd_num)
