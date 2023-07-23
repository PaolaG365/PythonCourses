import re

valid_furniture_data = r">>([a-z]+)<<(\d+[.\d]*)!(\d+)"
total_price = 0
valid_furniture = []
command = input()

while command != "Purchase":
    valid_data = re.search(valid_furniture_data, command, re.IGNORECASE)
    if valid_data:
        name_furniture, price, quantity = valid_data.groups()
        total_price += float(price) * int(quantity)
        valid_furniture.append(name_furniture)
    command = input()

print(f"Bought furniture:")
[print(name) for name in valid_furniture]
print(f"Total money spend: {total_price:.2f}")
