capacity = 255
num_of_lines = int(input())
total_liters = 0
for i in range(num_of_lines):
    current_liters = int(input())
    total_liters += current_liters
    if total_liters > capacity:
        total_liters -= current_liters
        print("Insufficient capacity!")
        continue

print(total_liters)