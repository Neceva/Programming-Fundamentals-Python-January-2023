# encrypted_message = input()
# message_list = []
# character = ""
#
# for i in encrypted_message:
#     message_list.append(i)
#
# while True:
#     line = input()
#     if line == "Decode":
#         print(f"The decrypted message is: {''.join(message_list)}")
#         break
#     instruction = line.split('|')
#     command = instruction[0]
#     if command == "Move":
#         character = message_list[:int(instruction[1])]
#         del message_list[:int(instruction[1])]
#         for letter in character:
#             message_list.append(letter)
#
#     elif command == "Insert":
#         message_list.insert(int(instruction[1]), instruction[2])
#     elif command == "ChangeAll":
#         for index in range(len(message_list)):
#             if message_list[index] == instruction[1]:
#                 message_list[index] = instruction[2]
#
#
text = input()

while True:
    line = input()
    if line == "Decode":
        break
    command = line.split("|")
    if "Move" in command:
        number = int(command[1])
        first_n_letters = text[0:number]
        text = text.replace(text[0:number], "")
        text += first_n_letters
    elif "Insert" in command:
        idx = int(command[1])
        value = command[2]
        text = text[0:idx] + value + text[idx:]
    elif "ChangeAll" in command:
        substring = command[1]
        replacement = command[2]
        text = text.replace(substring, replacement)

print(f"The decrypted message is: {text}")