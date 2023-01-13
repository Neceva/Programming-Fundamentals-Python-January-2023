first_string = input()
second_string = input()
last_input_string = first_string
for char_index in range(len(first_string)):
    left_part = second_string[:char_index + 1]
    right_part = first_string[char_index + 1:]
    current_string = left_part + right_part
    if last_input_string == current_string:
        continue
    last_input_string = current_string
    print(current_string)
