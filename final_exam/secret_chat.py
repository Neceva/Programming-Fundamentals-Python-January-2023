concealed_message = input()

while True:
    command = input()
    if command == "Reveal":
        print(f"You have a new text message: {concealed_message}")
        break
    instruction = command.split(":|:")
    if "InsertSpace" in instruction:
        index = int(instruction[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif "Reverse" in instruction:
        string = instruction[1]
        if string in concealed_message:
            concealed_message = concealed_message.replace(string, "", 1)
            new_string = string[::-1]
            concealed_message += new_string
            print(concealed_message)
        else:
            print("error")

    elif "ChangeAll" in instruction:
        substring = instruction[1]
        replacement = instruction[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

