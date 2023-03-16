num_of_cities = int(input())
total_earned_money = 0
total_expenses = 0
total = 0
for city_count in range(1, num_of_cities + 1):
    name_city = input()
    current_earned_money = float(input())
    current_owner_expenses = float(input())
    if city_count % 5 == 0:
        current_earned_money -= current_earned_money * 0.1
    elif city_count % 3 == 0:
        current_owner_expenses += current_owner_expenses * 0.5
    current_total = current_earned_money - current_owner_expenses
    print(f"In {name_city} Burger Bus earned {current_total:.2f} leva.")
    total += current_total
print(f"Burger Bus total profit: {total:.2f} leva.")

