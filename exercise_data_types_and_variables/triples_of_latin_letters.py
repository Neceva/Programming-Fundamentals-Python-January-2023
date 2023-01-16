integerN = int(input())
for i in range(0, integerN):
    for k in range(0, integerN):
        for j in range(0, integerN):
            print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}")
