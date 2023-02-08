def calculate_price(product, number_of_quantity):
    total_price = 0
    if product == "coffee":
        total_price = number_of_quantity * 1.50
    elif product == "coke":
        total_price = number_of_quantity * 1.40
    elif product == "water":
        total_price = number_of_quantity * 1.00
    elif product == "snacks":
        total_price = number_of_quantity * 2.00
    return f"{total_price:.2f}"


product_name = input()
quantity = int(input())
print(calculate_price(product_name, quantity))
