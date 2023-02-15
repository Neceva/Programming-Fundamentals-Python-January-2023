string_numbers = input().split(", ")
numbers = list(map(int, string_numbers))
indices = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]
print(indices)