in_stock = {}

item_and_quantity = input()

while item_and_quantity != "statistics":
    item_and_quantity = item_and_quantity.split(": ")
    item = item_and_quantity[0]
    quantity = int(item_and_quantity[1])
    if item in in_stock:
        in_stock[item] += quantity
    else:
        in_stock[item] = quantity

    item_and_quantity = input()

print("Products in stock:")

for key in in_stock:
    print(f"- {key}: {in_stock.get(key)}")

print(f"Total Products: {len(in_stock.keys())}\nTotal Quantity: {sum(in_stock.values())}")
