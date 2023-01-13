budget = float(input())
price_for_one_kg_flour = float(input())
price_for_one_pack_egg = price_for_one_kg_flour * 0.75
price_for_250ml_milk = (price_for_one_kg_flour + (price_for_one_kg_flour * 0.25)) / 4
price_for_one_bread = price_for_one_kg_flour \
                      + price_for_one_pack_egg \
                      + price_for_250ml_milk
bread_counter = 0
colored_eggs_counter = 0

while budget >= price_for_one_bread:
    bread_counter += 1
    colored_eggs_counter += 3
    budget -= price_for_one_bread
    if bread_counter % 3 == 0:
        colored_eggs_counter -= bread_counter - 2

if budget < price_for_one_bread:
    print(f"You made {bread_counter} loaves of Easter bread! ", end="")
    print(f"Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
