def all_char(first, last):
    lst_char = []
    for i in range(ord(first) + 1, ord(last)):
        lst_char.append(chr(i))
    return " ".join(lst_char)


first_char = input()
second_char = input()
print(all_char(first_char, second_char))
