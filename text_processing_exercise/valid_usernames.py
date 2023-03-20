def lenght_is_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def characters_are_valid(name):
    for char in name:
        if not (char.isalnum() or char == "_" or char == "-"):
            return False
    return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


def username_validation(name):
    if lenght_is_valid(name) and characters_are_valid(name) and no_redundant_symbols(name) is True:
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_validation(username):
        print(username)
