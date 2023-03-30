activation_key = input()

while True:
    line = input()
    if line == "Generate":
        print(f"Your activation key is: {activation_key}")
        break

    instruction = line.split(">>>")
    if "Contains" in instruction:
        substring = instruction[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif "Flip" in instruction:
        command = instruction[1]
        start = int(instruction[2])
        end = int(instruction[3])
        if command == "Upper":
            old_string = activation_key[start:end]
            new_string = old_string.upper()
            activation_key = activation_key.replace(old_string, new_string)
            print(activation_key)
        elif command == "Lower":
            old_string = activation_key[start:end]
            new_string = old_string.lower()
            activation_key = activation_key.replace(old_string, new_string)
            print(activation_key)

    elif "Slice" in instruction:
        start = int(instruction[1])
        end = int(instruction[2])
        old_string = activation_key[start:end]
        activation_key = activation_key.replace(old_string, "")
        print(activation_key)

