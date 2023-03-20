text = input()
string = input()

while text in string:
    string = string.replace(text, "")
print(string)
