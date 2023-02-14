names = input().split(", ")
result = sorted(names, key=lambda x: (-len(x), x))
print(result)
