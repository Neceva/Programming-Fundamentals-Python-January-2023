list_numbers = [int(num) for num in input().split(", ")]
max_number_loop = int(max(list_numbers) / 10)
max_limiting = 10
min_limiting = 0
row = []
for loops in range(max_number_loop + 1):
    for num in list_numbers:
        if min_limiting < num <= max_limiting:
            row.append(num)
    print(f"Group of {max_limiting}'s: {row}")
    if max(list_numbers) in row:
        exit(0)
    min_limiting = max_limiting
    max_limiting += 10
    row.clear()