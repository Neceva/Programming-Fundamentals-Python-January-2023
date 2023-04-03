text = input()

while True:
    line = input()
    if line == "Finish":
        break
    commands = line.split(" ")
    if "Replace" in commands:
        current_char = commands[1]
        new_char = commands[2]
        text = text.replace(current_char, new_char)
        print(text)
    elif "Cut" in commands:
        start = int(commands[1])
        end = int(commands[2])
        if 0 <= start <= (len(text) - 1) and 0 <= end <= (len(text) - 1):
            del_text = text.replace(text[start:end + 1], "")
            text = text[:start] + text[end + 1:]
            print(text)
        else:
            print("Invalid indices!")
    elif "Make" in commands:
        command = commands[1]
        if command == "Upper":
            text = text.upper()
            print(text)
        elif command == "Lower":
            text = text.lower()
            print(text)
    elif "Check" in commands:
        string = commands[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif "Sum" in commands:
        start = int(commands[1])
        end = int(commands[2])
        sum_num = 0
        if 0 <= start <= (len(text) - 1) and 0 <= end <= (len(text) - 1):
            substring = text[start:end + 1]
            for char in substring:
                sum_num += ord(char)
            print(sum_num)
        else:
            print("Invalid indices!")