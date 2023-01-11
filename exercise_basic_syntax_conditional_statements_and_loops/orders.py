num_of_orders = int(input())
total_price = 0
for i in range(num_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsule_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif needed_capsule_per_day < 1 or needed_capsule_per_day > 2000:
        continue
    price_for_order = price_per_capsule * needed_capsule_per_day * days
    total_price += price_for_order
    print(f"The price for the coffee is: ${price_for_order:.2f}")
print(f"Total: ${total_price:.2f}")


