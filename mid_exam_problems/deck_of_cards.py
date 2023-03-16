cards_deck = input().split(", ")
numbers_command = int(input())

while numbers_command > 0:
    command = input().split(", ")
    numbers_command -= 1
    com = command[0]

    if com == "Add":
        card_name = command[1]
        if card_name in cards_deck:
            print("Card is already in the deck")
        else:
            cards_deck.append(card_name)
            print("Card successfully added")

    if com == "Remove":
        card_name = command[1]
        if card_name in cards_deck:
            cards_deck.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")

    if com == "Remove At":
        index = int(command[1])
        if 0 <= index < len(cards_deck):
            cards_deck.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    if com == "Insert":
        index = int(command[1])
        card_name = command[2]
        if 0 <= index < len(cards_deck):
            if card_name in cards_deck:
                print("Card is already added")
            else:
                cards_deck.insert(index, card_name)
                print("Card successfully added")
        else:
            print("Index out of range")
print(", ".join(cards_deck))





