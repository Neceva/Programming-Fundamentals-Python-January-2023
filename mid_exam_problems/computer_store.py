user_input_taxes = input()
total_price_without_taxes = 0
taxes = 0
is_special = False
while True:
    if user_input_taxes == "special" \
            or user_input_taxes == "regular":
        if user_input_taxes == "special":
            is_special = True
        break
    else:
       current_part_price = float(user_input_taxes)
       total_price_without_taxes += current_part_price
       if current_part_price < 0:
           print("Invalid price!")
           total_price_without_taxes -= current_part_price

    user_input_taxes = input()

taxes = total_price_without_taxes * 0.20
total_price_special = (total_price_without_taxes + taxes) \
                      - (total_price_without_taxes + taxes) * 0.10
if total_price_without_taxes == 0:
    print("Invalid order!")
    exit(0)
if is_special:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price_without_taxes:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price_special:.2f}$")
else:
    print(f"Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {total_price_without_taxes:.2f}$\n"
              f"Taxes: {taxes:.2f}$\n"
              f"-----------\n"
              f"Total price: {(total_price_without_taxes + taxes):.2f}$")

