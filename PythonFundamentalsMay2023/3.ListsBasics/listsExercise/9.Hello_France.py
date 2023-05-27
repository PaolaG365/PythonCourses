items_list = input().split("|")
budget = float(input())

TRAIN_TICKET = 150
CLOTHES_MAX = 50.00
SHOES_MAX = 35.00
ACCESSORIES_MAX = 20.50
bought_items = []
profit = 0

# profit is calculated with item * 0.4
# what's left of budget + new Price tag items decides is we can go to France...

for item in range(len(items_list)):
    item_data = items_list[item].split("->")
    price_item = float(item_data[1])

    if "Clothes" in item_data and price_item <= 50.00:
        bought_items.append(item_data[1])
        budget -= price_item
    elif "Shoes" in item_data and price_item <= 35.00:
        bought_items.append(item_data[1])
        budget -= price_item
    elif "Accessories" in item_data and price_item <= 20.50:
        bought_items.append(item_data[1])
        budget -= price_item

    if budget < 0:
        bought_items.pop()
        budget += price_item
        continue

for item1 in range(len(bought_items)):
    profit += float(bought_items[item1]) * 0.4
    bought_items[item1] = float(bought_items[item1]) * 1.4

new_budget = budget + sum(bought_items)

for item2 in bought_items:
    print(f"{item2:.2f}", end=" ")
print()

print(f"Profit: {profit:.2f}")

if new_budget >= TRAIN_TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")
