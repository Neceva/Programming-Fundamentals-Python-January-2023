def repeat_string(string, repeat_time):
    return f"{string * repeat_time}"


user_input = input()
counter = int(input())
print(repeat_string(user_input, counter))