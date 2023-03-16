items = input().split()
searched_items = input().split()
bakery = {}

for index in range(0, len(items), 2):
    key = items[index]
    value = int(items[index+1])
    bakery[key] = value

for item in searched_items:
    if item in bakery.keys():
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")

