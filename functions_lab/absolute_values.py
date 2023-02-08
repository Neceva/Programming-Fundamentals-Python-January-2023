def abs_value(lst_inp):
    lst_as_numbers = []
    for num in lst_inp:
        lst_as_numbers.append(abs(float(num)))
    return lst_as_numbers


list_input = input().split()
print(abs_value(list_input))
