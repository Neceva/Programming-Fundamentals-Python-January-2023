password = input()
while True:
    line = input()
    if line == "Done":
        print(f"Your password is: {password}")
        break
    command = line.split(" ")
    if "TakeOdd" in command:
        password = password[1::2]
        print(password)

    elif "Cut" in command:
        index = int(command[1])
        length = int(command[2])
        password = password[:index] + password[index + length:]
        print(password)
    elif "Substitute" in command:
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
