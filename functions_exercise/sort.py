def ascending_order(num_lst):
    lst_as_int = []
    for num in num_lst:
        lst_as_int.append(int(num))
    return sorted(lst_as_int)


list_numbers = input().split()
print(ascending_order(list_numbers))
