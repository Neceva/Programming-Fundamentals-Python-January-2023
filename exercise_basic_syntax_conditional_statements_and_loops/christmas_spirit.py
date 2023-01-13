quantity_of_decorations = int(input())
left_day_until_christmas = int(input())
total_money = 0
christmas_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland = 3
tree_lights = 15

for day in range(1, left_day_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        total_money += ornament_set_price * quantity_of_decorations
        christmas_spirit += 5
    if day % 3 == 0:
        total_money += (tree_skirt_price + tree_garland) * quantity_of_decorations
        christmas_spirit += 13
    if day % 5 == 0:
        total_money += tree_lights * quantity_of_decorations
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total_money += tree_skirt_price + tree_garland + tree_lights

if left_day_until_christmas % 10 == 0:
     christmas_spirit -= 30

print(f"Total cost: {total_money}")
print(f"Total spirit: {christmas_spirit}")
