number_of_messages = int(input())
for i in range(number_of_messages):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88:
        print("GREAT!")
    elif number > 88:
        print("Bye.")

