sequence = [int(num) for num in input().split()]
sequence.sort(reverse=True)
average_num = sum(sequence) / len(sequence)
greater_numbers = []

for num in sequence:
    if num > average_num:
        greater_numbers.append(num)
        if len(greater_numbers) >= 5:
            break
    if len(greater_numbers) == 0:
        print("No")
        break
print(*greater_numbers)
