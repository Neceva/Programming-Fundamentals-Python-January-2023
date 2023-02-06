def even_numbers(number):
    if int(number) % 2 == 0:
        return True
    else:
        return False


lst_numbers = input().split()
even_num = filter(even_numbers, lst_numbers)
result = []
for dig in even_num:
    result.append(int(dig))
print(result)
