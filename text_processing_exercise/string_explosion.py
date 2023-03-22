some_text = input()
final_text = ""
strenght = 0

for index in range(len(some_text)):
    if strenght > 0 and some_text[index] != ">":
        strenght -= 1
    elif some_text[index] == ">":
        strenght += int(some_text[index + 1])
        final_text += some_text[index]
    else:
        final_text += some_text[index]
print(final_text)


        