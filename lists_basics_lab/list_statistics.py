number_count = int(input())
positives_list = []
negatives_list = []
for i in range(number_count):
    number = int(input())
    if number >= 0:
        positives_list.append(number)
    else:
        negatives_list.append(number)

print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum(negatives_list)}")
