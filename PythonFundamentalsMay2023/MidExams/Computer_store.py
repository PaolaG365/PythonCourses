total_price = 0
price_item = input()

while price_item != "special" and price_item != "regular":
    price = float(price_item)

    if price < 0:
        print("Invalid price!")
    else:
        total_price += price

    price_item = input()

taxes = total_price * 0.2
result = 0

if total_price == 0:
    print("Invalid order!")
    exit()

if price_item == "special":
    result = (total_price + taxes) - (total_price + taxes) * 0.1
else:
    result = total_price + taxes

print("Congratulations you've just bought a new computer!\n"
      f"Price without taxes: {total_price:.2f}$\n"
      f"Taxes: {taxes:.2f}$\n"
      "-----------\n"
      f"Total price: {result:.2f}$\n")
