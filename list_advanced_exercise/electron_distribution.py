number_electrons = int(input())
shell_count = 0
list_shells = []
left_electrons = number_electrons

while number_electrons > 0:
    shell_count += 1
    electrons_current_shell = 2 * shell_count * shell_count
    left_electrons -= electrons_current_shell
    if left_electrons < 0:
        list_shells.append(number_electrons)
        break
    else:
        number_electrons = left_electrons
        list_shells.append(electrons_current_shell)

print([int(num) for num in list_shells])
