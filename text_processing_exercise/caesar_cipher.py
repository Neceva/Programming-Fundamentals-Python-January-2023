start_message = input()
final_message = ''
for char in start_message:
    new_symbol = chr(ord(char) + 3)
    final_message += new_symbol
print(final_message)